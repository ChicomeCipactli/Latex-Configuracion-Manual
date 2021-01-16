pdflatex *.tex

if [ ! -d build ] ;
then 
    mkdir build
fi

mv *.aux build
mv *.out build
mv *.log build

if [ ! -d pdfs ] ;
then 
    mkdir pdfs
fi

mv *.pdf pdfs
