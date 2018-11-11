# coding: utf8

# Copyright 2015-2018 Vincent Jacques <vincent@vincent-jacques.net>

import timeit

setup = """
import cairo

from DrawTurksHead import TurksHead

img = cairo.ImageSurface(cairo.FORMAT_RGB24, 1600, 1200)
ctx = cairo.Context(img)
ctx.set_source_rgb(1, 1, 0xBF / 255.)
ctx.paint()
ctx.translate(800, 600)
ctx.scale(1, -1)
"""

print min(timeit.repeat("TurksHead(24, 18, 190, 1190, 20).draw(ctx)", repeat=10, number=1, setup=setup))
