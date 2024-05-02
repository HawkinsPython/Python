# import math

# # Constants
# c = 299792458 # speed of light in m/s

# # Calculate Lorentz factor
# v = c
# gamma = 1 / math.sqrt(1 - (v**2 / c**2))

# # Time dilation
# time_dilation = gamma

# print(f"Relativistic time dilation factor at light speed: {time_dilation}")

import math

def relativistic_time_dilation(speed, distance):
    c = 299792458  # speed of light in m/s
    beta = speed / c
    try:
        gamma = 1 / math.sqrt(1 - beta**2)
        relativistic_time = distance / (speed * gamma)
        return relativistic_time
    except ZeroDivisionError:
        print("that wont work when dividing by zero")
    
    
    

speed_of_light = 299792458  # m/s
distance = 1000000  # meters

time_dilation = relativistic_time_dilation(speed_of_light, distance)
print("Relativistic time dilation for a person traveling at the speed of light for a distance of {} meters: {} seconds".format(distance, time_dilation))