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

function publish {
    check
    bump
    doc
    push
}

function check {
    pep8 --ignore=E501 . || exit
}

function fix_headers {
    python scripts/fix_headers.py
}

function bump {
    previousVersion=$( grep '^version =' setup.py | sed 's/version = \"\(.*\)\"/\1/' )
    echo "Next version number? (previous: '$previousVersion')"
    read version
    sed -i -b "s/version = .*/version = \"$version\"/" setup.py
}

function doc {
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
    cd ../..
}

function push {
    echo "Break (Ctrl+c) here if something is wrong. Else, press enter"
    read foobar

    git commit -am "Publish version $version"

    sdist_upload

    git tag -m "Version $version" v$version

    git push github master master:develop
    git push --force github gh-pages
    git push --tags
}

function sdist_upload {
    cp COPYING* github
    python setup.py sdist upload
    rm -rf github/COPYING*
}


$1
