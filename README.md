# carto2gpd

[![Coverage Status](https://coveralls.io/repos/github/PhiladelphiaController/carto2gpd/badge.svg?branch=master)](https://coveralls.io/github/PhiladelphiaController/carto2gpd?branch=master)
[![PyPi version](https://img.shields.io/pypi/v/carto2gpd.svg)](https://pypi.python.org/pypi/carto2gpd/) 
[![Anaconda-Server Badge](https://anaconda.org/controllerphl/carto2gpd/badges/version.svg)](https://anaconda.org/controllerphl/carto2gpd)
[![](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/download/releases/3.6.0/) 
![t](https://img.shields.io/badge/status-stable-green.svg) 
[![](https://img.shields.io/github/license/PhiladelphiaController/carto2gpd.svg)](https://github.com/PhiladelphiaController/carto2gpd/blob/master/LICENSE)

A Python utility to query a CARTO database and return a geopandas GeoDataFrame.

# Example

```python
import carto2gpd

url = "https://phl.carto.com/api/v2/sql"
where = "date_ > current_date - 30"
gdf = carto2gpd.get(url, "shootings", fields=['age', 'fatal'], where=where, limit=5)

gdf.head()
```
