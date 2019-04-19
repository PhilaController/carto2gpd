from setuptools import setup


def find_version(path):
    import re

    # path shall be a plain ascii text file.
    s = open(path, "rt").read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", s, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Version not found")


setup(
    name="carto2sf",
    version=find_version("carto2sf/__init__.py"),
    author="Nick Hand",
    maintainer="Nick Hand",
    maintainer_email="nick.hand@phila.gov",
    description="A Python utility to query a CARTO database and return a geopandas GeoDataFrame",
    license="MIT",
)
