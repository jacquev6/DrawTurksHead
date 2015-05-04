=========
Algorithm
=========

Curves
======

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
        sp = plt.subplot(Q, P, (q - 1) * P + p, polar=True, axisbg=bg)
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

Intersections
=============

The string must go once up and once down each time it crosses another string (or itself).
So, we need to compute the coordinates of the intersection points.

Let's forget what has been said in previous section, and analyse this from a mathematical point of view.

Given two natural integers :math:`p` and :math:`q` and two real numbers :math:`r` and :math:`\delta_r` such that :math:`0 < \delta_r < r`.
Let's define the family of functions :math:`r_k : \theta \mapsto r + \delta_r \cdot \cos\left(\frac{p \cdot \theta - 2 \cdot k \cdot \pi}{q}\right)` for :math:`k \in \mathbb Z`.
Let :math:`\Gamma_k` be the graph of :math:`r_k` in polar coordinates, that is the graph of :math:`\vec{r_k} : \theta \mapsto r_k(\theta) \cdot \vec u(\theta)` where :math:`\vec u(\theta)` is the unit vector at polar angle :math:`\theta`.

:math:`\Gamma_m` and :math:`\Gamma_n` intersect if and only if :math:`\exists \theta_1, \theta_2 \in \mathbb R^2, \vec{r_m}(\theta_1) = \vec{r_n}(\theta_2)`.

