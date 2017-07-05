========
Analysis
========

In this part we perform a mathematical analysis of the family of curves we found previously.

Definitions
===========

Let :math:`p \in \mathbb N, p > 0` and :math:`q \in \mathbb N, q > 0`.
Let :math:`d = \gcd(p, q)`, :math:`p' = \frac{p}{d}` and :math:`q' = \frac{q}{d}`.
Let :math:`r \in \mathbb R` and :math:`\delta_r \in \mathbb R` such that :math:`0 < \delta_r < r`.
Let's define the following family of functions:

.. math::

    r_k : \theta \mapsto r + \delta_r \cdot \cos\left(\frac{p \cdot \theta - 2 \cdot k \cdot \pi}{q}\right)

    k \in \mathbb Z

Let :math:`\Gamma_k` be the graph of :math:`r_k` in polar coordinates, that is the graph of
:math:`\vec{r_k} : \theta \mapsto r_k(\theta) \cdot \vec u(\theta)`
where :math:`\vec u(\theta)` is the unit vector at polar angle :math:`\theta`.

Intersections
=============

For :math:`(m, n) \in \mathbb Z^2`, :math:`\Gamma_m` and :math:`\Gamma_n` intersect if and only if
:math:`\exists \theta_1, \theta_2 \in \mathbb R^2, \vec{r_m}(\theta_1) = \vec{r_n}(\theta_2)`.

.. math::

    \begin{array}{rcl}
        \vec{r_m}(\theta_1) = \vec{r_n}(\theta_2)
        & \iff & r_m(\theta_1) \cdot \vec u(\theta_1) = r_n(\theta_2) \cdot \vec u(\theta_2)
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

:math:`0 < \delta_r < r` and :math:`\cos` is between :math:`-1` and :math:`1`
so :math:`r_k(\theta) > 0` and we can drop the second case.

