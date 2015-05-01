#!/usr/bin/env python
# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import setuptools
import subprocess

version = "0.2.1"


def parse_pkg_config(*args):
    return [
        s[2:]
        for s
        in subprocess.check_output(["pkg-config"] + list(args)).strip().split(" ")
    ]

# @todo Add unit tests, reference them here to be run by setup.py test, change .travis.yml to run them (with coveralls)
# @todo Support Python 3 (on Travis as well)

setuptools.setup(
    name="DrawTurksHead",
    version=version,
    description="Draw... Turk's head knots!",
    author="Vincent Jacques",
    author_email="vincent@vincent-jacques.net",
    url="http://pythonhosted.org/DrawTurksHead",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
    ext_modules=[
        setuptools.Extension(
            "DrawTurksHead._turkshead",
            ["DrawTurksHead/turkshead_mod.cpp", "DrawTurksHead/turkshead.cpp"],
            include_dirs=parse_pkg_config("pycairo", "cairomm-1.0", "--cflags-only-I"),
            libraries=["boost_python"] + parse_pkg_config("cairomm-1.0", "--libs-only-l"),
        ),
    ],
)
