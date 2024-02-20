import matplotlib.pyplot as plt
import numpy as np

def local2latlon(x, y, z, origin_xyz):
    lat_scale = 1 / 100000  # Adjust this scale based on your requirements
    lon_scale = 1 / 100000  # Adjust this scale based on your requirements

    lat = origin_xyz[0] + x * lat_scale
    lon = origin_xyz[1] + y * lon_scale

    return lat, lon



# 2D points generation
np.random.seed(0)
x = np.random.randint(-100, 101, 1000000)
y = np.random.randint(-100, 101, 1000000)

# Origin point (position of the PU)
p0 = np.array([0, 0])
xyz = np.array([37.376654, 126.667303, 70])

fig, ax = plt.subplots(1, 1)
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])

for i in range(0, 1000000, 10):
    # Plate
    ax.add_patch(plt.Rectangle((-100, -100), 200, 200, edgecolor='black', facecolor='none'))

    # Origin
    ax.plot(p0[0], p0[1], 'r+', linewidth=1)

    # Target Points
    ax.plot(x[i], y[i], 'bs')

    # Origin to Target LOS Path
    ax.plot([p0[0], x[i]], [p0[1], y[i]])

    # Sensor Data
    distance = np.linalg.norm([x[i] - p0[0], y[i] - p0[1]])
    angle = np.degrees(np.arctan2(y[i] - p0[1], x[i] - p0[0]))

    # Result Data
    if x[i] < 0 and y[i] >= 0:  # Quadrant 2
        angle = np.abs(angle)
        x_ = distance * np.cos(np.radians(angle))
        x_ = -x_
        y_ = distance * np.sin(np.radians(angle))
    elif x[i] < 0 and y[i] < 0:  # Quadrant 3
        x_ = distance * np.cos(np.radians(angle))
        x_ = -x_
        y_ = distance * np.sin(np.radians(angle))
        y_ = -y_
    else:  # Quadrant 1,4
        x_ = distance * np.cos(np.radians(angle))
        y_ = distance * np.sin(np.radians(angle))

    # Check the result hit/miss
    x_diff = np.abs(x[i] - x_)
    y_diff = np.abs(y[i] - y_)

    if x_diff > 0.001 or y_diff > 0.001:
        print("Check This")
        print("x:", x[i])
        print("y:", y[i])
        print("x_diff:", x_diff)
        print("y_diff:", y_diff)

    # GPS Coordinate Result
    # xyz[0] = xyz[0] / 100000 + x_
    # xyz[1] = xyz[1] / 100000 + y_
    lat, lon = local2latlon(x_, y_, 0, xyz)
    print("Latitude:", lat, "Longitude:", lon)

    plt.pause(0.05)

plt.show()
