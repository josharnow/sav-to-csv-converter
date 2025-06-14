# sav-to-csv-converter
Python script to convert SPSS file format to CSV
------------------
([source](https://www.reddit.com/r/learnpython/comments/1jj5t2s/comment/mjktp8d/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button))

Step-by-Step Code

import pandas as pd import pyreadstat

Set the file paths

sav_file_path = 'your_file.sav' # Replace with your .sav file path csv_file_path = 'your_file.csv' # Replace with desired .csv output path

Read the .sav file

df, meta = pyreadstat.read_sav(sav_file_path)

Save to .csv

df.to_csv(csv_file_path, index=False)

print("Conversion complete:", csv_file_path)

Installation

install the required libraries using pip:

pip install pandas pyreadstat

A bit more if you’d like to include metadata or variable labels in the CSV!

Code that converts a .sav (SPSS) file to .csv with metadata and variable names/labels included in the CSV:

Python Code: Convert .sav to .csv with Metadata

import pandas as pd import pyreadstat

Set the file paths

sav_file_path = 'your_file.sav' # Replace with your actual .sav file path csv_file_path = 'your_file_with_labels.csv' # Desired output path

Read the .sav file along with metadata

df, meta = pyreadstat.read_sav(sav_file_path)

Optional: Replace variable names with labels for better readability

df.columns = [meta.variable_value_labels.get(var, var) if var in meta.variable_value_labels else var for var in df.columns]

Save to CSV

df.to_csv(csv_file_path, index=False)

Also, save the metadata (optional)

with open("variable_metadata.txt", "w", encoding="utf-8") as f: f.write("Variable Names and Labels:\n") for var in meta.column_names_to_labels: f.write(f"{var}: {meta.column_names_to_labels[var]}\n")

print("Conversion complete! CSV and metadata saved.")

This Script: • Loads your .sav file and retrieves: • DataFrame (df) with the values • Metadata (meta) containing variable labels and value labels • Optionally replaces column names with their human-readable labels • Saves a .csv file • Saves a .txt file listing variable names and their labels

You can get it more detailed and add value labels to any of the variables in your resulting CSV file, etc.
