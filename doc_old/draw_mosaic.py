#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
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

import cairo

import turkshead


class MyTurksHead(turkshead.TurksHead):
    def computeColorHsv(self, k, theta):
        return ((k * 360. / self.d + 240.) % 360., 0.5, 0.5 + self.getAltitude(k, theta) / 2)


width = 9
height = 5
size = 100

img = cairo.ImageSurface(cairo.FORMAT_RGB24, width * size, height * size)
ctx = cairo.Context(img)
ctx.set_source_rgb(1, 1, 0xBF / 255.)
ctx.paint()
ctx.translate(-size / 2, -size / 2)
ctx.set_source_rgb(0, 0, 0)

for leads in range(1, height + 1):
    for bights in range(1, width + 1):
        ctx.save()
        ctx.translate(size * bights, size * leads)
        t = MyTurksHead(leads, bights, size / 8. * 0.9, size / 2. * 0.9, size / 15.)
        t.draw(ctx)
        ctx.restore()

img.write_to_png("mosaic.png")
