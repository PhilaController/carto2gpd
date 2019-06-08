import requests
import geopandas as gpd


def _get_json_safely(response):
    """
    Check for JSON response errors, and if all clear, 
    return the JSON data
    """
    json = response.json()  # get the JSON
    if "error" in json:
        raise ValueError("Error: %s" % json["error"])

    return json


def get(url, table_name, fields=None, where=None, limit=None):
    """
    Query a CARTO database API, returning a GeoDataFrame.

    Parameters
    ----------
    url : str
        the URL for the database API
    table_name : str
        the name of the database table to query
    fields : list of str, optional
        the name of the fields to return; the default behavior returns
        all fields
    where : str, optional
        the where clause to select a subset of the data
    limit : int, optional
        limit the returned data to this many features
    
    Example
    -------
    >>> import carto2gpd
    >>> url = "https://phl.carto.com/api/v2/sql"
    >>> where = "date_ > current_date - 30"
    >>> gdf = carto2gpd.get(url, "shootings", fields=['age', 'fatal'], where=where, limit=5)
    >>> gdf
    """
    if fields is None:
        fields = "*"
    else:
        if "the_geom" not in fields:
            fields.append("the_geom")
        fields = ",".join(fields)

    # make the SQL query
    query = f"SELECT {fields} FROM {table_name}"
    if where:
        query += f" WHERE {where}"
    if limit:
        query += f" LIMIT {limit}"

    # get the response
    params = dict(q=query, format="geojson", skipfields=["cartodb_id"])
    r = requests.get(url, params=params)
    json = _get_json_safely(r)

    # convert to a GeoDataFrame
    return gpd.GeoDataFrame.from_features(json, crs={"init": "epsg:4326"})
