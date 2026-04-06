####################################################################
### Perform any necessary steps to set up the rest of the script ###
####################################################################
# Import the module needed for importing modules via a string
from importlib import import_module

# Initialize a dictionary of software used and their versions
version_per_software = {}


######################################################
### Check the current version of Python being used ###
######################################################
# Import sys to check the Python version
from platform import python_version

# Store this information
version_per_software["Python"] = python_version()


#############################################################################################
### Check the current versions of module being used but indicate if any are not installed ###
#############################################################################################
# List the module strings to check
all_modules_to_check = ["imageio", "matplotlib", "numpy", "pandas", "PIL", "plotly", "scipy", "tqdm"]

# Loop over the module strings and check their versions
for module_str in all_modules_to_check:
	try:
		# Attempt to import the module and store the version
		version_per_software[module_str] = import_module(module_str).__version__
	except:
		# Indicate that the module is not installed
		version_per_software[module_str] = "Not Installed"


##############################################################
### Print all information stored in the version dictionary ###
##############################################################
# Get the longest length software string in the dictionary
max_len = max([len(software_str) for software_str in version_per_software])

# Print the header for the section
print("SUMMARY:")

# Loop over the software strings and print the versions
for software_str in version_per_software:
	# Construct the string to print
	string_to_print = "    "
	string_to_print += software_str
	string_to_print += " "
	string_to_print += "-" * (max_len - len(software_str) + 3)
	string_to_print += "> "
	string_to_print += version_per_software[software_str]

	# Print the needed information
	print(string_to_print)