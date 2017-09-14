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
#print(fi_raw)
head = ['x', 'y', 'z', 'field_number']
df = pd.DataFrame(fi_raw, columns=head)
#print(df)

# Figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.tight_layout()

color = (172/255, 225/255, 174/255, 1)
grouped = df.groupby('field_number')
df.sort_values(['x', 'y'], inplace=True)
for name, group in grouped:
    print(name)
    #print(group)
    verts_field = [list(zip(group['x'], group['y'], group['z']))]
    print(verts_field)
    expl = mp3d.art3d.Poly3DCollection(verts_field, linewidth=0.2)
    expl.set_facecolor(color)
    expl.set_edgecolor('k')
    ax.add_collection3d(expl)

#ax.scatter(fi_raw[:, 0], fi_raw[:, 1], fi_raw[:, 2], c=y_pred)
ax.set_xlim([np.min(df['x']), np.max(df['x'])])
ax.set_ylim([np.min(df['y']), np.max(df['y'])])
ax.set_zlim([-700, -300])

plt.show()