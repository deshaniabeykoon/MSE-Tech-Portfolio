from FileProcessor import FileProcessor
from DataProcessor import DataProcessor

def main():

    monthly_rainfall_file = 'D:/Yoobee/Github/MSE800-PSE/Week4/Files/1427_Rain/1427__monthly__Total_rainfall__mm.csv'
    annual_rainfall_file = 'D:/Yoobee/Github/MSE800-PSE/Week4/Files/1427_Rain/1427__annual__Total_rainfall__mm.csv'
    combined_rainfall_file = 'D:/Yoobee/Github/MSE800-PSE/Week4/Files/1427_Rain/1427__combined__Total_rainfall__mm.csv'

    rainfiledata = FileProcessor(annual_rainfall_file)
    rainfiledata.load_data()
    rainfiledata.initial_processing()

    raindata = DataProcessor(rainfiledata.data)
    raindata.load_annual_rainfall_data(rainfiledata.data)

if __name__ == "__main__":
    main()
#     main()