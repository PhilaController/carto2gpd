import carto2gpd
import pytest


def test_get_size():
    url = "https://phl.carto.com/api/v2/sql"

    # all shootings
    size_all = carto2gpd.get_size(url, "shootings")

    # fatal shootings
    where = "fatal > 0"
    size_fatal = carto2gpd.get_size(url, "shootings", where=where)

    assert size_all > size_fatal
