"""

fetching the data from the js and predicting the weather event type 
simulating a live event of weather collection 
"""
import joblib
import pandas as pd
import numpy as np
import time

# Load model
model = joblib.load('test_model.pkl')

# Load data (simulating the API data with CSV)
data = pd.read_csv('Sample_Test_Data.csv')

# Mock function to simulate fetching data as if it’s live data
def fetch_weather_data():
    # Simulating data by returning one row at a time
    for _, row in data.iterrows():
        yield row.to_dict()

# Process data to align with model's expected input
def process_data(api_data):
    df = pd.DataFrame([api_data])

    expected_features = model.feature_names_in_
    for feature in expected_features:
        if feature not in df.columns:
            df[feature] = np.nan  
    df = df[expected_features]

    return df

# Weather monitoring function
def monitor_weather(testing_mode=True):
    interval = 5 if testing_mode else 1800  # 5 seconds for testing, 30 mins for production

    for api_data in fetch_weather_data():
        processed_data = process_data(api_data)
        prediction = model.predict(processed_data)[0]

        if prediction == 1:
            print(f"Alert! Potential hurricane detected at {api_data.get('DATE')} — Take Precautions!")
        else:
            print(f"No hurricane detected at {api_data.get('DATE')}")

        # Wait for the set interval
        time.sleep(interval)

if __name__ == "__main__":
    monitor_weather(testing_mode=True)
