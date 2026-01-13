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
from spline_helper import *

# External modules


########################################################
### Define unit tests for the various spline classes ###
########################################################
'''
x_values = [0, 3, 5, 9, 11]
y_values = [1, -2, 0, 0, 4]
spline = LinearSpline(x_values = x_values, y_values = y_values)
spline.plot(x_lower = -3, x_upper = 15, save_flag = True, show_flag = False, used_engine = "matplotlib")
spline.plot(x_lower = -3, x_upper = 15, save_flag = True, show_flag = False, used_engine = "plotly")
'''

'''
x_values = [0, 1, 3, 8]
y_values = [1, -1, 0, 4]
spline = LinearSpline(x_values = x_values, y_values = y_values)
spline.plot()
spline = NaturalCubicSpline(x_values = x_values, y_values = y_values)
spline.plot()
'''