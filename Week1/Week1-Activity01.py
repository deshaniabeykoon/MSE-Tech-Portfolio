import numpy as np

temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

print("Temperatures for a week (in Celsius):", temperatures)

# 1. Average temperature
average_temp = np.average(temperatures)
#print("Average temperature for a week:", average_temp)
#print("Average temperature for a week:", round(average_temp),2)
print(f"Average temperature for a week: {average_temp:.2f}°C")

# 2. Highest temperature
higest_temp = np.max(temperatures)
#print("Highest temperature for a week:", higest_temp)
print(f"Highest temperature for a week: {higest_temp:.2f}°C")

# 3. Lowest temperature
lowest_temp = np.min(temperatures)
#print("Lowest temperature for a week:", lowest_temp)
print(f"Lowest temperature for a week: {lowest_temp:.2f}°C")

# 4. Convert all temperatures to Fahrenheit
fahrenheit_temp = (temperatures * 9/5) + 32
print("Temperatures in Fahrenheit:", fahrenheit_temp)

# 5. days (by index) where the temperature was above 20°C
above_20_days = np.where(temperatures > 20)[0]
fahrenheit = ( above_20_days * 9/5) + 32
print("Days with temperature above 20°C (by index):", above_20_days)
for index in above_20_days:
    print(f"Index:{index} - Day {index}: {temperatures[index]:.2f}°C {temperatures[index]*9/5 + 32:.2f}°F")