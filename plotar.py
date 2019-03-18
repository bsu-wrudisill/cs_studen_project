import numpy as np
from netCDF4 import Dataset
from matplotlib import pyplot as plt
import numpy.ma as ma
from matplotlib import rcParams

PathToFile = "gfs_20190226_00.nc"
ds = Dataset(PathToFile)

U = ds["UGRD_P0_L100_GLL0"][:,:,:]
V = ds["VGRD_P0_L100_GLL0"][:,:,:]
#Q = ds["vgrd_p0_l100_gll0"][:,:,:]

# mean along pressure coords
u_mn = U.mean(axis=0)
v_mn = V.mean(axis=0)

# magnitude of wind vector
wmag = (u_mn**2)*(v_mn**2)**.5

# create mesh grid for plotting 
yy      = np.arange(0, v_mn.shape[0], 2)
xx      = np.arange(0, v_mn.shape[1], 2)
points  = np.meshgrid(yy, xx)                                 
xi      = np.arange(0, v_mn.shape[0])
yi      = np.arange(0, v_mn.shape[1])
xii, yii = np.meshgrid(yi,xi)


# create figure 
fig,ax = plt.subplots()

# plot magnitude
ax.imshow(wmag,zorder=1, alpha=.9, cmap='magma')

# plot wind barbs 
ax.quiver(xii[points], yii[points], u_mn[points], v_mn[points],zorder=2)

#save figure 
plt.savefig('testwind')

