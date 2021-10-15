#!/bin/bash

set -e

echo "Add setup.py file..."
echo "import setuptools; setuptools.setup()" >> setup.py

echo "Building conda recipe..."
conda build --variants "{python: $PYTHON_VERSIONS}" conda-recipe

echo "Converting conda package..."
conda convert --platform all $HOME/miniconda/conda-bld/*/carto2gpd-*.tar.bz2 --output-dir conda-bld/

echo "Deploying to Anaconda.org..."
anaconda -t $ANACONDA_TOKEN upload --skip-existing conda-bld/**/carto2gpd-*.tar.bz2

echo "Successfully deployed to Anaconda.org."
exit 0