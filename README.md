# FetchFMIOpen
A QGIS plugin to download meteorological observation data from the FMI open data archive.

### Overview
This [QGIS](http://www.qgis.org/en/site/) plugin provides a tool to download meteorological observation data from the [Finnish 
Meteorological Institute](http://www.en.ilmatieteenlaitos.fi/) (FMI) [open data archive](https://en.ilmatieteenlaitos.fi/open-data).

Most of the observational point data available from the open data archive is downloadable using the plugin. Available datasets include:
- Daily weather observations
- Instantaneous weather observations
- Monthly weather observations
- Solar radiation observations
- Soil parameter observations
- Sea water level, temperature and wave observations

![GUI preview](./GUI_preview.png)

### Instructions 
In order to acquire data from the FMI open data archive an API-key is required. To get the key you have to [register](https://ilmatieteenlaitos.fi/rekisteroityminen-avoimen-datan-kayttajaksi).

To download the data using the tool:
1. Extract the contents of FetchFMIOpen.zip to QGIS plugin folder. The default location of QGIS plugin folder on Linux, Mac and Windows are: 
  * \~/.qgis2/python/plugins/                   (Linux, Mac)
  * C:\Users\USERNAME\\.qgis2\python\plugins\\   (Windows)
2. Extract the contents of fmi_stations.zip
3. In QGIS, enable the FetchFMIOpen plugin 
4. Add the fmi_weather_stations.shp to a project
5. Select a single feature (station) from the fmi_weather_stations.shp and using the FetchFMIOpen plugin download the weather observation data from the station. 

Note that some stations only provide certain observations. E.g. solar radiation observations are only available from Sodankylä, Jokioinen, Helsinki, Parainen, Vantaa, Jyväskylä, Sotkamo and Utsjoki stations, the sea level observations from the mareographs, and the wave etc. observations from buoys. 

### Hints
- QGIS can show e.g. OpenStreetMap or Google Map layers through the [OpenLayers Plugin](http://hub.qgis.org/projects/openlayers/wiki) which can put the FMI measurement stations on a map (Web -> OpenLayers plugin -> OpenStreetMap)
- E.g. National Land Survey of Finland (Maanmittauslaitos) has opened maps and other spatial datasets that can help locating the FMI measurement stations ([https://www.avoindata.fi/data/en/dataset](https://www.avoindata.fi/data/en/dataset))
