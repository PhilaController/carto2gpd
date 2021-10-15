#!/bin/bash

set -e

echo "Building conda recipe..."
conda build --variants "{python: $PYTHON_VERSIONS}" conda-recipe

echo "Converting conda package..."
conda convert --platform all /usr/share/miniconda/conda-bld/linux-64/carto2gpd-*.tar.bz2 --output-dir conda-bld/

exit 0