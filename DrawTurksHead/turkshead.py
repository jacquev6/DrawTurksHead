# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

"""
.. class:: Colorer

    Objects passed as the ``colorer`` argument of :class:`.TurksHead` must implement this interface.
    More precisely, they must implement **one** of the following methods:

    .. py:method:: compute_color_hsv(knot, k, theta, altitude):

        Return a tuple ``(h, s, v)`` of the color to be applied to the ``k``-th string of the ``knot``,
        at angle ``theta``, at the given ``altitude``.

        ``h`` must be between 0 and 360
        ``s`` and ``v`` must be between 0 and 1.

        :param knot: the :class:`.TurksHead` instance.
        :param k: the index of the current string. Between 0 and ``knot.d``.
        :param theta: the angle on the current string. Between 0 and ``2 * knot.q_prime * math.pi``.
        :param altitude: the altitude of the string at this point. Between -1 and 1.

    .. py:method:: compute_color_rgb(knot, k, theta, altitude):

        Return a tuple ``(r, g, b)`` of the color to be applied to the ``k``-th string of the ``knot``,
        at angle ``theta``, at the given ``altitude``.

        ``r``, ``g`` and ``b`` must be between 0 and 1.

        :param knot: the :class:`.TurksHead` instance.
        :param k: the index of the current string. Between 0 and ``knot.d``.
        :param theta: the angle on the current string. Between 0 and ``2 * knot.q_prime * math.pi``.
        :param altitude: the altitude of the string at this point. Between -1 and 1.
"""

import collections
import math
import unittest

import cairo

from .color import hsv_to_rgb
from .knot import Knot
from .knot.knot import String, Segment, End, Bridge, Tunnel
from ._turkshead import Drawer


class DefaultColorer(object):
    """
    The :class:`Colorer` used when you don't provide one explicitly to :class:`.TurksHead`.

    It uses one color per string (spread on the spectrum) and makes it darker when the string goes down.
    """
    def compute_color_hsv(self, knot, k, theta, altitude):
        # @todo Could we (automatically) add this code to the generated doc?
        h = k * 360. / knot.d
        s = 0.5
        v = 0.5 + altitude / 2
        return h, s, v


class TurksHead(object):
    """
    Turk's head knot objects.

    :param bights: the number of times the string touches the outised of the knot.
    :param leads: the number of times the string turns around the center.
    :param inner: the radius of the empty area inside the knot.
    :param outer: the radius of the knot.
    :param line: the width of the string.
    :param colorer: a :class:`.Colorer` instance. If ``None`` or not provided, a :class:`.DefaultColorer` will be used.
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
        The number of bights.
        """
        return self.__p

    @property
    def q(self):
        """
        The number of leads.
        """
        return self.__q

    @property
    def d(self):
        """
        The greatest common divisor of :attr:`~.TurksHead.p` and :attr:`~.TurksHead.q`.
        """
        return self.__d

    @property
    def p_prime(self):
        """
        :attr:`~.TurksHead.p` divided by :attr:`~.TurksHead.d`.
        """
        return self.__p_prime

    @property
    def q_prime(self):
        """
        :attr:`~.TurksHead.q` divided by :attr:`~.TurksHead.d`.
        """
        return self.__q_prime

    @property
    def inner_radius(self):
        """
        The radius of the empty area inside the knot.
        """
        return self.__inner_radius

    @property
    def outer_radius(self):
        """
        The radius of the knot.
        """
        return self.__outer_radius

    @property
    def line_width(self):
        """
        The width of the string.
        """
        return self.__line_width

    def draw(self, ctx):
        """
        Draw the knot on a :class:`cairo.Context`.
        See `documentation of PyCairo <http://www.cairographics.org/documentation/pycairo/2/reference/context.html>`__.
        """
        self.__drawer.draw(ctx)
