import numpy as np
import cv2


def get_limits(color):

    c = np.uint8([[color]])  # Convert color to NumPy array
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # Convert the BGR color to HSV color

    # Set upper and lower limits
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    # Convert the limits to NumPy arrays
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
