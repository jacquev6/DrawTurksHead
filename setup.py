#!/usr/bin/env python
# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import setuptools
import subprocess

version = "0.3.0"


def parse_pkg_config(*args):
    return [
        s[2:]
        for s
        in subprocess.check_output(["pkg-config"] + list(args)).strip().split(" ")
    ]

# @todo Support Python 3 (on Travis as well)

setuptools.setup(
    name="DrawTurksHead",
    version=version,
    description="Draw... Turk's head knots!",
    author="Vincent Jacques",
    author_email="vincent@vincent-jacques.net",
    url="http://pythonhosted.org/DrawTurksHead",
    packages=setuptools.find_packages(),
    license="MIT",
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
            ["DrawTurksHead/_turkshead.cpp"],
            include_dirs=parse_pkg_config("pycairo", "cairomm-1.0", "--cflags-only-I"),
            libraries=["boost_python"] + parse_pkg_config("cairomm-1.0", "--libs-only-l"),
        ),
    ],
    test_suite="DrawTurksHead.tests",
    command_options={
        "build_sphinx": {
            "version": ("setup.py", version),
            "release": ("setup.py", version),
            "source_dir": ("setup.py", "doc"),
        },
    },
)
