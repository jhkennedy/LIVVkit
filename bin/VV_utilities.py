#!/usr/bin/env

import sys 
import os
import re
from optparse import OptionParser
import subprocess
import collections
import VV_outprocess
import VV_testsuite

def valid_conf(details_file,valid_configure_path,land_file,atm_file,icesheet_file)

    #this function allows creation of nested dictionaries on the fly (like PERL autovivification)
    def makehashdome():
        return collections.defaultdict(makehashdome)
    data = makehashdome()

    def makehashbench():
        return collections.defaultdict(makehashbench)
    bench = makehashbench()

    con_flag = False
    keywords = ('Time Management', 'Grid specification', 'Time steps', 'GLIDE options', 'Parameters', 'GLINT climate',)
    variable, value = '', ''

    for kw in keywords:
        try:
            configlog = open(configure_path, 'r')
        except:
            print "error reading" + configure_path
            sys.exit(1)
            raise
    
        try:
            benchlog = open(bench_configure_path, 'r')
        except:
            print "error reading" + bench_configure_path
            sys.exit(1)
            raise

        for cfline in configlog:
            if cfline.startswith('[' + kw + ']'):
                con_flag = True
                continue
            if cfline.startswith('['):
                con_flag = False
                continue
            if con_flag == True:
                line = cfline.strip('\r\n')
                if '#' in line:
                    tmp = line.split('#')
                    line = tmp[0]
                if line == '':
                    continue
                if line.endswith('='):
                    variable, junk = line.split()
                    value = ''
                else:
                    variable, value = line.split('=')
                variable = variable.strip()
                value = value.strip()
                datadome[kw][variable] = value

        configlog.close()


















#parse through the configure and xml file and print information
def confxml(configure_xml_file,configure_path,bench_configure_path,xml_path,bench_xml_path):

    #this function allows creation of nested dictionaries on the fly (like PERL autovivification)
    def makehashdome():
        return collections.defaultdict(makehashdome)
    datadome = makehashdome()

    def makehashbench():
        return collections.defaultdict(makehashbench)
    databench = makehashbench()

    con_flag = False
    keywords = ('parameters', 'CF output', 'grid', 'time', 'options', 'ho_options')
    variable, value = '', ''
    
    for kw in keywords:
        try:
            configlog = open(configure_path, 'r')
        except:
            print "error reading" + configure_path
            sys.exit(1)
            raise
    
        try:
            benchlog = open(bench_configure_path, 'r')
        except:
            print "error reading" + bench_configure_path
            sys.exit(1)
            raise

        for cfline in configlog:
            if cfline.startswith('[' + kw + ']'):
                con_flag = True
                continue
            if cfline.startswith('['):
                con_flag = False
                continue
            if con_flag == True:
                line = cfline.strip('\r\n')
                if '#' in line:
                    tmp = line.split('#')
                    line = tmp[0]
                if line == '':
                    continue
                if line.endswith('='):
                    variable, junk = line.split()
                    value = ''
                else:
                    variable, value = line.split('=')
                variable = variable.strip()
                value = value.strip()
                datadome[kw][variable] = value

        configlog.close()

        for cfline in benchlog:
            if cfline.startswith('[' + kw + ']'):
                con_flag = True
                continue
            if cfline.startswith('['):
                con_flag = False
                continue
            if con_flag == True:
                line = cfline.strip('\r\n')
                if '#' in line:
                    tmp = line.split('#')
                    line = tmp[0]
                if line == '':
                    continue
                if line.endswith('='):
                    variable, junk = line.split()
                    value = ''
                else:
                    variable, value = line.split('=')
                variable = variable.strip()
                value = value.strip()
                databench[kw][variable] = value

        benchlog.close()

#Calculate number of time steps: dome
    if datadome['time']['tend'] and datadome['time']['tstart']:
        diff = float(datadome['time']['tend']) - float(datadome['time']['tstart'])
        timestp = diff / float(datadome['time']['dt'])