.. math::

    \begin{array}{rcl}
        \vec{r_m}(\theta_1) = \vec{r_n}(\theta_2)
        & \iff & \left\{ \begin{array}{l}
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
        \vec{r_m}(\theta_1) = \vec{r_n}(\theta_2)
        & \iff & \left\{ \begin{array}{l}
            \exists a \in \mathbb Z, \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
        \\
            \exists b \in \mathbb Z, \left| \begin{array}{l}
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
            \exists (a, b) \in \mathbb Z^2, \left\{ \begin{array}{l}
                \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
            \\
                \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi +
                \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
            \end{array}\right.
            \qquad \mbox{Case 1}
        \\
            \mbox{or}
        \\
            \exists (a, b) \in \mathbb Z^2, \left\{ \begin{array}{l}
                \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
            \\
                \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi -
                \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
            \end{array}\right.
            \qquad \mbox{Case 2}
        \end{array} \right.
    \end{array}

Case 1
------

.. math::

    \begin{array}{cl}
        & \exists (a, b) \in \mathbb Z^2, \left\{ \begin{array}{l}
            \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
        \\
            \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi +
            \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
        \end{array}\right.
    \\
        \iff & \exists (a, b) \in \mathbb Z^2, \left\{ \begin{array}{l}
            \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
        \\
            n - m = a \cdot p + b \cdot q
        \end{array}\right.
    \end{array}

So if we can find :math:`a` and :math:`b` such that :math:`n - m = a \cdot p + b \cdot q`,
then :math:`\Gamma_m` and :math:`\Gamma_n` have an infinite number of intersection points and are identical.

According to `Bézout's identity <https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity>`__,
:math:`\exists (a, b) \in \mathbb Z, n - m = a \cdot p + b \cdot q` if and only if :math:`n - m` is a multiple of :math:`d`.

Reduction of the family
~~~~~~~~~~~~~~~~~~~~~~~

Applying this to :math:`n = m + d` proves that :math:`\Gamma_{n + d}` is identical to :math:`\Gamma_n`.
It's sufficient to consider intersections between :math:`\Gamma_m` and :math:`\Gamma_n` for :math:`(m, n) \in [0, d-1]^2` and :math:`m \le n`.
And it's enough to draw :math:`\Gamma_k` for :math:`k \in [0, d-1]`.

Periodicity of :math:`r_k`
~~~~~~~~~~~~~~~~~~~~~~~~~~

By construction, :math:`r_k` is :math:`2 \cdot q \cdot \pi \mbox{-periodic}`.

For :math:`m = n`, we can use :math:`a = q'` and :math:`b = -p'`.
Then we have :math:`\theta_2 = \theta_1 + 2 \cdot q' \cdot \pi`.
So :math:`r_k` is :math:`2 \cdot q' \cdot \pi \mbox{-periodic}`.
It's sufficient to consider intersections where :math:`(\theta_1, \theta_2) \in \left[0, 2 \cdot q' \cdot \pi\right[^2`.
And it's enough to draw each :math:`\Gamma_k` on :math:`\theta \in \left[0, 2 \cdot q' \cdot \pi\right[`.

Case 2
------

.. math::

    \begin{array}{cl}
        & \exists (a, b) \in \mathbb Z^2, \left\{ \begin{array}{l}
            \theta_2 = \theta_1 + 2 \cdot a \cdot \pi
        \\
            \frac{p \cdot \theta_1 - 2 \cdot m \cdot \pi}{q} = 2 \cdot b \cdot \pi -
            \frac{p \cdot \theta_2 - 2 \cdot n \cdot \pi}{q}
        \end{array}\right.
    \\
        \iff & \exists (a, b) \in \mathbb Z^2, \left\{ \begin{array}{l}
            \theta_1 = \frac{b \cdot q - a \cdot p + m + n}{p} \cdot \pi
        \\
            \theta_2 = \frac{b \cdot q + a \cdot p + m + n}{p} \cdot \pi
        \end{array}\right.
    \end{array}

So this case correspond to "real", individual intersection points.

Let's reduce the domain we need to search for :math:`a` and :math:`b`. So far, we have:

.. math::

    0 \le k \lt d

    0 \le \theta_1 \lt 2 \cdot q' \cdot \pi

    0 \le \theta_2 \lt 2 \cdot q' \cdot \pi

    \theta_1 = \frac{b \cdot q - a \cdot p + 2 \cdot k}{p} \cdot \pi

    \theta_2 = \frac{b \cdot q + a \cdot p + 2 \cdot k}{p} \cdot \pi

Replacing :math:`\theta_1` and :math:`\theta_2` in :math:`-2 \cdot q' \cdot \pi \lt \theta_2 - \theta_1 \lt 2 \cdot q' \cdot \pi`
and isolating :math:`a`, we obtain :math:`-q' + 1 \le a \lt q'`.

Then, replacing :math:`\theta_1` and :math:`\theta_2` in :math:`0 \le \theta_1 \lt 2 \cdot q' \cdot \pi`
and :math:`0 \le \theta_2 \lt 2 \cdot q' \cdot \pi` and isolating b, we obtain:

.. math::

    \frac{a \cdot p - m - n}{q} \le b \lt 2 \cdot p' - \frac{-a \cdot p + m + n}{q}

    \frac{-a \cdot p - m - n}{q} \le b \lt 2 \cdot p' - \frac{a \cdot p + m + n}{q}

We can regroup those two conditions in:

.. math::

    \frac{|a| \cdot p - m - n}{q} \le b \lt 2 \cdot p' - \frac{|a| \cdot p + m + n}{q}

So to obtain all intersections, it's enough to iterate on :math:`a` and :math:`b` in those ranges.
Note that if :math:`m = n`, this will give us each intersection twice.
We can consider only the cases where :math:`\theta_1 \lt \theta_2`,
which reduces the range of :math:`a` to :math:`1 \le a \lt q'`.

This is just a necessary condition on :math:`a` and :math:`b`.
We have proven that we obtain all intersections, but @todoc we might want to prove that we don't get duplicates.

.. plot::

    import fractions
    import math
    import matplotlib.pyplot as plt
    import numpy as np

    P = 7
    Q = 8

    plt.figure(figsize=(P, Q))

    for p in range(1, P + 1):
      for q in range(1, Q + 1):
        d = fractions.gcd(p, q)
        p_prime = p / d
        q_prime = q / d

        r = []
        for k in range(d):
          r.append(
            lambda theta, k=k: 2 + np.cos((p * theta - 2 * k * np.pi) / q)
          )
        theta = np.arange(0, 2 * q_prime * np.pi, 0.01)

        intersections = []
        # Note that these 4 imbricated loops are only O(p*q)
        for m in range(d):
          for n in range(m, d):
            if m == n:
                min_a = 1
            else:
                min_a = -q_prime + 1
            max_a = q_prime
            for a in range(min_a, max_a):
              min_b = int(math.ceil(float(abs(a) * p - m - n) / q))
              max_b = 2 * p_prime - int(math.floor(float(abs(a) * p + m + n) / q))
              for b in range(min_b, max_b):
                theta_1 = (b * q - a * p + m + n) * np.pi / p
                theta_2 = (b * q + a * p + m + n) * np.pi / p
                assert 0 <= theta_1 < 2 * q_prime * np.pi
                assert 0 <= theta_2 < 2 * q_prime * np.pi
                assert m != n or theta_1 < theta_2
                intersections.append((theta_1, r[m](theta_1)))
        assert len(intersections) == p * (q - 1)  # @todoc Explain

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
