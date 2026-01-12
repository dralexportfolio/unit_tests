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
'''
db_path = Path(__file__).parent.joinpath("test.db")
table_name = "table_1"
column_names = ["column_1", "column_2"]
column_types = ["BIGINT", "BIGINT"]

addTable(db_path = db_path, table_name = table_name, column_names = column_names, column_types = column_types)
print("Full table --------> " + str(readTable(db_path = db_path, table_name = table_name)))
print(" ")

appendRow(db_path = db_path, table_name = table_name)
appendRow(db_path = db_path, table_name = table_name)
appendRow(db_path = db_path, table_name = table_name)
replaceRow(db_path = db_path, table_name = table_name, new_row = [1, 2], row_index = 0)
replaceRow(db_path = db_path, table_name = table_name, new_row = [3, 4], row_index = 1)
replaceRow(db_path = db_path, table_name = table_name, new_row = [5, 6], row_index = 2)
print("Existing tables ---> " + str(getExistingTables(db_path = db_path)))
print("Column names ------> " + str(getColumnNames(db_path = db_path, table_name = table_name)))
print("Column types ------> " + str(getColumnTypes(db_path = db_path, table_name = table_name)))
print("Row count ---------> " + str(getRowCount(db_path = db_path, table_name = table_name)))
print("Column 1 ----------> " + str(readColumn(db_path = db_path, table_name = table_name, column_name = "column_1")))
print("Column 2 ----------> " + str(readColumn(db_path = db_path, table_name = table_name, column_name = "column_2")))
print("Row 0 -------------> " + str(readRow(db_path = db_path, table_name = table_name, row_index = 0)))
print("Row 1 -------------> " + str(readRow(db_path = db_path, table_name = table_name, row_index = 1)))
print("Row 2 -------------> " + str(readRow(db_path = db_path, table_name = table_name, row_index = 2)))
print("Column 1 Row 0 ----> " + str(readEntry(db_path = db_path, table_name = table_name, column_name = "column_1", row_index = 0)))
print("Column 1 Row 1 ----> " + str(readEntry(db_path = db_path, table_name = table_name, column_name = "column_1", row_index = 1)))
print("Column 1 Row 2 ----> " + str(readEntry(db_path = db_path, table_name = table_name, column_name = "column_1", row_index = 2)))
print("Column 2 Row 0 ----> " + str(readEntry(db_path = db_path, table_name = table_name, column_name = "column_2", row_index = 0)))
print("Column 2 Row 1 ----> " + str(readEntry(db_path = db_path, table_name = table_name, column_name = "column_2", row_index = 1)))
print("Column 2 Row 2 ----> " + str(readEntry(db_path = db_path, table_name = table_name, column_name = "column_2", row_index = 2)))
print("Full table --------> " + str(readTable(db_path = db_path, table_name = table_name)))
print(" ")

replaceEntry(db_path = db_path, table_name = table_name, column_name = "column_1", row_index = 1, new_entry = 10)
print("Full table --------> " + str(readTable(db_path = db_path, table_name = table_name)))
print(" ")

replaceColumn(db_path = db_path, table_name = table_name, column_name = "column_2", new_column = [7, 8, 9])
print("Full table --------> " + str(readTable(db_path = db_path, table_name = table_name)))
print(" ")

swapRows(db_path = db_path, table_name = table_name, row_index_1 = 0, row_index_2 = 2)
print("Full table --------> " + str(readTable(db_path = db_path, table_name = table_name)))
print(" ")

deleteRow(db_path = db_path, table_name = table_name, row_index = 0)
print("Full table --------> " + str(readTable(db_path = db_path, table_name = table_name)))
print(" ")

deleteColumn(db_path = db_path, table_name = table_name, column_name = "column_2")
print("Full table --------> " + str(readTable(db_path = db_path, table_name = table_name)))
print(" ")
'''