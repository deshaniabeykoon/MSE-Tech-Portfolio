# extract flower names from the dataset in IrisData.py
from IrisData import IrisData

def main():
    # Create an instance of the IrisData class
    iris_data = IrisData()

    # # Load the dataset
    # iris_data.load_data()

    # # Describe the dataset
    # iris_data.describe_data()

    # Read and print flower names
    iris_data.read_flower_names()
    # Print the number of records in the dataset

if __name__ == "__main__":
    main()