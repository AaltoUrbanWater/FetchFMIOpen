#!/usr/bin/env python
"""Get a list of road weather stations and save as a shapefile.

Copyright (C) 2018 Tero Niemi, Aalto University School of Engineering

    This file is part of FetchFMIOpen.

    FetchFMIOpen is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    FetchFMIOpen is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with FetchFMIOpen.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import urllib
import xml.etree.ElementTree as ET
import pandas as pd
import geopandas as gpd
import shapely.wkt


if (len(sys.argv) != 2):
    print("Usage:\n"
          "./get_livi_stations.py [PATH TO OUTPUT FILE AS *.shp]")
    sys.exit()
if (not sys.argv[1].lower().endswith('.shp')):
    print('Error:\n'
          'Argument has to be a [PATH TO OUTPUT *.shp FILE]')
    sys.exit()

out_fp = sys.argv[1]
crs = {'init': 'epsg:4326'}
dataRequest = 'http://opendata.fmi.fi/' + \
    ('wfs?request=getFeature&storedquery_id=livi::observations::road::finland'
        '::timevaluepair&parameters=TA&crs=epsg:4326')

nsm = {"wml2": "http://www.opengis.net/waterml/2.0",
       "wfs": "http://www.opengis.net/wfs/2.0",
       "om": "http://www.opengis.net/om/2.0",
       "xlink": "http://www.w3.org/1999/xlink",
       "gml": "http://www.opengis.net/gml/3.2",
       "target": "http://xml.fmi.fi/namespace/om/atmosphericfeatures/1.0"
       }

fmisidList = []
regionList = []
nameList = []
posList = []

# Read the data xml from the open data archive
try:
    conts = urllib.request.urlopen(dataRequest)
except urllib.error.URLError as e:
    if (e.code == 400):     # Bad request syntax error
        # Try to read the reason from xml structure
        errorXML = e.read()
        root = ET.fromstring(errorXML)
        # TJN: Not sure if the error is always here...
        reportText = root[0][0].text
    else:   # Other errors
        # Just show the web page contents
        reportText = urllib.urlopen(dataRequest).read()
    raise ValueError(reportText)
else:   # Everything is fine
    contents = conts.read()
    root = ET.fromstring(contents)
    WFSMembers = root.findall("wfs:member", namespaces=nsm)
    for element in WFSMembers:
        fmisidList.append([])
        regionList.append([])
        nameList.append([])
        posList.append([])
        # Find fmisid and region
        for target in element.findall(".//target:LocationCollection",
                                      namespaces=nsm):
            for identifier in target.findall(".//target:Location",
                                             namespaces=nsm):
                fmisidList[-1].append(identifier.findtext(
                    "gml:identifier", namespaces=nsm).strip())
            regionList[-1].append(identifier.findtext(
                "target:region", namespaces=nsm).strip())
        # Find name and coordinates
        for point in element.findall(".//gml:Point", namespaces=nsm):
            nameList[-1].append(point.findtext(
                "gml:name", namespaces=nsm).strip())
            posList[-1].append(point.findtext(
                "gml:pos", namespaces=nsm).strip())


# Flatten the lists
posList = [val for sublist in posList for val in sublist]
regionList = [val for sublist in regionList for val in sublist]
nameList = [val for sublist in nameList for val in sublist]
fmisidList = [int(val) for sublist in fmisidList for val in sublist]

# Reverse N and E coordinates and create a wkt string from the reversed values
wktList = ["POINT (" + ' '.join(x.split(' ')[::-1]) + ")" for x in posList]

# Create a dataframe
df = pd.DataFrame({
    'WKT':  wktList,
    'fmisid':  fmisidList,
    'region':  regionList,
    'name':  nameList
    })

geometry = df['WKT'].map(shapely.wkt.loads)
df = df.drop('WKT', axis=1)
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

# Write final dataframe into a shapefile
gdf.to_file(out_fp, driver='ESRI Shapefile', encoding='utf-8')
print('Saved road weather stations to ' + out_fp)
