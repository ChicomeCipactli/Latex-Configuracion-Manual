#! /bin/bash

archivo=main.tex

for item in *
do
    if [ ${item##*.} == tex ] ; then
        archivo=${item}
    fi
done

name=${archivo%.*}

if [ ! -d pdfs ] ;
then 
    echo -e "[\e[34mkdir\e[0m pdfs]"
    mkdir pdfs
fi

if [ ! -d build ] ;
then 
    echo -e "[\e[34mkdir\e[0m build]"
    mkdir build
fi

if [ ! -d logs ] ; then 
    echo -e "[\e[34mkdir\e[0m logs]"
    mkdir logs
fi

mv ${name}.{aux,out} build
mv ${name}.log logs
mv ${name}.pdf pdfs

