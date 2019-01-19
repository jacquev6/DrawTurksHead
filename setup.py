#!/usr/bin/env python
# coding: utf8

# Copyright 2013-2018 Vincent Jacques <vincent@vincent-jacques.net>

import setuptools

version = "0.3.5"


class DrawTurksHeadExtension(setuptools.Extension, object):
    def __init__(self):
        setuptools.Extension.__init__(
            self,
            name="DrawTurksHead._turkshead",
            sources=["DrawTurksHead/_turkshead.cpp"],
            libraries=["boost_python"] + self.cairomm_pkgconfig("--libs-only-l"),
        )

    @property
    def include_dirs(self):
        # Computing include_dirs requires pycairo,
        # so we make it a property and import cairo lazily,
        # after it's installed through setup_requires
        import cairo
        return [cairo.get_include()] + self.cairomm_pkgconfig("--cflags-only-I")

    @include_dirs.setter
    def include_dirs(self, value):
        # Used in setuptools.Extension.__init__
        pass

    def cairomm_pkgconfig(self, flag):
        import subprocess
        pkg_config = subprocess.check_output(["pkg-config", "cairomm-1.0", flag], universal_newlines=True)
        return [part[2:] for part in pkg_config.strip().split(" ")]


setuptools.setup(
    name="DrawTurksHead",
    version=version,
    description="Draw... Turk's head knots!",
    long_description=open("README.rst").read(),
    author="Vincent Jacques",
    author_email="vincent@vincent-jacques.net",
    url="http://jacquev6.github.io/DrawTurksHead",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: 2.7",
    ],
    packages=setuptools.find_packages(),
    ext_modules=[
        DrawTurksHeadExtension(),
    ],
    test_suite="DrawTurksHead.tests",
    install_requires=[
        "pycairo",
    ],
    command_options={
        "build_sphinx": {
            "version": ("setup.py", version),
            "release": ("setup.py", version),
            "source_dir": ("setup.py", "doc"),
        },
    },
    setup_requires=[
        "pycairo",
    ],
)
