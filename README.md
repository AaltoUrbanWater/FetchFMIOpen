# opendatafmi
A QGIS plugin to download meteorological data from the FMI open data archive

- Contributors: Teemu Kokkonen & [Tero Niemi](http://www.github.com/tjniemi/), Aalto University School of Engineering
- License: GNU GPL

### Overview
This [QGIS](http://www.qgis.org/en/site/) plugin provides a tool to download meteorological data from the [Finnish 
Meteorological Institute] (http://en.ilmatieteenlaitos.fi/) (FMI) [open data archive](https://en.ilmatieteenlaitos.fi/open-data).

### Instructions 
1. Extract the contents of OpenDataFMI.zip to QGIS plugin folder. The default location of QGIS plugin folder on Linux 
and and Windows are: 
  * \~/.qgis2/python/plugins/ 
  * C:\Users\USERNAME\\.qgis2\python\plugin\\
2. Extract the contents of fmi_stations.zip
3. In QGIS, enable the OpenDataFMI plugin 
4. Add the fmi_stations.shp to a project
5. Select a single feature (station) from the fmi_stations.shp and using the OpenDataFMI plugin download the meteorological 
data from the station.



