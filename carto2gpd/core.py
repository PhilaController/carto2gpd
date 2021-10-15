import urllib

import geopandas as gpd
import pandas as pd
import requests
from pkg_resources import packaging

GEOPANDAS_VERSION = packaging.version.parse(gpd.__version__)


def _get_json_safely(response):
    """
    Check for JSON response errors, and if all clear,
    return the JSON data
    """
    json = response.json()  # get the JSON
    if "error" in json:
        raise ValueError(json["error"][0])

    return json


def get_size(url, table_name, where=None):
    """
    Query a CARTO database API and return the total number
    of rows in the database.

    Parameters
    ----------
    url : str
        the URL for the database API
    table_name : str
        the name of the database table to query
    where : str, optional
        the where clause to select a subset of the data

    Returns
    -------
    size : int
        the number of rows in the database

    Example
    -------
    >>> import carto2gpd
    >>> url = "https://phl.carto.com/api/v2/sql"
    >>> size = carto2gpd.get_size(url, "shootings")
    >>> size
    """
    # make the SQL query
    query = f"SELECT COUNT(*) FROM {table_name}"

    # Add a where clause
    if where:
        query += f" WHERE {where}"

    # get the response
    params = dict(q=query)
    r = requests.get(
        url,
        params=urllib.parse.urlencode(params, quote_via=urllib.parse.quote),
        headers={"Content-Type": "application/json;charset=UTF-8"},
    )
    json = _get_json_safely(r)

    return json["rows"][0]["count"]


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
    r = requests.get(
        url,
        params=urllib.parse.urlencode(params, quote_via=urllib.parse.quote),
        headers={"Content-Type": "application/json;charset=UTF-8"},
    )
    json = _get_json_safely(r)

    # convert to a GeoDataFrame
    if GEOPANDAS_VERSION >= packaging.version.parse("0.7"):
        out = gpd.GeoDataFrame.from_features(json, crs="EPSG:4326")
    else:
        out = gpd.GeoDataFrame.from_features(json, crs={"init": "epsg:4326"})

    # check if we have any geometry values
    no_geometry = out.geometry.isnull().all()
    if no_geometry:
        out = pd.DataFrame(out.drop(labels=["geometry"], axis=1))

    return out
