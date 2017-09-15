'''Generate corners of exploitation fields.
Maciej Barnaś maciej.michal.barnas@gmail.com
2017-08-17, Last edited: 2017-08-18'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d

filename = 'xyz_file1.dat'  # Name of file with DEM

def randoming_corners(input_filename='xyz_file1.dat', output_filename='xyz_fields1.dat'):

    x_raw, y_raw = np.loadtxt(filename, usecols=(0, 1), unpack=True)  # Load only x and y column from DEM file

    nr_points = 50  # Number of corners of fields
    z_min = -600  # Minumum of z coordinate of corners
    z_max = -300  # Maximum of z coordinate of corners

    # Randoming conrners
    corners_x = np.random.uniform(np.min(x_raw), np.max(x_raw), nr_points)
    corners_y = np.random.uniform(np.min(y_raw), np.max(y_raw), nr_points)
    corners_z = np.random.uniform(z_min, z_max, nr_points)

    # Sorting - two of three coordinates (one from among x and y not sorted) - and we have almost flat surface of field
    # which looks realistic
    corners_x.sort()
    corners_z.sort()

    print(corners_x)
    print(corners_y)
    print(corners_z)

    # Saving to text file
    output_filename = 'xyz_fields1.dat'
    np.savetxt(output_filename, np.c_[corners_x, corners_y, corners_z])
    print(output_filename + ' was saved.')

    return corners_x, corners_y, corners_z

corners_x, corners_y, corners_z = randoming_corners()
# Plot for checking
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.tight_layout()

ax.scatter(corners_x, corners_y, corners_z)
plt.show()