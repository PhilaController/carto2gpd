# carto2sf

A Python utility to query a CARTO database and return a geopandas GeoDataFrame.

# Example

```python
import carto2sf

url = "https://phl.carto.com/api/v2/sql"
where = "date_ > current_date - 30"
gdf = carto2sf.get(url, "shootings", fields=['age', 'fatal'], where=where, limit=5)

gdf.head()
```
