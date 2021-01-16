if [ -e pdfs/*.pdf ] ;
then
    evince pdfs/*.pdf &
elif [ -e ../pdfs/*.pdf ]
then
    evince pdfs/*.pdf &
else
    echo -e "[\e[31mPDF\e[0m not found]"
fi

