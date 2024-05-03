# import math

# # Constants
# c = 299792458 # speed of light in m/s

# # Calculate Lorentz factor
# v = c
# gamma = 1 / math.sqrt(1 - (v**2 / c**2))

# # Time dilation
# time_dilation = gamma

# print(f"Relativistic time dilation factor at light speed: {time_dilation}")

# import math

# def relativistic_time_dilation(speed, distance):
#     c = 299792458  # speed of light in m/s
#     beta = speed / c
#     try:
#         gamma = 1 / math.sqrt(1 - beta**2)
#         relativistic_time = distance / (speed * gamma)
#         return relativistic_time
#     except ZeroDivisionError:
#         print("that wont work when dividing by zero")
    
    
    

# speed_of_light = 299792458  # m/s
# distance = 1000000  # meters

# time_dilation = relativistic_time_dilation(speed_of_light, distance)
# print("Relativistic time dilation for a person traveling at the speed of light for a distance of {} meters: {} seconds".format(distance, time_dilation))

# def time_dilation(v):
#     c = 299792458
# # speed of light in m/s gamma = 1 / math.sqrt(1 - (v2 / c2)) # Lorentz factor t = 1 
# # time in rest frame (seconds)

 
# t_dilated = gamma * t
# # time in moving reference frame

# return t_dilated

# velocity = float(input("Enter the velocity as a fraction of the speed of light: ")) dilated_time = time_dilation(velocity)

# print(f"The dilated time is {dilated_time} seconds.")

# import math

# def time_dilation(delta_t0, v):
#     c = 3.00e8  # speed of light in m/s
#     return delta_t0 / math.sqrt(1 - (v**2 / c**2))

# # Example usage:
# delta_t0 = 1  # Proper time in seconds
# v = 0.8 * 3.00e8  # Relative velocity in m/s
# delta_t = time_dilation(delta_t0, v)
# print("Dilated time:", delta_t, "seconds")

# import math

# def relativistic_mass(m0, v):
#     c = 3.00e8  # speed of light in m/s
#     return m0 / math.sqrt(1 - (v**2 / c**2))

# # Given values
# m0 = 85  # Rest mass in kg
# v = 298000000  # Velocity in m/s

# m = relativistic_mass(m0, v)
# print("Relativistic mass:", m, "kg")


# import math

# def time_dilation(delta_t0, v):
#     c = 299792458  # speed of light in m/s
#     return delta_t0 / math.sqrt(1 - (v**2 / c**2))

# # Given values
# delta_t0 = 1  # Proper time in years for Jerry
# v = 299792458  # Relative velocity in m/s

# delta_t = time_dilation(delta_t0, v)
# print("Time experienced by Tom:", delta_t, "years")

import math

def time_dilation(delta_t0, v):
    c = 299792458  # speed of light in m/s
    return delta_t0 / math.sqrt(1 - (v**2 / c**2))

# Given values
delta_t0 = 1  # Proper time in years for Tom
v = 299792458  # Relative velocity in m/s

delta_t = time_dilation(delta_t0, v)
print("Time experienced by Jerry relative to Tom:", delta_t, "years")
