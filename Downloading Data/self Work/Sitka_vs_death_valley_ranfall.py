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
    information_sitka_list = []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            sitka_rainfall_amount = row[3]
        except ValueError:
            print(f"Missing value for {current_date}")
        else:
            dates.append(current_date)
            sitka_rainfall_amounts.append(sitka_rainfall_amount)
            information_sitka = {current_date: sitka_rainfall_amount}
            information_sitka_list.append(information_sitka)
print(information_sitka_list)


with open(file_death_valley) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Extracting and Reading data.
    # Get date and daily rainfall amount

    death_valley_dates, death_valley_rainfall_amounts = [], []
    death_valley_information_list = []
    for row in reader:
        death_valley_current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            death_valley_rainfall_amount = row[3]
        except ValueError:
            print(f"Missing value for {death_valley_current_date}")
        else:
            death_valley_dates.append(death_valley_current_date)
            death_valley_rainfall_amounts.append(death_valley_rainfall_amount)
            death_valley_information = {death_valley_current_date: death_valley_rainfall_amount}
            death_valley_information_list.append(death_valley_information)
print(len(death_valley_information_list))

for date in death_valley_dates:
    if date in sit

common_dates = []
sitka_rainfall = []
death_valley_rainfall = []
for date in dates, death_valley_dates:
    common_dates.append(date)


print(len(death_valley_dates))
print(len(dates))
# Printing the Headers and Their Positions
for index, column_header in enumerate(header_row):
   print(index, column_header)

# Plotting data in Rainfall Chart

# Plot the daily Rainfall Amount of Sitka
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, sitka_rainfall_amounts, c='green', alpha=0.5)
ax.plot(death_valley_dates, death_valley_rainfall_amounts, c='red', alpha=0.5)
plt.fill_between(dates, sitka_rainfall_amounts, death_valley_rainfall_amounts, facecolor='blue', alpha=0.1)

# Formating Plot
plt.title("Daily Rainfall Amount", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Daily Rainfall", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()