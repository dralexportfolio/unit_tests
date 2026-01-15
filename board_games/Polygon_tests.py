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


#########################################################
### Define unit tests for the various Polygon objects ###
#########################################################
# Set the needed parameters
bevel_attitude = 25
bevel_size = 0.1
sun_angle = 120
sun_attitude = 35
dpi = 900
tint_shade = RGB((255, 0, 255))

# Preprocess the bevel information for each polygon
SQUARE_1x1.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_NE.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_NW.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_SE.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
TRIANGLE_1x1_SW.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
HEXAGON_2x3.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)
HEXAGON_3x2.preprocessBevelInfo(bevel_attitude = bevel_attitude, bevel_size = bevel_size)

# Preprocess the sun information for each polygon
SQUARE_1x1.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_NE.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_NW.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_SE.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
TRIANGLE_1x1_SW.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
HEXAGON_2x3.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)
HEXAGON_3x2.preprocessSunInfo(sun_angle = sun_angle, sun_attitude = sun_attitude)

# Render each polygon
SQUARE_1x1.render(dpi = dpi, tint_shade = tint_shade).show()
TRIANGLE_1x1_NE.render(dpi = dpi, tint_shade = tint_shade).show()
TRIANGLE_1x1_NW.render(dpi = dpi, tint_shade = tint_shade).show()
TRIANGLE_1x1_SE.render(dpi = dpi, tint_shade = tint_shade).show()
TRIANGLE_1x1_SW.render(dpi = dpi, tint_shade = tint_shade).show()
HEXAGON_2x3.render(dpi = dpi, tint_shade = tint_shade).show()
HEXAGON_3x2.render(dpi = dpi, tint_shade = tint_shade).show()