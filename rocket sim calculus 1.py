import numpy as np
import matplotlib.pyplot as plt

m = 26000
g = 9.8067
A = 1.85**2 * np.pi
Cd = 1
p = 1.225

Vo = np.sqrt((2*m*g)/(p*Cd*A))

Fthrust = 760000
ab = Fthrust/m - g

#vt = Vo + (g-Fthrust/m) * t
#ht = Ho - Vo * t - 0.5 * (g - Fthrust/m) * t**2

v = Vo/ab
t = Vo / ab
h = Vo**2/(2*ab)

print(ab, Vo, v, t, h)