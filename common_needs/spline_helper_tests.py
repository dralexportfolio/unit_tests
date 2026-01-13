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
from tkinter_helper import askSaveFilename

# External modules
import matplotlib.pyplot as plt
from numpy import random


########################################################
### Define unit tests for the various spline classes ###
########################################################
# Set the needed parameters
seed = 2
n_points = 7
x_min = -10
x_max = 20
y_min = -3
y_max = 8

# Set the random seed
random.seed(seed = seed)

# Randomly generate the x-values and y-values
# Initialize the lists
x_values = []
y_values = []
# Generate the random values
for _ in range(n_points):
	x_values.append(x_min + (x_max - x_min) * random.rand())
	y_values.append(y_min + (y_max - y_min) * random.rand())
# Sort the x-values to be in increasing order
x_values.sort(reverse = False)

# Compute the lower and upper x-values to use
x_lower = 1.1 * min(x_values) - 0.1 * max(x_values)
x_upper = 1.1 * max(x_values) - 0.1 * min(x_values)

# Create linear and natural cubic splines using these x-values and y-values
linear_spline = LinearSpline(x_values = x_values, y_values = y_values)
cubic_spline = NaturalCubicSpline(x_values = x_values, y_values = y_values)

# Generate the plot information for each spline
linear_plot_results = linear_spline.getPlotInfo(x_lower = x_lower, x_upper = x_upper)
cubic_plot_results = cubic_spline.getPlotInfo(x_lower = x_lower, x_upper = x_upper)

# Create a plot overlaying the two splines
# Create the figure
plt.figure(figsize = (10, 8))
# Add the needed traces
plt.plot(linear_plot_results["x_values_interpolated"], linear_plot_results["y_values_interpolated"], "b-", zorder = 0, label = "Linear")
plt.plot(cubic_plot_results["x_values_interpolated"], cubic_plot_results["y_values_interpolated"], "g-", zorder = 5, label = "Cubic")
plt.scatter(x_values, y_values, None, "k", zorder = 10)
# Format the figure
plt.title("Overlay Of Linear And Natural Cubic Splines")
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.legend()
# Save the figure
image_path = askSaveFilename(allowed_extensions = ["png"])
assert image_path is not None, "Unable to save matplotlib figure because cancel button was clicked"
plt.savefig(image_path)

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