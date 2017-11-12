#!/bin/bash

export PATH=\
/opt/buildout.python/bin:\
$PATH:

virtualenv  --clear .
pip install zc.buildout
buildout bootstrap
buildout

#virtualenv  --clear .
#bin/pip install zc.buildout
#bin/buildout bootstrap
#bin/buildout
make test

