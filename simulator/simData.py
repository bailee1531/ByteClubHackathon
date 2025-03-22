import datetime
import random

def get_sim_data(weather):
    simData = [datetime.now(), sim_temp(weather), sim_pressure(weather), sim_wind(weather)]
    return simData

def sim_temp(weather):
    if weather == 'rain':
        low, high = 7.77, 18.33
    if weather == 'hurricane':
        low, high = 26.1, 27.2
    if weather == 'tornado':
        low, high = 18.33, 28.89
    return random.uniform(low, high)


def sim_pressure(weather):
    if weather == 'rain':
        low, high = 29.80, 30.20
    if weather == 'hurricane':
        low, high = 26.57, 29.94
    if weather == 'tornado':
        low, high = 23.90, 26.90
    return random.uniform(low, high)

def sim_wind(weather):
    if weather == 'rain':
        low, high = 2.0, 5.0
    if weather == 'hurricane':
        low, high = 33.0, 69.0
    if weather == 'tornado':
        low, high = 49.1, 134.11
    return random.uniform(low, high)