# coding: utf8

# Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

import collections
import fractions
import math


def iter_overlaping_pairs(l):
    l = list(l)
    return list(zip(l, l[1:]))


def iter_successive_pairs(l):
    l = list(l)
    assert len(l) % 2 == 0
    return list(zip(l[::2], l[1::2]))


End = collections.namedtuple("End", "theta, altitude")
Segment = collections.namedtuple("Segment", "begin, end")
Bridge = collections.namedtuple("Bridge", "before, after, tunnel")
Tunnel = collections.namedtuple("Tunnel", "k, before, after")
String = collections.namedtuple("String", "k, segments, bridges")

Intersection = collections.namedtuple("Intersection", "m, n, theta_1, theta_2")


class Knot(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.d = fractions.gcd(p, q)
        self._ks = range(self.d)
        self.p_prime = p // self.d
        self.q_prime = q // self.d
        self.strings = list(self.__make_strings())

    def __make_strings(self):
        if self.q == 1:
            yield String(0, [Segment(End(0, 0), End(2 * self.p, 0))], [])
        else:
            intersections = []
            for m in range(self.d):
                for n in range(m, self.d):
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
                            assert 0 <= theta_1 < 2 * self.p * self.q_prime
                            assert 0 <= theta_2 < 2 * self.p * self.q_prime
                            assert m != n or theta_1 < theta_2
                            intersections.append(Intersection(m, n, theta_1, theta_2))
            assert len(intersections) == self.p * (self.q - 1)

            thetas_on_string = [[] for k in self._ks]
            for m, n, theta_1, theta_2 in intersections:
                thetas_on_string[m].append(theta_1)
                thetas_on_string[n].append(theta_2)
            for k in self._ks:
                assert len(thetas_on_string[k]) == len(thetas_on_string[0])
                thetas_on_string[k] = sorted(thetas_on_string[k])

            index_of_theta_on_string = [dict((theta, i) for i, theta in enumerate(thetas_on_string[k])) for k in self._ks]

            intersections_on_string = [{} for k in self._ks]
            for m, n, theta_1, theta_2 in intersections:
                intersections_on_string[m][theta_1] = (n, theta_2)
                intersections_on_string[n][theta_2] = (m, theta_1)

            altitudes_on_string = []
            altitudes_on_string.append([(-1) ** i for i in range(len(thetas_on_string[0]))])
            for k in range(1, self.d):
                cut = index_of_theta_on_string[k][thetas_on_string[0][0] + 2 * k]
                a = cut % 2
                altitudes_on_string.append([(-1) ** (i + a) for i in range(len(thetas_on_string[0]))])

            segments_on_string = [[] for k in self._ks]
            for k in self._ks:
                for begin, end in iter_overlaping_pairs(zip(thetas_on_string[k], altitudes_on_string[k])):
                    segments_on_string[k].append(Segment(End(*begin), End(*end)))
                begin = end
                end = thetas_on_string[k][0] + 2 * self.p * self.q_prime, altitudes_on_string[k][0]
                segments_on_string[k].append(Segment(End(*begin), End(*end)))

            bridges_on_string = [[] for k in self._ks]
            for k in self._ks:
                assert len(segments_on_string[k]) % 2 == 0
                if segments_on_string[k][0].end.altitude == 1:
                    segment_pairs = iter_successive_pairs(segments_on_string[k])
                else:
                    first_segment = segments_on_string[k][-1]
                    first_segment = Segment(End(first_segment.begin.theta - 2 * self.p * self.q_prime, first_segment.begin.altitude), End(first_segment.end.theta - 2 * self.p * self.q_prime, first_segment.end.altitude))
                    segment_pairs = iter_successive_pairs([first_segment] + segments_on_string[k][:-1])
                for before, after in segment_pairs:
                    assert before.begin.altitude == after.end.altitude == -1
                    assert before.end.altitude == after.begin.altitude == 1
                    assert before.end.theta == after.begin.theta
                    assert 0 <= before.end.theta < 2 * self.p * self.q_prime

                    n, theta_2 = intersections_on_string[k][before.end.theta]
                    i = index_of_theta_on_string[n][theta_2]
                    if i == 0:
                        bef_tunnel = segments_on_string[n][i - 1]
                        bef_tunnel = Segment(End(bef_tunnel.begin.theta - 2 * self.p * self.q_prime, bef_tunnel.begin.altitude), End(bef_tunnel.end.theta - 2 * self.p * self.q_prime, bef_tunnel.end.altitude))
                    else:
                        bef_tunnel = segments_on_string[n][i - 1]
                    aft_tunnel = segments_on_string[n][i]
                    assert bef_tunnel.end.theta == aft_tunnel.begin.theta, (bef_tunnel, aft_tunnel)

                    if self.p < 3 or self.q < 3:
                        before = Segment(End((before.begin.theta + before.end.theta) / 2, 0), before.end)
                        after = Segment(after.begin, End((after.begin.theta + after.end.theta) / 2, 0))
                        bef_tunnel = Segment(End((bef_tunnel.begin.theta + bef_tunnel.end.theta) / 2, 0), bef_tunnel.end)
                        aft_tunnel = Segment(aft_tunnel.begin, End((aft_tunnel.begin.theta + aft_tunnel.end.theta) / 2, 0))

                    bridges_on_string[k].append(Bridge(before, after, Tunnel(n, bef_tunnel, aft_tunnel)))

            for k in self._ks:
                yield String(k, segments_on_string[k], bridges_on_string[k])
