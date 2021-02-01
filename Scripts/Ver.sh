#! /bin/bash

archivo=main.tex

for item in * 
do
    if [ ${item##*.} == tex ] ; then
        archivo=$item
    fi
done    

name=${archivo%.*}

if [ -e ${name}.pdf ] ; then
    evince ${name}.pdf &
elif [ -e pdfs/*.pdf ] ;
then
    evince pdfs/${name}.pdf &
elif [ -e ../pdfs/${name}.pdf ] ; 
then
    evince pdfs/${name}.pdf &
else
    echo -e "[\e[31mPDF\e[0m not found]"
fi
