#! /bin/bash

# Make shure that the directory ./local/bin is executable

source setup

lib=/usr/share/doc/$NAME

[ -d $lib ] || mkdir $lib

# installing scripts
cp -r $scripts $lib
cp -r $ejemplos $lib
