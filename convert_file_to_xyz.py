'''Converting DEM .asc file from www website for text file with three columns (x, y and z coordinate of terrain) and
without no data values.
Maciej Barnaś, maciej.michal.barnas@gmail.com
2017-08-08, last edited: 2017-08-18'''

import numpy as np
import matplotlib.pyplot as plt

#filename = 'DEM_file1.asc'  # Name of file downloaded from www site
#headlines = 6  # number of rows in header

def convert_asc_xyz(filename='DEM_file1.asc', headlines=6):

    with open(filename) as f:
        head = [next(f) for i in range(headlines)]

    x_start = float(head[2].split(' ')[-1].split('\n')[0])  # The least value of x coordinate
    y_start = float(head[3].split(' ')[-1].split('\n')[0])  # The least value of y coordinate
    cellsize = float(head[4].split(' ')[-1].split('\n')[0])  # Resolution of DEM file
    nodata = float(head[5].split(' ')[-1].split('\n')[0])  # Value with no data
    print('no data = ', nodata)

    all_z_temp = np.loadtxt(filename, skiprows=6)  # Import all z values from DEM file
    all_z = all_z_temp.flatten()  # All z values in one 1-D array

    xyz = np.empty([all_z_temp.shape[0] * all_z_temp.shape[1], 3])  # Empty array with 3 columns (for x, y and z coordinate)

    # Make two 1-D arrays: with all x and all y coordinates
    all_x = np.empty(all_z_temp.shape[1])
    all_y = np.empty(all_z_temp.shape[0])

    for i in range(len(all_x)):
        all_x[i] = x_start + i * cellsize

    for i in range(len(all_y)):
        all_y[i] = y_start + i * cellsize

    # Fill in array with all 3 coordinates
    xyz[:, 0] = np.tile(all_x, len(all_y))  # x coordinates recurs like abcabcabc
    xyz[:, 1] = np.repeat(all_y, len(all_x))  # y coordinate recurs like aaabbbccc
    xyz[:, 2] = all_z

    # Delete all rows with no data value
    mask = np.any(np.equal(xyz, nodata), axis=1)
    xyz1 = xyz[~mask]

    # Save array to text file
    output_filename = 'xyz_file1.dat'
    np.savetxt(output_filename, xyz1)
    print(output_filename + ' was saved.')

    return xyz

xyz = convert_asc_xyz()
# Plots for checking - they are drawed a little time!
plt.figure(1)
plt.scatter(xyz[:, 0], xyz[:, 1], c=xyz[:, 2])
plt.figure(2)
plt.plot(xyz[:, 2], lw=0.001, marker='o', markersize=5)
plt.ylim(0, 1500)
plt.show()