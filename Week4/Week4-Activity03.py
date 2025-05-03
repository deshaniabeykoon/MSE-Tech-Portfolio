import pandas as pd

search_string = "_"
with open("D:/Yoobee/Github/MSE800-PSE/Week4/sample_text.txt", "r") as data:
    lines = data.readlines()
    count = 0
    line_count = 0
    for line in lines:
        line_count += 1
        if line.find(search_string) != -1:
            print("Found in line:",line_count, "Text is",line)
            count += 1
    
    print("Total occurrences of", search_string, ":", count)