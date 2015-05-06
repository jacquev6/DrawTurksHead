# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import unittest

from ._turkshead import hsv_to_rgb


class HsvToRgbTestCase(unittest.TestCase):
    def test_red(self):
        self.assertEqual(hsv_to_rgb(0., 1., 1.), (1, 0, 0))

    def test_yellow(self):
        self.assertEqual(hsv_to_rgb(60., 1., 1.), (1, 1, 0))

    def test_yellow_after_360(self):
        self.assertEqual(hsv_to_rgb(420., 1., 1.), (1, 1, 0))

    def test_green(self):
        self.assertEqual(hsv_to_rgb(120., 1., 1.), (0, 1, 0))

    def test_cyan(self):
        self.assertEqual(hsv_to_rgb(180., 1., 1.), (0, 1, 1))

    def test_blue(self):
        self.assertEqual(hsv_to_rgb(240., 1., 1.), (0, 0, 1))

    def test_magenta(self):
        self.assertEqual(hsv_to_rgb(300., 1., 1.), (1, 0, 1))

    def test_blacks(self):
        self.assertEqual(hsv_to_rgb(30., 1., 0.), (0, 0, 0))
        self.assertEqual(hsv_to_rgb(210., 1., 0.), (0, 0, 0))

    def test_whites(self):
        self.assertEqual(hsv_to_rgb(30., 0., 1.), (1, 1, 1))
        self.assertEqual(hsv_to_rgb(210., 0., 1.), (1, 1, 1))

    def test_greys(self):
        self.assertEqual(hsv_to_rgb(30., 0., 0.5), (0.5, 0.5, 0.5))
        self.assertEqual(hsv_to_rgb(210., 0., 0.5), (0.5, 0.5, 0.5))

    def test_grey_ishes(self):
        self.assertEqual(hsv_to_rgb(30., 0.5, 0.5), (0.5, 0.375, 0.25))
        self.assertEqual(hsv_to_rgb(210., 0.5, 0.5), (0.25, 0.375, 0.5))
