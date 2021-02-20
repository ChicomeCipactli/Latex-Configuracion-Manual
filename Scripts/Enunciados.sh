#! /bin/bash

archivo=main.tex
lector=zathura

# for item in * 
# do
#     if [ ${item##*.} == tex ] ; then
#         archivo=$item
#     fi
# done    
# 
# name=${archivo%.*}
# 
# if [ -e ${name}.pdf ] ; then
#     ${lector} ${name}.pdf &
# elif [ -e pdfs/*.pdf ] ;
# then
#     ${lector} pdfs/${name}.pdf &
# elif [ -e ../pdfs/${name}.pdf ] ; 
# then
#     ${lector} pdfs/${name}.pdf &
# else
#     echo -e "[\e[31mPDF\e[0m not found]"
# fi

if [ -d enunciados ] ;
then
    cd enunciados
    for pdf in *
    do
        if [ ${pdf##*.} == pdf ];
        then
            ${lector} ${pdf} &
        fi
    done
else
    echo -e "[\e[31menunciados\e[0m directory not found]"
fi
