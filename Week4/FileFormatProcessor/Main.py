from DataProcessor import DataProcessor
from MathProcessor import MathProcessor

def main():
    # Replace the file path below with your actual file path
    file_path = 'D:/Yoobee/Github/MSE800-PSE/Week4/Files/sample_text.txt'  # or 'your_data_file.parquet'
    processor = DataProcessor(file_path)
    processor.load_data()
    #processor.initial_processing()

    input_value = int(input("Enter a number to calculate its sin and cos: "))
    math_processor = MathProcessor(input_value)
    math_processor.calculate_sin_cos()

    print("diameter of circle is", math_processor.area_circle(input_value))

    print("Processing complete.")

if __name__ == "__main__":
    main()