#Calculate number of time steps: bench
    if databench['time']['tend'] and databench['time']['tstart']:
        diff = float(databench['time']['tend']) - float(databench['time']['tstart'])
        timestp_bench = diff / float(databench['time']['dt'])
#Put settings on website, check if they match the benchmark settings
    configure_xml_file.write('<HTML>\n')
    configure_xml_file.write('<BODY BGCOLOR="#CADFE0">\n')
    configure_xml_file.write('<H3>Case Details:</H3>')
    configure_xml_file.write('<HTML>\n')
    configure_xml_file.write('<TITLE>Configure Settings </TITLE>\n')
    configure_xml_file.write('<TABLE>\n')
    configure_xml_file.write('<TR>\n')
    configure_xml_file.write('<H4>Configure File Settings </H4>\n')
    if datadome['CF output']['variables']:
        configure_xml_file.write('Output available from test run: ' + datadome['CF output']['variables'] + "<BR>\n")

#Grid Size/spacing
    configure_xml_file.write("Grid Size (vert by ew by ns): " + datadome['grid']['upn'] + "x" + datadome['grid']['ewn'] + "x" + datadome['grid']['nsn'] + "<BR>\n")
    if datadome['grid']['upn'] != databench['grid']['upn']:
        configure_xml_file.write('<FONT COLOR="red">vertical dimension (upn) is different than benchmark run: ' + datadome['grid']['upn'] + ' versus ' + databench['grid']['upn'] + '</FONT><BR>\n')
    if datadome['grid']['ewn'] != databench['grid']['ewn']:
        configure_xml_file.write('<FONT COLOR="red">east/west dimension (ewn) is different than benchmark run: ' + datadome['grid']['ewn'] + ' versus ' + databench['grid']['ewn'] + '</FONT><BR>\n')
    if datadome['grid']['nsn'] != databench['grid']['nsn']:
        configure_xml_file.write('<FONT COLOR="red">north/south dimension (nsn) is different than benchmark run: ' + datadome['grid']['nsn'] + ' versus ' + databench['grid']['nsn'] + '</FONT><BR>\n')

    configure_xml_file.write("Grid Spacing (ew by ns): " + datadome['grid']['dew'] + "x" + datadome['grid']['dns'] + "<BR>\n")
    if datadome['grid']['dew'] != databench['grid']['dew']:
        configure_xml_file.write('<FONT COLOR="red">east/west spacing (dew) is different than benchmark run: ' + datadome['grid']['dew'] + ' versus ' + databench['grid']['dew'] + '</FONT><BR>\n')
    if datadome['grid']['dns'] != databench['grid']['dns']:
        configure_xml_file.write('<FONT COLOR="red">north/south spacing (dns) is different than benchmark run: ' + datadome['grid']['dns'] + ' versus ' + databench['grid']['dns'] + '</FONT><BR>\n')

#Simulation length and time steps
    configure_xml_file.write("Start/End Time: " + datadome['time']['tstart'] + "," + datadome['time']['tend'] + ", Number of time steps = " + str(timestp) + "<BR>\n")
    if datadome['time']['tstart'] != databench['time']['tstart']:
        configure_xml_file.write('<FONT COLOR="red">Start time is different than benchmark run: ' + datadome['time']['tstart'] + ' versus ' + databench['time']['tstart'] + '</FONT><BR>\n')
    if datadome['time']['tend'] != databench['time']['tend']:
        configure_xml_file.write('<FONT COLOR="red">Start time is different than benchmark run: ' + datadome['time']['tend'] + ' versus ' + databench['time']['tend'] + '</FONT><BR>\n')
    if str(timestp) != str(timestp_bench):
        configure_xml_file.write('<FONT COLOR="red">Number of timesteps is different than benchmark run: ' + str(timestp) + ' versus ' + str(timestp_bench) + '</FONT><BR>\n')

