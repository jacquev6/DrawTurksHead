# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import collections
import fractions
import math
import unittest

import cairo

from .color import hsv_to_rgb
from.knot import Knot


def frange(begin, end, step):
    assert isinstance(step, fractions.Fraction)
    steps = ((end - begin) / step)
    assert steps.denominator == 1
    assert steps.numerator >= 0
    return (begin + k * step for k in xrange(steps.numerator))


def fcos(f):
    assert isinstance(f, fractions.Fraction)
    return math.cos(f * math.pi)


def fsin(f):
    assert isinstance(f, fractions.Fraction)
    return math.sin(f * math.pi)


class Coordinates(object):
    __epsilon = fractions.Fraction(1, 1000)

    def __init__(self, bights, leads, inner, outer, line):
        self.p = bights
        self.q = leads
        self.average_radius = (outer + inner) / 2
        self.delta_radius = (outer - inner - line) / 2
        self.line_width = line

    def get_inner(self, k, theta):
        x, y = self.get(k, theta)
        nx, ny = self.__get_normal(k, theta)
        return x + nx, y + ny

    def get_outer(self, k, theta):
        x, y = self.get(k, theta)
        nx, ny = self.__get_normal(k, theta)
        return x - nx, y - ny

    def get(self, k, theta):
        r = self.average_radius + self.delta_radius * fcos((self.p * theta - 2 * k) / self.q)
        x = r * fcos(theta)
        y = r * fsin(theta)
        return x, y

    def __get_normal(self, k, theta):
        x0, y0 = self.get(k, theta - self.__epsilon);
        x1, y1 = self.get(k, theta + self.__epsilon);

        dx = x1 - x0
        dy = y1 - y0
        n = math.sqrt(dx * dx + dy * dy)

        nx = -self.line_width * dy / n / 2
        ny = self.line_width * dx / n / 2

        return nx, ny


class TurksHead(object):
    """
    @todoc

    Note: all angles are in :class:`fractions.Fraction` of :math:`\pi`.
    """

    def __init__(self, bights, leads, inner, outer, line):
        self.__knot = Knot(bights, leads)
        self.__coords = Coordinates(bights, leads, inner, outer, line)
        self.inner_radius = inner
        self.outer_radius = outer
        self.line_width = line
        self.theta_step = fractions.Fraction(1, 2 * self.p * max(1, 107 // self.p))

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

        # ctx.set_source_rgb(0, 0, 1)
        # for theta in frange(0, 2, self.theta_step):
        #     ctx.move_to(self.inner_radius * fcos(theta), self.inner_radius * fsin(theta))
        #     ctx.line_to(self.outer_radius * fcos(theta), self.outer_radius * fsin(theta))
        # ctx.stroke()

        ctx.set_antialias(cairo.ANTIALIAS_NONE)
        self.__draw_strings(ctx)
        self.__redraw_intersections(ctx)
        ctx.restore()

    def __draw_strings(self, ctx):
        for string in self.__knot.strings:
            for segment in string.segments:
                self.__draw_segment(ctx, string.k, segment)

    def __draw_segment(self, ctx, k, segment):
        for theta in frange(segment.begin.theta, segment.end.theta, self.theta_step):
            r, g, b = self.__compute_color(k, theta, segment)
            ctx.set_source_rgb(r, g, b)
            self.__path_segment(ctx, k, theta, theta + self.theta_step)
            ctx.fill()

    def __compute_color(self, k, theta, segment):
        # @todo normalize theta before calling overridable methods
        # assert 0 <= theta < 2 * self.q_prime
        assert segment.begin.theta <= theta <= segment.end.theta
        altitude = segment.begin.altitude + (segment.end.altitude - segment.begin.altitude) * (theta - segment.begin.theta) / (segment.end.theta - segment.begin.theta)
        return self.compute_color_rgb(k, theta, altitude)

    def __path_segment(self, ctx, k, min_theta, max_theta):
        ctx.move_to(*self.__coords.get_outer(k, min_theta))
        for theta in frange(min_theta, max_theta, self.theta_step):
            ctx.line_to(*self.__coords.get_outer(k, theta + self.theta_step))
        for theta in frange(max_theta, min_theta, -self.theta_step):
            ctx.line_to(*self.__coords.get_inner(k, theta))
        ctx.line_to(*self.__coords.get_inner(k, min_theta))
        ctx.close_path()

    def __redraw_intersections(self, ctx):
        for string in self.__knot.strings:
            for bridge in string.bridges:
                tunnel = bridge.tunnel
                self.__path_segment(ctx, tunnel.k, tunnel.before.begin.theta, tunnel.after.end.theta)
                ctx.clip()
                self.__draw_segment(ctx, string.k, bridge.before)
                self.__draw_segment(ctx, string.k, bridge.after)
                ctx.reset_clip()
