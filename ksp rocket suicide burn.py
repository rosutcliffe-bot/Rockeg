import numpy as np
import matplotlib.pyplot as plt

p = 1.167
Cd = 3
A = 1.85**2 * np.pi
mi = 100300
g = 9.8067
delta_t = 0.1
Fgrav = mi * g
Vt = np.sqrt((2 * Fgrav)/(p * A * Cd))
Fthrust = 2321286

mass_flow_rate = 822.75

v = 240
y = 1000
t = 0.0

y_distance = 0.0

while v > 0.001:
    Fgrav = mi * g
    Fdrag = 0.5 * p * np.abs(v) * v * A * Cd

    Fnet = (Fthrust + Fdrag) - Fgrav
    a = Fnet / mi

    y_distance = y_distance + (v * delta_t)

    v = v - (a * delta_t)
    y = y - (v * delta_t)
    t = t + delta_t

    mi = mi - (mass_flow_rate * delta_t)

print(f"--- AIRLESS SUICIDE BURN ANALYSIS ---")
print(f"True Engine Burn Duration: {t:.2f} seconds")
print(f"CRITICAL IGNITION ALTITUDE: {y_distance:.2f} meters")
print(f"--> Ignore the countdown clock! Hit Z the exact millisecond your SURFACE ALTITUDE hits {y_distance:.1f}m!")



print(t, Vt)