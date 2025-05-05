# Load data from - print the name of flowers? : https://archive.ics.uci.edu/dataset/53/iris
from ucimlrepo import fetch_ucirepo
import pandas as pd

"""
A class to handle the Iris dataset.

Attributes:
    file_path (str): The path to the Iris dataset CSV file.
    df (pd.DataFrame): The DataFrame containing the Iris dataset.
"""
class IrisData:

    # fetch dataset 
    iris = fetch_ucirepo(id=53) 

    def __init__(self):
        """
        Initializes the IrisData class and loads the dataset.
        """
        self.file_path = self.iris.data
        self.df = None


    def describe_data(self):
        """
        Prints the first 5 rows of the dataset and its summary.
        """
        if self.df is not None:

            # data (as pandas dataframes) 
            # X = iris.data.features 
            # y = iris.data.targets
            x = self.iris.data.features
            y = self.iris.data.targets

            # metadata 
            # print(iris.metadata)
            print("Metadata:")
            print(self.iris.metadata) 

            # variable information 
            print(self.iris.variables)

        else:
            print("Data not loaded. Please load the data first.")

    def load_data(self):
        """
        Loads the Iris dataset into a DataFrame.
        """
        if self.df is None:
            # Load the dataset into a DataFrame
            self.df = pd.DataFrame(self.iris.data.features, columns=self.iris.data.feature_names)
            print("Data loaded successfully.")
            print(self.df.head())
        else:
            print("Data already loaded.")


    def read_flower_names(self):
        # Extract flower names (target)
        flower_names = self.iris.data.targets
        #print(flower_names.columns)
        unique_flowers = flower_names['class'].unique()
        print("flower names are", unique_flowers)