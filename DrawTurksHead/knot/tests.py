# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

from fractions import Fraction
import unittest

from .knot import Knot, String, Segment, End, Bridge, Tunnel


class KnotTestCase(unittest.TestCase):
    def test_1_1(self):
        knot = Knot(1, 1)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(0, 1), 0), End(Fraction(2, 1), 0)),
                    ],
                    [
                    ],
                ),
            ]
        )

    def test_1_2(self):
        knot = Knot(1, 2)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 1), 1), End(Fraction(3, 1), -1)),
                        Segment(End(Fraction(3, 1), -1), End(Fraction(5, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), 0), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(2, 1), 0)),
                            Tunnel(0, Segment(End(Fraction(2, 1), 0), End(Fraction(3, 1), -1)), Segment(End(Fraction(3, 1), -1), End(Fraction(4, 1), 0))),
                        ),
                    ],
                ),
            ]
        )

    def test_2_1(self):
        knot = Knot(2, 1)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(0, 1), 0), End(Fraction(2, 1), 0)),
                    ],
                    [
                    ],
                ),
            ]
        )

    def test_1_3(self):
        knot = Knot(1, 3)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 1), 1), End(Fraction(2, 1), -1)),
                        Segment(End(Fraction(2, 1), -1), End(Fraction(4, 1), 1)),
                        Segment(End(Fraction(4, 1), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(7, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), 0), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(3, 2), 0)),
                            Tunnel(0, Segment(End(Fraction(9, 2), 0), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(6, 1), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(3, 1), 0), End(Fraction(4, 1), 1)),
                            Segment(End(Fraction(4, 1), 1), End(Fraction(9, 2), 0)),
                            Tunnel(0, Segment(End(Fraction(3, 2), 0), End(Fraction(2, 1), -1)), Segment(End(Fraction(2, 1), -1), End(Fraction(3, 1), 0))),
                        ),
                    ],
                ),
            ]
        )

    def test_2_2(self):
        knot = Knot(2, 2)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 2), 1), End(Fraction(3, 2), -1)),
                        Segment(End(Fraction(3, 2), -1), End(Fraction(5, 2), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), 0), End(Fraction(1, 2), 1)),
                            Segment(End(Fraction(1, 2), 1), End(Fraction(1, 1), 0)),
                            Tunnel(1, Segment(End(Fraction(0, 1), 0), End(Fraction(1, 2), -1)), Segment(End(Fraction(1, 2), -1), End(Fraction(1, 1), 0))),
                        ),
                    ],
                ),
                String(
                    1,
                    [
                        Segment(End(Fraction(1, 2), -1), End(Fraction(3, 2), 1)),
                        Segment(End(Fraction(3, 2), 1), End(Fraction(5, 2), -1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(1, 1), 0), End(Fraction(3, 2), 1)),
                            Segment(End(Fraction(3, 2), 1), End(Fraction(2, 1), 0)),
                            Tunnel(0, Segment(End(Fraction(1, 1), 0), End(Fraction(3, 2), -1)), Segment(End(Fraction(3, 2), -1), End(Fraction(2, 1), 0))),
                        ),
                    ],
                ),
            ]
        )

    def test_3_1(self):
        knot = Knot(3, 1)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(0, 1), 0), End(Fraction(2, 1), 0)),
                    ],
                    [
                    ],
                ),
            ]
        )

    def test_1_4(self):
        knot = Knot(1, 4)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 1), 1), End(Fraction(2, 1), -1)),
                        Segment(End(Fraction(2, 1), -1), End(Fraction(3, 1), 1)),
                        Segment(End(Fraction(3, 1), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(6, 1), 1)),
                        Segment(End(Fraction(6, 1), 1), End(Fraction(7, 1), -1)),
                        Segment(End(Fraction(7, 1), -1), End(Fraction(9, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), 0), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(3, 2), 0)),
                            Tunnel(0, Segment(End(Fraction(13, 2), 0), End(Fraction(7, 1), -1)), Segment(End(Fraction(7, 1), -1), End(Fraction(8, 1), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 2), 0), End(Fraction(3, 1), 1)),
                            Segment(End(Fraction(3, 1), 1), End(Fraction(4, 1), 0)),
                            Tunnel(0, Segment(End(Fraction(4, 1), 0), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(11, 2), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 2), 0), End(Fraction(6, 1), 1)),
                            Segment(End(Fraction(6, 1), 1), End(Fraction(13, 2), 0)),
                            Tunnel(0, Segment(End(Fraction(3, 2), 0), End(Fraction(2, 1), -1)), Segment(End(Fraction(2, 1), -1), End(Fraction(5, 2), 0))),
                        ),
                    ],
                ),
            ]
        )

    def test_2_3(self):
        knot = Knot(2, 3)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 2), 1), End(Fraction(1, 1), -1)),
                        Segment(End(Fraction(1, 1), -1), End(Fraction(2, 1), 1)),
                        Segment(End(Fraction(2, 1), 1), End(Fraction(5, 2), -1)),
                        Segment(End(Fraction(5, 2), -1), End(Fraction(7, 2), 1)),
                        Segment(End(Fraction(7, 2), 1), End(Fraction(4, 1), -1)),
                        Segment(End(Fraction(4, 1), -1), End(Fraction(5, 1), 1)),
                        Segment(End(Fraction(5, 1), 1), End(Fraction(11, 2), -1)),
                        Segment(End(Fraction(11, 2), -1), End(Fraction(13, 2), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), 0), End(Fraction(1, 2), 1)),
                            Segment(End(Fraction(1, 2), 1), End(Fraction(3, 4), 0)),
                            Tunnel(0, Segment(End(Fraction(9, 4), 0), End(Fraction(5, 2), -1)), Segment(End(Fraction(5, 2), -1), End(Fraction(3, 1), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(3, 2), 0), End(Fraction(2, 1), 1)),
                            Segment(End(Fraction(2, 1), 1), End(Fraction(9, 4), 0)),
                            Tunnel(0, Segment(End(Fraction(15, 4), 0), End(Fraction(4, 1), -1)), Segment(End(Fraction(4, 1), -1), End(Fraction(9, 2), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(3, 1), 0), End(Fraction(7, 2), 1)),
                            Segment(End(Fraction(7, 2), 1), End(Fraction(15, 4), 0)),
                            Tunnel(0, Segment(End(Fraction(21, 4), 0), End(Fraction(11, 2), -1)), Segment(End(Fraction(11, 2), -1), End(Fraction(6, 1), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(9, 2), 0), End(Fraction(5, 1), 1)),
                            Segment(End(Fraction(5, 1), 1), End(Fraction(21, 4), 0)),
                            Tunnel(0, Segment(End(Fraction(3, 4), 0), End(Fraction(1, 1), -1)), Segment(End(Fraction(1, 1), -1), End(Fraction(3, 2), 0))),
                        ),
                    ],
                ),
            ]
        )

    def test_3_2(self):
        knot = Knot(3, 2)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 3), 1), End(Fraction(1, 1), -1)),
                        Segment(End(Fraction(1, 1), -1), End(Fraction(5, 3), 1)),
                        Segment(End(Fraction(5, 3), 1), End(Fraction(7, 3), -1)),
                        Segment(End(Fraction(7, 3), -1), End(Fraction(3, 1), 1)),
                        Segment(End(Fraction(3, 1), 1), End(Fraction(11, 3), -1)),
                        Segment(End(Fraction(11, 3), -1), End(Fraction(13, 3), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), 0), End(Fraction(1, 3), 1)),
                            Segment(End(Fraction(1, 3), 1), End(Fraction(2, 3), 0)),
                            Tunnel(0, Segment(End(Fraction(2, 1), 0), End(Fraction(7, 3), -1)), Segment(End(Fraction(7, 3), -1), End(Fraction(8, 3), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(4, 3), 0), End(Fraction(5, 3), 1)),
                            Segment(End(Fraction(5, 3), 1), End(Fraction(2, 1), 0)),
                            Tunnel(0, Segment(End(Fraction(10, 3), 0), End(Fraction(11, 3), -1)), Segment(End(Fraction(11, 3), -1), End(Fraction(4, 1), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(8, 3), 0), End(Fraction(3, 1), 1)),
                            Segment(End(Fraction(3, 1), 1), End(Fraction(10, 3), 0)),
                            Tunnel(0, Segment(End(Fraction(2, 3), 0), End(Fraction(1, 1), -1)), Segment(End(Fraction(1, 1), -1), End(Fraction(4, 3), 0))),
                        ),
                    ],
                ),
            ]
        )

    def test_4_1(self):
        knot = Knot(4, 1)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(0, 1), 0), End(Fraction(2, 1), 0)),
                    ],
                    [
                    ],
                ),
            ]
        )

    def test_2_4(self):
        knot = Knot(2, 4)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 2), 1), End(Fraction(1, 1), -1)),
                        Segment(End(Fraction(1, 1), -1), End(Fraction(3, 2), 1)),
                        Segment(End(Fraction(3, 2), 1), End(Fraction(5, 2), -1)),
                        Segment(End(Fraction(5, 2), -1), End(Fraction(3, 1), 1)),
                        Segment(End(Fraction(3, 1), 1), End(Fraction(7, 2), -1)),
                        Segment(End(Fraction(7, 2), -1), End(Fraction(9, 2), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), 0), End(Fraction(1, 2), 1)),
                            Segment(End(Fraction(1, 2), 1), End(Fraction(3, 4), 0)),
                            Tunnel(1, Segment(End(Fraction(1, 4), 0), End(Fraction(1, 2), -1)), Segment(End(Fraction(1, 2), -1), End(Fraction(1, 1), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 4), 0), End(Fraction(3, 2), 1)),
                            Segment(End(Fraction(3, 2), 1), End(Fraction(2, 1), 0)),
                            Tunnel(1, Segment(End(Fraction(3, 1), 0), End(Fraction(7, 2), -1)), Segment(End(Fraction(7, 2), -1), End(Fraction(15, 4), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 4), 0), End(Fraction(3, 1), 1)),
                            Segment(End(Fraction(3, 1), 1), End(Fraction(13, 4), 0)),
                            Tunnel(0, Segment(End(Fraction(3, 4), 0), End(Fraction(1, 1), -1)), Segment(End(Fraction(1, 1), -1), End(Fraction(5, 4), 0))),
                        ),
                    ],
                ),
                String(
                    1,
                    [
                        Segment(End(Fraction(0, 1), 1), End(Fraction(1, 2), -1)),
                        Segment(End(Fraction(1, 2), -1), End(Fraction(3, 2), 1)),
                        Segment(End(Fraction(3, 2), 1), End(Fraction(2, 1), -1)),
                        Segment(End(Fraction(2, 1), -1), End(Fraction(5, 2), 1)),
                        Segment(End(Fraction(5, 2), 1), End(Fraction(7, 2), -1)),
                        Segment(End(Fraction(7, 2), -1), End(Fraction(4, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 4), 0), End(Fraction(0, 1), 1)),
                            Segment(End(Fraction(0, 1), 1), End(Fraction(1, 4), 0)),
                            Tunnel(1, Segment(End(Fraction(7, 4), 0), End(Fraction(2, 1), -1)), Segment(End(Fraction(2, 1), -1), End(Fraction(9, 4), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 1), 0), End(Fraction(3, 2), 1)),
                            Segment(End(Fraction(3, 2), 1), End(Fraction(7, 4), 0)),
                            Tunnel(0, Segment(End(Fraction(13, 4), 0), End(Fraction(7, 2), -1)), Segment(End(Fraction(7, 2), -1), End(Fraction(4, 1), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(9, 4), 0), End(Fraction(5, 2), 1)),
                            Segment(End(Fraction(5, 2), 1), End(Fraction(3, 1), 0)),
                            Tunnel(0, Segment(End(Fraction(2, 1), 0), End(Fraction(5, 2), -1)), Segment(End(Fraction(5, 2), -1), End(Fraction(11, 4), 0))),
                        ),
                    ],
                ),
            ]
        )

    def test_3_3(self):
        knot = Knot(3, 3)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 3), 1), End(Fraction(2, 3), -1)),
                        Segment(End(Fraction(2, 3), -1), End(Fraction(4, 3), 1)),
                        Segment(End(Fraction(4, 3), 1), End(Fraction(5, 3), -1)),
                        Segment(End(Fraction(5, 3), -1), End(Fraction(7, 3), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 3), -1), End(Fraction(1, 3), 1)),
                            Segment(End(Fraction(1, 3), 1), End(Fraction(2, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(0, 1), 1), End(Fraction(1, 3), -1)), Segment(End(Fraction(1, 3), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 3), -1), End(Fraction(4, 3), 1)),
                            Segment(End(Fraction(4, 3), 1), End(Fraction(5, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(1, 1), 1), End(Fraction(4, 3), -1)), Segment(End(Fraction(4, 3), -1), End(Fraction(2, 1), 1))),
                        ),
                    ],
                ),
                String(
                    1,
                    [
                        Segment(End(Fraction(0, 1), 1), End(Fraction(1, 3), -1)),
                        Segment(End(Fraction(1, 3), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(4, 3), -1)),
                        Segment(End(Fraction(4, 3), -1), End(Fraction(2, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-2, 3), -1), End(Fraction(0, 1), 1)),
                            Segment(End(Fraction(0, 1), 1), End(Fraction(1, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(-1, 3), 1), End(Fraction(0, 1), -1)), Segment(End(Fraction(0, 1), -1), End(Fraction(2, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 3), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(4, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(2, 3), 1), End(Fraction(1, 1), -1)), Segment(End(Fraction(1, 1), -1), End(Fraction(5, 3), 1))),
                        ),
                    ],
                ),
                String(
                    2,
                    [
                        Segment(End(Fraction(0, 1), -1), End(Fraction(2, 3), 1)),
                        Segment(End(Fraction(2, 3), 1), End(Fraction(1, 1), -1)),
                        Segment(End(Fraction(1, 1), -1), End(Fraction(5, 3), 1)),
                        Segment(End(Fraction(5, 3), 1), End(Fraction(2, 1), -1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), -1), End(Fraction(2, 3), 1)),
                            Segment(End(Fraction(2, 3), 1), End(Fraction(1, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 3), 1), End(Fraction(2, 3), -1)), Segment(End(Fraction(2, 3), -1), End(Fraction(4, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 1), -1), End(Fraction(5, 3), 1)),
                            Segment(End(Fraction(5, 3), 1), End(Fraction(2, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(4, 3), 1), End(Fraction(5, 3), -1)), Segment(End(Fraction(5, 3), -1), End(Fraction(7, 3), 1))),
                        ),
                    ],
                ),
            ]
        )

    def test_4_2(self):
        knot = Knot(4, 2)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 4), 1), End(Fraction(3, 4), -1)),
                        Segment(End(Fraction(3, 4), -1), End(Fraction(5, 4), 1)),
                        Segment(End(Fraction(5, 4), 1), End(Fraction(7, 4), -1)),
                        Segment(End(Fraction(7, 4), -1), End(Fraction(9, 4), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), 0), End(Fraction(1, 4), 1)),
                            Segment(End(Fraction(1, 4), 1), End(Fraction(1, 2), 0)),
                            Tunnel(1, Segment(End(Fraction(0, 1), 0), End(Fraction(1, 4), -1)), Segment(End(Fraction(1, 4), -1), End(Fraction(1, 2), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 1), 0), End(Fraction(5, 4), 1)),
                            Segment(End(Fraction(5, 4), 1), End(Fraction(3, 2), 0)),
                            Tunnel(1, Segment(End(Fraction(1, 1), 0), End(Fraction(5, 4), -1)), Segment(End(Fraction(5, 4), -1), End(Fraction(3, 2), 0))),
                        ),
                    ],
                ),
                String(
                    1,
                    [
                        Segment(End(Fraction(1, 4), -1), End(Fraction(3, 4), 1)),
                        Segment(End(Fraction(3, 4), 1), End(Fraction(5, 4), -1)),
                        Segment(End(Fraction(5, 4), -1), End(Fraction(7, 4), 1)),
                        Segment(End(Fraction(7, 4), 1), End(Fraction(9, 4), -1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(1, 2), 0), End(Fraction(3, 4), 1)),
                            Segment(End(Fraction(3, 4), 1), End(Fraction(1, 1), 0)),
                            Tunnel(0, Segment(End(Fraction(1, 2), 0), End(Fraction(3, 4), -1)), Segment(End(Fraction(3, 4), -1), End(Fraction(1, 1), 0))),
                        ),
                        Bridge(
                            Segment(End(Fraction(3, 2), 0), End(Fraction(7, 4), 1)),
                            Segment(End(Fraction(7, 4), 1), End(Fraction(2, 1), 0)),
                            Tunnel(0, Segment(End(Fraction(3, 2), 0), End(Fraction(7, 4), -1)), Segment(End(Fraction(7, 4), -1), End(Fraction(2, 1), 0))),
                        ),
                    ],
                ),
            ]
        )

    def test_3_4(self):
        knot = Knot(3, 4)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 3), 1), End(Fraction(2, 3), -1)),
                        Segment(End(Fraction(2, 3), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(5, 3), -1)),
                        Segment(End(Fraction(5, 3), -1), End(Fraction(2, 1), 1)),
                        Segment(End(Fraction(2, 1), 1), End(Fraction(7, 3), -1)),
                        Segment(End(Fraction(7, 3), -1), End(Fraction(3, 1), 1)),
                        Segment(End(Fraction(3, 1), 1), End(Fraction(10, 3), -1)),
                        Segment(End(Fraction(10, 3), -1), End(Fraction(11, 3), 1)),
                        Segment(End(Fraction(11, 3), 1), End(Fraction(13, 3), -1)),
                        Segment(End(Fraction(13, 3), -1), End(Fraction(14, 3), 1)),
                        Segment(End(Fraction(14, 3), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(17, 3), 1)),
                        Segment(End(Fraction(17, 3), 1), End(Fraction(6, 1), -1)),
                        Segment(End(Fraction(6, 1), -1), End(Fraction(19, 3), 1)),
                        Segment(End(Fraction(19, 3), 1), End(Fraction(7, 1), -1)),
                        Segment(End(Fraction(7, 1), -1), End(Fraction(22, 3), 1)),
                        Segment(End(Fraction(22, 3), 1), End(Fraction(23, 3), -1)),
                        Segment(End(Fraction(23, 3), -1), End(Fraction(25, 3), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 3), -1), End(Fraction(1, 3), 1)),
                            Segment(End(Fraction(1, 3), 1), End(Fraction(2, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(2, 1), 1), End(Fraction(7, 3), -1)), Segment(End(Fraction(7, 3), -1), End(Fraction(3, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 3), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(5, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(19, 3), 1), End(Fraction(7, 1), -1)), Segment(End(Fraction(7, 1), -1), End(Fraction(22, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 3), -1), End(Fraction(2, 1), 1)),
                            Segment(End(Fraction(2, 1), 1), End(Fraction(7, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(17, 3), 1), End(Fraction(6, 1), -1)), Segment(End(Fraction(6, 1), -1), End(Fraction(19, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 3), -1), End(Fraction(3, 1), 1)),
                            Segment(End(Fraction(3, 1), 1), End(Fraction(10, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(14, 3), 1), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(17, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 3), -1), End(Fraction(11, 3), 1)),
                            Segment(End(Fraction(11, 3), 1), End(Fraction(13, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 1), 1), End(Fraction(5, 3), -1)), Segment(End(Fraction(5, 3), -1), End(Fraction(2, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 3), -1), End(Fraction(14, 3), 1)),
                            Segment(End(Fraction(14, 3), 1), End(Fraction(5, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 3), 1), End(Fraction(2, 3), -1)), Segment(End(Fraction(2, 3), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 1), -1), End(Fraction(17, 3), 1)),
                            Segment(End(Fraction(17, 3), 1), End(Fraction(6, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(22, 3), 1), End(Fraction(23, 3), -1)), Segment(End(Fraction(23, 3), -1), End(Fraction(25, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(6, 1), -1), End(Fraction(19, 3), 1)),
                            Segment(End(Fraction(19, 3), 1), End(Fraction(7, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(11, 3), 1), End(Fraction(13, 3), -1)), Segment(End(Fraction(13, 3), -1), End(Fraction(14, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 1), -1), End(Fraction(22, 3), 1)),
                            Segment(End(Fraction(22, 3), 1), End(Fraction(23, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(3, 1), 1), End(Fraction(10, 3), -1)), Segment(End(Fraction(10, 3), -1), End(Fraction(11, 3), 1))),
                        ),
                    ],
                ),
            ]
        )

    def test_4_3(self):
        knot = Knot(4, 3)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 4), 1), End(Fraction(1, 2), -1)),
                        Segment(End(Fraction(1, 2), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(5, 4), -1)),
                        Segment(End(Fraction(5, 4), -1), End(Fraction(7, 4), 1)),
                        Segment(End(Fraction(7, 4), 1), End(Fraction(2, 1), -1)),
                        Segment(End(Fraction(2, 1), -1), End(Fraction(5, 2), 1)),
                        Segment(End(Fraction(5, 2), 1), End(Fraction(11, 4), -1)),
                        Segment(End(Fraction(11, 4), -1), End(Fraction(13, 4), 1)),
                        Segment(End(Fraction(13, 4), 1), End(Fraction(7, 2), -1)),
                        Segment(End(Fraction(7, 2), -1), End(Fraction(4, 1), 1)),
                        Segment(End(Fraction(4, 1), 1), End(Fraction(17, 4), -1)),
                        Segment(End(Fraction(17, 4), -1), End(Fraction(19, 4), 1)),
                        Segment(End(Fraction(19, 4), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(11, 2), 1)),
                        Segment(End(Fraction(11, 2), 1), End(Fraction(23, 4), -1)),
                        Segment(End(Fraction(23, 4), -1), End(Fraction(25, 4), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 4), -1), End(Fraction(1, 4), 1)),
                            Segment(End(Fraction(1, 4), 1), End(Fraction(1, 2), -1)),
                            Tunnel(0, Segment(End(Fraction(4, 1), 1), End(Fraction(17, 4), -1)), Segment(End(Fraction(17, 4), -1), End(Fraction(19, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 2), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(5, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(19, 4), 1), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(11, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 4), -1), End(Fraction(7, 4), 1)),
                            Segment(End(Fraction(7, 4), 1), End(Fraction(2, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(11, 2), 1), End(Fraction(23, 4), -1)), Segment(End(Fraction(23, 4), -1), End(Fraction(25, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 1), -1), End(Fraction(5, 2), 1)),
                            Segment(End(Fraction(5, 2), 1), End(Fraction(11, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 4), 1), End(Fraction(1, 2), -1)), Segment(End(Fraction(1, 2), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 4), -1), End(Fraction(13, 4), 1)),
                            Segment(End(Fraction(13, 4), 1), End(Fraction(7, 2), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 1), 1), End(Fraction(5, 4), -1)), Segment(End(Fraction(5, 4), -1), End(Fraction(7, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 2), -1), End(Fraction(4, 1), 1)),
                            Segment(End(Fraction(4, 1), 1), End(Fraction(17, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(7, 4), 1), End(Fraction(2, 1), -1)), Segment(End(Fraction(2, 1), -1), End(Fraction(5, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 4), -1), End(Fraction(19, 4), 1)),
                            Segment(End(Fraction(19, 4), 1), End(Fraction(5, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(5, 2), 1), End(Fraction(11, 4), -1)), Segment(End(Fraction(11, 4), -1), End(Fraction(13, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 1), -1), End(Fraction(11, 2), 1)),
                            Segment(End(Fraction(11, 2), 1), End(Fraction(23, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(13, 4), 1), End(Fraction(7, 2), -1)), Segment(End(Fraction(7, 2), -1), End(Fraction(4, 1), 1))),
                        ),
                    ],
                ),
            ]
        )

    def test_4_4(self):
        knot = Knot(4, 4)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 4), 1), End(Fraction(1, 2), -1)),
                        Segment(End(Fraction(1, 2), -1), End(Fraction(3, 4), 1)),
                        Segment(End(Fraction(3, 4), 1), End(Fraction(5, 4), -1)),
                        Segment(End(Fraction(5, 4), -1), End(Fraction(3, 2), 1)),
                        Segment(End(Fraction(3, 2), 1), End(Fraction(7, 4), -1)),
                        Segment(End(Fraction(7, 4), -1), End(Fraction(9, 4), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 4), -1), End(Fraction(1, 4), 1)),
                            Segment(End(Fraction(1, 4), 1), End(Fraction(1, 2), -1)),
                            Tunnel(1, Segment(End(Fraction(0, 1), 1), End(Fraction(1, 4), -1)), Segment(End(Fraction(1, 4), -1), End(Fraction(3, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 2), -1), End(Fraction(3, 4), 1)),
                            Segment(End(Fraction(3, 4), 1), End(Fraction(5, 4), -1)),
                            Tunnel(3, Segment(End(Fraction(1, 4), 1), End(Fraction(3, 4), -1)), Segment(End(Fraction(3, 4), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 4), -1), End(Fraction(3, 2), 1)),
                            Segment(End(Fraction(3, 2), 1), End(Fraction(7, 4), -1)),
                            Tunnel(2, Segment(End(Fraction(5, 4), 1), End(Fraction(3, 2), -1)), Segment(End(Fraction(3, 2), -1), End(Fraction(7, 4), 1))),
                        ),
                    ],
                ),
                String(
                    1,
                    [
                        Segment(End(Fraction(0, 1), 1), End(Fraction(1, 4), -1)),
                        Segment(End(Fraction(1, 4), -1), End(Fraction(3, 4), 1)),
                        Segment(End(Fraction(3, 4), 1), End(Fraction(1, 1), -1)),
                        Segment(End(Fraction(1, 1), -1), End(Fraction(5, 4), 1)),
                        Segment(End(Fraction(5, 4), 1), End(Fraction(7, 4), -1)),
                        Segment(End(Fraction(7, 4), -1), End(Fraction(2, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 4), -1), End(Fraction(0, 1), 1)),
                            Segment(End(Fraction(0, 1), 1), End(Fraction(1, 4), -1)),
                            Tunnel(3, Segment(End(Fraction(-1, 4), 1), End(Fraction(0, 1), -1)), Segment(End(Fraction(0, 1), -1), End(Fraction(1, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 4), -1), End(Fraction(3, 4), 1)),
                            Segment(End(Fraction(3, 4), 1), End(Fraction(1, 1), -1)),
                            Tunnel(2, Segment(End(Fraction(1, 2), 1), End(Fraction(3, 4), -1)), Segment(End(Fraction(3, 4), -1), End(Fraction(5, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 1), -1), End(Fraction(5, 4), 1)),
                            Segment(End(Fraction(5, 4), 1), End(Fraction(7, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(3, 4), 1), End(Fraction(5, 4), -1)), Segment(End(Fraction(5, 4), -1), End(Fraction(3, 2), 1))),
                        ),
                    ],
                ),
                String(
                    2,
                    [
                        Segment(End(Fraction(1, 4), -1), End(Fraction(1, 2), 1)),
                        Segment(End(Fraction(1, 2), 1), End(Fraction(3, 4), -1)),
                        Segment(End(Fraction(3, 4), -1), End(Fraction(5, 4), 1)),
                        Segment(End(Fraction(5, 4), 1), End(Fraction(3, 2), -1)),
                        Segment(End(Fraction(3, 2), -1), End(Fraction(7, 4), 1)),
                        Segment(End(Fraction(7, 4), 1), End(Fraction(9, 4), -1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(1, 4), -1), End(Fraction(1, 2), 1)),
                            Segment(End(Fraction(1, 2), 1), End(Fraction(3, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 4), 1), End(Fraction(1, 2), -1)), Segment(End(Fraction(1, 2), -1), End(Fraction(3, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(3, 4), -1), End(Fraction(5, 4), 1)),
                            Segment(End(Fraction(5, 4), 1), End(Fraction(3, 2), -1)),
                            Tunnel(3, Segment(End(Fraction(1, 1), 1), End(Fraction(5, 4), -1)), Segment(End(Fraction(5, 4), -1), End(Fraction(7, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(3, 2), -1), End(Fraction(7, 4), 1)),
                            Segment(End(Fraction(7, 4), 1), End(Fraction(9, 4), -1)),
                            Tunnel(1, Segment(End(Fraction(5, 4), 1), End(Fraction(7, 4), -1)), Segment(End(Fraction(7, 4), -1), End(Fraction(2, 1), 1))),
                        ),
                    ],
                ),
                String(
                    3,
                    [
                        Segment(End(Fraction(0, 1), -1), End(Fraction(1, 4), 1)),
                        Segment(End(Fraction(1, 4), 1), End(Fraction(3, 4), -1)),
                        Segment(End(Fraction(3, 4), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(5, 4), -1)),
                        Segment(End(Fraction(5, 4), -1), End(Fraction(7, 4), 1)),
                        Segment(End(Fraction(7, 4), 1), End(Fraction(2, 1), -1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(0, 1), -1), End(Fraction(1, 4), 1)),
                            Segment(End(Fraction(1, 4), 1), End(Fraction(3, 4), -1)),
                            Tunnel(2, Segment(End(Fraction(-1, 4), 1), End(Fraction(1, 4), -1)), Segment(End(Fraction(1, 4), -1), End(Fraction(1, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(3, 4), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(5, 4), -1)),
                            Tunnel(1, Segment(End(Fraction(3, 4), 1), End(Fraction(1, 1), -1)), Segment(End(Fraction(1, 1), -1), End(Fraction(5, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 4), -1), End(Fraction(7, 4), 1)),
                            Segment(End(Fraction(7, 4), 1), End(Fraction(2, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(3, 2), 1), End(Fraction(7, 4), -1)), Segment(End(Fraction(7, 4), -1), End(Fraction(9, 4), 1))),
                        ),
                    ],
                ),
            ]
        )

    def test_9_12(self):
        knot = Knot(9, 12)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 9), 1), End(Fraction(2, 9), -1)),
                        Segment(End(Fraction(2, 9), -1), End(Fraction(1, 3), 1)),
                        Segment(End(Fraction(1, 3), 1), End(Fraction(4, 9), -1)),
                        Segment(End(Fraction(4, 9), -1), End(Fraction(5, 9), 1)),
                        Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)),
                        Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1)),
                        Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)),
                        Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)),
                        Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1)),
                        Segment(End(Fraction(11, 9), 1), End(Fraction(13, 9), -1)),
                        Segment(End(Fraction(13, 9), -1), End(Fraction(14, 9), 1)),
                        Segment(End(Fraction(14, 9), 1), End(Fraction(5, 3), -1)),
                        Segment(End(Fraction(5, 3), -1), End(Fraction(16, 9), 1)),
                        Segment(End(Fraction(16, 9), 1), End(Fraction(17, 9), -1)),
                        Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1)),
                        Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)),
                        Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1)),
                        Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)),
                        Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1)),
                        Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)),
                        Segment(End(Fraction(23, 9), -1), End(Fraction(25, 9), 1)),
                        Segment(End(Fraction(25, 9), 1), End(Fraction(26, 9), -1)),
                        Segment(End(Fraction(26, 9), -1), End(Fraction(3, 1), 1)),
                        Segment(End(Fraction(3, 1), 1), End(Fraction(28, 9), -1)),
                        Segment(End(Fraction(28, 9), -1), End(Fraction(29, 9), 1)),
                        Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)),
                        Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1)),
                        Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)),
                        Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1)),
                        Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)),
                        Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1)),
                        Segment(End(Fraction(35, 9), 1), End(Fraction(37, 9), -1)),
                        Segment(End(Fraction(37, 9), -1), End(Fraction(38, 9), 1)),
                        Segment(End(Fraction(38, 9), 1), End(Fraction(13, 3), -1)),
                        Segment(End(Fraction(13, 3), -1), End(Fraction(40, 9), 1)),
                        Segment(End(Fraction(40, 9), 1), End(Fraction(41, 9), -1)),
                        Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1)),
                        Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)),
                        Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1)),
                        Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1)),
                        Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)),
                        Segment(End(Fraction(47, 9), -1), End(Fraction(49, 9), 1)),
                        Segment(End(Fraction(49, 9), 1), End(Fraction(50, 9), -1)),
                        Segment(End(Fraction(50, 9), -1), End(Fraction(17, 3), 1)),
                        Segment(End(Fraction(17, 3), 1), End(Fraction(52, 9), -1)),
                        Segment(End(Fraction(52, 9), -1), End(Fraction(53, 9), 1)),
                        Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)),
                        Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1)),
                        Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)),
                        Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1)),
                        Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)),
                        Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1)),
                        Segment(End(Fraction(59, 9), 1), End(Fraction(61, 9), -1)),
                        Segment(End(Fraction(61, 9), -1), End(Fraction(62, 9), 1)),
                        Segment(End(Fraction(62, 9), 1), End(Fraction(7, 1), -1)),
                        Segment(End(Fraction(7, 1), -1), End(Fraction(64, 9), 1)),
                        Segment(End(Fraction(64, 9), 1), End(Fraction(65, 9), -1)),
                        Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1)),
                        Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)),
                        Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1)),
                        Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)),
                        Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1)),
                        Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)),
                        Segment(End(Fraction(71, 9), -1), End(Fraction(73, 9), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 9), -1), End(Fraction(1, 9), 1)),
                            Segment(End(Fraction(1, 9), 1), End(Fraction(2, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(0, 1), 1), End(Fraction(1, 9), -1)), Segment(End(Fraction(1, 9), -1), End(Fraction(1, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 9), -1), End(Fraction(1, 3), 1)),
                            Segment(End(Fraction(1, 3), 1), End(Fraction(4, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)), Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(4, 9), -1), End(Fraction(5, 9), 1)),
                            Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)), Segment(End(Fraction(23, 9), -1), End(Fraction(8, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1)),
                            Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)), Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(62, 9), 1), End(Fraction(7, 1), -1)), Segment(End(Fraction(7, 1), -1), End(Fraction(64, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1)),
                            Segment(End(Fraction(11, 9), 1), End(Fraction(13, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(7, 1), 1), End(Fraction(65, 9), -1)), Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 9), -1), End(Fraction(14, 9), 1)),
                            Segment(End(Fraction(14, 9), 1), End(Fraction(5, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(13, 9), 1), End(Fraction(14, 9), -1)), Segment(End(Fraction(14, 9), -1), End(Fraction(5, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 3), -1), End(Fraction(16, 9), 1)),
                            Segment(End(Fraction(16, 9), 1), End(Fraction(17, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)), Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1)),
                            Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)), Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1)),
                            Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)), Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1)),
                            Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(1, 3), 1), End(Fraction(4, 9), -1)), Segment(End(Fraction(4, 9), -1), End(Fraction(5, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 9), -1), End(Fraction(25, 9), 1)),
                            Segment(End(Fraction(25, 9), 1), End(Fraction(26, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(8, 3), 1), End(Fraction(25, 9), -1)), Segment(End(Fraction(25, 9), -1), End(Fraction(3, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(26, 9), -1), End(Fraction(3, 1), 1)),
                            Segment(End(Fraction(3, 1), 1), End(Fraction(28, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(28, 9), -1), End(Fraction(29, 9), 1)),
                            Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)), Segment(End(Fraction(47, 9), -1), End(Fraction(16, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1)),
                            Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)), Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1)),
                            Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(14, 9), 1), End(Fraction(5, 3), -1)), Segment(End(Fraction(5, 3), -1), End(Fraction(16, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1)),
                            Segment(End(Fraction(35, 9), 1), End(Fraction(37, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(5, 3), 1), End(Fraction(17, 9), -1)), Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(37, 9), -1), End(Fraction(38, 9), 1)),
                            Segment(End(Fraction(38, 9), 1), End(Fraction(13, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(37, 9), 1), End(Fraction(38, 9), -1)), Segment(End(Fraction(38, 9), -1), End(Fraction(13, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 3), -1), End(Fraction(40, 9), 1)),
                            Segment(End(Fraction(40, 9), 1), End(Fraction(41, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)), Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1)),
                            Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)), Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1)),
                            Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)),
                            Tunnel(2, Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)), Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1)),
                            Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(3, 1), 1), End(Fraction(28, 9), -1)), Segment(End(Fraction(28, 9), -1), End(Fraction(29, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(47, 9), -1), End(Fraction(49, 9), 1)),
                            Segment(End(Fraction(49, 9), 1), End(Fraction(50, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(16, 3), 1), End(Fraction(49, 9), -1)), Segment(End(Fraction(49, 9), -1), End(Fraction(17, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(50, 9), -1), End(Fraction(17, 3), 1)),
                            Segment(End(Fraction(17, 3), 1), End(Fraction(52, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)), Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(52, 9), -1), End(Fraction(53, 9), 1)),
                            Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)),
                            Tunnel(2, Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)), Segment(End(Fraction(71, 9), -1), End(Fraction(8, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1)),
                            Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)), Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1)),
                            Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(38, 9), 1), End(Fraction(13, 3), -1)), Segment(End(Fraction(13, 3), -1), End(Fraction(40, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1)),
                            Segment(End(Fraction(59, 9), 1), End(Fraction(61, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(13, 3), 1), End(Fraction(41, 9), -1)), Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(61, 9), -1), End(Fraction(62, 9), 1)),
                            Segment(End(Fraction(62, 9), 1), End(Fraction(7, 1), -1)),
                            Tunnel(2, Segment(End(Fraction(61, 9), 1), End(Fraction(62, 9), -1)), Segment(End(Fraction(62, 9), -1), End(Fraction(7, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 1), -1), End(Fraction(64, 9), 1)),
                            Segment(End(Fraction(64, 9), 1), End(Fraction(65, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)), Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1)),
                            Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)), Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1)),
                            Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)), Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1)),
                            Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(17, 3), 1), End(Fraction(52, 9), -1)), Segment(End(Fraction(52, 9), -1), End(Fraction(53, 9), 1))),
                        ),
                    ],
                ),
                String(
                    1,
                    [
                        Segment(End(Fraction(0, 1), 1), End(Fraction(1, 9), -1)),
                        Segment(End(Fraction(1, 9), -1), End(Fraction(1, 3), 1)),
                        Segment(End(Fraction(1, 3), 1), End(Fraction(4, 9), -1)),
                        Segment(End(Fraction(4, 9), -1), End(Fraction(5, 9), 1)),
                        Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)),
                        Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1)),
                        Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)),
                        Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)),
                        Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1)),
                        Segment(End(Fraction(11, 9), 1), End(Fraction(4, 3), -1)),
                        Segment(End(Fraction(4, 3), -1), End(Fraction(13, 9), 1)),
                        Segment(End(Fraction(13, 9), 1), End(Fraction(5, 3), -1)),
                        Segment(End(Fraction(5, 3), -1), End(Fraction(16, 9), 1)),
                        Segment(End(Fraction(16, 9), 1), End(Fraction(17, 9), -1)),
                        Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1)),
                        Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)),
                        Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1)),
                        Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)),
                        Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1)),
                        Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)),
                        Segment(End(Fraction(23, 9), -1), End(Fraction(8, 3), 1)),
                        Segment(End(Fraction(8, 3), 1), End(Fraction(25, 9), -1)),
                        Segment(End(Fraction(25, 9), -1), End(Fraction(3, 1), 1)),
                        Segment(End(Fraction(3, 1), 1), End(Fraction(28, 9), -1)),
                        Segment(End(Fraction(28, 9), -1), End(Fraction(29, 9), 1)),
                        Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)),
                        Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1)),
                        Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)),
                        Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1)),
                        Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)),
                        Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1)),
                        Segment(End(Fraction(35, 9), 1), End(Fraction(4, 1), -1)),
                        Segment(End(Fraction(4, 1), -1), End(Fraction(37, 9), 1)),
                        Segment(End(Fraction(37, 9), 1), End(Fraction(13, 3), -1)),
                        Segment(End(Fraction(13, 3), -1), End(Fraction(40, 9), 1)),
                        Segment(End(Fraction(40, 9), 1), End(Fraction(41, 9), -1)),
                        Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1)),
                        Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)),
                        Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1)),
                        Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1)),
                        Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)),
                        Segment(End(Fraction(47, 9), -1), End(Fraction(16, 3), 1)),
                        Segment(End(Fraction(16, 3), 1), End(Fraction(49, 9), -1)),
                        Segment(End(Fraction(49, 9), -1), End(Fraction(17, 3), 1)),
                        Segment(End(Fraction(17, 3), 1), End(Fraction(52, 9), -1)),
                        Segment(End(Fraction(52, 9), -1), End(Fraction(53, 9), 1)),
                        Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)),
                        Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1)),
                        Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)),
                        Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1)),
                        Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)),
                        Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1)),
                        Segment(End(Fraction(59, 9), 1), End(Fraction(20, 3), -1)),
                        Segment(End(Fraction(20, 3), -1), End(Fraction(61, 9), 1)),
                        Segment(End(Fraction(61, 9), 1), End(Fraction(7, 1), -1)),
                        Segment(End(Fraction(7, 1), -1), End(Fraction(64, 9), 1)),
                        Segment(End(Fraction(64, 9), 1), End(Fraction(65, 9), -1)),
                        Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1)),
                        Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)),
                        Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1)),
                        Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)),
                        Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1)),
                        Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)),
                        Segment(End(Fraction(71, 9), -1), End(Fraction(8, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 9), -1), End(Fraction(0, 1), 1)),
                            Segment(End(Fraction(0, 1), 1), End(Fraction(1, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)), Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 9), -1), End(Fraction(1, 3), 1)),
                            Segment(End(Fraction(1, 3), 1), End(Fraction(4, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(2, 9), 1), End(Fraction(1, 3), -1)), Segment(End(Fraction(1, 3), -1), End(Fraction(5, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(4, 9), -1), End(Fraction(5, 9), 1)),
                            Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)), Segment(End(Fraction(23, 9), -1), End(Fraction(8, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1)),
                            Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)), Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1)),
                            Segment(End(Fraction(11, 9), 1), End(Fraction(4, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(64, 9), 1), End(Fraction(65, 9), -1)), Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(4, 3), -1), End(Fraction(13, 9), 1)),
                            Segment(End(Fraction(13, 9), 1), End(Fraction(5, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(11, 9), 1), End(Fraction(13, 9), -1)), Segment(End(Fraction(13, 9), -1), End(Fraction(14, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 3), -1), End(Fraction(16, 9), 1)),
                            Segment(End(Fraction(16, 9), 1), End(Fraction(17, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)), Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1)),
                            Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(35, 9), 1), End(Fraction(4, 1), -1)), Segment(End(Fraction(4, 1), -1), End(Fraction(37, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1)),
                            Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)), Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1)),
                            Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 3), 1), End(Fraction(4, 9), -1)), Segment(End(Fraction(4, 9), -1), End(Fraction(5, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 9), -1), End(Fraction(8, 3), 1)),
                            Segment(End(Fraction(8, 3), 1), End(Fraction(25, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)), Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(25, 9), -1), End(Fraction(3, 1), 1)),
                            Segment(End(Fraction(3, 1), 1), End(Fraction(28, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(26, 9), 1), End(Fraction(3, 1), -1)), Segment(End(Fraction(3, 1), -1), End(Fraction(29, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(28, 9), -1), End(Fraction(29, 9), 1)),
                            Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)), Segment(End(Fraction(47, 9), -1), End(Fraction(16, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1)),
                            Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)), Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1)),
                            Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)), Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1)),
                            Segment(End(Fraction(35, 9), 1), End(Fraction(4, 1), -1)),
                            Tunnel(1, Segment(End(Fraction(16, 9), 1), End(Fraction(17, 9), -1)), Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(4, 1), -1), End(Fraction(37, 9), 1)),
                            Segment(End(Fraction(37, 9), 1), End(Fraction(13, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(35, 9), 1), End(Fraction(37, 9), -1)), Segment(End(Fraction(37, 9), -1), End(Fraction(38, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 3), -1), End(Fraction(40, 9), 1)),
                            Segment(End(Fraction(40, 9), 1), End(Fraction(41, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)), Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1)),
                            Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(59, 9), 1), End(Fraction(20, 3), -1)), Segment(End(Fraction(20, 3), -1), End(Fraction(61, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1)),
                            Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)),
                            Tunnel(1, Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)), Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1)),
                            Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(3, 1), 1), End(Fraction(28, 9), -1)), Segment(End(Fraction(28, 9), -1), End(Fraction(29, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(47, 9), -1), End(Fraction(16, 3), 1)),
                            Segment(End(Fraction(16, 3), 1), End(Fraction(49, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)), Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(49, 9), -1), End(Fraction(17, 3), 1)),
                            Segment(End(Fraction(17, 3), 1), End(Fraction(52, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(50, 9), 1), End(Fraction(17, 3), -1)), Segment(End(Fraction(17, 3), -1), End(Fraction(53, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(52, 9), -1), End(Fraction(53, 9), 1)),
                            Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)),
                            Tunnel(1, Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)), Segment(End(Fraction(71, 9), -1), End(Fraction(8, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1)),
                            Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)), Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1)),
                            Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)), Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1)),
                            Segment(End(Fraction(59, 9), 1), End(Fraction(20, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(40, 9), 1), End(Fraction(41, 9), -1)), Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(20, 3), -1), End(Fraction(61, 9), 1)),
                            Segment(End(Fraction(61, 9), 1), End(Fraction(7, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(59, 9), 1), End(Fraction(61, 9), -1)), Segment(End(Fraction(61, 9), -1), End(Fraction(62, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 1), -1), End(Fraction(64, 9), 1)),
                            Segment(End(Fraction(64, 9), 1), End(Fraction(65, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)), Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1)),
                            Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(11, 9), 1), End(Fraction(4, 3), -1)), Segment(End(Fraction(4, 3), -1), End(Fraction(13, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1)),
                            Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)), Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1)),
                            Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)),
                            Tunnel(0, Segment(End(Fraction(17, 3), 1), End(Fraction(52, 9), -1)), Segment(End(Fraction(52, 9), -1), End(Fraction(53, 9), 1))),
                        ),
                    ],
                ),
                String(
                    2,
                    [
                        Segment(End(Fraction(0, 1), 1), End(Fraction(1, 9), -1)),
                        Segment(End(Fraction(1, 9), -1), End(Fraction(2, 9), 1)),
                        Segment(End(Fraction(2, 9), 1), End(Fraction(1, 3), -1)),
                        Segment(End(Fraction(1, 3), -1), End(Fraction(5, 9), 1)),
                        Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)),
                        Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1)),
                        Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)),
                        Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)),
                        Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1)),
                        Segment(End(Fraction(11, 9), 1), End(Fraction(4, 3), -1)),
                        Segment(End(Fraction(4, 3), -1), End(Fraction(13, 9), 1)),
                        Segment(End(Fraction(13, 9), 1), End(Fraction(14, 9), -1)),
                        Segment(End(Fraction(14, 9), -1), End(Fraction(5, 3), 1)),
                        Segment(End(Fraction(5, 3), 1), End(Fraction(17, 9), -1)),
                        Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1)),
                        Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)),
                        Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1)),
                        Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)),
                        Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1)),
                        Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)),
                        Segment(End(Fraction(23, 9), -1), End(Fraction(8, 3), 1)),
                        Segment(End(Fraction(8, 3), 1), End(Fraction(25, 9), -1)),
                        Segment(End(Fraction(25, 9), -1), End(Fraction(26, 9), 1)),
                        Segment(End(Fraction(26, 9), 1), End(Fraction(3, 1), -1)),
                        Segment(End(Fraction(3, 1), -1), End(Fraction(29, 9), 1)),
                        Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)),
                        Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1)),
                        Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)),
                        Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1)),
                        Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)),
                        Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1)),
                        Segment(End(Fraction(35, 9), 1), End(Fraction(4, 1), -1)),
                        Segment(End(Fraction(4, 1), -1), End(Fraction(37, 9), 1)),
                        Segment(End(Fraction(37, 9), 1), End(Fraction(38, 9), -1)),
                        Segment(End(Fraction(38, 9), -1), End(Fraction(13, 3), 1)),
                        Segment(End(Fraction(13, 3), 1), End(Fraction(41, 9), -1)),
                        Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1)),
                        Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)),
                        Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1)),
                        Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1)),
                        Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)),
                        Segment(End(Fraction(47, 9), -1), End(Fraction(16, 3), 1)),
                        Segment(End(Fraction(16, 3), 1), End(Fraction(49, 9), -1)),
                        Segment(End(Fraction(49, 9), -1), End(Fraction(50, 9), 1)),
                        Segment(End(Fraction(50, 9), 1), End(Fraction(17, 3), -1)),
                        Segment(End(Fraction(17, 3), -1), End(Fraction(53, 9), 1)),
                        Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)),
                        Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1)),
                        Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)),
                        Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1)),
                        Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)),
                        Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1)),
                        Segment(End(Fraction(59, 9), 1), End(Fraction(20, 3), -1)),
                        Segment(End(Fraction(20, 3), -1), End(Fraction(61, 9), 1)),
                        Segment(End(Fraction(61, 9), 1), End(Fraction(62, 9), -1)),
                        Segment(End(Fraction(62, 9), -1), End(Fraction(7, 1), 1)),
                        Segment(End(Fraction(7, 1), 1), End(Fraction(65, 9), -1)),
                        Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1)),
                        Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)),
                        Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1)),
                        Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)),
                        Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1)),
                        Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)),
                        Segment(End(Fraction(71, 9), -1), End(Fraction(8, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 9), -1), End(Fraction(0, 1), 1)),
                            Segment(End(Fraction(0, 1), 1), End(Fraction(1, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)), Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 9), -1), End(Fraction(2, 9), 1)),
                            Segment(End(Fraction(2, 9), 1), End(Fraction(1, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 9), 1), End(Fraction(2, 9), -1)), Segment(End(Fraction(2, 9), -1), End(Fraction(1, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 3), -1), End(Fraction(5, 9), 1)),
                            Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)), Segment(End(Fraction(23, 9), -1), End(Fraction(25, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1)),
                            Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(8, 3), 1), End(Fraction(25, 9), -1)), Segment(End(Fraction(25, 9), -1), End(Fraction(26, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1)),
                            Segment(End(Fraction(11, 9), 1), End(Fraction(4, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(64, 9), 1), End(Fraction(65, 9), -1)), Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(4, 3), -1), End(Fraction(13, 9), 1)),
                            Segment(End(Fraction(13, 9), 1), End(Fraction(14, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)), Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(14, 9), -1), End(Fraction(5, 3), 1)),
                            Segment(End(Fraction(5, 3), 1), End(Fraction(17, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(13, 9), 1), End(Fraction(5, 3), -1)), Segment(End(Fraction(5, 3), -1), End(Fraction(16, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1)),
                            Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(35, 9), 1), End(Fraction(4, 1), -1)), Segment(End(Fraction(4, 1), -1), End(Fraction(37, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1)),
                            Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)), Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1)),
                            Segment(End(Fraction(22, 9), 1), End(Fraction(23, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)), Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 9), -1), End(Fraction(8, 3), 1)),
                            Segment(End(Fraction(8, 3), 1), End(Fraction(25, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(5, 9), 1), End(Fraction(2, 3), -1)), Segment(End(Fraction(2, 3), -1), End(Fraction(7, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(25, 9), -1), End(Fraction(26, 9), 1)),
                            Segment(End(Fraction(26, 9), 1), End(Fraction(3, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(25, 9), 1), End(Fraction(26, 9), -1)), Segment(End(Fraction(26, 9), -1), End(Fraction(3, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(3, 1), -1), End(Fraction(29, 9), 1)),
                            Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)), Segment(End(Fraction(47, 9), -1), End(Fraction(49, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1)),
                            Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(16, 3), 1), End(Fraction(49, 9), -1)), Segment(End(Fraction(49, 9), -1), End(Fraction(50, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1)),
                            Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)), Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1)),
                            Segment(End(Fraction(35, 9), 1), End(Fraction(4, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(16, 9), 1), End(Fraction(17, 9), -1)), Segment(End(Fraction(17, 9), -1), End(Fraction(2, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(4, 1), -1), End(Fraction(37, 9), 1)),
                            Segment(End(Fraction(37, 9), 1), End(Fraction(38, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(2, 1), 1), End(Fraction(19, 9), -1)), Segment(End(Fraction(19, 9), -1), End(Fraction(20, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(38, 9), -1), End(Fraction(13, 3), 1)),
                            Segment(End(Fraction(13, 3), 1), End(Fraction(41, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(37, 9), 1), End(Fraction(13, 3), -1)), Segment(End(Fraction(13, 3), -1), End(Fraction(40, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1)),
                            Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(59, 9), 1), End(Fraction(20, 3), -1)), Segment(End(Fraction(20, 3), -1), End(Fraction(61, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1)),
                            Segment(End(Fraction(44, 9), 1), End(Fraction(5, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(7, 9), 1), End(Fraction(8, 9), -1)), Segment(End(Fraction(8, 9), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 1), -1), End(Fraction(46, 9), 1)),
                            Segment(End(Fraction(46, 9), 1), End(Fraction(47, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(1, 1), 1), End(Fraction(10, 9), -1)), Segment(End(Fraction(10, 9), -1), End(Fraction(11, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(47, 9), -1), End(Fraction(16, 3), 1)),
                            Segment(End(Fraction(16, 3), 1), End(Fraction(49, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(29, 9), 1), End(Fraction(10, 3), -1)), Segment(End(Fraction(10, 3), -1), End(Fraction(31, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(49, 9), -1), End(Fraction(50, 9), 1)),
                            Segment(End(Fraction(50, 9), 1), End(Fraction(17, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(49, 9), 1), End(Fraction(50, 9), -1)), Segment(End(Fraction(50, 9), -1), End(Fraction(17, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 3), -1), End(Fraction(53, 9), 1)),
                            Segment(End(Fraction(53, 9), 1), End(Fraction(6, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)), Segment(End(Fraction(71, 9), -1), End(Fraction(73, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(6, 1), -1), End(Fraction(55, 9), 1)),
                            Segment(End(Fraction(55, 9), 1), End(Fraction(56, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(0, 1), 1), End(Fraction(1, 9), -1)), Segment(End(Fraction(1, 9), -1), End(Fraction(2, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(56, 9), -1), End(Fraction(19, 3), 1)),
                            Segment(End(Fraction(19, 3), 1), End(Fraction(58, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(20, 9), 1), End(Fraction(7, 3), -1)), Segment(End(Fraction(7, 3), -1), End(Fraction(22, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(58, 9), -1), End(Fraction(59, 9), 1)),
                            Segment(End(Fraction(59, 9), 1), End(Fraction(20, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(40, 9), 1), End(Fraction(41, 9), -1)), Segment(End(Fraction(41, 9), -1), End(Fraction(14, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(20, 3), -1), End(Fraction(61, 9), 1)),
                            Segment(End(Fraction(61, 9), 1), End(Fraction(62, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(14, 3), 1), End(Fraction(43, 9), -1)), Segment(End(Fraction(43, 9), -1), End(Fraction(44, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(62, 9), -1), End(Fraction(7, 1), 1)),
                            Segment(End(Fraction(7, 1), 1), End(Fraction(65, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(61, 9), 1), End(Fraction(7, 1), -1)), Segment(End(Fraction(7, 1), -1), End(Fraction(64, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(65, 9), -1), End(Fraction(22, 3), 1)),
                            Segment(End(Fraction(22, 3), 1), End(Fraction(67, 9), -1)),
                            Tunnel(1, Segment(End(Fraction(11, 9), 1), End(Fraction(4, 3), -1)), Segment(End(Fraction(4, 3), -1), End(Fraction(13, 9), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(67, 9), -1), End(Fraction(68, 9), 1)),
                            Segment(End(Fraction(68, 9), 1), End(Fraction(23, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(31, 9), 1), End(Fraction(32, 9), -1)), Segment(End(Fraction(32, 9), -1), End(Fraction(11, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 3), -1), End(Fraction(70, 9), 1)),
                            Segment(End(Fraction(70, 9), 1), End(Fraction(71, 9), -1)),
                            Tunnel(2, Segment(End(Fraction(11, 3), 1), End(Fraction(34, 9), -1)), Segment(End(Fraction(34, 9), -1), End(Fraction(35, 9), 1))),
                        ),
                    ],
                ),
            ]
        )

    def test_12_9(self):
        knot = Knot(12, 9)
        self.assertEqual(
            knot.strings,
            [
                String(
                    0,
                    [
                        Segment(End(Fraction(1, 12), 1), End(Fraction(1, 6), -1)),
                        Segment(End(Fraction(1, 6), -1), End(Fraction(1, 4), 1)),
                        Segment(End(Fraction(1, 4), 1), End(Fraction(1, 3), -1)),
                        Segment(End(Fraction(1, 3), -1), End(Fraction(5, 12), 1)),
                        Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)),
                        Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1)),
                        Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)),
                        Segment(End(Fraction(2, 3), -1), End(Fraction(5, 6), 1)),
                        Segment(End(Fraction(5, 6), 1), End(Fraction(11, 12), -1)),
                        Segment(End(Fraction(11, 12), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(13, 12), -1)),
                        Segment(End(Fraction(13, 12), -1), End(Fraction(7, 6), 1)),
                        Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)),
                        Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1)),
                        Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)),
                        Segment(End(Fraction(17, 12), -1), End(Fraction(19, 12), 1)),
                        Segment(End(Fraction(19, 12), 1), End(Fraction(5, 3), -1)),
                        Segment(End(Fraction(5, 3), -1), End(Fraction(7, 4), 1)),
                        Segment(End(Fraction(7, 4), 1), End(Fraction(11, 6), -1)),
                        Segment(End(Fraction(11, 6), -1), End(Fraction(23, 12), 1)),
                        Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)),
                        Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1)),
                        Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)),
                        Segment(End(Fraction(13, 6), -1), End(Fraction(7, 3), 1)),
                        Segment(End(Fraction(7, 3), 1), End(Fraction(29, 12), -1)),
                        Segment(End(Fraction(29, 12), -1), End(Fraction(5, 2), 1)),
                        Segment(End(Fraction(5, 2), 1), End(Fraction(31, 12), -1)),
                        Segment(End(Fraction(31, 12), -1), End(Fraction(8, 3), 1)),
                        Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)),
                        Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1)),
                        Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)),
                        Segment(End(Fraction(35, 12), -1), End(Fraction(37, 12), 1)),
                        Segment(End(Fraction(37, 12), 1), End(Fraction(19, 6), -1)),
                        Segment(End(Fraction(19, 6), -1), End(Fraction(13, 4), 1)),
                        Segment(End(Fraction(13, 4), 1), End(Fraction(10, 3), -1)),
                        Segment(End(Fraction(10, 3), -1), End(Fraction(41, 12), 1)),
                        Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)),
                        Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1)),
                        Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)),
                        Segment(End(Fraction(11, 3), -1), End(Fraction(23, 6), 1)),
                        Segment(End(Fraction(23, 6), 1), End(Fraction(47, 12), -1)),
                        Segment(End(Fraction(47, 12), -1), End(Fraction(4, 1), 1)),
                        Segment(End(Fraction(4, 1), 1), End(Fraction(49, 12), -1)),
                        Segment(End(Fraction(49, 12), -1), End(Fraction(25, 6), 1)),
                        Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)),
                        Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1)),
                        Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)),
                        Segment(End(Fraction(53, 12), -1), End(Fraction(55, 12), 1)),
                        Segment(End(Fraction(55, 12), 1), End(Fraction(14, 3), -1)),
                        Segment(End(Fraction(14, 3), -1), End(Fraction(19, 4), 1)),
                        Segment(End(Fraction(19, 4), 1), End(Fraction(29, 6), -1)),
                        Segment(End(Fraction(29, 6), -1), End(Fraction(59, 12), 1)),
                        Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1)),
                        Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)),
                        Segment(End(Fraction(31, 6), -1), End(Fraction(16, 3), 1)),
                        Segment(End(Fraction(16, 3), 1), End(Fraction(65, 12), -1)),
                        Segment(End(Fraction(65, 12), -1), End(Fraction(11, 2), 1)),
                        Segment(End(Fraction(11, 2), 1), End(Fraction(67, 12), -1)),
                        Segment(End(Fraction(67, 12), -1), End(Fraction(17, 3), 1)),
                        Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)),
                        Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1)),
                        Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)),
                        Segment(End(Fraction(71, 12), -1), End(Fraction(73, 12), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 12), -1), End(Fraction(1, 12), 1)),
                            Segment(End(Fraction(1, 12), 1), End(Fraction(1, 6), -1)),
                            Tunnel(1, Segment(End(Fraction(0, 1), 1), End(Fraction(1, 12), -1)), Segment(End(Fraction(1, 12), -1), End(Fraction(1, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 6), -1), End(Fraction(1, 4), 1)),
                            Segment(End(Fraction(1, 4), 1), End(Fraction(1, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)), Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 3), -1), End(Fraction(5, 12), 1)),
                            Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)),
                            Tunnel(2, Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)), Segment(End(Fraction(53, 12), -1), End(Fraction(9, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1)),
                            Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(5, 2), 1), End(Fraction(31, 12), -1)), Segment(End(Fraction(31, 12), -1), End(Fraction(8, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 3), -1), End(Fraction(5, 6), 1)),
                            Segment(End(Fraction(5, 6), 1), End(Fraction(11, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(3, 4), 1), End(Fraction(5, 6), -1)), Segment(End(Fraction(5, 6), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 12), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(13, 12), -1)),
                            Tunnel(0, Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 12), -1), End(Fraction(7, 6), 1)),
                            Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)),
                            Tunnel(2, Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)), Segment(End(Fraction(31, 6), -1), End(Fraction(21, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1)),
                            Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(13, 4), 1), End(Fraction(10, 3), -1)), Segment(End(Fraction(10, 3), -1), End(Fraction(41, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 12), -1), End(Fraction(19, 12), 1)),
                            Segment(End(Fraction(19, 12), 1), End(Fraction(5, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(3, 2), 1), End(Fraction(19, 12), -1)), Segment(End(Fraction(19, 12), -1), End(Fraction(7, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 3), -1), End(Fraction(7, 4), 1)),
                            Segment(End(Fraction(7, 4), 1), End(Fraction(11, 6), -1)),
                            Tunnel(0, Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)), Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 6), -1), End(Fraction(23, 12), 1)),
                            Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)),
                            Tunnel(2, Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)), Segment(End(Fraction(71, 12), -1), End(Fraction(6, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1)),
                            Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)),
                            Tunnel(1, Segment(End(Fraction(4, 1), 1), End(Fraction(49, 12), -1)), Segment(End(Fraction(49, 12), -1), End(Fraction(25, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 6), -1), End(Fraction(7, 3), 1)),
                            Segment(End(Fraction(7, 3), 1), End(Fraction(29, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(9, 4), 1), End(Fraction(7, 3), -1)), Segment(End(Fraction(7, 3), -1), End(Fraction(5, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(29, 12), -1), End(Fraction(5, 2), 1)),
                            Segment(End(Fraction(5, 2), 1), End(Fraction(31, 12), -1)),
                            Tunnel(0, Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)), Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(31, 12), -1), End(Fraction(8, 3), 1)),
                            Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)),
                            Tunnel(2, Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)), Segment(End(Fraction(2, 3), -1), End(Fraction(3, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1)),
                            Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(19, 4), 1), End(Fraction(29, 6), -1)), Segment(End(Fraction(29, 6), -1), End(Fraction(59, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(35, 12), -1), End(Fraction(37, 12), 1)),
                            Segment(End(Fraction(37, 12), 1), End(Fraction(19, 6), -1)),
                            Tunnel(1, Segment(End(Fraction(3, 1), 1), End(Fraction(37, 12), -1)), Segment(End(Fraction(37, 12), -1), End(Fraction(13, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(19, 6), -1), End(Fraction(13, 4), 1)),
                            Segment(End(Fraction(13, 4), 1), End(Fraction(10, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)), Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 3), -1), End(Fraction(41, 12), 1)),
                            Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)),
                            Tunnel(2, Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)), Segment(End(Fraction(17, 12), -1), End(Fraction(3, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1)),
                            Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(11, 2), 1), End(Fraction(67, 12), -1)), Segment(End(Fraction(67, 12), -1), End(Fraction(17, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 3), -1), End(Fraction(23, 6), 1)),
                            Segment(End(Fraction(23, 6), 1), End(Fraction(47, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(15, 4), 1), End(Fraction(23, 6), -1)), Segment(End(Fraction(23, 6), -1), End(Fraction(4, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(47, 12), -1), End(Fraction(4, 1), 1)),
                            Segment(End(Fraction(4, 1), 1), End(Fraction(49, 12), -1)),
                            Tunnel(0, Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)), Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(49, 12), -1), End(Fraction(25, 6), 1)),
                            Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)),
                            Tunnel(2, Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)), Segment(End(Fraction(13, 6), -1), End(Fraction(9, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1)),
                            Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(1, 4), 1), End(Fraction(1, 3), -1)), Segment(End(Fraction(1, 3), -1), End(Fraction(5, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(53, 12), -1), End(Fraction(55, 12), 1)),
                            Segment(End(Fraction(55, 12), 1), End(Fraction(14, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(9, 2), 1), End(Fraction(55, 12), -1)), Segment(End(Fraction(55, 12), -1), End(Fraction(19, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(14, 3), -1), End(Fraction(19, 4), 1)),
                            Segment(End(Fraction(19, 4), 1), End(Fraction(29, 6), -1)),
                            Tunnel(0, Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)), Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(29, 6), -1), End(Fraction(59, 12), 1)),
                            Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)),
                            Tunnel(2, Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)), Segment(End(Fraction(35, 12), -1), End(Fraction(3, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1)),
                            Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)),
                            Tunnel(1, Segment(End(Fraction(1, 1), 1), End(Fraction(13, 12), -1)), Segment(End(Fraction(13, 12), -1), End(Fraction(7, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(31, 6), -1), End(Fraction(16, 3), 1)),
                            Segment(End(Fraction(16, 3), 1), End(Fraction(65, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(21, 4), 1), End(Fraction(16, 3), -1)), Segment(End(Fraction(16, 3), -1), End(Fraction(11, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(65, 12), -1), End(Fraction(11, 2), 1)),
                            Segment(End(Fraction(11, 2), 1), End(Fraction(67, 12), -1)),
                            Tunnel(0, Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)), Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(67, 12), -1), End(Fraction(17, 3), 1)),
                            Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)),
                            Tunnel(2, Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)), Segment(End(Fraction(11, 3), -1), End(Fraction(15, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1)),
                            Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(7, 4), 1), End(Fraction(11, 6), -1)), Segment(End(Fraction(11, 6), -1), End(Fraction(23, 12), 1))),
                        ),
                    ],
                ),
                String(
                    1,
                    [
                        Segment(End(Fraction(0, 1), 1), End(Fraction(1, 12), -1)),
                        Segment(End(Fraction(1, 12), -1), End(Fraction(1, 4), 1)),
                        Segment(End(Fraction(1, 4), 1), End(Fraction(1, 3), -1)),
                        Segment(End(Fraction(1, 3), -1), End(Fraction(5, 12), 1)),
                        Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)),
                        Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1)),
                        Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)),
                        Segment(End(Fraction(2, 3), -1), End(Fraction(3, 4), 1)),
                        Segment(End(Fraction(3, 4), 1), End(Fraction(5, 6), -1)),
                        Segment(End(Fraction(5, 6), -1), End(Fraction(1, 1), 1)),
                        Segment(End(Fraction(1, 1), 1), End(Fraction(13, 12), -1)),
                        Segment(End(Fraction(13, 12), -1), End(Fraction(7, 6), 1)),
                        Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)),
                        Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1)),
                        Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)),
                        Segment(End(Fraction(17, 12), -1), End(Fraction(3, 2), 1)),
                        Segment(End(Fraction(3, 2), 1), End(Fraction(19, 12), -1)),
                        Segment(End(Fraction(19, 12), -1), End(Fraction(7, 4), 1)),
                        Segment(End(Fraction(7, 4), 1), End(Fraction(11, 6), -1)),
                        Segment(End(Fraction(11, 6), -1), End(Fraction(23, 12), 1)),
                        Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)),
                        Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1)),
                        Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)),
                        Segment(End(Fraction(13, 6), -1), End(Fraction(9, 4), 1)),
                        Segment(End(Fraction(9, 4), 1), End(Fraction(7, 3), -1)),
                        Segment(End(Fraction(7, 3), -1), End(Fraction(5, 2), 1)),
                        Segment(End(Fraction(5, 2), 1), End(Fraction(31, 12), -1)),
                        Segment(End(Fraction(31, 12), -1), End(Fraction(8, 3), 1)),
                        Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)),
                        Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1)),
                        Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)),
                        Segment(End(Fraction(35, 12), -1), End(Fraction(3, 1), 1)),
                        Segment(End(Fraction(3, 1), 1), End(Fraction(37, 12), -1)),
                        Segment(End(Fraction(37, 12), -1), End(Fraction(13, 4), 1)),
                        Segment(End(Fraction(13, 4), 1), End(Fraction(10, 3), -1)),
                        Segment(End(Fraction(10, 3), -1), End(Fraction(41, 12), 1)),
                        Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)),
                        Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1)),
                        Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)),
                        Segment(End(Fraction(11, 3), -1), End(Fraction(15, 4), 1)),
                        Segment(End(Fraction(15, 4), 1), End(Fraction(23, 6), -1)),
                        Segment(End(Fraction(23, 6), -1), End(Fraction(4, 1), 1)),
                        Segment(End(Fraction(4, 1), 1), End(Fraction(49, 12), -1)),
                        Segment(End(Fraction(49, 12), -1), End(Fraction(25, 6), 1)),
                        Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)),
                        Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1)),
                        Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)),
                        Segment(End(Fraction(53, 12), -1), End(Fraction(9, 2), 1)),
                        Segment(End(Fraction(9, 2), 1), End(Fraction(55, 12), -1)),
                        Segment(End(Fraction(55, 12), -1), End(Fraction(19, 4), 1)),
                        Segment(End(Fraction(19, 4), 1), End(Fraction(29, 6), -1)),
                        Segment(End(Fraction(29, 6), -1), End(Fraction(59, 12), 1)),
                        Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1)),
                        Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)),
                        Segment(End(Fraction(31, 6), -1), End(Fraction(21, 4), 1)),
                        Segment(End(Fraction(21, 4), 1), End(Fraction(16, 3), -1)),
                        Segment(End(Fraction(16, 3), -1), End(Fraction(11, 2), 1)),
                        Segment(End(Fraction(11, 2), 1), End(Fraction(67, 12), -1)),
                        Segment(End(Fraction(67, 12), -1), End(Fraction(17, 3), 1)),
                        Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)),
                        Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1)),
                        Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)),
                        Segment(End(Fraction(71, 12), -1), End(Fraction(6, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 12), -1), End(Fraction(0, 1), 1)),
                            Segment(End(Fraction(0, 1), 1), End(Fraction(1, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)), Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 12), -1), End(Fraction(1, 4), 1)),
                            Segment(End(Fraction(1, 4), 1), End(Fraction(1, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(1, 6), 1), End(Fraction(1, 4), -1)), Segment(End(Fraction(1, 4), -1), End(Fraction(5, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 3), -1), End(Fraction(5, 12), 1)),
                            Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)),
                            Tunnel(1, Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)), Segment(End(Fraction(53, 12), -1), End(Fraction(9, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1)),
                            Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(5, 2), 1), End(Fraction(31, 12), -1)), Segment(End(Fraction(31, 12), -1), End(Fraction(8, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 3), -1), End(Fraction(3, 4), 1)),
                            Segment(End(Fraction(3, 4), 1), End(Fraction(5, 6), -1)),
                            Tunnel(2, Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)), Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 6), -1), End(Fraction(1, 1), 1)),
                            Segment(End(Fraction(1, 1), 1), End(Fraction(13, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(11, 12), 1), End(Fraction(1, 1), -1)), Segment(End(Fraction(1, 1), -1), End(Fraction(7, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 12), -1), End(Fraction(7, 6), 1)),
                            Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)),
                            Tunnel(1, Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)), Segment(End(Fraction(31, 6), -1), End(Fraction(21, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1)),
                            Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)),
                            Tunnel(0, Segment(End(Fraction(13, 4), 1), End(Fraction(10, 3), -1)), Segment(End(Fraction(10, 3), -1), End(Fraction(41, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 12), -1), End(Fraction(3, 2), 1)),
                            Segment(End(Fraction(3, 2), 1), End(Fraction(19, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)), Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(19, 12), -1), End(Fraction(7, 4), 1)),
                            Segment(End(Fraction(7, 4), 1), End(Fraction(11, 6), -1)),
                            Tunnel(2, Segment(End(Fraction(5, 3), 1), End(Fraction(7, 4), -1)), Segment(End(Fraction(7, 4), -1), End(Fraction(23, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 6), -1), End(Fraction(23, 12), 1)),
                            Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)),
                            Tunnel(1, Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)), Segment(End(Fraction(71, 12), -1), End(Fraction(6, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1)),
                            Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)),
                            Tunnel(0, Segment(End(Fraction(4, 1), 1), End(Fraction(49, 12), -1)), Segment(End(Fraction(49, 12), -1), End(Fraction(25, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 6), -1), End(Fraction(9, 4), 1)),
                            Segment(End(Fraction(9, 4), 1), End(Fraction(7, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)), Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 3), -1), End(Fraction(5, 2), 1)),
                            Segment(End(Fraction(5, 2), 1), End(Fraction(31, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(29, 12), 1), End(Fraction(5, 2), -1)), Segment(End(Fraction(5, 2), -1), End(Fraction(8, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(31, 12), -1), End(Fraction(8, 3), 1)),
                            Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)),
                            Tunnel(1, Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)), Segment(End(Fraction(2, 3), -1), End(Fraction(3, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1)),
                            Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)),
                            Tunnel(0, Segment(End(Fraction(19, 4), 1), End(Fraction(29, 6), -1)), Segment(End(Fraction(29, 6), -1), End(Fraction(59, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(35, 12), -1), End(Fraction(3, 1), 1)),
                            Segment(End(Fraction(3, 1), 1), End(Fraction(37, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(37, 12), -1), End(Fraction(13, 4), 1)),
                            Segment(End(Fraction(13, 4), 1), End(Fraction(10, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(19, 6), 1), End(Fraction(13, 4), -1)), Segment(End(Fraction(13, 4), -1), End(Fraction(41, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(10, 3), -1), End(Fraction(41, 12), 1)),
                            Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)),
                            Tunnel(1, Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)), Segment(End(Fraction(17, 12), -1), End(Fraction(3, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1)),
                            Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)),
                            Tunnel(0, Segment(End(Fraction(11, 2), 1), End(Fraction(67, 12), -1)), Segment(End(Fraction(67, 12), -1), End(Fraction(17, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 3), -1), End(Fraction(15, 4), 1)),
                            Segment(End(Fraction(15, 4), 1), End(Fraction(23, 6), -1)),
                            Tunnel(2, Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)), Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 6), -1), End(Fraction(4, 1), 1)),
                            Segment(End(Fraction(4, 1), 1), End(Fraction(49, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(47, 12), 1), End(Fraction(4, 1), -1)), Segment(End(Fraction(4, 1), -1), End(Fraction(25, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(49, 12), -1), End(Fraction(25, 6), 1)),
                            Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)),
                            Tunnel(1, Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)), Segment(End(Fraction(13, 6), -1), End(Fraction(9, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1)),
                            Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 4), 1), End(Fraction(1, 3), -1)), Segment(End(Fraction(1, 3), -1), End(Fraction(5, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(53, 12), -1), End(Fraction(9, 2), 1)),
                            Segment(End(Fraction(9, 2), 1), End(Fraction(55, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)), Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(55, 12), -1), End(Fraction(19, 4), 1)),
                            Segment(End(Fraction(19, 4), 1), End(Fraction(29, 6), -1)),
                            Tunnel(2, Segment(End(Fraction(14, 3), 1), End(Fraction(19, 4), -1)), Segment(End(Fraction(19, 4), -1), End(Fraction(59, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(29, 6), -1), End(Fraction(59, 12), 1)),
                            Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)),
                            Tunnel(1, Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)), Segment(End(Fraction(35, 12), -1), End(Fraction(3, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1)),
                            Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 1), 1), End(Fraction(13, 12), -1)), Segment(End(Fraction(13, 12), -1), End(Fraction(7, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(31, 6), -1), End(Fraction(21, 4), 1)),
                            Segment(End(Fraction(21, 4), 1), End(Fraction(16, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)), Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(16, 3), -1), End(Fraction(11, 2), 1)),
                            Segment(End(Fraction(11, 2), 1), End(Fraction(67, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(65, 12), 1), End(Fraction(11, 2), -1)), Segment(End(Fraction(11, 2), -1), End(Fraction(17, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(67, 12), -1), End(Fraction(17, 3), 1)),
                            Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)),
                            Tunnel(1, Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)), Segment(End(Fraction(11, 3), -1), End(Fraction(15, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1)),
                            Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)),
                            Tunnel(0, Segment(End(Fraction(7, 4), 1), End(Fraction(11, 6), -1)), Segment(End(Fraction(11, 6), -1), End(Fraction(23, 12), 1))),
                        ),
                    ],
                ),
                String(
                    2,
                    [
                        Segment(End(Fraction(0, 1), 1), End(Fraction(1, 12), -1)),
                        Segment(End(Fraction(1, 12), -1), End(Fraction(1, 6), 1)),
                        Segment(End(Fraction(1, 6), 1), End(Fraction(1, 4), -1)),
                        Segment(End(Fraction(1, 4), -1), End(Fraction(5, 12), 1)),
                        Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)),
                        Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1)),
                        Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)),
                        Segment(End(Fraction(2, 3), -1), End(Fraction(3, 4), 1)),
                        Segment(End(Fraction(3, 4), 1), End(Fraction(5, 6), -1)),
                        Segment(End(Fraction(5, 6), -1), End(Fraction(11, 12), 1)),
                        Segment(End(Fraction(11, 12), 1), End(Fraction(1, 1), -1)),
                        Segment(End(Fraction(1, 1), -1), End(Fraction(7, 6), 1)),
                        Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)),
                        Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1)),
                        Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)),
                        Segment(End(Fraction(17, 12), -1), End(Fraction(3, 2), 1)),
                        Segment(End(Fraction(3, 2), 1), End(Fraction(19, 12), -1)),
                        Segment(End(Fraction(19, 12), -1), End(Fraction(5, 3), 1)),
                        Segment(End(Fraction(5, 3), 1), End(Fraction(7, 4), -1)),
                        Segment(End(Fraction(7, 4), -1), End(Fraction(23, 12), 1)),
                        Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)),
                        Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1)),
                        Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)),
                        Segment(End(Fraction(13, 6), -1), End(Fraction(9, 4), 1)),
                        Segment(End(Fraction(9, 4), 1), End(Fraction(7, 3), -1)),
                        Segment(End(Fraction(7, 3), -1), End(Fraction(29, 12), 1)),
                        Segment(End(Fraction(29, 12), 1), End(Fraction(5, 2), -1)),
                        Segment(End(Fraction(5, 2), -1), End(Fraction(8, 3), 1)),
                        Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)),
                        Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1)),
                        Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)),
                        Segment(End(Fraction(35, 12), -1), End(Fraction(3, 1), 1)),
                        Segment(End(Fraction(3, 1), 1), End(Fraction(37, 12), -1)),
                        Segment(End(Fraction(37, 12), -1), End(Fraction(19, 6), 1)),
                        Segment(End(Fraction(19, 6), 1), End(Fraction(13, 4), -1)),
                        Segment(End(Fraction(13, 4), -1), End(Fraction(41, 12), 1)),
                        Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)),
                        Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1)),
                        Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)),
                        Segment(End(Fraction(11, 3), -1), End(Fraction(15, 4), 1)),
                        Segment(End(Fraction(15, 4), 1), End(Fraction(23, 6), -1)),
                        Segment(End(Fraction(23, 6), -1), End(Fraction(47, 12), 1)),
                        Segment(End(Fraction(47, 12), 1), End(Fraction(4, 1), -1)),
                        Segment(End(Fraction(4, 1), -1), End(Fraction(25, 6), 1)),
                        Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)),
                        Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1)),
                        Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)),
                        Segment(End(Fraction(53, 12), -1), End(Fraction(9, 2), 1)),
                        Segment(End(Fraction(9, 2), 1), End(Fraction(55, 12), -1)),
                        Segment(End(Fraction(55, 12), -1), End(Fraction(14, 3), 1)),
                        Segment(End(Fraction(14, 3), 1), End(Fraction(19, 4), -1)),
                        Segment(End(Fraction(19, 4), -1), End(Fraction(59, 12), 1)),
                        Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)),
                        Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1)),
                        Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)),
                        Segment(End(Fraction(31, 6), -1), End(Fraction(21, 4), 1)),
                        Segment(End(Fraction(21, 4), 1), End(Fraction(16, 3), -1)),
                        Segment(End(Fraction(16, 3), -1), End(Fraction(65, 12), 1)),
                        Segment(End(Fraction(65, 12), 1), End(Fraction(11, 2), -1)),
                        Segment(End(Fraction(11, 2), -1), End(Fraction(17, 3), 1)),
                        Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)),
                        Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1)),
                        Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)),
                        Segment(End(Fraction(71, 12), -1), End(Fraction(6, 1), 1)),
                    ],
                    [
                        Bridge(
                            Segment(End(Fraction(-1, 12), -1), End(Fraction(0, 1), 1)),
                            Segment(End(Fraction(0, 1), 1), End(Fraction(1, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)), Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 12), -1), End(Fraction(1, 6), 1)),
                            Segment(End(Fraction(1, 6), 1), End(Fraction(1, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(1, 12), 1), End(Fraction(1, 6), -1)), Segment(End(Fraction(1, 6), -1), End(Fraction(1, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 4), -1), End(Fraction(5, 12), 1)),
                            Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)),
                            Tunnel(0, Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)), Segment(End(Fraction(53, 12), -1), End(Fraction(55, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1)),
                            Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(9, 2), 1), End(Fraction(55, 12), -1)), Segment(End(Fraction(55, 12), -1), End(Fraction(14, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 3), -1), End(Fraction(3, 4), 1)),
                            Segment(End(Fraction(3, 4), 1), End(Fraction(5, 6), -1)),
                            Tunnel(1, Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)), Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 6), -1), End(Fraction(11, 12), 1)),
                            Segment(End(Fraction(11, 12), 1), End(Fraction(1, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(5, 6), 1), End(Fraction(11, 12), -1)), Segment(End(Fraction(11, 12), -1), End(Fraction(1, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(1, 1), -1), End(Fraction(7, 6), 1)),
                            Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)), Segment(End(Fraction(31, 6), -1), End(Fraction(16, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1)),
                            Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(21, 4), 1), End(Fraction(16, 3), -1)), Segment(End(Fraction(16, 3), -1), End(Fraction(65, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 12), -1), End(Fraction(3, 2), 1)),
                            Segment(End(Fraction(3, 2), 1), End(Fraction(19, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)), Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(19, 12), -1), End(Fraction(5, 3), 1)),
                            Segment(End(Fraction(5, 3), 1), End(Fraction(7, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(19, 12), 1), End(Fraction(5, 3), -1)), Segment(End(Fraction(5, 3), -1), End(Fraction(7, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 4), -1), End(Fraction(23, 12), 1)),
                            Segment(End(Fraction(23, 12), 1), End(Fraction(2, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)), Segment(End(Fraction(71, 12), -1), End(Fraction(73, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(2, 1), -1), End(Fraction(25, 12), 1)),
                            Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)),
                            Tunnel(2, Segment(End(Fraction(0, 1), 1), End(Fraction(1, 12), -1)), Segment(End(Fraction(1, 12), -1), End(Fraction(1, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 6), -1), End(Fraction(9, 4), 1)),
                            Segment(End(Fraction(9, 4), 1), End(Fraction(7, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)), Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 3), -1), End(Fraction(29, 12), 1)),
                            Segment(End(Fraction(29, 12), 1), End(Fraction(5, 2), -1)),
                            Tunnel(0, Segment(End(Fraction(7, 3), 1), End(Fraction(29, 12), -1)), Segment(End(Fraction(29, 12), -1), End(Fraction(5, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 2), -1), End(Fraction(8, 3), 1)),
                            Segment(End(Fraction(8, 3), 1), End(Fraction(11, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(7, 12), 1), End(Fraction(2, 3), -1)), Segment(End(Fraction(2, 3), -1), End(Fraction(5, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 4), -1), End(Fraction(17, 6), 1)),
                            Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(3, 4), 1), End(Fraction(5, 6), -1)), Segment(End(Fraction(5, 6), -1), End(Fraction(11, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(35, 12), -1), End(Fraction(3, 1), 1)),
                            Segment(End(Fraction(3, 1), 1), End(Fraction(37, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)), Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(37, 12), -1), End(Fraction(19, 6), 1)),
                            Segment(End(Fraction(19, 6), 1), End(Fraction(13, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(37, 12), 1), End(Fraction(19, 6), -1)), Segment(End(Fraction(19, 6), -1), End(Fraction(13, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(13, 4), -1), End(Fraction(41, 12), 1)),
                            Segment(End(Fraction(41, 12), 1), End(Fraction(7, 2), -1)),
                            Tunnel(0, Segment(End(Fraction(4, 3), 1), End(Fraction(17, 12), -1)), Segment(End(Fraction(17, 12), -1), End(Fraction(19, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(7, 2), -1), End(Fraction(43, 12), 1)),
                            Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)),
                            Tunnel(2, Segment(End(Fraction(3, 2), 1), End(Fraction(19, 12), -1)), Segment(End(Fraction(19, 12), -1), End(Fraction(5, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 3), -1), End(Fraction(15, 4), 1)),
                            Segment(End(Fraction(15, 4), 1), End(Fraction(23, 6), -1)),
                            Tunnel(1, Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)), Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 6), -1), End(Fraction(47, 12), 1)),
                            Segment(End(Fraction(47, 12), 1), End(Fraction(4, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(23, 6), 1), End(Fraction(47, 12), -1)), Segment(End(Fraction(47, 12), -1), End(Fraction(4, 1), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(4, 1), -1), End(Fraction(25, 6), 1)),
                            Segment(End(Fraction(25, 6), 1), End(Fraction(17, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(25, 12), 1), End(Fraction(13, 6), -1)), Segment(End(Fraction(13, 6), -1), End(Fraction(7, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(17, 4), -1), End(Fraction(13, 3), 1)),
                            Segment(End(Fraction(13, 3), 1), End(Fraction(53, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(9, 4), 1), End(Fraction(7, 3), -1)), Segment(End(Fraction(7, 3), -1), End(Fraction(29, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(53, 12), -1), End(Fraction(9, 2), 1)),
                            Segment(End(Fraction(9, 2), 1), End(Fraction(55, 12), -1)),
                            Tunnel(1, Segment(End(Fraction(5, 12), 1), End(Fraction(1, 2), -1)), Segment(End(Fraction(1, 2), -1), End(Fraction(7, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(55, 12), -1), End(Fraction(14, 3), 1)),
                            Segment(End(Fraction(14, 3), 1), End(Fraction(19, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(55, 12), 1), End(Fraction(14, 3), -1)), Segment(End(Fraction(14, 3), -1), End(Fraction(19, 4), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(19, 4), -1), End(Fraction(59, 12), 1)),
                            Segment(End(Fraction(59, 12), 1), End(Fraction(5, 1), -1)),
                            Tunnel(0, Segment(End(Fraction(17, 6), 1), End(Fraction(35, 12), -1)), Segment(End(Fraction(35, 12), -1), End(Fraction(37, 12), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(5, 1), -1), End(Fraction(61, 12), 1)),
                            Segment(End(Fraction(61, 12), 1), End(Fraction(31, 6), -1)),
                            Tunnel(2, Segment(End(Fraction(3, 1), 1), End(Fraction(37, 12), -1)), Segment(End(Fraction(37, 12), -1), End(Fraction(19, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(31, 6), -1), End(Fraction(21, 4), 1)),
                            Segment(End(Fraction(21, 4), 1), End(Fraction(16, 3), -1)),
                            Tunnel(1, Segment(End(Fraction(7, 6), 1), End(Fraction(5, 4), -1)), Segment(End(Fraction(5, 4), -1), End(Fraction(4, 3), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(16, 3), -1), End(Fraction(65, 12), 1)),
                            Segment(End(Fraction(65, 12), 1), End(Fraction(11, 2), -1)),
                            Tunnel(0, Segment(End(Fraction(16, 3), 1), End(Fraction(65, 12), -1)), Segment(End(Fraction(65, 12), -1), End(Fraction(11, 2), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(11, 2), -1), End(Fraction(17, 3), 1)),
                            Segment(End(Fraction(17, 3), 1), End(Fraction(23, 4), -1)),
                            Tunnel(0, Segment(End(Fraction(43, 12), 1), End(Fraction(11, 3), -1)), Segment(End(Fraction(11, 3), -1), End(Fraction(23, 6), 1))),
                        ),
                        Bridge(
                            Segment(End(Fraction(23, 4), -1), End(Fraction(35, 6), 1)),
                            Segment(End(Fraction(35, 6), 1), End(Fraction(71, 12), -1)),
                            Tunnel(2, Segment(End(Fraction(15, 4), 1), End(Fraction(23, 6), -1)), Segment(End(Fraction(23, 6), -1), End(Fraction(47, 12), 1))),
                        ),
                    ],
                ),
            ]
        )
