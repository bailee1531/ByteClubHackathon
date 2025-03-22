from simData import get_sim_data
from sensorData import get_data
from csv import writer

async def log_sense_data(flag):
    # Creates the CSV file with data
    with open('data.csv', 'w', newline='') as f:
        dataWriter = writer(f)
        dataWriter.writerow(['DateTime', 'Temperature', 'Pressure', 'Wind Speed'])    # Sets column headers

        # Gets the data and writes it to the csv file
        while flag:
            data, checkJoystick = get_data()
            dataWriter.writerow(data)

            for e in checkJoystick:
                if e.action == 'pressed' and e.direction == 'up':
                    flag = False

async def log_sim_data(flag, weather):
    with open('simdata.csv', 'w', newline='') as f:
        dataWriter = writer(f)
        dataWriter.writerow(['DateTime', 'Temperature', 'Pressure', 'Wind Speed'])    # Sets column headers

        while flag:
            data = get_sim_data(weather)
            dataWriter.writerow(data)