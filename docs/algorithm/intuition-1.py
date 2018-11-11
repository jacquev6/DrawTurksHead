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