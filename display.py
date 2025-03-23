from sense_hat import SenseHat
import pandas as pd
import numpy as np
import random
from app import monitor_weather

## Displays a message with the color that corresponds to the probability of that event
def show_event(weather, probability):
    sense.show_message(f'{weather}', back_colour = probability, text_colour=[255, 255, 255])


# dataframe of the probability values
# index 0: red
# index 9: green
colorRange = pd.DataFrame([(255.0, 0.0, 0.0), (np.nan, np.nan, np.nan), (np.nan, np.nan, np.nan),
                           (np.nan, np.nan, np.nan), (127.5, 127.5, np.nan), (np.nan, np.nan, np.nan),
                           (np.nan, np.nan, np.nan), (np.nan, np.nan, np.nan), (np.nan, np.nan, np.nan),
                           (0.0, 255.0, 0.0)], columns=['Red', 'Green', 'Blue'])

# interpolates to get rest of values in df
colorRange.interpolate(method='linear', limit_direction='forward', axis=0, inplace=True)

sense = SenseHat()
event = sense.stick.wait_for_event()    # waits for the first center press to start the display
weatherEvents = ['Drought', 'Hurricane', 'Tornado']    # list of the events to cycle through
colorMap = {'Drought': [0, 255, 0], 'Hurricane': [255, 0, 0], 'Tornado': [0, 0, 255]}

# TO DO: Get probability of events
event_return = monitor_weather(True) # currently just using random int

if event.action == 'pressed' and event.direction == 'middle':
    displayResults = True

    while displayResults:
        # TO DO: Initially display event with highest probability
        show_event(weatherEvents[event_return], colorMap.get(str(weatherEvents[event_return])))

        # determines which direction to cycle
        checkJoystick = sense.stick.get_events()
        for e in checkJoystick:
            if e.action == 'pressed' and e.direction == 'middle':
                displayResults = False
                sense.clear()