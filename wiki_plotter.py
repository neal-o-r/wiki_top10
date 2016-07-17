import numpy as np
import matplotlib.pyplot as plt

import matplotlib.patheffects as path_effects
from mpl_toolkits.basemap import Basemap
################################################################################
# READING 

# get the data from the lats_lons file
filename1 = "lat_lons.txt"
f = open(filename1, 'r')
data = f.readlines()
f.close()

lons = [float(x.split(",")[-1][1:-2]) for x in data]
lats = [float(x.split(",")[-2][2:]) for x in data]

names = [x.split(",")[0] for x in data]


# get the data from the size file
filename2 = "size.txt"
sizes = np.loadtxt(filename2)

################################################################################
# PLOTTING
water = "DodgerBlue"
land = "LightGreen"


m = Basemap(projection = 'merc', llcrnrlat= 51.4, urcrnrlat= 55.4, llcrnrlon=-10.5, urcrnrlon=-5, resolution='h',area_thresh=100)

m.drawcoastlines(color = 'k', linewidth = 2)
m.drawparallels(np.arange(0,360,1) ,labels=[1, 1, 0, 0], color = 'k', fontsize = 22)
m.drawmeridians(np.arange(0,360,1),labels=[0,0,0,1], color = 'k', fontsize = 22)
m.drawmapboundary(fill_color=water)
m.fillcontinents(color=land,lake_color=water)
m.drawcountries(linewidth = 2)

# get the coordinates in basemap coordinates
xx, yy = m(lons, lats)
top10 = [names[i] for i in np.argsort(sizes)[::-1][:10]]

for x, y, z, n in zip(xx, yy, sizes, names):
	
	if n in top10:
		plt.scatter(x, y, marker = 'o', color = "yellow", s = (z/75.), zorder = 200, alpha = 1, edgecolor = "black")
	
	else:
		plt.scatter(x, y, marker = 'o', color = "red", s = (z/75.), zorder = 100, alpha = 0.6, edgecolor = "black")

plt.title("Ireland's Most Interesting Towns", fontsize = 24)

plt.show()
