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