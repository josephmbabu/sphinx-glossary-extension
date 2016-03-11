#! /bin/bash

sphinx-apidoc -o source/coderst source/code -f 
sphinx-build -b html source build
