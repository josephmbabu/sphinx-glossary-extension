#! /bin/bash

sphinx-apidoc -o source/coderst source/Code -f 
sphinx-build -b html source build
