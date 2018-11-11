=========
Intuition
=========

Let's find a family of curves looking like Turk's head knots.

General shape
=============

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

    r = r_0 + \delta_r \cdot \cos \left(\frac{p \cdot \theta}{q} \right)

    \theta \in \left[0, 2 \cdot q \cdot \pi \right[

Let's draw this with :math:`r_0 = 2` and :math:`\delta_r = 1` for for small values of :math:`p` and :math:`q`:

.. plot::

    import numpy as np
    import matplotlib.pyplot as plt
    import fractions

    P = 7
    Q = 8

    plt.figure(figsize=(P, Q))

    for p in range(1, P + 1):
      for q in range(1, Q + 1):
        d = fractions.gcd(p, q)  # Explained below

        r = lambda theta: 2 + np.cos(p * theta / q)
        theta = np.arange(0, 2 * q * np.pi / d, 0.01)

        if d == 1:
          bg = "white"
        elif (p, q) == (3, 6):
          bg = "#ff6666"
        else:
          bg = "#ffaaaa"
        sp = plt.subplot(Q, P, (q - 1) * P + p, polar=True, facecolor=bg)
        sp.plot(theta, r(theta))
        sp.set_rmin(0)
        sp.set_rmax(3.1)
        sp.set_yticks([1, 2, 3])
        sp.set_yticklabels([])
        sp.set_xticklabels([])
        sp.spines['polar'].set_visible(False)

    plt.tight_layout()

In the previous figure, :math:`q = 1` on the first line (the string makes one turn around the center) and
:math:`p = 1` on the left column (the string touches the outside once).

Adjustment for several strings
==============================

This is mainly ok, but cases on red background look wrong (For example, :math:`p = 3` and :math:`q = 6`, with a darker red background).
This is due to the known result that, if :math:`d = \gcd(p, q)`, you need :math:`d` strings to make a Turk's head knot with :math:`p` bights and :math:`q` leads.
This means that we have to draw :math:`d` curves.
The total number of turns around the center is still the same, so each string makes :math:`q/d` turns,
and the range for :math:`\theta` is reduced to :math:`[0, 2 \cdot q \cdot \pi / d]` for each curve.

Since the second curve must draw the second bight, it means that the second curve must be shifted by :math:`2 \cdot \pi / p`.
Extending this result tells us that the :math:`k^{th}` curve must be shifted by :math:`2 \cdot k \cdot \pi / p`.
So :math:`r_k = r_0 + \delta_r \cdot \cos \left(\frac{p \cdot (\theta - 2 \cdot k \cdot \pi / p)}{q} \right)`.

This give use our final family of curves:

.. math::

    r_k = r_0 + \delta_r \cdot \cos \left( \frac{p \cdot \theta - 2 \cdot k \cdot \pi}{q} \right)

    \theta \in \left[0, \frac{2 \cdot q \cdot \pi}{d} \right[

    k \in [0, d - 1]

.. plot::

    import numpy as np
    import matplotlib.pyplot as plt
    import fractions

    P = 7
    Q = 8

    plt.figure(figsize=(P, Q))

    for p in range(1, P + 1):
      for q in range(1, Q + 1):
        d = fractions.gcd(p, q)

        r = []
        for k in range(d):
          r.append(
            lambda theta, k=k: 2 + np.cos((p * theta - 2 * k * np.pi) / q)
          )
        theta = np.arange(0, 2 * q * np.pi / d, 0.01)

        sp = plt.subplot(Q, P, (q - 1) * P + p, polar=True)
        for k in range(d):
          sp.plot(theta, r[k](theta))
        sp.set_rmin(0)
        sp.set_rmax(3.1)
        sp.set_yticks([1, 2, 3])
        sp.set_yticklabels([])
        sp.set_xticklabels([])
        sp.spines['polar'].set_visible(False)

    plt.tight_layout()

Ups and downs
=============

In a Turk's head knot, each string alternate between going up and going down every time it crosses itself or another string.
So we'll need to compute intersection points between curves of our family.
Then we'll assign alternative "altitudes" to the curves at those points.
A simple linear interpolation will give us the altitude of the string between two known altitudes.
This could be made smoother if we wanted to build a 3D model of the knot, but this is enough to draw it from above.
