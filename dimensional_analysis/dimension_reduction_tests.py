##########################################
### Import needed general dependencies ###
##########################################
# Add paths for internal modules
# Import dependencies
from pathlib import Path
from sys import path
# Get the shared active projects folder
active_projects_folder = Path(__file__).parent.parent
# Get the shared parent folder
parent_folder = active_projects_folder.parent
# Get the shared infrastructure folder
infrastructure_folder = parent_folder.joinpath("infrastructure")
# Add the needed paths
path.insert(0, str(infrastructure_folder.joinpath("dimensional_analysis")))

# Internal modules
from dimension_reduction import performPCA

# External modules
from math import cos, pi, sin, sqrt
import matplotlib.pyplot as plt
from numpy import random, zeros


###############################################
### Perform basic PCA and generate a figure ###
###############################################
# Define the needed settings
seed = 1
n_points = 200
x_center = 2
y_center = 1
semi_major_axis = 3
semi_minor_axis = 1
rotate_angle = 30

# Set the random seed (if needed)
if seed is not None:
	random.seed(seed = seed)

# Generate the raw data array
raw_data_array = zeros((n_points, 2), dtype = float)
for row_index in range(n_points):
	# Randomly generate an x-value and y-value in an ellipse
	while True:
		# Generate an x-value and y-value
		x_value = semi_major_axis * (2 * random.rand() - 1)
		y_value = semi_minor_axis * (2 * random.rand() - 1)

		# Break if the pair is in the ellipse
		if (x_value / semi_major_axis)**2 + (y_value / semi_minor_axis)**2 <= 1:
			break

	# Rotate the coordinate system by the needed angle
	rotated_x_value = x_value * cos(rotate_angle * pi / 180) - y_value * sin(rotate_angle * pi / 180)
	rotated_y_value = x_value * sin(rotate_angle * pi / 180) + y_value * cos(rotate_angle * pi / 180)

	# Store the shifted point in the array
	raw_data_array[row_index, 0] = x_center + rotated_x_value
	raw_data_array[row_index, 1] = y_center + rotated_y_value

# Perform PCA to get the needed results
pca_results = performPCA(raw_data_array = raw_data_array)

# Plot the raw data array along with the principal component directions
# Create the figure
plt.figure(figsize = (10, 8))
# Add the needed traces
plt.scatter(raw_data_array[:, 0], raw_data_array[:, 1], None, "k", zorder = 0)
plt.scatter([pca_results["inputs"]["center_vector"][0]],
			[pca_results["inputs"]["center_vector"][1]],
			None,
			"r",
			label = "Center Of Mass",
			zorder = 30)
plt.arrow(pca_results["inputs"]["center_vector"][0],
		  pca_results["inputs"]["center_vector"][1],
		  pca_results["outputs"]["ordered_principal_components"][0, 0],
		  pca_results["outputs"]["ordered_principal_components"][1, 0],
		  width = 0.05,
		  head_width = 0.3,
		  head_length = 0.3,
		  fc = "b",
		  ec = "k",
		  label = "1st Principal Direction",
		  zorder = 10)
plt.arrow(pca_results["inputs"]["center_vector"][0],
		  pca_results["inputs"]["center_vector"][1],
		  pca_results["outputs"]["ordered_principal_components"][0, 1],
		  pca_results["outputs"]["ordered_principal_components"][1, 1],
		  width = 0.05,
		  head_width = 0.3,
		  head_length = 0.3,
		  fc = "g",
		  ec = "k",
		  label = "2nd Principal Direction",
		  zorder = 20)
# Format the figure
plt.title("Principal Component Analysis Example: Recovering Major And Minor Axes Of Ellipse")
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.axis("equal")
plt.legend(loc = "upper left")
plt.tight_layout()
# Show the figure
plt.show()