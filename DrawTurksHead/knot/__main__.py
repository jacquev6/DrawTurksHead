# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import itertools
import re

from .knot import Knot


def remove_kwargs(s):
    return re.sub("[a-z]*=", "", s)


def make_test(p, q):
    knot = Knot(p, q)
    yield "    def test_{}_{}(self):".format(p, q)
    yield "        knot = Knot({}, {})".format(p, q)
    yield "        self.assertEqual("
    yield "            knot.strings,"
    yield "            ["
    for string in knot.strings:
        yield "                String("
        yield "                    {},".format(string.k)
        yield "                    ["
        for segment in string.segments:
            yield remove_kwargs("                        {},".format(segment))
        yield "                    ],"
        yield "                    ["
        for bridge in string.bridges:
            yield "                        Bridge("
            yield remove_kwargs("                            {},".format(bridge.before))
            yield remove_kwargs("                            {},".format(bridge.after))
            yield remove_kwargs("                            {},".format(bridge.tunnel))
            yield "                        ),"
        yield "                    ],"
        yield "                ),"
    yield "            ]"
    yield "        )"


print """# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import unittest

from .knot import Knot, String, Segment, End, Bridge, Tunnel


class KnotTestCase(unittest.TestCase):"""

tests = []
for p, q in sorted(itertools.product(range(1, 13), repeat=2), key=lambda (p, q): (p + q, p)):
    tests.append("\n".join(make_test(p, q)))
print "\n\n".join(tests)
