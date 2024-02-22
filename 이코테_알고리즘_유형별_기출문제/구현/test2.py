import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import distance

def calculate_destination_coordinates(start_lat, start_lon, start_alt, distance_meters, bearing_deg):
    # Calculate destination coordinates using Haversine formula
    destination_point = distance(meters=distance_meters).destination((start_lat, start_lon), bearing_deg)

    # Extract destination latitude, longitude, and altitude
    dest_lat = destination_point.latitude
    dest_lon = destination_point.longitude
    dest_alt = start_alt  # Assuming the altitude doesn't change in this example

    return dest_lat, dest_lon, dest_alt

# 2D points generation
np.random.seed(42)
x = np.random.randint(-100, 100, 1000000)
y = np.random.randint(-100, 100, 1000000)

# Origin point (position of the PU)
p0 = np.array([0, 0])
xyz = [37.376654, 126.667303, 70]

fig, ax = plt.subplots()
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])

for i in range(0, 1000000, 10):
    # Plate
    ax.add_patch(plt.Rectangle((-100, -100), 200, 200, edgecolor='black', facecolor='none'))

    # Origin
    ax.scatter(p0[0], p0[1], c='red', marker='+', linewidth=1)

    # Target Points
    ax.plot(x[i], y[i], 'bs')

    # Origin to Target LOS Path
    ax.plot([p0[0], x[i]], [p0[1], y[i]])

    # Sensor Data
    dist = np.linalg.norm(np.array([p0[0], p0[1]]) - np.array([x[i], y[i]]))
    angle = np.degrees(np.arctan2(y[i] - p0[1], x[i] - p0[0]))

    

    # Result Data
    if x[i] < 0 and y[i] >= 0:  # Quadrant 2
        angle = abs(angle)
        x_ = dist * np.cos(np.radians(angle))
        x_ = -x_
        y_ = dist * np.sin(np.radians(angle))
    elif x[i] < 0 and y[i] < 0:  # Quadrant 3
        x_ = dist * np.cos(np.radians(angle))
        x_ = -x_
        y_ = dist * np.sin(np.radians(angle))
        y_ = -y_
    else:  # Quadrant 1,4
        x_ = dist * np.cos(np.radians(angle))
        y_ = dist * np.sin(np.radians(angle))

    # Check the result hit/miss
    x_diff = abs(x[i] - x_)
    y_diff = abs(y[i] - y_)

    if x_diff > 0.001 or y_diff > 0.001:
        print("Check This")
        print(f"x: {x[i]}, y: {y[i]}")
        print(f"x_diff: {x_diff}, y_diff: {y_diff}")



    destination_latitude, destination_longitude, destination_altitude =calculate_destination_coordinates(x,y,0,dist,angle)

    print(f"Destination Latitude: {destination_latitude}")
    print(f"Destination Longitude: {destination_longitude}")
    print(f"Destination Altitude: {destination_altitude}")

    # GPS Coordinate Result
    # result_coord_function = distance((xyz[0], xyz[1]), (x_, y_)).destination
    # latitude, longitude = result_coord_function.latitude, result_coord_function.longitude
    # print(f"Latitude: {latitude}, Longitude: {longitude}")

plt.show()
