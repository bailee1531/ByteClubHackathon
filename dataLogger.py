from sense_hat import SenseHat
from datetime import datetime
from csv import writer

## Gets the data from the sense HAT and appends it to the list
def get_data():
    senseData = []
    senseData.append(datetime.now())
    senseData.append(sense.get_temperature())
    senseData.append(sense.get_pressure())
    senseData.append(sense.get_humidity())
    return senseData

# Creates the event listener for the joystick
sense = SenseHat()
event = sense.stick.wait_for_event()

# Opens csv files and writes column headers after the joystick is pressed downward
if event.action == 'pressed' and event.direction == 'down':
    logData = True

    # Creates the CSV file with data
    with open('data.csv', 'w', newline='') as f:
        dataWriter = writer(f)
        dataWriter.writerow(['DateTime', 'Temperature', 'Pressure', 'Humidity'])    # Sets column headers

# Stops data logging once the joystick is pressed upward
if event.action == 'pressed' and event.direction == 'up':
    logData = False

# Gets the data and writes it to the csv file
while logData:
    data = get_data()
    dataWriter.writerow(data)