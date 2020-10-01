#!/bin/bash

set -e

echo "Building conda recipe..."
conda build --variants "{python: [3.6, 3.7, 3.8]}" conda-recipe

echo "Converting conda package..."
conda convert --platform all $HOME/miniconda/conda-bld/linux-64/carto2gpd-*.tar.bz2 --output-dir conda-bld/

echo "Deploying to Anaconda.org..."
anaconda -t $ANACONDA_TOKEN upload --skip-existing conda-bld/**/carto2gpd-*.tar.bz2

echo "Successfully deployed to Anaconda.org."
exit 0