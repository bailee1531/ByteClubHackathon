from datetime import datetime, timedelta
from csv import writer
import random

## Creates a list of the simulated data and returns it to the logging function
def get_sim_data(weather, time):
    simData = [time, sim_temp(weather), sim_pressure(weather), sim_wind(weather)]
    return simData

## Generates a temperature datapoint that is within the typical range associated
# with each weather event in Celsius and returns it to be put in data list
def sim_temp(weather):
    if weather == 'Rain':
        low, high = 7.77, 18.33
    elif weather == 'Hurricane Event':
        low, high = 26.1, 27.2
    elif weather == 'Tornado Event':
        low, high = 18.33, 28.89
    else:
        low, high = 7.21, 25.5
    return random.uniform(low, high)

## Generates a pressure datapoint that is within the typical range associated
# with each weather event in inches of Mercury and returns it to be put in data list
def sim_pressure(weather):
    if weather == 'Rain':
        low, high = 29.80, 30.20
    elif weather == 'Hurricane Event':
        low, high = 26.57, 29.94
    elif weather == 'Tornado Event':
        low, high = 23.90, 26.90
    else:
        low, high = 29.90, 30.10
    return random.uniform(low, high)

## Generates a wind speed datapoint that is within the typical range associated
# with each weather event in m/s and returns it to be put in data list
def sim_wind(weather):
    if weather == 'Rain':
        low, high = 2.0, 5.0
    elif weather == 'Hurricane Event':
        low, high = 33.0, 69.0
    elif weather == 'Tornado Event':
        low, high = 49.1, 134.11
    else:
        low, high = 3.58, 5.36
    return random.uniform(low, high)

## Calls get_sim_data in a for loop to generate 50000 lists of datapoints
# and writes them to the file line by line. Simulates time as if data
# is collected once per second
def log_sim_data(weather):
    time = datetime.now()
    with open('simdata.csv', 'a', newline='') as f:
        dataWriter = writer(f)

        for i in range(0, 50000):
            time += timedelta(seconds=1)
            data = get_sim_data(weather, time)
            dataWriter.writerow(data)