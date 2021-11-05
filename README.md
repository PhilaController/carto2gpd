# carto2gpd


[![Coverage Status](https://coveralls.io/repos/github/PhiladelphiaController/carto2gpd/badge.svg?branch=master)](https://coveralls.io/github/PhiladelphiaController/carto2gpd?branch=master)
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/download/releases/3.7.0/)
![t](https://img.shields.io/badge/status-stable-green.svg)
[![](https://img.shields.io/github/license/PhiladelphiaController/carto2gpd.svg)](https://github.com/PhiladelphiaController/carto2gpd/blob/master/LICENSE)
[![PyPi version](https://img.shields.io/pypi/v/carto2gpd.svg)](https://pypi.python.org/pypi/carto2gpd/)
[![Anaconda-Server Badge](https://anaconda.org/controllerphl/carto2gpd/badges/version.svg)](https://anaconda.org/controllerphl/carto2gpd)

A Python utility to query a CARTO database and return a geopandas GeoDataFrame.

## Installation

Via conda:

```
conda install -c controllerphl carto2gpd
```

Via PyPi:

```
pip install carto2gpd
```

## Example

```python
import carto2gpd

url = "https://phl.carto.com/api/v2/sql"
where = "date_ > current_date - 30"
gdf = carto2gpd.get(url, "shootings", fields=['age', 'fatal'], where=where, limit=5)

gdf.head()
```

There is also a utility function to get the size of a CARTO database:

```python
url = "https://phl.carto.com/api/v2/sql"
size = carto2gpd.get_size(url, "shootings")
size
```
