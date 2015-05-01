# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>
"""
Import:

    >>> import cairo
    >>> from DrawTurksHead import TurksHead

.. @todo Use named parameters once they are implemented.

Create :

    >>> leads = 3
    >>> bights = 7
    >>> inner = 100
    >>> outer = 330
    >>> line = 50
    >>> knot = TurksHead(leads, bights, inner, outer, line)

Create a `Cairo <http://www.cairographics.org/pycairo/>`__ context:

    >>> img = cairo.ImageSurface(cairo.FORMAT_RGB24, 700, 700)
    >>> ctx = cairo.Context(img)
    >>> ctx.set_source_rgb(1, 1, 1)
    >>> ctx.paint()
    >>> ctx.translate(350, 350)

Draw:

    >>> knot.draw(ctx)

Save to a file:

    >>> img.write_to_png("knot.png")

@todoc Describe how to override compute_color_hsv
"""

from _turkshead import *
