from sense_hat import SenseHat
from datetime import datetime
import numpy as np

## Gets the data from the sense HAT and appends it to the list
def get_data():
    senseData = [datetime.now(), sense.get_temperature(), sense.get_pressure()]
    pitch, roll, yaw = sense.get_accelerometer().values()
    x, y, z = sense.get_accelerometer_raw().values()
    senseData.append(calc_vel(x, y, z, pitch, roll, yaw))
    return senseData, checkJoystick

## Gets the direct cosine matrix
# theta: pitch angle in radians
# phi: roll angle in radians
# psi: yaw angle in radians
def direct_cos_mat(theta, phi, psi):
    cosPhi = np.cos(phi)
    sinPhi = np.sin(phi)
    cosTheta = np.cos(theta)
    sinTheta = np.sin(theta)
    cosPsi = np.cos(psi)
    sinPsi = np.sin(psi)

    matrix = np.array([[cosTheta*cosPsi, sinPhi*sinTheta*cosPsi - cosPhi*sinPsi, cosPhi*sinTheta*cosPsi + sinPhi*sinPsi],
                      [cosTheta*sinPsi, sinPhi*sinTheta*sinPsi + cosPhi*cosPsi, cosPhi*sinTheta*sinPsi - sinPhi*cosPsi],
                      [-sinTheta, sinPhi*cosTheta, cosPhi*cosTheta]])
    
    return matrix

## Calculates velocity
# ax: acceleration in the x axis
# ay: acceleration in the y axis
# az: acceleration in the z axis
# theta: pitch angle in radians
# phi: roll angle in radians
# psi: yaw angle in radians
# g: acceleration from gravity
def calc_vel(ax, ay, az, theta, phi, psi, g=9.81):
    matrix = direct_cos_mat(phi, theta, psi)
    aValues = np.array([ax, ay, az])
    gVector = np.array([0, 0, g])

    velDot = np.dot(matrix, aValues) - gVector
    magnitude = np.linalg.norm(velDot)
    return magnitude

# Creates the event listener for the joystick
sense = SenseHat()
event = sense.stick.wait_for_event()
checkJoystick = sense.stick.get_events()

# Opens csv files and writes column headers after the joystick is pressed downward
if event.action == 'pressed' and event.direction == 'down':
    logData = True