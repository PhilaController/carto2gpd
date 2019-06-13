from setuptools import setup


def find_version(path):
    import re

    # path shall be a plain ascii text file.
    s = open(path, "rt").read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", s, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Version not found")


def get_requirements(filename):
    with open(filename, "r") as fh:
        return [l.strip() for l in fh]


setup(
    name="carto2gpd",
    version=find_version("carto2gpd/__init__.py"),
    author="Nick Hand",
    maintainer="Nick Hand",
    maintainer_email="nick.hand@phila.gov",
    packages=["carto2gpd"],
    description="A Python utility to query a CARTO database and return a geopandas GeoDataFrame",
    license="MIT",
    python_requires=">=3.6",
    install_requires=get_requirements("requirements.txt"),
    extras_require={"dev": get_requirements("requirements.dev.txt")},
)
