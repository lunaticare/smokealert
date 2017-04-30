# spacehack
Models and data for Space Hack 2017 challenge

Requirements
 * georasters package for Python
 * requires sex with libgdal >= 2.0

## Amendments to `georasters` README:
 * `data.raster = data.raster[layer]` for multicolor GeoTIFF is required, otherwise multiple operations will be disabled. You can use any of the channels, or apply a function to merge them.
 * Don't forget to call `matplotlib.pyplot.show()` to show the map
 * Don't forget to import `numpy`