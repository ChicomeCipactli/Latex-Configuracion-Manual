EJEMPLOS=~/Latex-Configuración-Manual/Ejemplos

nombre=$1

function readWord( ){
    read word
    if [ -z word ] ; then
        word="word"
    fi
    return word
}

echo -e "\e[1;36m¿Cuál ejemplo quieres que mueva?\e[0m"
echo -e "\e[1;36mdefault:\e[0m Tarea1"
ls $EJEMPLOS

echo -e "\e[1;36m>>\e[0m "
read ejemplo



if [ -d $EJEMPLOS/$ejemplo ] ;
then
    echo -e "\e[1;36mCopiando $ejemplo\e[0m"
    if [ $# -eq 0 ]; then
        echo -e "\e[1;36m¿Cuál es el nuevo nombre?\e[0m"
        echo -e "\e[1;36m>>\e[0m "
        read nombre
    fi
    cp -r $EJEMPLOS/$ejemplo ./$nombre
    mv $nombre/main.tex $nombre/$nombre.tex
else 
    echo -e "\e[1;36mcopiando Tarea1\e[0m"
    if [ $# -eq 0 ]; then
        echo -e "\e[1;36m¿Cuál es el nuevo nombre?\e[0m"
        echo -e "\e[1;36m>>\e[0m "
        read nombre
    fi
    # ls $EJEMPLOS/*
    # cp -r $EJEMPLOS/Tarea1 ./$nombre
    # mv $nombre/main.tex $nombre/$nombre.tex
fi
