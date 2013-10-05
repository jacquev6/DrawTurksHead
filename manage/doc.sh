# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright                                                                    #
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

rm -rf doc/build
mkdir doc/build
cd doc/build
git init
sphinx-build -b html -d doctrees .. . || exit
touch .nojekyll
echo /doctrees/ > .gitignore
git add . || exit
git commit --message "Automatic generation" || exit
git push --force ../.. HEAD:gh-pages || exit
