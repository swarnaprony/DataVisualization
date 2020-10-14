#exercise_16_2
#date:18/9/2020

# Parsing the csv file Headers
import csv
import matplotlib.pyplot as plt
from datetime import datetime


#filename = 'C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/csv_formated_data/sitka_weather_07-2018_simple.csv'
filename = 'C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/csv_formated_data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

# Extracting and Reading Data

    # Get dates and High and low temperature from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
print(highs)

# Printing the Headers and Their Positions
for index, column_header in enumerate(header_row):
   print(index, column_header)

# Plotting data in a Temperature Chart

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatting plot
plt.title("Sitka's Daily high and low temperatures, 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(20,150)

plt.show()
