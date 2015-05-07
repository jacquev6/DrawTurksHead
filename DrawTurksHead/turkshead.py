# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import collections
import math
import unittest

import cairo

from .color import hsv_to_rgb
from .knot import Knot
from .knot.knot import String, Segment, End, Bridge, Tunnel
from ._turkshead import Drawer


# class Colorer(object):
"""
@todoc Document the Colorer interface with either compute_color_rgb or compute_color_hsv
"""


class DefaultColorer(object):
    """
    @todoc
    """
    def compute_color_hsv(self, knot, k, theta, altitude):
        """
        @todoc
        """
        h = k * 360. / knot.d
        s = 0.5
        v = 0.5 + altitude / 2
        return h, s, v


class TurksHead(object):
    """
    @todoc
    """
    def __init__(self, bights, leads, inner, outer, line, colorer=None):
        knot = Knot(bights, leads)

        self.__p = knot.p
        self.__q = knot.q
        self.__d = knot.d
        self.__p_prime = knot.p_prime
        self.__q_prime = knot.q_prime
        self.__inner_radius = inner
        self.__outer_radius = outer
        self.__line_width = line

        self.__drawer = Drawer(
            knot=self,
            colorer=colorer or DefaultColorer(),
            strings=knot.strings,
        )


    @property
    def p(self):
        """
        @todoc
        """
        return self.__p

    @property
    def q(self):
        """
        @todoc
        """
        return self.__q

    @property
    def d(self):
        """
        @todoc
        """
        return self.__d

    @property
    def p_prime(self):
        """
        @todoc
        """
        return self.__p_prime

    @property
    def q_prime(self):
        """
        @todoc
        """
        return self.__q_prime

    @property
    def inner_radius(self):
        """
        @todoc
        """
        return self.__inner_radius

    @property
    def outer_radius(self):
        """
        @todoc
        """
        return self.__outer_radius

    @property
    def line_width(self):
        """
        @todoc
        """
        return self.__line_width

    def draw(self, ctx):
        """
        @todoc
        """
        self.__drawer.draw(ctx)