.. math::

    \begin{array}{rcl}
        \vec{r_m}(\theta_1) = \vec{r_n}(\theta_2) & \iff & r_m(\theta_1) \cdot \vec u(\theta_1) = r_n(\theta_2) \cdot \vec u(\theta_2)
    \\
        & \iff & \left| \begin{array}{l}
            \left\{ \begin{array}{l}
                \vec u(\theta_1) = \vec u(\theta_2)
            \\
                r_m(\theta_1) = r_n(\theta_2)
            \end{array} \right.
        \\
            \mbox{or}
        \\
            \left\{ \begin{array}{l}
                \vec u(\theta_1) = -\vec u(\theta_2)
            \\
                r_m(\theta_1) = -r_n(\theta_2)
            \end{array} \right.
        \end{array} \right.
    \end{array}

:math:`r_k(\theta) > 0` so we can drop the case where :math:`\vec u(\theta_1) = - \vec u(\theta_2)`.

.. math::

    \begin{array}{rcl}
        \vec{r_m}(\theta_1) = \vec{r_n}(\theta_2) & \iff & \left\{ \begin{array}{l}
            \vec u(\theta_1) = \vec u(\theta_2)
        \\
            r_m(\theta_1) = r_n(\theta_2)
        \end{array} \right.
    \\
        & \iff & \left\{ \begin{array}{l}
            \vec u(\theta_1) = \vec u(\theta_2)
        \\
            \cos\left(\frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q}\right) =
            \cos\left(\frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}\right)
        \end{array} \right.
    \end{array}

:math:`\vec u` is :math:`2 \pi \mbox{-periodic}` and :math:`\cos` is even and :math:`2 \pi \mbox{-periodic}` so:

.. math::

    \begin{array}{rcl}
        \vec{r_m}(\theta_1) = \vec{r_n}(\theta_2) & \iff & \left\{ \begin{array}{l}
            \exists a \in \mathbb{Z}, \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
        \\
            \exists b \in \mathbb{Z}, \left| \begin{array}{l}
                \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi +
                \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
            \\
                \mbox{or}
            \\
                \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi -
                \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
            \end{array} \right.
        \end{array} \right.
    \\
        & \iff & \left| \begin{array}{l}
            \exists (a, b) \in \mathbb{Z}^2, \left\{ \begin{array}{l}
                \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
            \\
                \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi +
                \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
            \end{array}\right.
        \\
            \mbox{or}
        \\
            \exists (a, b) \in \mathbb{Z}^2, \left\{ \begin{array}{l}
                \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
            \\
                \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi -
                \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
            \end{array}\right.
        \end{array} \right.
    \end{array}

The first case corresponds to identical curves:

.. math::

    \begin{array}{cl}
        & \exists (a, b) \in \mathbb{Z}^2, \left\{ \begin{array}{l}
            \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
        \\
            \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi +
            \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
        \end{array}\right.
    \\
        \iff & \exists (a, b) \in \mathbb{Z}^2, \left\{ \begin{array}{l}
            \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
        \\
            n - m = a \cdot p + b \cdot q
        \end{array}\right.
    \end{array}

So, given :math:`m`, :math:`n`, :math:`p` and :math:`q`, if we can find :math:`a` and :math:`b` such that :math:`n - m = a \cdot p + b \cdot q`,
then :math:`\Gamma_m` and :math:`\Gamma_n` will be identical.
Let :math:`d = \gcd(p, q)`.
According to `Bézout's identity <https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity>`__,
:math:`\exists (a, b) \in \mathbb{Z}, n - m = a \cdot p + b \cdot q` if and only if :math:`n - m` is a multiple of :math:`d`.

Applying this to :math:`n = m + d` proves that :math:`\Gamma_{n + d}` is identical to :math:`\Gamma_{n}`.
This proves that it's enough to draw :math:`\Gamma_{k}` for :math:`k \in [0, d-1]`.

For :math:`m = n`, we can use :math:`a = q/d` and :math:`b = -p/d`.
Then we have :math:`\theta_2 = \theta_1 + \frac{2 \cdot q \cdot \pi}{d}`.
This proves that it's enough to draw each :math:`\Gamma_{k}` on :math:`\theta \in \left[0, \frac{2 \cdot q \cdot \pi}{d}\right[`.


The second case corresponds to intersections of different curves:

.. math::

    \begin{array}{cl}
        & \exists (a, b) \in \mathbb{Z}^2, \left\{ \begin{array}{l}
            \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
        \\
            \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi -
            \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
        \end{array}\right.
    \\
        \iff & \exists (a, b) \in \mathbb{Z}^2, \left\{ \begin{array}{l}
            \theta_1 = \frac{b \cdot q - a \cdot p + m + n}{p} \cdot \pi
        \\
            \theta_2 = \frac{b \cdot q + a \cdot p + m + n}{p} \cdot \pi
        \end{array}\right.
    \end{array}

Let's limit the domain to search for :math:`a` and :math:`b`: to find all intersection points,
it's enough to consider :math:`0 \le m \le n \lt d`
and :math:`(\theta_1, \theta_2) \in \left[0, \frac{2 \cdot q \cdot \pi}{d}\right[`.

.. math::

    \begin{array}{cl}
        & \left\{ \begin{array}{l}
            0 \le \theta_1 \lt \frac{2 \cdot \pi}{d}
        \\
            0 \le \theta_2 \lt \frac{2 \cdot \pi}{d}
        \end{array}\right.
    \\
        \iff & \left\{ \begin{array}{l}
            0 \le \frac{b \cdot q - a \cdot p + m + n}{p} \cdot \pi \lt \frac{2 \cdot q \cdot \pi}{d}
        \\
            0 \le \frac{b \cdot q + a \cdot p + m + n}{p} \cdot \pi \lt \frac{2 \cdot q \cdot \pi}{d}
        \end{array}\right.
    \\
        \iff & \left\{ \begin{array}{l}
            - m - n \le b \cdot q - a \cdot p \lt \frac{2 \cdot p \cdot q}{d} - m - n
        \\
            - m - n \le b \cdot q + a \cdot p \lt \frac{2 \cdot p \cdot q}{d} - m - n
        \end{array}\right.
    \\
        \implies & \left\{ \begin{array}{l}
            -\frac{m+n}{q} \le b \lt \frac{2 \cdot p}{d} - \frac{m+n}{q} \qquad \mbox{(sum)}
        \\
            -\frac{q}{d} < a < \frac{q}{d} \qquad \mbox{(difference)}
        \end{array}\right.
    \end{array}

So to find all intersections, it's enough to loop on :math:`a \in \left[-\frac{q}{d}, \frac{q}{d} \right]`
and :math:`b \in \left[-\frac{m+n}{q}, \frac{2 \cdot p}{d} - \frac{m+n}{q} \right]`.
There is an intersection for those :math:`a` and :math:`b` if and only if the third system of inequations above is verified.
   
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

        intersections = []
        for m in range(d):
          for n in range(m, d):
            minA = int(np.ceil(-q / d))
            maxA = int(np.ceil(q / d))
            minB = int(np.ceil(-(m + n) / q))
            maxB = int(np.floor(2 * p / d - (m + n) / q))
            if m == n:
              minA = 1  # @todoc Explain why we get several instances of intersections with self when we don't change minA (we add a constraint: theta_1 < theta_2 that translates to a > 0)
            for a in range(minA, maxA):
              for b in range(minB, maxB):
                if (
                  -m - n <= b * q - a * p < 2 * p * q / d - m - n
                  and
                  -m - n <= b * q + a * p < 2 * p * q / d - m - n
                ):
                  theta_1 = (b * q - a * p + m + n) * np.pi / p
                  intersections.append((theta_1, r[m](theta_1)))
        # @todoc Explain why the total number of intersections is (q - 1) * p
        assert len(intersections) == (q - 1) * p

        sp = plt.subplot(Q, P, (q - 1) * P + p, polar=True)
        for k in range(d):
          sp.plot(theta, r[k](theta))
        sp.plot(
          [theta for theta, r in intersections],
          [r for theta, r in intersections],
          "r."
        )
        sp.set_rmin(0)
        sp.set_rmax(3.1)
        sp.set_yticks([1, 2, 3])
        sp.set_yticklabels([])
        sp.set_xticklabels([])
        sp.spines['polar'].set_visible(False)

    plt.tight_layout()

@todoc There is more structure: all intersections are 0 mod pi/p so we could iterate directly on theta_1 instead of a and b. No?
