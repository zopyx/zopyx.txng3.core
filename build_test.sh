#!/bin/bash

export PATH=\
/opt/buildout.python/bin:\
$PATH:

virtualenv .
bin/python bootstrap.py
bin/buildout
make test

