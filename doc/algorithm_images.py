#!/usr/bin/env python
# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import itertools
import fractions
import math
import os.path

import cairo


def create(directory):
    hcell = 40
    cells = 7
    create_wave_for_small_pqs(directory, hcell, cells)
    create_families_for_small_pqs(directory, hcell, cells)


def create_wave_for_small_pqs(directory, hcell, cells):
    cell = 2 * hcell

    def draw(ctx, p, q):
        def coord(theta):
            r = hcell * (3 + math.cos(p * theta / q)) / 5
            return r * math.cos(theta), r * math.sin(theta)

        if fractions.gcd(p, q) != 1:
            ctx.set_source_rgb(1, 0.8, 0.8)
            if p == 3 and q == 6:
                ctx.set_source_rgb(1, 0.6, 0.6)
            ctx.rectangle(-hcell, -hcell, cell, cell)
            ctx.fill()

        ctx.set_source_rgb(0, 0, 0)
        ctx.move_to(*coord(0))
        for i in range(1, 2 * q * 25):
            theta = i * math.pi / 25
            ctx.line_to(*coord(theta))
        ctx.close_path()
        ctx.stroke()

    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, cell * cells, cell * cells)
    ctx = cairo.Context(img)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    ctx.translate(hcell, hcell)
    ctx.scale(1, -1)

    for p in range(cells):
        for q in range(cells):
            ctx.save()
            ctx.translate(cell * p, -cell * q)
            draw(ctx, p + 1, q + 1)
            ctx.restore()

    filename = os.path.join(directory, "wave_for_small_pqs.png")
    img.write_to_png(filename)


def create_families_for_small_pqs(directory, hcell, cells):
    cell = 2 * hcell

    def draw(ctx, p, q):
        for k, color in zip(
            range(fractions.gcd(p, q)),
            itertools.cycle([
                (.7, 0, 0), (0, .7, 0), (0, 0, .7), (0, .7, .7),
                (.7, .7, 0), (.7, 0, .7), (0, 0, 0)
            ])
        ):
            def coord(theta):
                r = hcell * (3 + math.cos((p * theta - 2 * k * math.pi) / q)) / 5
                return r * math.cos(theta), r * math.sin(theta)

            ctx.set_source_rgb(*color)
            ctx.move_to(*coord(0))
            for i in range(1, 2 * q * 25):
                theta = i * math.pi / 25
                ctx.line_to(*coord(theta))
            ctx.close_path()
            ctx.stroke()

    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, cell * cells, cell * cells)
    ctx = cairo.Context(img)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    ctx.translate(hcell, hcell)
    ctx.scale(1, -1)

    for p in range(cells):
        for q in range(cells):
            ctx.save()
            ctx.translate(cell * p, -cell * q)
            draw(ctx, p + 1, q + 1)
            ctx.restore()

    filename = os.path.join(directory, "families_for_small_pqs.png")
    img.write_to_png(filename)
