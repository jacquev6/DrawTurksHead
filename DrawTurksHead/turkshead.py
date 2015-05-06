# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import collections
import fractions
import math
import unittest

import cairo

from .color import hsv_to_rgb
from .knot import Knot
from .knot.knot import String, Segment, End, Bridge, Tunnel
from ._turkshead import Coordinates


def normalize_string(theta_step, string):
    return String(
        k=string.k,
        segments=[normalize_segment(theta_step, segment) for segment in string.segments],
        bridges=[normalize_bridge(theta_step, bridge) for bridge in string.bridges],
    )


def normalize_segment(theta_step, segment):
    return Segment(
        begin=normalize_end(theta_step, segment.begin),
        end=normalize_end(theta_step, segment.end),
    )


def normalize_bridge(theta_step, bridge):
    return Bridge(
        before=normalize_segment(theta_step, bridge.before),
        after=normalize_segment(theta_step, bridge.after),
        tunnel=normalize_tunnel(theta_step, bridge.tunnel)
    )


def normalize_tunnel(theta_step, tunnel):
    return Tunnel(
        k=tunnel.k,
        before=normalize_segment(theta_step, tunnel.before),
        after=normalize_segment(theta_step, tunnel.after),
    )


def normalize_end(theta_step, end):
    new_theta = end.theta / theta_step
    assert new_theta.denominator == 1
    return End(
        theta=new_theta.numerator,
        altitude=end.altitude,
    )


class TurksHead(object):
    """
    @todoc

    Note: all angles are in :class:`fractions.Fraction` of :math:`\pi`.
    """

    def __init__(self, bights, leads, inner, outer, line):
        self.__knot = Knot(bights, leads)
        self.inner_radius = inner
        self.outer_radius = outer
        self.line_width = line
        theta_step = fractions.Fraction(1, 2 * self.p * max(1, 509 // self.p))
        self.__strings = [normalize_string(theta_step, string) for string in self.__knot.strings]
        self.__coords = Coordinates(float(theta_step), bights, leads, inner, outer, line)

    @property
    def p(self):
        """
        @todoc
        """
        return self.__knot.p

    @property
    def q(self):
        """
        @todoc
        """
        return self.__knot.q

    @property
    def d(self):
        """
        @todoc
        """
        return self.__knot.d

    @property
    def p_prime(self):
        """
        @todoc
        """
        return self.__knot.p_prime

    @property
    def q_prime(self):
        """
        @todoc
        """
        return self.__knot.q_prime

    def compute_color_hsv(self, k, theta, altitude):
        """
        @todoc
        """
        return (k * 360. / self.d, 0.5, 0.5 + altitude / 2)

    def compute_color_rgb(self, k, theta, altitude):
        """
        @todoc
        """
        return hsv_to_rgb(*self.compute_color_hsv(k, theta, altitude))

    def draw(self, ctx):
        """
        @todoc
        """
        ctx.save()
        ctx.set_antialias(cairo.ANTIALIAS_NONE)
        self.__draw_strings(ctx)
        self.__redraw_intersections(ctx)
        ctx.restore()

    def __draw_strings(self, ctx):
        for string in self.__strings:
            for segment in string.segments:
                self.__draw_segment(ctx, string.k, segment)

    def __draw_segment(self, ctx, k, segment):
        for theta in xrange(segment.begin.theta, segment.end.theta):
            r, g, b = self.__compute_color(k, theta, segment)
            ctx.set_source_rgb(r, g, b)
            self.__path_segment(ctx, k, theta, theta + 1)
            ctx.fill()

    def __compute_color(self, k, theta, segment):
        # @todo normalize theta before calling overridable methods
        # assert 0 <= theta < 2 * self.q_prime
        assert segment.begin.theta <= theta <= segment.end.theta
        altitude = segment.begin.altitude + (segment.end.altitude - segment.begin.altitude) * float(theta - segment.begin.theta) / (segment.end.theta - segment.begin.theta)
        return self.compute_color_rgb(k, theta, altitude)

    def __path_segment(self, ctx, k, min_theta, max_theta):
        ctx.move_to(*self.__coords.get_outer(k, min_theta))
        for theta in xrange(min_theta, max_theta):
            ctx.line_to(*self.__coords.get_outer(k, theta + 1))
        for theta in xrange(max_theta, min_theta, -1):
            ctx.line_to(*self.__coords.get_inner(k, theta))
        ctx.line_to(*self.__coords.get_inner(k, min_theta))
        ctx.close_path()

    def __redraw_intersections(self, ctx):
        for string in self.__strings:
            for bridge in string.bridges:
                tunnel = bridge.tunnel
                self.__path_segment(ctx, tunnel.k, tunnel.before.begin.theta, tunnel.after.end.theta)
                ctx.clip()
                self.__draw_segment(ctx, string.k, bridge.before)
                self.__draw_segment(ctx, string.k, bridge.after)
                ctx.reset_clip()
