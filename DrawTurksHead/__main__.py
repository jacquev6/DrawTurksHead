# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import optparse

import cairo

from . import TurksHead

parser = optparse.OptionParser()
parser.add_option("--width", type="int", default=800, help="Width")
parser.add_option("--height", type="int", default=600, help="Height")
parser.add_option("--bights", type="int", default=4, help="Bights")
parser.add_option("--leads", type="int", default=3, help="Leads")
parser.add_option("--radius-variation", type="int", default=200, help="Radius variation")
parser.add_option("--line-width", type="int", default=50, help="Radius variation")
parser.add_option("--output", type="string", default="turkshead.png", help="Output file")
options, arguments = parser.parse_args()

width = options.width
height = options.height
outerRadius = min(width, height) / 2 - 10
innerRadius = outerRadius - options.radius_variation

img = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
ctx = cairo.Context(img)
ctx.set_source_rgb(1, 1, 0xBF / 255.)
ctx.paint()
ctx.translate(width / 2, height / 2)
ctx.scale(1, -1)

TurksHead(options.leads, options.bights, innerRadius, outerRadius, options.line_width).draw(ctx)

img.write_to_png(options.output)
