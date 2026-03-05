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
from sqlite3_helper import *
from tkinter_helper import askSaveFilename

# External modules
from pandas import DataFrame


###########################################################################
### Define a function for comparing a table in a db file to a dataframe ###
###########################################################################
def compareData(data_df:DataFrame, connection_manager:ConnectionManager, table_name:str) -> True:
	# Return True if the data in the db file's table matches the dataframe, otherwise return False
	# Verify the inputs
	assert type(data_df) == DataFrame, "compareData: Provided value for 'data_df' must be a DataFrame object"
	assert type(connection_manager) == ConnectionManager, "compareData: Provided value for 'connection_manager' must be a ConnectionManager object"
	assert type(table_name) == str, "compareData: Provided value for 'table_name' must be a str object"
	assert table_name in getExistingTables(connection_manager = connection_manager), "compareData: Provided value for 'table_name' must be present in the db file"

	# Make sure the columns names match
	column_names_df = data_df.columns.to_list()
	column_names_db = getColumnNames(connection_manager = connection_manager, table_name = table_name)
	if column_names_df != column_names_db:
		return False

	# Make sure the row counts match
	row_count_df = len(data_df.index)
	row_count_db = getRowCount(connection_manager = connection_manager, table_name = table_name)
	if row_count_df != row_count_db:
		return False

	# Loop over the values and make sure they match
	for row_index in range(row_count_db):
		for column_name in column_names_db:
			entry_df = data_df.at[row_index, column_name]
			entry_db = readEntry(connection_manager = connection_manager, table_name = table_name, column_name = column_name, row_index = row_index)
			if entry_df != entry_db:
				return False

	# Return True to indicate that the data matches
	return True

############################################################################
### Execute the unit test comparing db file actions to dataframe actions ###
############################################################################
# Get a path to which the data should be saved and make sure cancel wasn't clicked
db_path = askSaveFilename(allowed_extensions = ["db"])
assert db_path is not None, "Unable to create db file because cancel button was clicked"

# Initialize a connection manager using this path
connection_manager = ConnectionManager(db_path = db_path, max_buffer_size = 1)

# Set the parameters for the initial table and dataframe
table_name = "table_1"
column_names = ["column_1", "column_2", "column_3"]
column_types = ["BIGINT", "BIGINT", "TEXT"]

# Create a table in the db file along with a corresponding empty dataframe and make sure they match
# Initialize the dataframe
data_dict = {}
for column_name in column_names:
	data_dict[column_name] = []
data_df = DataFrame(data_dict)
# Add the table to the db file and make the comparison
addTable(connection_manager = connection_manager, table_name = table_name, column_names = column_names, column_types = column_types)
assert compareData(data_df = data_df, connection_manager = connection_manager, table_name = table_name) == True, "Dataframe and db file don't match after initialization"

# Add three rows to each object and make sure they match
# Define the rows to add
row_to_add_1st = [1, 2, "test"]
row_to_add_2nd = [3, 4, "row"]
row_to_add_3rd = [5, 6, "values"]
# Add the rows to the dataframe
data_df.loc[0] = row_to_add_1st
data_df.loc[1] = row_to_add_2nd
data_df.loc[2] = row_to_add_3rd
# Add rows to the db file
appendRow(connection_manager = connection_manager, table_name = table_name)
appendRow(connection_manager = connection_manager, table_name = table_name)
appendRow(connection_manager = connection_manager, table_name = table_name)
replaceRow(connection_manager = connection_manager, table_name = table_name, new_row = row_to_add_1st, row_index = 0)
replaceRow(connection_manager = connection_manager, table_name = table_name, new_row = row_to_add_2nd, row_index = 1)
replaceRow(connection_manager = connection_manager, table_name = table_name, new_row = row_to_add_3rd, row_index = 2)
# Make sure the objects match
assert compareData(data_df = data_df, connection_manager = connection_manager, table_name = table_name) == True, "Dataframe and db file don't match after adding 3 initial rows"

# Replace a single entry in both objects and make sure they still match
# Define the replacement information
row_index_replace_single = 1
column_name_replace_single = "column_1"
new_entry_replace_single = 10
# Replace the entry in both objects
data_df.at[row_index_replace_single, column_name_replace_single] = new_entry_replace_single
replaceEntry(connection_manager = connection_manager, table_name = table_name, column_name = column_name_replace_single, row_index = row_index_replace_single, new_entry = new_entry_replace_single)
# Make sure the objects match
assert compareData(data_df = data_df, connection_manager = connection_manager, table_name = table_name) == True, "Dataframe and db file don't match after replacing a single entry"

# Replace an entire column in both objects and make sure they still match
# Define the replacement information
column_name_replace_column = "column_2"
new_column_replace_column = [7, 8, 9]
# Replace the column in both objects
data_df[column_name_replace_column] = new_column_replace_column
replaceColumn(connection_manager = connection_manager, table_name = table_name, column_name = column_name_replace_column, new_column = new_column_replace_column)
# Make sure the objects match
assert compareData(data_df = data_df, connection_manager = connection_manager, table_name = table_name) == True, "Dataframe and db file don't match after replacing an entire column"

# Replace an entire row in both objects and make sure they still match
# Define the replacement information
row_index_replace_row = 2
new_row_replace_row = [11, 12, "replace"]
# Replace the row in both objects
data_df.loc[row_index_replace_row] = new_row_replace_row
replaceRow(connection_manager = connection_manager, table_name = table_name, row_index = row_index_replace_row, new_row = new_row_replace_row)
# Make sure the objects match
assert compareData(data_df = data_df, connection_manager = connection_manager, table_name = table_name) == True, "Dataframe and db file don't match after replacing an entire row"

# Swap two rows in both objects and make sure they still match
# Define the swap information
row_index_1 = 0
row_index_2 = 2
# Swap the rows in the dataframe
row_1 = data_df.loc[row_index_1]
row_2 = data_df.loc[row_index_2]
data_df.loc[row_index_1] = row_2
data_df.loc[row_index_2] = row_1
# Swap the rows in the db file
swapRows(connection_manager = connection_manager, table_name = table_name, row_index_1 = row_index_1, row_index_2 = row_index_2)
# Make sure the objects match
assert compareData(data_df = data_df, connection_manager = connection_manager, table_name = table_name) == True, "Dataframe and db file don't match after swapping rows"

# Delete a row in both objects and make sure they still match
# Define the deletion information
row_index_delete_row = 0
# Delete the row from the dataframe
data_df = data_df.drop(row_index_delete_row)
data_df = data_df.reset_index(drop = True)
# Delete the row from the db file
deleteRow(connection_manager = connection_manager, table_name = table_name, row_index = row_index_delete_row)
# Make sure the objects match
assert compareData(data_df = data_df, connection_manager = connection_manager, table_name = table_name) == True, "Dataframe and db file don't match after deleting a row"

# Delete a column in both objects and make sure they still match
# Define the deletion information
column_name_delete_column = "column_3"
# Delete the column from the dataframe
data_df = data_df.drop(column_name_delete_column, axis = 1)
# Delete the column from the db file
deleteColumn(connection_manager = connection_manager, table_name = table_name, column_name = column_name_delete_column)
# Make sure the objects match
assert compareData(data_df = data_df, connection_manager = connection_manager, table_name = table_name) == True, "Dataframe and db file don't match after deleting a column"

# Close the connection manager
connection_manager.close()