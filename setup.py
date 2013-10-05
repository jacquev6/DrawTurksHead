#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
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

import setuptools
import textwrap
import subprocess

version = "0.1.0"


def parsePkgConfig(*args):
    return [
        s[2:]
        for s
        in subprocess.check_output(["pkg-config"] + list(args)).strip().split(" ")
    ]


_turkshead = setuptools.Extension(
    "turkshead._turkshead",
    ["turkshead/_turkshead.cpp", "turkshead/TurksHead.cpp"],
    include_dirs=parsePkgConfig("pycairo", "cairomm-1.0", "--cflags-only-I"),
    libraries=["boost_python"] + parsePkgConfig("cairomm-1.0", "--libs-only-l"),
)


if __name__ == "__main__":
    setuptools.setup(
        name="DrawTurksHead",
        version=version,
        description="Draw... Turk's head knots!",
        author="Vincent Jacques",
        author_email="vincent@vincent-jacques.net",
        url="http://jacquev6.github.com/DrawTurksHead",
        packages=[
            "turkshead",
        ],
        package_data={
            "turkshead": ["COPYING*"],
        },
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
        ],
        ext_modules=[_turkshead],
    )
