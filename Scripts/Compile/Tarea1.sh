#! /bin/bash

archivo=main.tex

for item in * 
do
    if [ ${item##*.} == tex ] ; then
        archivo=$item
    fi
done    

name=${archivo%.*}

compile=`pdflatex ${name}.tex`

# value=[ $(compile) ]
# 
# echo $value

# echo -e "[COMPILING \e[33m\e[1m${name}.tex\e[0m]"
# # if ${compile} > logs/${name}.log 2>&1 ; then
# if ${compile} ; then
#     cat ${name}.log
#     echo -e "[\e[34m\e[1mDONE\e[0m]"
# else
#     ${compile}
#     cat ${name}.log
#     echo -e "[\e[34m\e[1mFINISHED WITH ERROR\e[0m]"
# fi


