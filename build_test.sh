#!/bin/bash

export PATH=\
/opt/buildout.python/bin:\
$PATH:

virtualenv  --clear .
bin/pip install zc.buildout
bin/buildout bootstrap
bin/buildout
make test

