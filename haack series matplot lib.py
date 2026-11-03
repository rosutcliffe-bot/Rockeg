import numpy as np
import matplotlib.pyplot as plt

D = 6.6
L = 20
C = 0
R = D / 2
pi = 3.14159265358979323846

theta = np.linspace(0, pi, 1001)

x = (L/2) * (1 - np.cos(theta))
y = (R/np.sqrt(pi)) * np.sqrt(theta - np.sin(2 * theta)/2+C*np.sin(theta)**3)

fig, ax = plt.subplots()
ax.plot(x, y, color="C0")
ax.plot(x, -y, color="C0")
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("radius")
ax.set_title(f"Haack Series Nose Cone (C = {C:.5f})")
plt.show()