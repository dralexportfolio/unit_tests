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
from color_helper import RGB
from Polygon import *
from tkinter_helper import askDirectory


#########################################################
### Define unit tests for the various Polygon objects ###
#########################################################
# Set the needed parameters
show_renders_flag = False
bevel_attitude = 25
bevel_size = 0.1
sun_angle = 120
sun_attitude = 35
dpi = 600
tint_shade = RGB((255, 0, 255))

# Preprocess the bevel information for each polygon
SQUARE_1x1.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_NE.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_NW.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_SE.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_SW.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
HEXAGON_2x3.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
HEXAGON_3x2.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
HEXAGON_REGULAR_TALL.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
HEXAGON_REGULAR_WIDE.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)

# Preprocess the sun information for each polygon
SQUARE_1x1.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_NE.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_NW.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_SE.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_SW.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
HEXAGON_2x3.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
HEXAGON_3x2.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
HEXAGON_REGULAR_TALL.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
HEXAGON_REGULAR_WIDE.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)

# Render each polygon into a PIL image
square_1x1_render = SQUARE_1x1.render(dpi = dpi, tint_shade = tint_shade)
triangle_1x1_ne_render = TRIANGLE_1x1_NE.render(dpi = dpi, tint_shade = tint_shade)
triangle_1x1_nw_render = TRIANGLE_1x1_NW.render(dpi = dpi, tint_shade = tint_shade)
triangle_1x1_se_render = TRIANGLE_1x1_SE.render(dpi = dpi, tint_shade = tint_shade)
triangle_1x1_sw_render = TRIANGLE_1x1_SW.render(dpi = dpi, tint_shade = tint_shade)
hexagon_2x3_render = HEXAGON_2x3.render(dpi = dpi, tint_shade = tint_shade)
hexagon_3x2_render = HEXAGON_3x2.render(dpi = dpi, tint_shade = tint_shade)
hexagon_regular_tall_render = HEXAGON_REGULAR_TALL.render(dpi = dpi, tint_shade = tint_shade)
hexagon_regular_wide_render = HEXAGON_REGULAR_WIDE.render(dpi = dpi, tint_shade = tint_shade)

# Show the rendered polygons (if needed)
if show_renders_flag == True:
	square_1x1_render.show()
	triangle_1x1_ne_render.show()
	triangle_1x1_nw_render.show()
	triangle_1x1_ne_render.show()
	triangle_1x1_sw_render.show()
	hexagon_2x3_render.show()
	hexagon_3x2_render.show()
	hexagon_regular_tall_render.show()
	hexagon_regular_wide_render.show()


################################################################
### Create and save a series of nice renders for the website ###
################################################################
# Ask for a save directory and end early if not selected
directory_path = askDirectory()
assert directory_path is not None, "Unable to proceed with saving renders because no directory was selected"

# Set the default parameters
bevel_attitude = 25
bevel_size = 0.1
sun_angle = 120
sun_attitude = 35
dpi = 300
tint_shade = RGB((255, 255, 255))

# Create copies of the square object to use in renders below
square_1 = SQUARE_1x1.deepcopy()
square_2 = SQUARE_1x1.deepcopy()
square_3 = SQUARE_1x1.deepcopy()

# Create a series of renders ranging over different shapes
# Preprocess the needed bevel information
SQUARE_1x1.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_NE.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
HEXAGON_REGULAR_TALL.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
# Preprocess the needed sun information
SQUARE_1x1.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_NE.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
HEXAGON_REGULAR_TALL.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
# Render and save the needed images
SQUARE_1x1.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_1-render-1.png"))
TRIANGLE_1x1_NE.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_1-render-2.png"))
HEXAGON_REGULAR_TALL.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_1-render-3.png"))

# Create a series of renders ranging over different bevel sizes
# Preprocess the needed bevel information
square_1.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = 0.5 * bevel_size)
square_2.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = 1.0 * bevel_size)
square_3.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = 2.0 * bevel_size)
# Preprocess the needed sun information
square_1.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
square_2.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
square_3.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
# Render and save the needed images
square_1.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_2-render-1.png"))
square_2.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_2-render-2.png"))
square_3.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_2-render-3.png"))

# Create a series of renders ranging over different sun angles
# Preprocess the needed bevel information
square_1.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
square_2.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
square_3.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
# Preprocess the needed sun information
square_1.preprocessSunInfo(sun_angle = (sun_angle - 120) % 360, sun_attitude = sun_attitude)
square_2.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
square_3.preprocessSunInfo(sun_angle = (sun_angle + 120) % 360, sun_attitude = sun_attitude)
# Render and save the needed images
square_1.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_3-render-1.png"))
square_2.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_3-render-2.png"))
square_3.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_3-render-3.png"))

# Create a series of renders ranging over different sun attitudes
# Preprocess the needed bevel information
square_1.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
square_2.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
square_3.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
# Preprocess the needed sun information
square_1.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = 0.9 * bevel_attitude + 0.1 * 90)
square_2.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = 0.6 * bevel_attitude + 0.4 * 90)
square_3.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = 0.3 * bevel_attitude + 0.7 * 90)
# Render and save the needed images
square_1.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_4-render-1.png"))
square_2.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_4-render-2.png"))
square_3.render(dpi = dpi, tint_shade = tint_shade).save(directory_path.joinpath("polygon-set_4-render-3.png"))

# Create a series of renders ranging over different tint shades
# Preprocess the needed bevel information
SQUARE_1x1.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
# Preprocess the needed sun information
SQUARE_1x1.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
# Render and save the needed images
SQUARE_1x1.render(dpi = dpi, tint_shade = RGB((255, 255, 255))).save(directory_path.joinpath("polygon-set_5-render-1.png"))
SQUARE_1x1.render(dpi = dpi, tint_shade = RGB((255, 0, 0))).save(directory_path.joinpath("polygon-set_5-render-2.png"))
SQUARE_1x1.render(dpi = dpi, tint_shade = RGB((0, 127, 127))).save(directory_path.joinpath("polygon-set_5-render-3.png"))