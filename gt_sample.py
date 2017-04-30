#coding=utf-8
# @author Oleg Urzhumtcev aka NetBUG
# @desc Fiddling around GeoTIFF

import georasters as gr
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass
# Load data
#raster = './data/slope.tif' #nasa-worldview-2016-07-09.tiff'
raster = './data/nasa-worldview-2016-07-20.tiff'
data = gr.from_file(raster)
NDV, xsize, ysize, GeoT, Projection, DataType = gr.get_geo_info(raster)

print("NDV: %s; size: %dx%d; GeoT: %s; Projection: %s; Data: %s" % (NDV, xsize, ysize, GeoT, Projection, DataType))
print()
x = 101.45
y = 66
#col, row = gr.map_pixel(x,y,GeoT[1],GeoT[-1], GeoT[0],GeoT[3])
#value = data[0,row,col]
#print("%d, %d: %s" % (col, row, repr(value)))

# Plot data
#print(data)
#plt.figure(figsize=(12, 8))
data.raster = data.raster[0]
data.plot()
plt.show()

'''
# Get some stats
data.mean()
data.sum()
data.std()

# Convert to Pandas DataFrame
df = data.to_pandas()

# Save transformed data to GeoTiff
data2 = data**2
data2.to_tiff('./data2')

# Algebra with rasters
data3 = np.sin(data.raster) / data2
data3.plot()

# Notice that by using the data.raster object,
# you can do any mathematical operation that handles
# Numpy Masked Arrays

# Find value at point (x,y) or at vectors (X,Y)
value = data.map_pixel(x,y)
'''