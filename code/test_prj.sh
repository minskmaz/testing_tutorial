#!/bin/sh

# Set test directory where this script is located
cd $(dirname $0)

echo "Run doctests"
python -m doctest -v my_program.py

echo
echo "Run unitests"
python -m unittest discover -v
