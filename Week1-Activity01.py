import numpy as np

temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# 1. Average temperature
average_temp = np.mean(temperatures)
print("Average temperature for a week:", round(average_temp),2)

# 2. Highest temperature
higest_temp = np.max(temperatures)
print("Highest temperature for a week:", higest_temp)

# 3. Lowest temperature
lowest_temp = np.min(temperatures)
print("Lowest temperature for a week:", lowest_temp)

# 4. Convert all temperatures to Fahrenheit
fahrenheit_temp = (temperatures * 9/5) + 32
print("Temperatures in Fahrenheit:", fahrenheit_temp)

# 5. days (by index) where the temperature was above 20°C
above_20_days = np.where(temperatures > 20)[0]
print("Days with temperature above 20°C (by index):", above_20_days)