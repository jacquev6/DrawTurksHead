# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import collections
import fractions
import math


End = collections.namedtuple("End", "theta, altitude")
Segment = collections.namedtuple("Segment", "begin, end")
Bridge = collections.namedtuple("Bridge", "before, after, tunnel")
Tunnel = collections.namedtuple("Tunnel", "k, before, after")
String = collections.namedtuple("String", "k, segments, bridges")


class Knot(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.d = fractions.gcd(p, q)
        self._ks = range(self.d)
        self.p_prime = p // self.d
        self.q_prime = q // self.d
        self.__one_turn = 2 * self.p * self.q_prime
        if self.q == 1:
            self.strings = [String(0, [Segment(End(0, 0), End(2 * self.p, 0))], [])]
        else:
            self.strings = list(self.__make_strings())

    def __make_strings(self):
        intersections = list(self.__find_intersections())
        tidied_intersections = self.__tidy_intersections(intersections)
        ends = list(self.__make_ends(tidied_intersections))
        segments = list(self.__make_segments(ends))
        bridges = list(self.__make_bridges(tidied_intersections, segments))
        for k in self._ks:
            yield String(k, segments[k], bridges[k])

    def __find_intersections(self):
        found = 0
        for m in range(self.d):
            for n in range(m, self.d):
                for theta_1, theta_2 in self.__find_strings_intersections(m, n):
                    assert 0 <= theta_1 < self.__one_turn
                    assert 0 <= theta_2 < self.__one_turn
                    assert m != n or theta_1 < theta_2
                    found += 1
                    yield m, n, theta_1, theta_2
        assert found == self.p * (self.q - 1)

    def __find_strings_intersections(self, m, n):
        if m == n:
            min_a = 1
        else:
            min_a = -self.q_prime + 1
        max_a = self.q_prime
        for a in range(min_a, max_a):
            min_b = int(math.ceil(float(abs(a) * self.p - m - n) / self.q))
            max_b = 2 * self.p_prime - int(math.floor(float(abs(a) * self.p + m + n) / self.q))
            for b in range(min_b, max_b):
                theta_1 = b * self.q - a * self.p + m + n
                theta_2 = b * self.q + a * self.p + m + n
                yield theta_1, theta_2

    def __tidy_intersections(self, intersections):
        tidied_intersections = [{} for k in self._ks]
        for m, n, theta_1, theta_2 in intersections:
            tidied_intersections[m][theta_1] = (n, theta_2)
            tidied_intersections[n][theta_2] = (m, theta_1)
        return tidied_intersections

    def __make_ends(self, tidied_intersections):
        ref_ends = list(self.__make_ref_ends(tidied_intersections))
        yield ref_ends
        ref_ends = {e.theta: e for e in ref_ends}
        for k in range(1, self.d):
            yield list(self.__make_string_ends(ref_ends, tidied_intersections, k))

    def __make_ref_ends(self, tidied_intersections):
        for (i, theta) in enumerate(sorted(tidied_intersections[0].iterkeys())):
            yield End(theta, (-1)**i)

    def __make_string_ends(self, ref_ends, tidied_intersections, k):
        for theta in tidied_intersections[k].iterkeys():
            altitude = ref_ends[(theta - 2 * k) % (self.__one_turn)].altitude
            yield End(theta, altitude)

    def __make_segments(self, ends):
        for string_ends in ends:
            yield list(self.__make_string_segments(string_ends))

    def __make_string_segments(self, string_ends):
        for begin, end in zip(string_ends, string_ends[1:]):
            yield Segment(begin, end)
        yield Segment(
            string_ends[-1],
            End(string_ends[0].theta + self.__one_turn, string_ends[0].altitude)
        )

    def __make_bridges(self, tidied_intersections, segments):
        segs_by_begin = [{s.begin.theta: s for s in string_segments} for string_segments in segments]
        segs_by_end = [{s.end.theta: s for s in string_segments} for string_segments in segments]
        for k, string_segments in enumerate(segments):
            yield list(self.__make_string_bridges(tidied_intersections, segs_by_begin, segs_by_end, k, string_segments))

    def __make_string_bridges(self, tidied_intersections, segs_by_begin, segs_by_end, k, string_segments):
        assert len(string_segments) % 2 == 0
        it = iter(string_segments)  # Inspired by grouper in https://docs.python.org/2/library/itertools.html#recipes
        if string_segments[0].end.altitude != 1:
            after = it.next()
            before = self.__rotate_segment(string_segments[-1])
            yield self.__make_bridge(tidied_intersections, segs_by_begin, segs_by_end, k, before, after)
        for before, after in zip(it, it):
            yield self.__make_bridge(tidied_intersections, segs_by_begin, segs_by_end, k, before, after)

    def __rotate_segment(self, segment):
        return Segment(
            End(segment.begin.theta - self.__one_turn, segment.begin.altitude),
            End(segment.end.theta - self.__one_turn, segment.end.altitude),
        )

    def __make_bridge(self, tidied_intersections, segs_by_begin, segs_by_end, k, before, after):
        assert before.end.theta == after.begin.theta
        assert before.end.altitude == after.begin.altitude == 1
        n, theta_2 = tidied_intersections[k][before.end.theta]
        tunnel = self.__make_tunnel(segs_by_begin, segs_by_end, n, theta_2)
        bridge = Bridge(before, after, tunnel)
        if self.p < 3 or self.q < 3:
            return self.__shorten_bridge(bridge)
        else:
            return bridge

    def __make_tunnel(self, segs_by_begin, segs_by_end, n, theta_2):
        if theta_2 in segs_by_end[n]:
            bef_tunnel = segs_by_end[n][theta_2]
        else:
            bef_tunnel = self.__rotate_segment(segs_by_end[n][theta_2 + self.__one_turn])
        aft_tunnel = segs_by_begin[n][theta_2]
        return Tunnel(n, bef_tunnel, aft_tunnel)

    def __shorten_bridge(self, bridge):
        return Bridge(
            Segment(End((bridge.before.begin.theta + bridge.before.end.theta) / 2, 0), bridge.before.end),
            Segment(bridge.after.begin, End((bridge.after.begin.theta + bridge.after.end.theta) / 2, 0)),
            Tunnel(
                bridge.tunnel.k,
                Segment(End((bridge.tunnel.before.begin.theta + bridge.tunnel.before.end.theta) / 2, 0), bridge.tunnel.before.end),
                Segment(bridge.tunnel.after.begin, End((bridge.tunnel.after.begin.theta + bridge.tunnel.after.end.theta) / 2, 0)),
            ),
        )
