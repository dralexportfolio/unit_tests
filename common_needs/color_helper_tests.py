##########################################
### Import needed general dependencies ###
##########################################
# Add paths for internal modules
# Import dependencies
from pathlib import Path
from sys import path
# Get the shared unit tests folder
unit_tests_folder = Path(__file__).parent.parent
# Get the shared parent folder
parent_folder = unit_tests_folder.parent
# Get the shared infrastructure folder
infrastructure_folder = parent_folder.joinpath("infrastructure")
# Add the needed paths
path.insert(0, str(infrastructure_folder.joinpath("common_needs")))

# Internal modules
from color_helper import *

# External modules


#########################################################
### Define unit tests for the customSpectrum function ###
#########################################################
'''
print(customSpectrum(parameter = 0.0))
print(customSpectrum(parameter = 0.1))
print(customSpectrum(parameter = 0.2))
print(customSpectrum(parameter = 0.3))
print(customSpectrum(parameter = 0.4))
print(customSpectrum(parameter = 0.5))
print(customSpectrum(parameter = 0.6))
print(customSpectrum(parameter = 0.7))
print(customSpectrum(parameter = 0.8))
print(customSpectrum(parameter = 0.9))
print(customSpectrum(parameter = 1.0))
'''