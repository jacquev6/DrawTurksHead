#!/bin/bash
# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2010 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of DrawTurksHead. http://jacquev6.github.com/DrawTurksHead #
#                                                                              #
# DrawTurksHead is free software: you can redistribute it and/or modify it     #
# under the terms of the GNU Lesser General Public License as published by the #
# Free Software Foundation, either version 3 of the License, or (at your       #
# option) any later version.                                                   #
#                                                                              #
# DrawTurksHead is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License  #
# for more details.                                                            #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with DrawTurksHead. If not, see <http://www.gnu.org/licenses/>.        #
#                                                                              #
################################################################################
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
