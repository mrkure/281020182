"""
Created on Fri Mar 23 09:31:12 2018

@author: CAZ2BJ

# =============================================================================
# PACKAGES
# =============================================================================

SEARCHING FOR PACKAGES
USE THE TERMINAL OR AN ANACONDA PROMPT FOR THE FOLLOWING STEPS.
TO SEE IF A SPECIFIC PACKAGE SUCH AS SCIPY IS AVAILABLE FOR INSTALLATION
------------------------------------------------------------------------
conda search scipy
conda search --override-channels --channel http://conda.anaconda.org/mutirri iminuit

LIST PACKAGES
-------------
conda list
conda list -n myenv

INSTALL PACKAGES
----------------
conda install scipy
conda install scipy=0.15.0
conda install --name myenv scipy=0.15.0

INSTALLING NON-CONDA PACKAGES
IF A PACKAGE IS NOT AVAILABLE FROM CONDA OR ANACONDA.ORG, YOU MAY BE ABLE TO FIND
AND INSTALL THE PACKAGE WITH ANOTHER PACKAGE MANAGER LIKE PIP.
PIP PACKAGES DO NOT HAVE ALL THE FEATURES OF CONDA PACKAGES, AND WE RECOMMEND
FIRST TRYING TO INSTALL ANY PACKAGE WITH CONDA. IF THE PACKAGE IS UNAVAILABLE 
THROUGH CONDA, TRY INSTALLING IT WITH PIP. THE DIFFERENCES BETWEEN PIP AND CONDA 
PACKAGES CAUSE CERTAIN UNAVOIDABLE LIMITS IN COMPATIBILITY, BUT CONDA WORKS HARD 
TO BE AS COMPATIBLE WITH PIP AS POSSIBLE.
-------------------------------------------------------------------------------
pip install see



UPDATING PACKAGES
USE CONDA UPDATE COMMAND TO CHECK TO SEE IF A NEW UPDATE IS AVAILABLE. IF CONDA 
TELLS YOU AN UPDATE IS AVAILABLE, YOU CAN THEN CHOOSE WHETHER OR NOT TO INSTALL IT.
-------------------------------------------------------------------------------
conda update biopython
conda update python

To update conda itself:
conda update conda

REMOVE PACKAGE
-------------------------
conda remove scipy
conda remove -n myenv scipy

# =============================================================================
# ENVIRONMENTS
# =============================================================================

LIST ENVIRONMENTS
-----------------
conda info --envs
OR
conda env list

ACTIVATE AND DEACTIVATE EVIRONMENT
----------------------------------
conda activate myenv
conda deactivate

CREATE ENVIRONMENT
------------------
conda create -n myenv python=3.4
conda create -n myenv python=3.4 scipy=0.15.0
conda create -n myenv python=3.4 scipy=0.15.0 numpy xlsreader

this is pyyhon36 with anaconda
conda create -n py36 python=3.6 anaconda
conda create -n py27 python=2.7 anaconda

REMOVE ENVIRONMENT
-------------------
conda remove --name myenv --all

CLONING AN ENVIRONMENT
YOU CAN MAKE AN EXACT COPY OF AN ENVIRONMENT BY CREATING A CLONE OF IT
-----------------------------------------------------------------------
conda create --name myclone --clone myenv



USING PIP IN AN ENVIRONMENT
TO USE PIP IN YOUR ENVIRONMENT, IN YOUR TERMINAL WINDOW OR AN ANACONDA PROMPT, RUN
--------------------------
conda install -n myenv pip
source activate myenv
pip <pip_subcommand>


# =============================================================================
# INFO VERSIONS
# =============================================================================

PRINTS VERSION OF PYTHON
python --version

PRINTS VERSION OF WIN/CONDA/PYTHON/ AND PATHS TO FILES
conda info

PRINTS ALL VERSIONS WITH ADDITIONAL INFROMATIONS 
conda info matplotlib


conda info python = 3.6


# =============================================================================
# MANUAL INSTALATION FROM FILES USING PIP
# =============================================================================
pip install C:\Users\caz2bj\Downloads\spyder-3.2.8-py3-none-any.whl




# =============================================================================
# CHANNELS
# =============================================================================
TO LIST CURRENTLY USED CHANNELS 
conda config --get channel
RESULT CAN REFER TO CONCRETE URL OR PLACEHOLDER NAME TO FILE C:\Program Files\Anaconda3\.condarc

SO AFTER THIS INSTRUCTION
C:\WINDOWS\system32>conda config --get channels

WE CAN SEE THIS RESULT WHICH MEANS THERE ARE ONLY CHANNELS LISTED IN .CONDARC
C:\WINDOWS\system32>conda config --get channels
--add channels 'defaults'   # lowest priority

IN THE FILE CONDARC IT LOOKS LIKE THIS
channels:
  - http://rb-conda.bosch.com/repo.continuum.io.free
  - http://rb-conda.bosch.com/simconnect.autobuild
  - http://rb-conda.bosch.com/simconnect.dev
  - http://rb-conda.bosch.com/mse.dev
  - http://rb-conda.bosch.com/r.conda.anaconda.org
#  - http://rb-conda.bosch.com/conda-forge.


ADD CHANNEL
THE FOLLOWING COMMAND ADDS THE CHANNEL “NEW_CHANNEL” TO THE TOP OF THE CHANNEL LIST,
MAKING IT THE HIGHEST PRIORITY: (IF HIGHEST CHANNEL FAIL, ALL OTHERS FAIL TOO)

conda config --add channels new_channel
CONDA NOW HAS AN EQUIVALENT COMMAND:
conda config --prepend channels new_channel


ADD CHANNEL
Conda also now has a command that adds the new channel to the bottom of the channel
list, making it the lowest priority:

conda config --append channels new_channel

CONDA REMOVE CHANNEL
conda config --remove channels new_channel
OR EDIR
C:\Program Files\Anaconda3\.condarc

"""

