#coding=utf-8
# @author Oleg Urzhumtcev aka NetBUG
# @desc Fiddling around GeoTIFF

import georasters as gr

# Load data
raster = './data/nasa-worldview-2016-07-09.tiff'
data = gr.from_file(raster)

# Plot data
print(data)
data.plot()

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
