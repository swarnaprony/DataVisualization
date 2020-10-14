# Sitka Rainfall Analysis.
#exercise_16_1
#date: 15/09/2020

# Parsing the csv file header.

import csv
import matplotlib.pyplot as plt
from datetime import datetime 

file_sitka = 'C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/csv_formated_data/sitka_weather_2018_simple.csv'
file_death_valley = 'C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/csv_formated_data/death_valley_2018_simple.csv'
with open(file_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Extracting and Reading data.
    # Get date and daily rainfall amount

    dates, sitka_rainfall_amounts = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            sitka_rainfall_amount = row[3]
        except ValueError:
            print(f"Missing value for {current_date}")
        else:
            dates.append(current_date)
            sitka_rainfall_amounts.append(sitka_rainfall_amount)
print(sitka_rainfall_amounts)
print(len(dates))


# Printing the Headers and Their Positions
for index, column_header in enumerate(header_row):
   print(index, column_header)

# Plotting data in Rainfall Chart

# Plot the daily Rainfall Amount of Sitka
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, sitka_rainfall_amounts, c='green', alpha=0.5)

# Formating Plot
plt.title("Daily Rainfall Amount", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Daily Rainfall", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.ylim(0,10)

plt.show()