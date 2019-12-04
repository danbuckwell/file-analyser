'''
CSV Analyser

A Python script to load and analyse a CSV document
'''

# Library Imports
import pandas as pd
import csv_analyser_functions as functions
# Import datetime to access time and date functions
import datetime as dt

# Log Program Start Time
start_time = dt.datetime.now()

# File Path to CSV
path = r''

# Read CSV file to DataFrame
df = functions.read_file(path)

# Get List of Columns
columns = functions.get_column_names(df)

print('')

# Get number of rows
print('Total rows')
print(len(df))
print('')

# Get missing values
list_of_missing_values = []

for i in range(len(columns)):
    name = str(columns[i])
    values = functions.missing_values(df[columns[i]])
    list_of_missing_values.append([name, values[0], values[1]])

missing_values = pd.DataFrame(
    list_of_missing_values,
    columns=['Column', 'Missing Values', 'Percentage']
)

print('Number of missing values per column')
print(missing_values)
print('')

# Get unique values
list_of_unique_values = []

for i in range(len(columns)):
    name = str(columns[i])
    value = len(functions.get_unique_values(df[columns[i]]))
    list_of_unique_values.append([name, value])

unique_values = pd.DataFrame(
    list_of_unique_values,
    columns=['Column', 'Unique Values']
)

print('Number of unique values per column')
print(unique_values)

print('')

# Calculate Program Run Time
runtime = dt.datetime.now() - start_time
# Print Program Runtime
print('Execution Time: ' + str(runtime.total_seconds()) + ' seconds')
