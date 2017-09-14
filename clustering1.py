import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpl_toolkits.mplot3d as mp3d
import pandas as pd

fields_fileneme = 'xyz_fields1.dat'
#x_fi_raw, y_fi_raw, z_fi_raw = np.loadtxt(fields_fileneme, unpack=True)
fi_raw = np.loadtxt(fields_fileneme, unpack=True, usecols=(0, 1, 2))
fi_raw = fi_raw.transpose()

y_pred = KMeans(n_clusters=10).fit_predict(fi_raw)
fi_raw = np.column_stack((fi_raw, y_pred.T))
print(fi_raw)

# Figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.tight_layout()

ax.scatter(fi_raw[:, 0], fi_raw[:, 1], fi_raw[:, 2], c=y_pred)

plt.show()