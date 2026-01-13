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
from tkinter_helper import askSaveFilename

# External modules
import matplotlib.pyplot as plt


#########################################################
### Define unit tests for the customSpectrum function ###
#########################################################
# Set the needed parameters
n_div = 1000

# Create the list of all parameter values
all_parameters = [index / (n_div - 1) for index in range(n_div)]

# Initialize the lists of all RGB values in the spectrum
all_red_values = []
all_green_values = []
all_blue_values = []

# Compute the needed values
for parameter in all_parameters:
	# Compute the red, green and blue values as a tuple of integers
	rgb_tuple = customSpectrum(parameter = parameter).asTupleInt()

	# Append to the needed lists
	all_red_values.append(rgb_tuple[0])
	all_green_values.append(rgb_tuple[1])
	all_blue_values.append(rgb_tuple[2])

# Create a plot of the RGB curves
# Create the figure
plt.figure(figsize = (10, 8))
# Add the needed traces
plt.plot(all_parameters, all_red_values, "r-", zorder = 0, label = "Red")
plt.plot(all_parameters, all_green_values, "g-", zorder = 5, label = "Green")
plt.plot(all_parameters, all_blue_values, "b-", zorder = 10, label = "Blue")
# Format the figure
plt.title("Red, Green And Blue Curves Of The Default Color Spectrum")
plt.xlabel("parameter")
plt.ylabel("value")
plt.grid()
plt.legend()
# Save the figure
image_path = askSaveFilename(allowed_extensions = ["png"])
assert image_path is not None, "Unable to save matplotlib figure because cancel button was clicked"
plt.savefig(image_path, bbox_inches = "tight")