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
path.insert(0, str(infrastructure_folder.joinpath("board_games")))
path.insert(0, str(infrastructure_folder.joinpath("common_needs")))

# Internal modules
from Board import *
from color_helper import RGB
from Polygon import *
from tkinter_helper import askSaveFilename


#########################################################
### Define unit tests for the various Polygon objects ###
#########################################################
# Set the needed parameters
n_rows = 8
n_cols = 8
bevel_attitude = 25
bevel_size = 0.1
sun_angle = 120
sun_attitude = 35
dpi = 300
tint_shade_1 = RGB((200, 200, 200))
tint_shade_2 = RGB((200, 127, 100))

# Set the number of polygons and create the associated list
n_polygons = n_rows * n_cols
all_polygons = [SQUARE_1x1 for _ in range(n_polygons)]

# Create the lists of x-value and y-value shifts for each polygon
# Initialize the lists
x_shift_per_polygon = []
y_shift_per_polygon = []
# Initialize the current shift amounts
x_shift = 0
y_shift = 0
# Loop until all are accounted for
while True:
	# Add the current shift amounts
	x_shift_per_polygon.append(x_shift)
	y_shift_per_polygon.append(y_shift)
	# Iterate to the next shifts, end loop if needed
	x_shift += 1
	if x_shift == n_cols:
		x_shift = 0
		y_shift += 1
		if y_shift == n_rows:
			break

# Create the needed Board object
board = Board(n_polygons = n_polygons,
			  all_polygons = all_polygons,
			  x_shift_per_polygon = x_shift_per_polygon,
			  y_shift_per_polygon = y_shift_per_polygon)

# Preprocess the needed bevel and sun information
board.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
board.preprocessAllSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)

# Set the tint shade for all the polygons on the board
for row_index in range(n_rows):
	for col_index in range(n_cols):
		tint_shade = tint_shade_1 if (row_index + col_index) % 2 == 0 else tint_shade_2
		board.setTintShade(tint_shade = tint_shade, polygon_index = col_index + n_cols * row_index)

# Render the board with the needed settings and save it to the given location
filename_path = askSaveFilename(allowed_extensions = ["png"])
assert filename_path is not None, "Unable to proceed with saving render because no filename was selected"
board.render(dpi = dpi).save(filename_path)