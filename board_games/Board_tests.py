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

# External modules
from imageio.v2 import get_writer, imread
from os import remove
from math import pi, sin
from tqdm import tqdm

#########################################################
### Define unit tests for the various Polygon objects ###
#########################################################
# Set all of the needed parameters
# Board size
n_rows = 8
n_cols = 8
# Bevel settings
bevel_attitude = 25
bevel_size = 0.1
# Initial sun settings
initial_sun_angle = 120
initial_sun_attitude = 35
# Animation settings
n_frames = 100
frame_duration = 50
dpi = 300
# Tint settings
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

# Set the tint shade for all the polygons on the board
for row_index in range(n_rows):
	for col_index in range(n_cols):
		tint_shade = tint_shade_1 if (row_index + col_index) % 2 == 0 else tint_shade_2
		board.setTintShade(tint_shade = tint_shade, polygon_index = col_index + n_cols * row_index)

# Preprocess the bevel information for all polygons on the board
board.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)

# Ask for a path to which an animation should be saved, raise error if not selected
filename_path = askSaveFilename(allowed_extensions = ["mp4"])
assert filename_path is not None, "Unable to proceed with saving render because no filename was selected"

# Generate a sequence of board renders and save them to a single animation file
with get_writer(filename_path, fps = int(1000 / frame_duration)) as video_writer:
	for frame_index in tqdm(range(n_frames)):
		# Set the sun angle and attitude accordingly
		sun_angle = (initial_sun_angle + 360 * frame_index / n_frames) % 360
		sun_attitude = initial_sun_attitude + (65 - initial_sun_attitude) * sin(pi * frame_index / n_frames)**2

		# Preprocess the needed sun information
		board.preprocessAllSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)

		# Get the path for the current image file, append to the list, and render the current image
		current_filename_path = filename_path.parent.joinpath(filename_path.name[:-4] + "_" + str(frame_index) + ".png")
		current_image = board.render(dpi = dpi)

		# Save the current image and delete the PIL object
		current_image.save(current_filename_path)
		current_image.close()

		# Load the generated image using imageio, add it to the video file, then delete the loaded image object and associated file
		# Add rendered image to the gif
		loaded_image = imread(current_filename_path)
		video_writer.append_data(loaded_image)
		# Delete the original render
		del loaded_image
		remove(current_filename_path)