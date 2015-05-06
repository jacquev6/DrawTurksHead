# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import optparse

import cairo

from . import TurksHead

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--bights", type="int", default=8, help="Bights")
    parser.add_option("--leads", type="int", default=6, help="Leads")
    parser.add_option("--output", type="string", default="mosaic.png", help="Output file")
    parser.add_option("--base-size", type="int", default=100, help="Increase for bigger image")
    options, arguments = parser.parse_args()

    base_size = options.base_size

    img = cairo.ImageSurface(cairo.FORMAT_RGB24, options.bights * 2 * base_size, options.leads * 2 * base_size)
    ctx = cairo.Context(img)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    ctx.translate(-base_size, -base_size)

    for p in range(1, options.bights + 1):
        for q in range(1, options.leads + 1):
            ctx.save()
            ctx.translate(p * 2 * base_size, q * 2 * base_size)
            TurksHead(p, q, base_size // 4, 9 * base_size // 10, base_size // 10).draw(ctx)
            ctx.restore()

    img.write_to_png(options.output)
