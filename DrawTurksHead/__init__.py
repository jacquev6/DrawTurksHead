# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>
"""
Import:

    >>> import cairo
    >>> from DrawTurksHead import TurksHead

Create a Turk's head:

    >>> knot = TurksHead(leads=3, bights=7, inner=50, outer=200, line=30)

Create a `Cairo <http://www.cairographics.org/pycairo/>`__ context:

    >>> img = cairo.ImageSurface(cairo.FORMAT_RGB24, 440, 440)
    >>> ctx = cairo.Context(img)
    >>> ctx.set_source_rgb(1, 1, 1)
    >>> ctx.paint()
    >>> ctx.translate(220, 220)

Draw the Turk's head on the Cairo context:

    >>> knot.draw(ctx)

Save the result to a file:

    >>> img.write_to_png("doc/doctest/1.png")

.. figure:: doctest/1.png
    :align: center

    ``doc/doctest/1.png``

@todoc Describe how to override compute_color_hsv

Let's define a utility method:

    >>> def draw_to_png(knot, filename):
    ...   img = cairo.ImageSurface(cairo.FORMAT_RGB24, 440, 440)
    ...   ctx = cairo.Context(img)
    ...   ctx.set_source_rgb(1, 1, 1)
    ...   ctx.paint()
    ...   ctx.translate(220, 220)
    ...   knot.draw(ctx)
    ...   img.write_to_png(filename)

You can choose the color of the drawing by overriding the :meth:`.TurksHead.compute_color_hsv` method:

    >>> class MyTurksHead(TurksHead):
    ...   def compute_color_hsv(self, k, theta):
    ...     h = 180 + k * 360 / self.d
    ...     s = 1
    ...     v = .5 + self.get_altitude(k, theta) / 2
    ...     return h, s, v
    >>> knot = MyTurksHead(leads=3, bights=7, inner=50, outer=200, line=30)
    >>> draw_to_png(knot, "doc/doctest/2.png")

.. figure:: doctest/2.png
    :align: center

    ``doc/doctest/2.png``

Or:

    >>> class MyTurksHead(TurksHead):
    ...   def compute_color_hsv(self, k, theta):
    ...     h, s, v = super(MyTurksHead, self).compute_color_hsv(k, theta)
    ...     s = 0.25
    ...     v = v / 2
    ...     return h, s, v
    >>> knot = MyTurksHead(leads=3, bights=7, inner=50, outer=200, line=30)
    >>> draw_to_png(knot, "doc/doctest/3.png")

.. figure:: doctest/3.png
    :align: center

    ``doc/doctest/3.png``
"""

from _turkshead import *
