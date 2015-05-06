# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import unittest


def hsv_to_rgb(h, s, v):
    hi = int(h / 60)
    f = h / 60 - hi;
    hi %= 60;
    p = v * (1 - s);
    q = v * (1 - f * s);
    t = v * (1 - (1 - f) * s);
    if hi == 0:
        return v, t, p
    elif hi == 1:
        return q, v, p
    elif hi == 2:
        return p, v, t
    elif hi == 3:
        return p, q, v
    elif hi == 4:
        return t, p, v
    else:
        assert hi == 5
        return v, p, q


class HsvToRgbTestCase(unittest.TestCase):
    def test_red(self):
        self.assertEqual(hsv_to_rgb(0, 1, 1), (1, 0, 0))

    def test_yellow(self):
        self.assertEqual(hsv_to_rgb(60, 1, 1), (1, 1, 0))

    def test_green(self):
        self.assertEqual(hsv_to_rgb(120, 1, 1), (0, 1, 0))

    def test_cyan(self):
        self.assertEqual(hsv_to_rgb(180, 1, 1), (0, 1, 1))

    def test_blue(self):
        self.assertEqual(hsv_to_rgb(240, 1, 1), (0, 0, 1))

    def test_magenta(self):
        self.assertEqual(hsv_to_rgb(300, 1, 1), (1, 0, 1))

    def test_blacks(self):
        self.assertEqual(hsv_to_rgb(30, 1, 0), (0, 0, 0))
        self.assertEqual(hsv_to_rgb(210, 1, 0), (0, 0, 0))

    def test_whites(self):
        self.assertEqual(hsv_to_rgb(30, 0, 1), (1, 1, 1))
        self.assertEqual(hsv_to_rgb(210, 0, 1), (1, 1, 1))

    def test_greys(self):
        self.assertEqual(hsv_to_rgb(30, 0, 0.5), (0.5, 0.5, 0.5))
        self.assertEqual(hsv_to_rgb(210, 0, 0.5), (0.5, 0.5, 0.5))

    def test_grey_ishes(self):
        self.assertEqual(hsv_to_rgb(30, 0.5, 0.5), (0.5, 0.25, 0.25))
        self.assertEqual(hsv_to_rgb(210, 0.5, 0.5), (0.25, 0.5, 0.5))
