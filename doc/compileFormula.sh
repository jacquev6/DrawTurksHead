#!/bin/sh

name=${1%.fml}

mkdir -p $name
echo "\documentclass[fleqn]{article} \usepackage{amssymb,amsmath,bm,color} \usepackage[latin1]{inputenc} \\\begin{document} \\\thispagestyle{empty} \mathindent0cm \parindent0cm \\\begin{displaymath}" > $name/$name.tex
cat $name.fml >> $name/$name.tex
echo "\end{displaymath} \end{document}" >> $name/$name.tex
cd $name

latex -interaction=nonstopmode $name.tex
#dvipng -q -T tight -bg Transparent -D 300 -o ../$name.png $name.dvi
dvipng -q -T tight -bg White -D 300 -o ../$name.png $name.dvi

cd ..
rm -rf $name
