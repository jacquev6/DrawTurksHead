# coding: utf8

# Copyright 2015-2018 Vincent Jacques <vincent@vincent-jacques.net>

import cProfile as profile
import pstats

import cairo

from DrawTurksHead import TurksHead

stats_filename = "/tmp/profile.stats"

img = cairo.ImageSurface(cairo.FORMAT_RGB24, 3200, 2400)
ctx = cairo.Context(img)
ctx.set_source_rgb(1, 1, 0xBF / 255.)
ctx.paint()
ctx.translate(1600, 1200)
ctx.scale(1, -1)

profile.run("TurksHead(24, 18, 190, 1190, 20).draw(ctx)", stats_filename)

img.write_to_png("profiling/reference.png")

p = pstats.Stats(stats_filename)
p.strip_dirs().sort_stats("cumtime").print_stats().print_callees()
