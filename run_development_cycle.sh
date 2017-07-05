#!/bin/bash

set -o errexit

clear

git checkout docs

python2 setup.py build

python2 setup.py test --quiet

python2 setup.py build_sphinx --builder=doctest

# pep8 --max-line-length=120 DrawTurksHead *.py doc/conf.py

python2 setup.py build_sphinx
rm -rf docs
cp -r build/sphinx/html docs
touch docs/.nojekyll
rm -f docs/.buildinfo
echo
echo "See documentation in $(pwd)/docs/index.html"
echo

echo "Development cycle OK"
