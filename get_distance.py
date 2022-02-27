import math
import sys

from lxml import etree
from geopy import distance

GPX_NAMESPACE = 'http://www.topografix.com/GPX/1/0'
GROUNDSPEAK_NAMESPACE = 'http://www.groundspeak.com/cache/1/0/1'
NAMESPACES = { 'gpx': GPX_NAMESPACE }

def parse_gpx(gpx, latitude, longitude, radius):

	xml = etree.parse(gpx)
	
	for wpt in xml.xpath('//gpx:wpt', namespaces = NAMESPACES):
		gpx_name = wpt.find('.//{' + GPX_NAMESPACE + '}name').text
		groundspeak_name = wpt.find('.//{' + GROUNDSPEAK_NAMESPACE + '}name').text
		wpt_lat = float(wpt.attrib['lat'])
		wpt_lon = float(wpt.attrib['lon'])
		
		d = round(distance.distance((latitude, longitude), (wpt_lat, wpt_lon)).m)
		
		if d <= radius:
			print(gpx_name + ';' + groundspeak_name + ';' + str(d))

if len(sys.argv) < 4:
	print('Parameter error! Usage: <gpx> <latitude> <longitude> <radius>', file=sys.stderr)
else:
	gpx = sys.argv[1]
	latitude = float(sys.argv[2])
	longitude = float(sys.argv[3])
	radius = float(sys.argv[4])
	
	parse_gpx(gpx, latitude, longitude, radius)