import pandas as pd

# Load the Parquet file into a Pandas DataFrame
try:
    df = pd.read_parquet("D:/Yoobee/Github/MSE800-PSE/Week4/Sample_data_2.parquet", engine='pyarrow')
except FileNotFoundError:
    print("Error: Parquet file not found. Please check the file path.")
except Exception as e:
     print(f"An error occurred: {e}")
else:
    # Get the number of features (columns)
    num_features = len(df.columns)

# Print the number of features
print(f"The number of features in the Parquet file is: {num_features}")