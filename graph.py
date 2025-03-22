import pandas as pd
import matplotlib.pyplot as plt

filename = input("Enter the name of the file you want to create graphs for: ")

df = pd.read_csv(filename)
time = df["Phenomenon Time"]
temp = df["Temperature (°C)"]
pres = df["Pressure (hPa)"]
wind_speed = df["Wind Speed (m/s)"]
wind_dir = df["Wind Direction (°)"]

fig, ax = plt.subplots(2, 2)
ax[0,0].plot(time, temp, color='red', label='Temperature (°C)')
ax[0,0].set_xlabel('Time')
ax[0,0].set_ylabel('Temperature (°C)', color='red')
ax[0,0].tick_params('y', colors='red')

ax[0,1].plot(time, pres, color='blue', label='Pressure (hPa)')
ax[0,0].set_xlabel('Time')
ax[0,1].set_ylabel('Pressure (hPa)', color='blue')
ax[0,1].tick_params('y', colors='blue')


ax[1,0].plot(time, wind_speed, color='green', label='Wind Speed (m/s)')
ax[0,0].set_xlabel('Time')
ax[1,0].set_ylabel('Wind Speed (m/s)', color='green')
ax[1,0].tick_params('y', colors='green')


ax[1,1].plot(time, wind_dir, color='orange', label='Wind Direction (°)')
ax[0,0].set_xlabel('Time')
ax[1,1].set_ylabel('Wind Direction (°)', color='orange')
ax[1,1].tick_params('y', colors='orange')

plt.title('Temperature vs Time')
plt.show()