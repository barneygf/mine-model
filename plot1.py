import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpl_toolkits.mplot3d as mp3d

# Import xyz coordinates from earlier prepared text file
DEM_filename = 'xyz_file1.dat'
x_dem_raw, y_dem_raw, z_dem_raw = np.loadtxt(DEM_filename, unpack=True)

# Make grid for surface plot
grid = 300  # Number of points for grid
x_dem1 = np.linspace(x_dem_raw.min(), x_dem_raw.max(), grid)
y_dem1 = np.linspace(y_dem_raw.min(), y_dem_raw.max(), grid)
z_dem = griddata((x_dem_raw, y_dem_raw), z_dem_raw, (x_dem1[None, :], y_dem1[:, None]), method='linear')
x_dem, y_dem = np.meshgrid(x_dem1, y_dem1)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.tight_layout()
surf = ax.plot_surface(x_dem, y_dem, z_dem, linewidth=0, alpha=0.5, cmap='terrain', rstride=3, cstride=3)

fields_fileneme = 'xyz_fields1.dat'
x_fi_raw, y_fi_raw, z_fi_raw = np.loadtxt(fields_fileneme, unpack=True)
field_corners = 5  # Number of corners for every field
color = (172/255, 225/255, 174/255, 1)
fields_zip = [list(zip(x_fi_raw, y_fi_raw, z_fi_raw))]
print('ttt: ', fields_zip[0][1])

for i in range(int((len(x_fi_raw))/5)):
    field_temp = fields_zip[5*i:5*i+4]
    field_plot = mp3d.art3d.Poly3DCollection(field_temp, linewidth=0.2)
    field_plot.set_facecolor(color)
    field_plot.set_edgecolor('k')
    field_plot.set_alpha(1)
    ax.add_collection3d(field_plot)

ax.set_zlim([np.min(z_fi_raw), 900])
plt.show()