import pandas
import os

# Read data from input CSV
file_path = os.path.expanduser('~/input.csv')

with open(file_path, newline='') as file_path:
    df = pandas.read_csv(file_path)

# Add new column to data frame
df['New_Column'] = range(21, 30)


# Write data to output CSV
file_path = os.path.expanduser('~/output.csv')

with open(file_path, 'w', newline='') as file_path:
    df.to_csv(file_path, index=False)