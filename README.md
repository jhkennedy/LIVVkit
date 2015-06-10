![](https://github.com/ACME-Climate/LIVV/blob/develop/docs/livv.png)

===================================================================================================
  Land Ice Verification and Validation Toolkit
===================================================================================================
Last updated 4/17/2015
If this document is out of date send us an email!  See the contact section below for more details.


  Introduction
================
LIVVkit is a python-based toolkit for verification and validation of Ice Sheet Models.  LIVVkit provides a way for testing model output against a set of benchmark data.  Verification testing checks bitwise accuracy of solutions, and reports inconsistencies, as well as providing differences in configurations between model and benchmark data.  Standard output files are parsed for key information.  Validation and performance testing are under development.

For further documentation view the [wiki](https://github.com/LIVVkit/LIVVkit/wiki)

  Before Using
================
Some requirements must be met before using LIVVkit.  LIVVkit was designed to be used with Python 2.7.  If you are using any other version of Python by default, use the command for Python 2.7 in place of any calls to `python` in this document (or any other LIVVkit Documentation).  If you are not sure what version of Python you are running try running `python --version` from a terminal.

LIVVkit depends on several software packages and libraries. We are working towards a completely automatic dependency management system, but some use cases may have been overlooked.  The complete list of dependencies for LIVVkit is as follows: 

 * Python 2.7
 * NetCDF 4.3.0+
 * NCO (NetCDF Operators) 4.4.0
 * HDF5 1.8.6
 * NCL (NCAR Command Language) 6.1.2
 * python-netCDF4
 * python-matplotlib
 * python-numpy
 * python-jinja2

If you are having any troubles with dependencies email us!  See the contact section below for more details.

 
  Obtaining Benchmark Data
============================
Send us an email to get a set of benchmark data.


  How to Use
==============
Using LIVVkit should be a painless experience.  You can give it a go with default settings simply by running:

> python livv.py

The default options will run all of the verification cases for the Dome, Ishom, and Shelf tests.  If you have a configuration with specific options that you have set up you can use:

> python livv.py -m CONFIG_NAME

To save your own configuration use:

> python livv.py [options] -m CONFIG_NAME -s

For a detailed list of options see the Options section, below.


  Options
===========
A variety of options can be used with LIVVkit.  A detailed list follows:

|	Option	| Description |
| ------------: | :-------------------------------------------------------------------------------------------------------------------------------- |
|  -h, --help |	Show the help message |
|  --verification=VER | Specifies the verification tests to run                      |
|  --performance=PERF | Specifies the performance tests to run                      |
|  --comment=COMMENT |	Log a comment about this run									|
|  -o OUTPUTDIR, --outputDir=OUTPUTDIR | Location to output the LIVVkit webpages.							|
|  -i INPUTDIR, --inputDir=INPUTDIR | Location of the input for running tests.						|
|  -b BENCHDIR, --benchmarkDir=BENCHDIR | Location of the input for running tests.						|
|  --load CONFIG | Load a preconfigured set of options for the given name.		|
|  --save CONFIG |	Store the configuration being run with the given name.	|


  Contact
===========
Bug reports/Feature Requests:
  https://github.com/LIVVkit/LIVVkit/issues

Andrew Bennett : 
  Github: arbennett
  Email:  bennettar@ornl.gov

Joseph Kennedy : 
  Github: jhkennedy
  Email:  kennedyjh@ornl.gov

Kate Evans : 
  Github: kevans32
  Email: evanskj@ornl.gov


TODO: A list of things that need to be updated.
-----------------------------------------------
 * Detail options more clearly
 * Give some use-cases (ie if the user wants to save a new configuration with a custom name)
 * Tell us what needs adding!
