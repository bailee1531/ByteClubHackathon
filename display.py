from sense_hat import SenseHat
import pandas as pd
import numpy as np
import random

## Displays a message with the color that corresponds to the probability of that event
def show_event(weather, probability):
    sense.show_message(f'{weather}', back_colour=[int(colorRange.at[probability-1, 'Red']), int(colorRange.at[probability-1, 'Green']), int(colorRange.at[probability-1, 'Blue'])], text_colour=[255, 255, 255])


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
weatherEvents = ['Rain', 'Hurricane', 'Tornado']    # list of the events to cycle through
i = 0   # starting event index

# TO DO: Get probability of events
probability = random.randint(1, 10)     # currently just using random int

if event.action == 'pressed' and event.direction == 'middle':
    displayResults = True

    while displayResults:
        # TO DO: Initially display event with highest probability
        show_event(weatherEvents[i], probability)    # currently just displaying the first one

        # determines which direction to cycle
        checkJoystick = sense.stick.get_events()
        for e in checkJoystick:
            probability = random.randint(1, 10)
            if e.action == 'pressed' and e.direction == 'left':
                show_event(weatherEvents[i + 2], probability)
            elif e.action == 'pressed' and e.direction == 'right':
                show_event(weatherEvents[i + 1], probability)
            # stops displaying
            elif e.action == 'pressed' and e.direction == 'middle':
                displayResults = False