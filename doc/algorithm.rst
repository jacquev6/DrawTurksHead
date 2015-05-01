=========
Algorithm
=========

Intuitive construction of the curves to be drawn
================================================

Looking at the flat form of Turk's head knots, we see that the string oscillates between the center
and the outside while it turns around the center.
This is why the first idea is to draw some sine wave is polar coordinates.
(Oscillation means sine wave, turning around the center means polar coordinates)

.. figure:: https://upload.wikimedia.org/wikipedia/commons/9/94/Turks-head-3-lead-10-bight-doubled.jpg
    :height: 270
    :align: center

    A Turk's head node in flat form (Image from `Wikipedia <https://en.wikipedia.org/wiki/File:Turks-head-3-lead-10-bight-doubled.jpg>`__).

Since we don't want the curve to go through the center of the image, we have to keep the radius strictly positive,
so we will draw :math:`r = r_0+\delta_r \cdot \cos(\alpha \cdot \theta)`, with :math:`0 < \delta_r < r_0`.

The next question is how to fix :math:`\alpha`.
For a knot with :math:`q` leads, the string makes :math:`q` turns around the center, so we will draw the wave for :math:`\theta \in [0, 2 \cdot q \cdot \pi]`.
Then, for a knot with :math:`p` bights, the string touches the center :math:`p` times, and the outside :math:`p` times.
Thus, the wave must have :math:`p` maxima and :math:`p` minima on the range.
:math:`\cos` has exactly one maximum and one minimum on :math:`[0, 2 \cdot \pi]`, so we can use :math:`\alpha=p/q`.
This gives us:

.. math::

    r = r_0+\delta_r \cdot \cos(p \cdot \theta/q)

    \theta \in [0, 2 \cdot q \cdot \pi]

.. figure:: wave_for_small_pqs.png
    :align: center

    :math:`r = 3 + \cos(p \cdot \theta/q)` for small values of :math:`p` and :math:`q`.

    :math:`q = 1` on the first line: the string makes one turn around the center.

    :math:`p = 1` on the left column: the string touches the outside once.

This is mainly ok, but some cases look wrong (or example, :math:`p=3` and :math:`q=6`, with a darker red background on the previous figure).
This is due to the known result that, if :math:`d=\gcd(p, q)`, you need :math:`d` strings to make a Turk's head knot with :math:`p` bights and :math:`q` leads.
This mean that we have to draw :math:`d` curves.
The total number of turns around the center is still the same, so each string makes :math:`q/d` turns,
and the range for :math:`\theta` is reduced to :math:`[0, 2 \cdot q \cdot \pi / d]` for each curve.

Since the second curve must draw the second bight, it means that the second curve must be shifted by :math:`2 \cdot \pi / p`.
Extending this result tells us that the :math:`k^{th}` curve must be shifted by :math:`2 \cdot k \cdot \pi / p`.

This give use our final family of curves:

.. math::

    r_k = r_0 + \delta_r \cdot \cos \left( \frac{p \cdot \theta - 2 \cdot k \cdot \pi}{q} \right)

    \theta \in [0, 2 \cdot q \cdot \pi / d]

    k \in [0, d]

.. figure:: families_for_small_pqs.png
    :align: center

    :math:`r_k = 3 + \cos(p \cdot \theta/q - 2 \cdot k \cdot \pi/q)` for small values of :math:`p` and :math:`q`.
