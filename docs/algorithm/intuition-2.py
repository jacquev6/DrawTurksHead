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