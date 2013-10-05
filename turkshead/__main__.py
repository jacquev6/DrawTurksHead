#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright                                                                    #
#                                                                              #
# This file is part of DrawTurksHead. http://jacquev6.github.com/DrawTurksHead #
#                                                                              #
# DrawTurksHead is free software: you can redistribute it and/or modify it     #
# under the terms of the GNU Lesser General Public License as published by the #
# Free Software Foundation, either version 3 of the License, or (at your       #
# option) any later version.                                                   #
#                                                                              #
# DrawTurksHead is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License  #
# for more details.                                                            #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with DrawTurksHead. If not, see <http://www.gnu.org/licenses/>.        #
#                                                                              #
################################################################################

import optparse

import cairo

import turkshead

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

turkshead.TurksHead(options.leads, options.bights, innerRadius, outerRadius, options.line_width).draw(ctx)

img.write_to_png(options.output)
