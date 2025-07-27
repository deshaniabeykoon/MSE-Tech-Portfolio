import pandas as pd
import os

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        match(self.file_path.split('.')[-1]):
            case 'csv':
                self.data = pd.read_csv(self.file_path)
            case 'parquet':
                self.data = pd.read_parquet(self.file_path)
            case 'txt':
                self.data = pd.read_csv(self.file_path, sep="\t")
            case 'xlsx':
                self.data = pd.read_excel(self.file_path)
            case _:
                raise ValueError("Unsupported file format. Please use CSV, Parquet, TXT, or Excel.")
        
        print(f"Data loaded successfully from {self.file_path}")
        print(self.data.head())
        return self.data

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())