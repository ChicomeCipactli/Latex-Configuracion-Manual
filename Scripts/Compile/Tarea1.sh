#! /bin/bash

archivo=main.tex

for item in * 
do
    if [ ${item##*.} == tex ] ; then
        archivo=$item
    fi
done    

name=${archivo%.*}

pdflatex ${name}.tex

