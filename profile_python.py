# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import cProfile as profile
import pstats

import cairo

from DrawTurksHead import TurksHead

stats_filename = "profiling/profile_python.stats"

img = cairo.ImageSurface(cairo.FORMAT_RGB24, 1600, 1200)
ctx = cairo.Context(img)
ctx.set_source_rgb(1, 1, 0xBF / 255.)
ctx.paint()
ctx.translate(800, 600)
ctx.scale(1, -1)

profile.run("TurksHead(12, 9, 140, 590, 39).draw(ctx)", stats_filename)

img.write_to_png("profiling/reference.png")

p = pstats.Stats(stats_filename)
p.strip_dirs().sort_stats("cumtime").print_stats().print_callees()
