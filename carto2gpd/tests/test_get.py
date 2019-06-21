import carto2gpd
import pytest
import pandas as pd


def test_limit():
    url = "https://phl.carto.com/api/v2/sql"
    gdf = carto2gpd.get(url, "shootings", limit=5)
    assert len(gdf) == 5


def test_fields():
    url = "https://phl.carto.com/api/v2/sql"
    fields = ["age", "fatal"]
    gdf = carto2gpd.get(url, "shootings", fields=fields, limit=5)
    assert all(col in gdf.columns for col in ["age", "fatal", "geometry"])


def test_where():
    url = "https://phl.carto.com/api/v2/sql"
    where = "fatal > 0"
    gdf = carto2gpd.get(url, "shootings", where=where, limit=5)
    assert (gdf.fatal > 0).all()


def test_bad_table():
    url = "https://phl.carto.com/api/v2/sql"
    with pytest.raises(ValueError):
        gdf = carto2gpd.get(url, "nonexistent_table", limit=5)


def test_bad_where():
    url = "https://phl.carto.com/api/v2/sql"
    where = "bad_column > 0"
    with pytest.raises(ValueError):
        gdf = carto2gpd.get(url, "shootings", where=where, limit=5)


def test_no_geometry():
    url = "https://phl.carto.com/api/v2/sql"
    df = carto2gpd.get(url, "li_com_act_licenses", limit=5)
    assert isinstance(df, pd.DataFrame)
