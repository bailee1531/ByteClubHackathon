import pandas as pd
import random

# Load the existing data
file_path = "Weather_Data_Encoded.csv"  # Ensure this file is in the same directory as the script
weather_data = pd.read_csv(file_path)

# Generate simulated hurricane data
num_new_rows = 300
hurricane_data = pd.DataFrame({
    'TEMP_AIR_MEAN': [random.uniform(25, 35) for _ in range(num_new_rows)],
    'RH_MEAN': [random.uniform(85, 100) for _ in range(num_new_rows)],
    'BARO_PRES_MEAN': [random.uniform(950, 1000) for _ in range(num_new_rows)],
    'TEMP_SBE37_MEAN': [random.uniform(26, 32) for _ in range(num_new_rows)],
    'WIND_FROM_MEAN': [random.uniform(0, 360) for _ in range(num_new_rows)],
    'WIND_SPEED_MEAN': [random.uniform(20, 50) for _ in range(num_new_rows)],
    'SAL_SBE37_MEAN': [random.uniform(30, 37) for _ in range(num_new_rows)],
    'WATER_CURRENT_SPEED_MEAN': [random.uniform(1, 3) for _ in range(num_new_rows)],
    'WATER_CURRENT_DIRECTION_MEAN': [random.uniform(0, 360) for _ in range(num_new_rows)],
    'WAVE_DOMINANT_PERIOD': [random.uniform(8, 15) for _ in range(num_new_rows)],
    'WAVE_SIGNIFICANT_HEIGHT': [random.uniform(3, 10) for _ in range(num_new_rows)],
    'EVENT_TYPE': ['Hurricane'] * num_new_rows,
    'EVENT_TYPE_ENCODED': [16.0] * num_new_rows
})

# Append the new data to the existing data
updated_weather_data = pd.concat([weather_data, hurricane_data], ignore_index=True)

# Save the updated dataset
updated_file_path = "Updated_Weather_Data_Encoded.csv"
updated_weather_data.to_csv(updated_file_path, index=False)

print(f"Updated data successfully saved to: {updated_file_path}")
