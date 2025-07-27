# How many records is available in the attached file?

import pandas as pd

"""
Reads a Parquet file and returns the DataFrame.

Parameters:
file_path (str): The path to the Parquet file.

Returns:
pd.DataFrame: The DataFrame containing the data from the Parquet file.
    """
def read_parquet_file(file_path):
    try:
        df = pd.read_parquet(file_path, engine='pyarrow')
        return df
    except FileNotFoundError:
        print("Error: Parquet file not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_records(df):
    if df is not None:
        return len(df)
    else:
        return 0
    
def get_num_features(df):
    if df is not None:
        return len(df.columns)
    else:
        return 0

# Print the number of records in the Parquet file
print("Reading the Parquet file...")
df = read_parquet_file("D:/Yoobee/Github/MSE800-PSE/Week4/Files/Sample-1m.parquet")
num_records = count_records(df)
print(f"The number of records in the Parquet file is: {num_records}")