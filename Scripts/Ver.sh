#! /bin/bash

archivo=main.tex
lector=zathura

for item in * 
do
    if [ ${item##*.} == tex ] ; then
        archivo=$item
    fi
done    

name=${archivo%.*}

if [ -e ${name}.pdf ] ; then
    ${lector} ${name}.pdf &
elif [ -e pdfs/*.pdf ] ;
then
    ${lector} pdfs/${name}.pdf &
elif [ -e ../pdfs/${name}.pdf ] ; 
then
    ${lector} pdfs/${name}.pdf &
else
    echo -e "[\e[31mPDF\e[0m not found]"
fi
