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

# External modules


#####################################################################
### Define unit tests for the functions related to table creation ###
#####################################################################
db_path = Path(__file__).parent.joinpath("test.db")
table_name = "table_1"
column_names = ["column_1", "column_2"]
column_types = ["BIGINT", "BIGINT"]

connection_manager = ConnectionManager(db_path = db_path)

addTable(connection_manager = connection_manager, table_name = table_name, column_names = column_names, column_types = column_types)
print("Full table --------> " + str(readTable(connection_manager = connection_manager, table_name = table_name)))
print(" ")


appendRow(connection_manager = connection_manager, table_name = table_name)
appendRow(connection_manager = connection_manager, table_name = table_name)
appendRow(connection_manager = connection_manager, table_name = table_name)
replaceRow(connection_manager = connection_manager, table_name = table_name, new_row = [1, 2], row_index = 0)
replaceRow(connection_manager = connection_manager, table_name = table_name, new_row = [3, 4], row_index = 1)
replaceRow(connection_manager = connection_manager, table_name = table_name, new_row = [5, 6], row_index = 2)
print("Existing tables ---> " + str(getExistingTables(connection_manager = connection_manager)))
print("Column names ------> " + str(getColumnNames(connection_manager = connection_manager, table_name = table_name)))
print("Column types ------> " + str(getColumnTypes(connection_manager = connection_manager, table_name = table_name)))
print("Row count ---------> " + str(getRowCount(connection_manager = connection_manager, table_name = table_name)))
print("Column 1 ----------> " + str(readColumn(connection_manager = connection_manager, table_name = table_name, column_name = "column_1")))
print("Column 2 ----------> " + str(readColumn(connection_manager = connection_manager, table_name = table_name, column_name = "column_2")))
print("Row 0 -------------> " + str(readRow(connection_manager = connection_manager, table_name = table_name, row_index = 0)))
print("Row 1 -------------> " + str(readRow(connection_manager = connection_manager, table_name = table_name, row_index = 1)))
print("Row 2 -------------> " + str(readRow(connection_manager = connection_manager, table_name = table_name, row_index = 2)))
print("Column 1 Row 0 ----> " + str(readEntry(connection_manager = connection_manager, table_name = table_name, column_name = "column_1", row_index = 0)))
print("Column 1 Row 1 ----> " + str(readEntry(connection_manager = connection_manager, table_name = table_name, column_name = "column_1", row_index = 1)))
print("Column 1 Row 2 ----> " + str(readEntry(connection_manager = connection_manager, table_name = table_name, column_name = "column_1", row_index = 2)))
print("Column 2 Row 0 ----> " + str(readEntry(connection_manager = connection_manager, table_name = table_name, column_name = "column_2", row_index = 0)))
print("Column 2 Row 1 ----> " + str(readEntry(connection_manager = connection_manager, table_name = table_name, column_name = "column_2", row_index = 1)))
print("Column 2 Row 2 ----> " + str(readEntry(connection_manager = connection_manager, table_name = table_name, column_name = "column_2", row_index = 2)))
print("Full table --------> " + str(readTable(connection_manager = connection_manager, table_name = table_name)))
print(" ")

replaceEntry(connection_manager = connection_manager, table_name = table_name, column_name = "column_1", row_index = 1, new_entry = 10)
print("Full table --------> " + str(readTable(connection_manager = connection_manager, table_name = table_name)))
print(" ")

replaceColumn(connection_manager = connection_manager, table_name = table_name, column_name = "column_2", new_column = [7, 8, 9])
print("Full table --------> " + str(readTable(connection_manager = connection_manager, table_name = table_name)))
print(" ")

swapRows(connection_manager = connection_manager, table_name = table_name, row_index_1 = 0, row_index_2 = 2)
print("Full table --------> " + str(readTable(connection_manager = connection_manager, table_name = table_name)))
print(" ")

deleteRow(connection_manager = connection_manager, table_name = table_name, row_index = 0)
print("Full table --------> " + str(readTable(connection_manager = connection_manager, table_name = table_name)))
print(" ")

deleteColumn(connection_manager = connection_manager, table_name = table_name, column_name = "column_2")
print("Full table --------> " + str(readTable(connection_manager = connection_manager, table_name = table_name)))
print(" ")

connection_manager.close()