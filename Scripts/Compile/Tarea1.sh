#! /bin/bash

archivo=main.tex

for item in * 
do
    if [ ${item##*.} == tex ] ; then
        archivo=$item
    fi
done    

name=${archivo%.*}

compile=$(pdflatex ${name}.tex)

# if [ ! -d pdfs ] ;
# then 
#     echo -e "[\e[34mkdir\e[0m pdfs]"
#     mkdir pdfs
# fi
# 
# if [ ! -d build ] ;
# then 
#     echo -e "[\e[34mkdir\e[0m build]"
#     mkdir build
# fi
# 
# if [ ! -d logs ] ; then 
#     echo -e "[\e[34mkdir\e[0m logs]"
#     mkdir logs
# fi

echo -e "[COMPILING \e[33m\e[1m${name}.tex\e[0m]"
# if ${compile} > logs/${name}.log 2>&1 ; then
if ${compile} ; then
    # cat ${name}.log
    echo -e "[\e[34m\e[1mDONE\e[0m]"
else
    ${compile}
    # cat ${name}.log
    echo -e "[\e[34m\e[1mFINISHED WITH ERROR\e[0m]"
fi

# evince ${name}.pdf &

# mv ${name}.aux build
# mv ${name}.out build
# mv ${name}.log logs
# 
# mv ${name}.pdf pdfs
