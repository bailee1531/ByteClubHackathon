from datetime import datetime
from csv import writer
import random

def get_sim_data(weather):
    simData = [datetime.now(), sim_temp(weather), sim_pressure(weather), sim_wind(weather)]
    return simData

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

def log_sim_data(weather):
    with open('simdata.csv', 'a', newline='') as f:
        dataWriter = writer(f)

        for i in range(0, 50000):
            data = get_sim_data(weather)
            dataWriter.writerow(data)