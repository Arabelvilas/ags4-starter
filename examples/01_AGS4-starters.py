# Import Libraries

# Install via pip 
pip install python-AGS4 pandas openpyxl matplotlib pathlib

# Import libraries and modules
from python_ags4 import AGS4
from pathlib import Path
import pandas as pd

# Check what the AGS4 module can do by listing the functions (attributes and methods) within the AGS4 class: 
print(dir(AGS4))


# Read, Convert, Validate and Export AGS4 Files

# Set the directory of your AGS file -> because your Python and AGS file are in the same folder, you can use the filename of the AGS file directly. Otherwise, you need to add the whole path as a string. For example: ags_file = 'C:/Projects/AGS_Data/...'

ags_path = '202002050937108.ags' # This is the name of your ags file.

# 1a) Load .ags file in a DataFrame (as a tuple) -> we will need Pandas from now on.
ags_dataframe = AGS4.AGS4_to_dataframe(str(ags_path))
print(type(ags_out)) # This should be a tuple. It confirms AGS4_to_dataframe() returns a tuple. However, we can't easily use the tables yet.

# 1b) Load .ags file into DataFrames:
tables, headings = AGS4.AGS4_to_dataframe(str(ags_path))
print("Groups loaded:", list(tables.keys()))

# QA: Check the GROUPS loaded as part of this dataframe
print("Groups loaded:")
print(list(ags_dict.keys()))

''' In this case:
Groups loaded:
['PROJ', 'UNIT', 'TYPE', 'TRAN', 'FILE', 'DICT', 'ABBR', 'LOCA', 'GEOL', 'BKFL', 'CDIA', 'WSTG', 'WSTD', 'ISPT', 'SAMP']
'''

# 2) Convert all numbers to numeric 
for group in tables.keys():
    tables[group] = AGS4.convert_to_numeric(tables[group]) # if you want to know more about this function: help(AGS4.convert_to_numeric)

# 3) Validate an AGS4 file
errors = AGS4.check_file(str(ags_path))

# Print validation results
if errors:
    print("Validation errors found:")
    for error in errors:
        print(f"  {error}") # Errors can be further investigated here: https://www.ags.org.uk/data-format/ags4-data-format/
else:
    print("File is valid!")

# 4a) Export .ags file into .csv file and check it in Excel
out_xlsx = Path("yourpath/01 AGS Data/202002050937108/ags_export.xlsx")

with pd.ExcelWriter(out_xlsx, engine="openpyxl") as writer:
    for group_name, df in ags_dict.items():
        if df is None:
            continue

        df = pd.DataFrame(df)  # ensure it's a DataFrame

        safe_name = str(group_name)

        df.to_excel(writer, sheet_name=safe_name, index=False)

print("Export complete:", out_xlsx)

# 4b) Export .ags file as a new .ags file:
AGS4.dataframe_to_AGS4(
    tables,
    headings,
    "202002050937108exported_file.ags"
)

# Check the GROUPS

# 1) Extract three key AGS groups and turning them into working tables for analysis. In AGS, each GROUP (e.g., LOCA, GEOL, ISPT) is essentially a table:

df_loca = tables["LOCA"].copy() 
df_geol = tables["GEOL"].copy()
df_ispt = tables["ISPT"].copy()

# Note: Using copy(), you prevent accidental modification of the original tables dictionary. Without .copy(), modifying df_loca may modify tables["LOCA"] directly.

# 2) Inspect the table structure to confirm available fields, identify key columns, etc.
print(df_loca.columns)
print(df_geol.columns)
print(df_ispt.columns)

#3) Preview the data as a quick visual validation step
df_loca.head(10) # Preview the first 10 rows of the LOCA group.
df_geol.head(10)
df_ispt.head(10)
df_ispt.tail(10) # Preview the last 10 rows of the ISPT group.
