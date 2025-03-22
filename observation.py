"""

Observation of the environment every minute 

Questions:
--------------
1. How do we compare the averages or observations?
2. Will the change from the columns in the data be significant enough to make confident decisions? 
3. What will be our confidence store? 
4. 

Weather types:
--------------
Winter Weather 
High Wind
Tornado 
Thunderstorm Wind
Flash Flood
Strong Wind
Frost/Freeze
Hail 
Lightning
Excessive Heat
Heat
Funnel Cloud
Drought
Sleet

Type of Key Data Features we want to collect (and have available):
---------------------------------------------------------------------
1. Wind (speed / direction)
2. Temperature
3. Pressure
4. Time 

 - Concatenate all of the same weather types
"""
import pandas as pd 
from sklearn.preprocessing import StandardScaler 

# load the data 
data = pd.read_csv(r'data/hunstville_0123_1224.csv')


# grab the weather types we want 
weather_types = ['Winter Weather', 'High Wind', 'Tornado', 'Thunderstorm Wind', 'Flash Flood', 'Strong Wind', 'Frost/Freeze', 'Hail', 'Lightning', 'Excessive Heat', 'Heat', 'Funnel Cloud', 'Drought', 'Sleet']

# filter the data and put them in their own CSV files. Same weather types will go into same CSV files 
for weather in weather_types:
    weather_data = data[data['EVENT_TYPE'] == weather]
    weather_data.to_csv(f'data/{weather}.csv', index=False)

# normalize data 
# scaler = StandardScaler()