#Parameter settings
    configure_xml_file.write('<BR\n>')
    configure_xml_file.write("Parameters<BR>\n")
    configure_xml_file.write("------------------------<BR>\n")
    if datadome['parameters']['flow_factor']:
        if datadome['parameters']['flow_factor'] == databench['parameters']['flow_factor']:
            configure_xml_file.write('flow_factor = ' + datadome['parameters']['flow_factor'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">flow_factor = ' + datadome['parameters']['flow_factor'] + ' different than benchmark value:  ' + databench['parameters']['flow_factor'] + '</FONT><BR>\n')
    if datadome['parameters']['ice_limit']:
        if datadome['parameters']['ice_limit'] == databench['parameters']['ice_limit']:
            configure_xml_file.write('ice_limit = ' + datadome['parameters']['ice_limit'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">Ice Limit = ' + datadome['parameters']['ice_limit'] + ' different than benchmark value:  ' + databench['parameters']['ice_limit'] + '</FONT><BR>\n')
    if datadome['parameters']['default_flwa']:
        if datadome['parameters']['default_flwa'] == databench['parameters']['default_flwa']:
            configure_xml_file.write('default_flwa = ' + datadome['parameters']['default_flwa'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">default_flwa = ' + datadome['parameters']['default_flwa'] + ' different than benchmark value:  ' + databench['parameters']['default_flwa'] + '</FONT><BR>\n')

#Options settings
    configure_xml_file.write('<BR\n>')
    configure_xml_file.write("Options<BR>\n")
    configure_xml_file.write("------------------------<BR>\n")
    if datadome['options']['dycore']:
        if datadome['options']['dycore'] == databench['options']['dycore']:
            configure_xml_file.write('dycore = ' + datadome['options']['dycore'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">dycore = ' + datadome['options']['dycore'] + ' different than benchmark value:  ' + databench['options']['dycore'] + '</FONT><BR>\n')
    if datadome['options']['flow_law']:
        if datadome['options']['flow_law'] == databench['options']['flow_law']:
            configure_xml_file.write('flow_law = ' + datadome['options']['flow_law'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">flow_law = ' + datadome['options']['flow_law'] + ' different than benchmark value:  ' + databench['options']['flow_law'] + '</FONT><BR>\n')
    if datadome['options']['evolution']:
        if datadome['options']['evolution'] == databench['options']['evolution']:
            configure_xml_file.write('evolution = ' + datadome['options']['evolution'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">evolution = ' + datadome['options']['evolution'] + ' different than benchmark value:  ' + databench['options']['evolution'] + '</FONT><BR>\n')
    if datadome['options']['temperature']:
        if datadome['options']['temperature'] == databench['options']['temperature']:
            configure_xml_file.write('temperature = ' + datadome['options']['temperature'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">temperature = ' + datadome['options']['temperature'] + ' different than benchmark value:  ' + databench['options']['temperature'] + '</FONT><BR>\n')
    if datadome['options']['slip_coeff']:
        if datadome['options']['slip_coeff'] == databench['options']['slip_coeff']:
            configure_xml_file.write('slip_coeff = ' + datadome['options']['slip_coeff'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">slip_coeff = ' + datadome['options']['slip_coeff'] + ' different than benchmark value:  ' + databench['options']['slip_coeff'] + '</FONT><BR>\n')
    if datadome['options']['basal_water']:
        if datadome['options']['basal_water'] == databench['options']['basal_water']:
            configure_xml_file.write('basal_water = ' + datadome['options']['basal_water'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">basal_water = ' + datadome['options']['basal_water'] + ' different than benchmark value:  ' + databench['options']['basal_water'] + '</FONT><BR>\n')
    if datadome['options']['marine_margin']:
        if datadome['options']['marine_margin'] == databench['options']['marine_margin']:
            configure_xml_file.write('marine_margin = ' + datadome['options']['marine_margin'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">marine_margin = ' + datadome['options']['marine_margin'] + ' different than benchmark value:  ' + databench['options']['marine_margin'] + '</FONT><BR>\n')
    if datadome['options']['isostasy']:
        if datadome['options']['isostasy'] == databench['options']['isostasy']:
            configure_xml_file.write('isostasy = ' + datadome['options']['isostasy'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">isostasy = ' + datadome['options']['isostasy'] + ' different than benchmark value:  ' + databench['options']['isostasy'] + '</FONT><BR>\n')
    if datadome['options']['restart']:
        if datadome['options']['restart'] == databench['options']['restart']:
            configure_xml_file.write('restart = ' + datadome['options']['restart'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">restart = ' + datadome['options']['restart'] + ' different than benchmark value:  ' + databench['options']['restart'] + '</FONT><BR>\n')

#HO Options settings
    configure_xml_file.write('<BR\n>')
    configure_xml_file.write("HO Options<BR>\n")
    configure_xml_file.write("------------------------<BR>\n")
    if datadome['ho_options']['diagnostic_scheme']:
        if datadome['ho_options']['diagnostic_scheme'] == databench['ho_options']['diagnostic_scheme']:
            configure_xml_file.write('diagnostic_scheme = ' + datadome['ho_options']['diagnostic_scheme'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">diagnostic_scheme = ' + datadome['ho_options']['diagnostic_scheme'] + ' different than benchmark value:  ' + databench['ho_options']['diagnostic_scheme'] + '</FONT><BR>\n')
    if datadome['ho_options']['which_ho_babc']:
        if datadome['ho_options']['which_ho_babc'] == databench['ho_options']['which_ho_babc']:
            configure_xml_file.write('which_ho_babc = ' + datadome['ho_options']['which_ho_babc'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">which_ho_babc = ' + datadome['ho_options']['which_ho_babc'] + ' different than benchmark value:  ' + databench['ho_options']['which_ho_babc'] + '</FONT><BR>\n')
    if datadome['ho_options']['which_ho_efvs']:
        if datadome['ho_options']['which_ho_efvs'] == databench['ho_options']['which_ho_efvs']:
            configure_xml_file.write('which_ho_efvs = ' + datadome['ho_options']['which_ho_efvs'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">which_ho_efvs = ' + datadome['ho_options']['which_ho_efvs'] + ' different than benchmark value:  ' + databench['ho_options']['which_ho_efvs'] + '</FONT><BR>\n')
    if datadome['ho_options']['which_ho_sparse']:
        if datadome['ho_options']['which_ho_sparse'] == databench['ho_options']['which_ho_sparse']:
            configure_xml_file.write('which_ho_sparse = ' + datadome['ho_options']['which_ho_sparse'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">which_ho_sparse = ' + datadome['ho_options']['which_ho_sparse'] + ' different than benchmark value:  ' + databench['ho_options']['which_ho_sparse'] + '</FONT><BR>\n')
    if datadome['ho_options']['which_ho_nonlinear']:
        if datadome['ho_options']['which_ho_nonlinear'] == databench['ho_options']['which_ho_nonlinear']:
            configure_xml_file.write('which_ho_nonlinear = ' + datadome['ho_options']['which_ho_nonlinear'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">which_ho_nonlinear = ' + datadome['ho_options']['which_ho_nonlinear'] + ' different than benchmark value:  ' + databench['ho_options']['which_ho_nonlinear'] + '</FONT><BR>\n')
    if datadome['ho_options']['which_ho_resid']:
        if datadome['ho_options']['which_ho_resid'] == databench['ho_options']['which_ho_resid']:
            configure_xml_file.write('which_ho_resid = ' + datadome['ho_options']['which_ho_resid'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">which_ho_resid = ' + datadome['ho_options']['which_ho_resid'] + ' different than benchmark value:  ' + databench['ho_options']['which_ho_resid'] + '</FONT><BR>\n')
    configure_xml_file.write('<BR\n>')


#parse through xml file information
    file_keywords_l1 = ('Convergence Tolerance', 'Maximum Iterations', 'Preconditioner Type', 'Prec Type', 'Overlap', 'fact: level-of-fill')
    file_keywords_l2 = ('Jacobian Operator', 'Forcing Term Method', 'Forcing Term Alpha', 'Forcing Term Gamma', 'Matrix-Free Perturbation', 'Linear Solver Type', 'Solver Type', 'Convergence Tolerance', 'Flexible Gmres')
    bench_keywords_l1 = ('Convergence Tolerance', 'Maximum Iterations', 'Preconditioner Type', 'Prec Type', 'Overlap', 'fact: level-of-fill')
    bench_keywords_l2 = ('Jacobian Operator', 'Forcing Term Method', 'Forcing Term Alpha', 'Forcing Term Gamma', 'Matrix-Free Perturbation', 'Linear Solver Type', 'Solver Type', 'Convergence Tolerance', 'Flexible Gmres')

#create dictionaries
    fileL1parameters = {}
    fileL2parameters = {}
    benchL1parameters = {}
    benchL2parameters = {}
    file_max_it = []
    bench_max_it = []
    flag = False

#open files
    try:
        xml_log = open(xml_path, 'r')
    except:
        print "error reading" + xml_log
        sys.exit(1)
        raise
    try:
        bench_log = open(bench_xml_path, 'r')
    except:
        print "error reading" + bench_log
        sys.exit(1)
        raise

#read through xml file
    while True:
        line = xml_log.readline()
        if 'Trilinos nonlinear solver options' in line:
            break;
        for kw1 in file_keywords_l1:
            if ('"' + kw1 + '"' in line):
                value = line.split('value=')
                match = re.search('"(.*)"', value[1])
                fileL1parameters[kw1] = match.group(1)

    for line in xml_log.readlines():
        for kw2 in file_keywords_l2:
            if ('"' + kw2 + '"' in line):
                value = line.split('value=')
                match = re.search('"(.*)"', value[1])
                fileL2parameters[kw2] = match.group(1)
            if 'Forcing Term Alpha' in line:
                flag = True
            if 'Maximum Iterations' in line:
                value = line.split('value=')
                match = re.search('"(.*)"', value[1])
                file_max_it.append(match.group(1))
    xml_log.close()

#read through bench xml file
    while True:
        line = bench_log.readline()
        if 'Trilinos nonlinear solver options' in line:
            break;
        for kw1 in bench_keywords_l1:
            if ('"' + kw1 + '"' in line):
                value = line.split('value=')
                match = re.search('"(.*)"', value[1])
                benchL1parameters[kw1] = match.group(1)

    for line in bench_log.readlines():
        for kw2 in bench_keywords_l2:
            if ('"' + kw2 + '"' in line):
                value = line.split('value=')
                match = re.search('"(.*)"', value[1])
                benchL2parameters[kw2] = match.group(1)
            if 'Maximum Iterations' in line:
                value = line.split('value=')
                match = re.search('"(.*)"', value[1])
                bench_max_it.append(match.group(1))
    bench_log.close()

#Put Preconditioner settings on website, check if they match the benchmark settings
    configure_xml_file.write('<HTML>\n')
    configure_xml_file.write('<H3>Velocity Solver Settings:</H3>')
    configure_xml_file.write('<HTML>\n')
    configure_xml_file.write('<TITLE>XML Settings </TITLE>\n')
    configure_xml_file.write('<TABLE>\n')
    configure_xml_file.write('<TR>\n')
    configure_xml_file.write('<H4>XML File Settings </H4>\n')
    configure_xml_file.write('Preconditioner: Picard<BR>\n')
    configure_xml_file.write('------------------------<BR>\n')
    if fileL1parameters['Convergence Tolerance']:
        if fileL1parameters['Convergence Tolerance'] == benchL1parameters['Convergence Tolerance']:
            configure_xml_file.write('Block GMRES: Convergence Tolerance = ' + fileL1parameters['Convergence Tolerance'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">Block GMRES: Convergence Tolerance = ' + fileL1parameters['Convergence Tolerance'] + ' different than benchmark value: ' + benchL1parameters['Convergence Tolerance'] + '</FONT><BR>\n')
    if fileL1parameters['Maximum Iterations']:
        if fileL1parameters['Maximum Iterations'] == benchL1parameters['Maximum Iterations']:
            configure_xml_file.write('Block GMRES: Maximum Iterations = ' + fileL1parameters['Maximum Iterations'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">Block GMRES: Maximum Iterations = ' + fileL1parameters['Maximum Iterations'] + ' different than benchmark value: ' + benchL1parameters['Maximum Iterations'] + '</FONT><BR>\n')
    if fileL1parameters['Preconditioner Type']:
        if fileL1parameters['Preconditioner Type'] == benchL1parameters['Preconditioner Type']:
            configure_xml_file.write('Preconditioner Type = ' + fileL1parameters['Preconditioner Type'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">Block GMRES: Maximum Iterations = ' + fileL1parameters['Maximum Iterations'] + ' different than benchmark value: ' + benchL1parameters['Maximum Iterations'] + '</FONT><BR>\n')
    if fileL1parameters['Prec Type']:
        if fileL1parameters['Prec Type'] == benchL1parameters['Prec Type']:
            configure_xml_file.write('Prec Type = ' + fileL1parameters['Prec Type'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">Prec Type = ' + fileL1parameters['Prec Type'] + ' different than benchmark value: ' + benchL1parameters['Prec Type'] + '</FONT><BR>\n')
    if fileL1parameters['Overlap']:
        if fileL1parameters['Overlap'] == benchL1parameters['Overlap']:
            configure_xml_file.write('Overlap = ' + fileL1parameters['Overlap'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">Overlap = ' + fileL1parameters['Overlap'] + ' different than benchmark value: ' + benchL1parameters['Overlap'] + '</FONT><BR>\n')
    if fileL1parameters['fact: level-of-fill']:
        if fileL1parameters['fact: level-of-fill'] == benchL1parameters['fact: level-of-fill']:
            configure_xml_file.write('Fact: Level-of-Fill = ' + fileL1parameters['fact: level-of-fill'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="red">Fact: Level-of-Fill = ' + fileL1parameters['fact: level-of-fill'] + ' different than benchmark value: ' + benchL1parameters['fact: level-of-fill'] + '</FONT><BR>\n')

#Put Solver settings on website, check if they match the benchmark settings
    configure_xml_file.write('<BR\n>')
    configure_xml_file.write('<BR\n>')
    configure_xml_file.write('Solver: NK<BR>\n')
    configure_xml_file.write('------------------------<BR>\n')
    if fileL2parameters['Jacobian Operator']:
        if fileL2parameters['Jacobian Operator'] == benchL2parameters['Jacobian Operator']:
            configure_xml_file.write('Newton: Jacobian Operator = ' + fileL2parameters['Jacobian Operator'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">Newton: Jacobian Operator = ' + fileL2parameters['Jacobian Operator'] + ' different than benchmark value: ' + benchL2parameters['Jacobian Operator'] + '</FONT><BR>\n')
    if fileL2parameters['Forcing Term Method']:
        if fileL2parameters['Forcing Term Method'] == benchL2parameters['Forcing Term Method']:
            configure_xml_file.write('Newton: Forcing Term Method = ' + fileL2parameters['Forcing Term Method'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">Newton: Forcing Term Method = ' + fileL2parameters['Forcing Term Method'] + ' different than benchmark value: ' + benchL2parameters['Forcing Term Method'] + '</FONT><BR>\n')
    if flag == True:
        if fileL2parameters['Forcing Term Alpha'] == benchL2parameters['Forcing Term Alpha']:
            configure_xml_file.write('Newton: Forcing Term Alpha = ' + fileL2parameters['Forcing Term Alpha'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">Newton: Forcing Term Alpha = ' + fileL2parameters['Forcing Term Alpha'] + ' different than benchmark value: ' + benchL2parameters['Forcing Term Alpha'] + '</FONT><BR>\n')
    if flag == True:
        if fileL2parameters['Forcing Term Gamma'] == benchL2parameters['Forcing Term Gamma']:
            configure_xml_file.write('Newton: Forcing Term Gamma = ' + fileL2parameters['Forcing Term Gamma'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">Newton: Forcing Term Gamma = ' + fileL2parameters['Forcing Term Gamma'] + ' different than benchmark value: ' + benchL2parameters['Forcing Term Gamma'] + '</FONT><BR>\n')
    if file_max_it[1]:
        if file_max_it[1] == bench_max_it[1]:
            configure_xml_file.write('Newton: Maximum Iterations = ' + file_max_it[1] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">Newton: Maximum Iterations = ' + file_max_it[1] + ' different than benchmark value: ' + bench_max_it[1] + '</FONT><BR>\n')
    if fileL2parameters['Matrix-Free Perturbation']:
        if fileL2parameters['Matrix-Free Perturbation'] == benchL2parameters['Matrix-Free Perturbation']:
            configure_xml_file.write('Matrix-Free Perturbation = ' + fileL2parameters['Matrix-Free Perturbation'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">Matrix-Free Perturbation = ' + fileL2parameters['Matrix-Free Perturbation'] + ' different than benchmark value: ' + benchL2parameters['Matrix-Free Perturbation'] + '</FONT><BR>\n')
    if fileL2parameters['Linear Solver Type']:
        if fileL2parameters['Linear Solver Type'] == benchL2parameters['Linear Solver Type']:
            configure_xml_file.write('Linear Solver Type = ' + fileL2parameters['Linear Solver Type'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">Linear Solver Type = ' + fileL2parameters['Linear Solver Type'] + ' different than benchmark value: ' + benchL2parameters['Linear Solver Type'] + '</FONT><BR>\n')
    if fileL2parameters['Solver Type']:
        if fileL2parameters['Solver Type'] == benchL2parameters['Solver Type']:
            configure_xml_file.write('Solver Type = ' + fileL2parameters['Solver Type'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">Solver Type = ' + fileL2parameters['Solver Type'] + ' different than benchmark value: ' + benchL2parameters['Solver Type'] + '</FONT><BR>\n')
    if fileL2parameters['Convergence Tolerance']:
        if fileL2parameters['Convergence Tolerance'] == benchL2parameters['Convergence Tolerance']:
            configure_xml_file.write('GMRES: Convergence Tolerance = ' + fileL2parameters['Convergence Tolerance'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">GMRES: Convergence Tolerance = ' + fileL2parameters['Convergence Tolerance'] + ' different than benchmark value: ' + benchL2parameters['Convergence Tolerance'] + '</FONT><BR>\n')
    if file_max_it[0]:
        if file_max_it[0] == bench_max_it[0]:
            configure_xml_file.write('GMRES: Maximum Iterations = ' + file_max_it[0] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">GMRES: Maximum Iterations = ' + file_max_it[0] + ' different than benchmark value: ' + bench_max_it[0] + '</FONT><BR>\n')
    if fileL2parameters['Flexible Gmres']:
        if fileL2parameters['Flexible Gmres'] == benchL2parameters['Flexible Gmres']:
            configure_xml_file.write('GMRES: Flexible GMRES = ' + fileL2parameters['Flexible Gmres'] + "<BR>\n")
        else:
            configure_xml_file.write('<FONT COLOR="RED">GMRES: Flexible GMRES = ' + fileL2parameters['Flexible Gmres'] + ' different than benchmark value: ' + benchL2parameters['Flexible Gmres'] + '</FONT><BR>\n')

    configure_xml_file.write('<BR\n>')
    configure_xml_file.write('</HTML>\n')
    configure_xml_file.close()


def format(file, list):
    i = 0
    for item in list:
        if i != 0:
            file.write(", " + str(item))
        else:
            file.write(str(item))
        i = 1
