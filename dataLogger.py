from sense_hat import SenseHat
from datetime import datetime
from csv import writer

## Gets the data from the sense HAT and appends it to the list
def get_data():
    senseData = []
    senseData.append(datetime.now())
    senseData.append(sense.get_temperature())
    senseData.append(sense.get_pressure())
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
        dataWriter.writerow(['DateTime', 'Temperature', 'Pressure'])    # Sets column headers

        # Gets the data and writes it to the csv file
        while logData:
            data = get_data()
            dataWriter.writerow(data)

            checkJoystick = sense.stick.get_events()
            for e in checkJoystick:
                if e.action == 'pressed' and e.direction == 'up':
                    logData = False