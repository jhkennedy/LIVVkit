'''
A general parser for extracting data from text files

Created on Feb 19, 2015

@author: arbennett
'''
import re
import os
import sys
import glob
import subprocess
import ConfigParser

import livv
from livv import *
from timeit import itertools

## 
#
class Parser(object):
    
    ## Constructor
    #
    def __init__(self):
        self.configParser = ConfigParser.ConfigParser()
        self.benchData = dict()
        self.modelData = dict()
    
    ##
    #
    def parseConfigurations(self, modelDir, benchDir):
        modelFiles = os.listdir(modelDir)
        benchFiles = os.listdir(benchDir)        
        sameList = set(modelFiles).intersection(benchFiles)
        
        # Pull in the information from the model run
        for modelF in modelFiles:
            modelFile = modelDir + os.sep + modelF
            modelFileData = dict()
            self.configParser.read(modelFile)

            # Go through each header section (ones that look like [section])
            for section in self.configParser.sections():
                subDict = dict()
                
                # Go through each item in the section and put {var : val} into subDict
                for entry in self.configParser.items(section):
                    subDict[[entry[0]]] = entry[1]
                    
                # Map the sub-dictionary to the section 
                modelFileData[section] = subDict.copy()
            
            # Associate the data to the file
            self.modelData[modelF] = modelFileData

        # Pull in the information from the benchmark 
        for benchF in benchFiles:
            benchFile = benchDir + os.sep + benchF
            benchFileData = dict()
            self.configParser.read(benchFile)
            
            # Go through each header section (ones that look like [section])
            for section in self.configParser.sections():
                subDict = dict()
                
                # Go through each item in the section and put {var : val} into subDict
                for entry in self.configParser.items(section):
                    subDict[[entry[0]]] = entry[1] 
                
                # Map the sub-dictionary to the section 
                benchFileData[section] = subDict.copy()
            
            # Associate the data with the file
            self.benchData[benchF] = benchFileData
        
        # Return both of the datasets
        return self.modelData, self.benchData
                    
                
    ## parseOutput
    #
    def parseOutput(self, file):
        # Initialize a dictionary that will store all of the information
        testDict = livv.parserVars.copy()
        
        # Set up variables that we can use to map data and information
        dycoreTypes = {"0" : "Glide", "1" : "Glam", "2" : "Glissade", "3" : "AlbanyFelix", "4" : "BISICLES"}
        numberProcs = 0
        currentStep = 0
        avgItersToConverge = 0
        convergedIters = []
        itersToConverge = []
        
        # Make sure that we can actually read the file
        try:
            logfile = open(file, 'r')
        except:
            print "ERROR: Could not read " + file
        
        # Go through and build up information about the simulation
        for line in logfile:
            #Determine the dycore type
            if ('CISM dycore type' in line):
                if line.split()[-1] == '=':
                    testDict['Dycore Type'] = dycoreTypes[next(logfile).strip()]
                else:
                    testDict['Dycore Type'] = dycoreTypes[line.split()[-1]]

            # Calculate the total number of processors used
            if ('total procs' in line):
                numberProcs += int(line.split()[-1])
            
            # Grab the current timestep
            if ('Nonlinear Solver Step' in line):
                currentStep = int(line.split()[4])
            
            # Get the number of iterations per timestep
            if ('"SOLVE_STATUS_CONVERGED"' in line):
                splitLine = line.split()
                itersToConverge.append(int(splitLine[splitLine.index('"SOLVE_STATUS_CONVERGED"') + 2]))
                
            # If the timestep converged mark it with a positive
            if ('Converged!' in line):
                convergedIters.append(currentStep)
                
            # If the timestep didn't converge mark it with a negative
            if ('Failed!' in line):
                convergedIters.append(-1*currentStep)
            
        # Calculate the average number of iterations it took to converge
        if (len(itersToConverge) > 0):
            avgItersToConverge = sum(itersToConverge) / len(itersToConverge)
    
        # Record some of the data in the testDict
        testDict['Number of processors'] = numberProcs
        testDict['Number of timesteps'] = currentStep
        if avgItersToConverge > 0:
            testDict['Average iterations to converge'] = avgItersToConverge 
        
        if testDict['Dycore Type'] == None: testDict['Dycore Type'] = 'Unavailable'
        for key in testDict.keys():
            if testDict[key] == None:
                testDict[key] = 'N/A'
        
        return testDict     