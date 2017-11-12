#!/bin/bash

pip install zc.buildout
buildout bootstrap
buildout

#virtualenv  --clear .
#bin/pip install zc.buildout
#bin/buildout bootstrap
#bin/buildout
make test

