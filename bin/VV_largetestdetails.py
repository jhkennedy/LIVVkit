#!/usr/bin/env

import sys 
import os
from optparse import OptionParser
import subprocess
import collections
import VV_outprocess
import VV_utilities
import VV_checks

failedt_list = []

def details60(solver_file,perf_test,data_dir):  # using data, fill the web page with info
        
    failedt_list = []
    solver_file.write('<HTML>\n')
    solver_file.write('<BODY BGCOLOR="#CADFE0">\n')
    solver_file.write('<H3>Dome 60 Iteration Count Details:</H3>')
    solver_file.write('<BR> \n')

# JFNK gnu 9 proc

# failure checking
    failedt1 = VV_checks.failcheck(perf_test, '/dome60/' + data_dir + '/out.60.JFNK')
    failedt_list.append(failedt1)

    solver_file.write('<H4>New Run: out.60.JFNK</H4>')
    procttl_dd301, nonlist_dd301,avg2_dd301,out_flag_dd301,ndd301_name,ldd301_name = \
        VV_outprocess.jobprocess(perf_test + '/dome60/' + data_dir + '/out.60.JFNK', 'domed301')
    solver_file.write("Number of Processors = " + str(procttl_dd301[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301)
    solver_file.write('<BR>\n')

    if out_flag_dd301 == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301)
    solver_file.write('<BR> \n')

    solver_file.write('<H4>Benchmark Run: out.60.JFNK</H4>')
    procttl_dd301b, nonlist_dd301b,avg2_dd301b,out_flag_dd301b,ndd301b_name,ldd301b_name = \
        VV_outprocess.jobprocess(perf_test + '/bench/dome60/' + data_dir + '/out.60.JFNK', 'domed301b')

    solver_file.write("Number of Processors = " + str(procttl_dd301b[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301b)
    solver_file.write('<BR>\n')
                  
    if out_flag_dd301b == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301b)
    solver_file.write('<BR> \n')

    if 1 in failedt_list:
        failedt = 1
    else:
        failedt = 0

    return failedt

def details120(solver_file,perf_test,data_dir):  # using data, fill the web page with info
        
    failedt_list = []
    solver_file.write('<HTML>\n')
    solver_file.write('<BODY BGCOLOR="#CADFE0">\n')
    solver_file.write('<H3>Dome 120 Iteration Count Details:</H3>')
    solver_file.write('<BR> \n')

# JFNK gnu 9 proc

# failure checking
    failedt1 = VV_checks.failcheck(perf_test, '/dome120/' + data_dir + '/out.120.JFNK')
    failedt_list.append(failedt1)

    solver_file.write('<H4>New Run: out.120.JFNK</H4>')
    procttl_dd301, nonlist_dd301,avg2_dd301,out_flag_dd301,ndd301_name,ldd301_name = \
        VV_outprocess.jobprocess(perf_test + '/dome120/' + data_dir + '/out.120.JFNK', 'domed301')
    solver_file.write("Number of Processors = " + str(procttl_dd301[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301)
    solver_file.write('<BR>\n')

    if out_flag_dd301 == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301)
    solver_file.write('<BR> \n')

    solver_file.write('<H4>Benchmark Run: out.120.JFNK</H4>')
    procttl_dd301b, nonlist_dd301b,avg2_dd301b,out_flag_dd301b,ndd301b_name,ldd301b_name = \
        VV_outprocess.jobprocess(perf_test + '/bench/dome120/' + data_dir + '/out.120.JFNK', 'domed301b')

    solver_file.write("Number of Processors = " + str(procttl_dd301b[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301b)
    solver_file.write('<BR>\n')
                  
    if out_flag_dd301b == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301b)
    solver_file.write('<BR> \n')

    if 1 in failedt_list:
        failedt = 1
    else:
        failedt = 0

    return failedt

def details240(solver_file,perf_test,data_dir):  # using data, fill the web page with info
        
    failedt_list = []
    solver_file.write('<HTML>\n')
    solver_file.write('<BODY BGCOLOR="#CADFE0">\n')
    solver_file.write('<H3>Dome 240 Iteration Count Details:</H3>')
    solver_file.write('<BR> \n')

# JFNK gnu 9 proc

# failure checking
    failedt1 = VV_checks.failcheck(perf_test, '/dome240/' + data_dir + '/out.240.JFNK')
    failedt_list.append(failedt1)

    solver_file.write('<H4>New Run: out.240.JFNK</H4>')
    procttl_dd301, nonlist_dd301,avg2_dd301,out_flag_dd301,ndd301_name,ldd301_name = \
        VV_outprocess.jobprocess(perf_test + '/dome240/' + data_dir + '/out.240.JFNK', 'domed301')
    solver_file.write("Number of Processors = " + str(procttl_dd301[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301)
    solver_file.write('<BR>\n')

    if out_flag_dd301 == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301)
    solver_file.write('<BR> \n')

    solver_file.write('<H4>Benchmark Run: out.240.JFNK</H4>')
    procttl_dd301b, nonlist_dd301b,avg2_dd301b,out_flag_dd301b,ndd301b_name,ldd301b_name = \
        VV_outprocess.jobprocess(perf_test + '/bench/dome240/' + data_dir + '/out.240.JFNK', 'domed301b')

    solver_file.write("Number of Processors = " + str(procttl_dd301b[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301b)
    solver_file.write('<BR>\n')
                  
    if out_flag_dd301b == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301b)
    solver_file.write('<BR> \n')

    if 1 in failedt_list:
        failedt = 1
    else:
        failedt = 0

    return failedt

def details500(solver_file,perf_test,data_dir):  # using data, fill the web page with info
        
    failedt_list = []
    solver_file.write('<HTML>\n')
    solver_file.write('<BODY BGCOLOR="#CADFE0">\n')
    solver_file.write('<H3>Dome 500 Iteration Count Details:</H3>')
    solver_file.write('<BR> \n')

# JFNK gnu 9 proc

# failure checking
    failedt1 = VV_checks.failcheck(perf_test, '/dome500/' + data_dir + '/out.500.JFNK')
    failedt_list.append(failedt1)

    solver_file.write('<H4>New Run: out.500.JFNK</H4>')
    procttl_dd301, nonlist_dd301,avg2_dd301,out_flag_dd301,ndd301_name,ldd301_name = \
        VV_outprocess.jobprocess(perf_test + '/dome500/' + data_dir + '/out.500.JFNK', 'domed301')
    solver_file.write("Number of Processors = " + str(procttl_dd301[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301)
    solver_file.write('<BR>\n')

    if out_flag_dd301 == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301)
    solver_file.write('<BR> \n')

    solver_file.write('<H4>Benchmark Run: out.500.JFNK</H4>')
    procttl_dd301b, nonlist_dd301b,avg2_dd301b,out_flag_dd301b,ndd301b_name,ldd301b_name = \
        VV_outprocess.jobprocess(perf_test + '/bench/dome500/' + data_dir + '/out.500.JFNK', 'domed301b')

    solver_file.write("Number of Processors = " + str(procttl_dd301b[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301b)
    solver_file.write('<BR>\n')
                  
    if out_flag_dd301b == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301b)
    solver_file.write('<BR> \n')

    if 1 in failedt_list:
        failedt = 1
    else:
        failedt = 0

    return failedt

def details1000(solver_file,perf_test,data_dir):  # using data, fill the web page with info
        
    failedt_list = []
    solver_file.write('<HTML>\n')
    solver_file.write('<BODY BGCOLOR="#CADFE0">\n')
    solver_file.write('<H3>Dome 1000 Iteration Count Details:</H3>')
    solver_file.write('<BR> \n')

# JFNK gnu 9 proc

# failure checking
    failedt1 = VV_checks.failcheck(perf_test, '/dome1000/' + data_dir + '/out.1000.JFNK')
    failedt_list.append(failedt1)

    solver_file.write('<H4>New Run: out.1000.JFNK</H4>')
    procttl_dd301, nonlist_dd301,avg2_dd301,out_flag_dd301,ndd301_name,ldd301_name = \
        VV_outprocess.jobprocess(perf_test + '/dome1000/' + data_dir + '/out.1000.JFNK', 'domed301')
    solver_file.write("Number of Processors = " + str(procttl_dd301[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301)
    solver_file.write('<BR>\n')

    if out_flag_dd301 == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301)
    solver_file.write('<BR> \n')

    solver_file.write('<H4>Benchmark Run: out.1000.JFNK</H4>')
    procttl_dd301b, nonlist_dd301b,avg2_dd301b,out_flag_dd301b,ndd301b_name,ldd301b_name = \
        VV_outprocess.jobprocess(perf_test + '/bench/dome1000/' + data_dir + '/out.1000.JFNK', 'domed301b')

    solver_file.write("Number of Processors = " + str(procttl_dd301b[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301b)
    solver_file.write('<BR>\n')
                  
    if out_flag_dd301b == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301b)
    solver_file.write('<BR> \n')

    if 1 in failedt_list:
        failedt = 1
    else:
        failedt = 0

    return failedt


def detailsgis4km(solver_file,perf_test,data_dir):  # using data, fill the web page with info
        
    failedt_list = []
    solver_file.write('<HTML>\n')
    solver_file.write('<BODY BGCOLOR="#CADFE0">\n')
    solver_file.write('<H3>GIS 4KM Iteration Count Details:</H3>')
    solver_file.write('<BR> \n')

# GIS 4KM

# failure checking
    failedt1 = VV_checks.failcheck(perf_test, '/gis_4km/' + data_dir + '/out.gis.4km')
    failedt_list.append(failedt1)

    solver_file.write('<H4>New Run: out.gis.4km</H4>')
    procttl_dd301, nonlist_dd301,avg2_dd301,out_flag_dd301,ndd301_name,ldd301_name = \
        VV_outprocess.jobprocess(perf_test + '/gis_4km/' + data_dir + '/out.gis.4km', 'domed301')
    solver_file.write("Number of Processors = " + str(procttl_dd301[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301)
    solver_file.write('<BR>\n')

    if out_flag_dd301 == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301)
    solver_file.write('<BR> \n')

    solver_file.write('<H4>Benchmark Run: out.gis.4km</H4>')
    procttl_dd301b, nonlist_dd301b,avg2_dd301b,out_flag_dd301b,ndd301b_name,ldd301b_name = \
        VV_outprocess.jobprocess(perf_test + '/bench/gis_4km/' + data_dir + '/out.gis.4km', 'domed301b')

    solver_file.write("Number of Processors = " + str(procttl_dd301b[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301b)
    solver_file.write('<BR>\n')
                  
    if out_flag_dd301b == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301b)
    solver_file.write('<BR> \n')

    if 1 in failedt_list:
        failedt = 1
    else:
        failedt = 0

    return failedt


def detailsgis2km(solver_file,perf_test,data_dir):  # using data, fill the web page with info
        
    failedt_list = []
    solver_file.write('<HTML>\n')
    solver_file.write('<BODY BGCOLOR="#CADFE0">\n')
    solver_file.write('<H3>GIS 2KM Iteration Count Details:</H3>')
    solver_file.write('<BR> \n')

# GIS 2KM

# failure checking
    failedt1 = VV_checks.failcheck(perf_test, '/gis_2km/' + data_dir + '/out.gis.2km')
    failedt_list.append(failedt1)

    solver_file.write('<H4>New Run: out.gis.2km</H4>')
    procttl_dd301, nonlist_dd301,avg2_dd301,out_flag_dd301,ndd301_name,ldd301_name = \
        VV_outprocess.jobprocess(perf_test + '/gis_2km/' + data_dir + '/out.gis.2km', 'domed301')
    solver_file.write("Number of Processors = " + str(procttl_dd301[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301)
    solver_file.write('<BR>\n')

    if out_flag_dd301 == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301)
    solver_file.write('<BR> \n')

    solver_file.write('<H4>Benchmark Run: out.gis.2km</H4>')
    procttl_dd301b, nonlist_dd301b,avg2_dd301b,out_flag_dd301b,ndd301b_name,ldd301b_name = \
        VV_outprocess.jobprocess(perf_test + '/bench/gis_2km/' + data_dir + '/out.gis.2km', 'domed301b')

    solver_file.write("Number of Processors = " + str(procttl_dd301b[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301b)
    solver_file.write('<BR>\n')
                  
    if out_flag_dd301b == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301b)
    solver_file.write('<BR> \n')

    if 1 in failedt_list:
        failedt = 1
    else:
        failedt = 0

    return failedt


def detailsgis1km(solver_file,perf_test,data_dir):  # using data, fill the web page with info
        
    failedt_list = []
    solver_file.write('<HTML>\n')
    solver_file.write('<BODY BGCOLOR="#CADFE0">\n')
    solver_file.write('<H3>GIS 1KM Iteration Count Details:</H3>')
    solver_file.write('<BR> \n')

# GIS 1KM

# failure checking
    failedt1 = VV_checks.failcheck(perf_test, '/gis_1km/' + data_dir + '/out.gis.1km')
    failedt_list.append(failedt1)

    solver_file.write('<H4>New Run: out.gis.1km</H4>')
    procttl_dd301, nonlist_dd301,avg2_dd301,out_flag_dd301,ndd301_name,ldd301_name = \
        VV_outprocess.jobprocess(perf_test + '/gis_1km/' + data_dir + '/out.gis.1km', 'domed301')
    solver_file.write("Number of Processors = " + str(procttl_dd301[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301)
    solver_file.write('<BR>\n')

    if out_flag_dd301 == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301)
    solver_file.write('<BR> \n')

    solver_file.write('<H4>Benchmark Run: out.gis.1km</H4>')
    procttl_dd301b, nonlist_dd301b,avg2_dd301b,out_flag_dd301b,ndd301b_name,ldd301b_name = \
        VV_outprocess.jobprocess(perf_test + '/bench/gis_1km/' + data_dir + '/out.gis.1km', 'domed301b')

    solver_file.write("Number of Processors = " + str(procttl_dd301b[-1]) + "<BR>\n")
    solver_file.write("Number of Nonlinear Iterations = ")
    VV_utilities.format(solver_file, nonlist_dd301b)
    solver_file.write('<BR>\n')
                  
    if out_flag_dd301b == 1:
        solver_file.write('<FONT COLOR="red">***TIME STEP(S) WHICH FAILED TO CONVERGE</FONT> <BR>\n')
    solver_file.write("Average Number of Linear Iterations per Time-Step = ")
    VV_utilities.format(solver_file, avg2_dd301b)
    solver_file.write('<BR> \n')

    if 1 in failedt_list:
        failedt = 1
    else:
        failedt = 0

    return failedt
