#coding=utf-8
# @author Oleg Urzhumtcev aka NetBUG
# @desc Fetches data from NASA EarthData locally

import math
import requests
from dateutil.parser import parse
from geopy.distance import vincenty

# MODIS_Terra_SurfaceReflectance_Bands143
# MODIS_Terra_CorrectedReflectance_Bands721
#layers = 'MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines'
layers = 'MODIS_Terra_CorrectedReflectance_Bands367,Coastlines'
bTiff = True
url = 'https://gibs.earthdata.nasa.gov/image-download?TIME=%DATE%&extent=%COORD%&epsg=4326&layers=%LAYERS%&opacities=1,1&worldfile='+('false' if bTiff else 'true')+'&format=image/geotiff&width=%W%&height=%H%'

pOut = '/tmp/webex/'
sz = 160000000
mult = 3.02

def convert_coord(x1, x2, y1, y2):
    avg_lat = min(abs(x1), abs(x2)) + abs(x2 - x1)
    ratio = vincenty((avg_lat, y1), (avg_lat, y2)).miles / vincenty((x1, y1), (x2, y1)).miles
    ratio = ratio
    print('Ratio: ' + str(ratio));
    return math.sqrt(sz / (mult * ratio)) * ratio, math.sqrt(sz / (mult * ratio))

def get_coord(coord='23.754282758933314,43.51028066217235,60.738657758933314,67.02981191217235', date='2017-04-20'):
    x1, x2, y1, y2 = [float(x) for x in coord.split(',')]
    size_x, size_y = convert_coord(x1, x2, y1, y2)
    print('Image size: ' + str(size_x) + "x" + str(size_y));
    #return
    d = parse(date)
    ds = str(d.year) + str(d.timetuple().tm_yday)
    furl = url.replace("%COORD%", coord).replace('%LAYERS%', layers).replace('%DATE%', ds).replace('%W%', str(size_x)).replace('%H%', str(size_y))
    r = requests.get(furl, stream=True)
    filename = pOut + coord + '_' + ds + ('.tiff' if bTiff else'.zip')
    with open(filename, 'wb') as fd:
      for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

if __name__ == '__main__':
    #get_coord() #coord='23.754282758933314,33.51028066217235,60.738657758933314,67.02981191217235')
    #lon, lat, lon, lat
    #get_coord(coord='94.297600000000,48.863499000000,115.614000000000,62.0000000000', date='2015-08-20') 
    get_coord(coord='35.33203125,51.06901665960,117.0703125,68.46379965520', date='2016-07-09')