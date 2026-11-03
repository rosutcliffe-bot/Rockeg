import numpy as np
import matplotlib.pyplot as plt

p = 1.2105
Cd = 1
A = 1.85**2 * np.pi
mi = 26000
g = 9.8067
delta_t = 0.1
Fgrav = mi * g
Vt = np.sqrt((2 * Fgrav)/(p * A * Cd))
Fthrust = 760000

mass_flow_rate = 300

v = Vt
y = 1129.101
t = 0.0

t_log = []
v_log = []
y_log = []

while v > 0 and y > 0:
    Fgrav = mi * g
    Fdrag = 0.5 * p * v**2 * A * Cd

    if v < 100:
        #current_thrust = max(Fthrust * 0.4, Fthrust * (v / 100))
        current_flow = max(mass_flow_rate * 0.4, mass_flow_rate * (v/100))
    else:
        current_thrust = Fthrust
        current_flow = mass_flow_rate
    Fnet = (current_thrust + Fdrag) - Fgrav
    a = Fnet / mi

    v = v - (a * delta_t)
    y = y - (v * delta_t)
    t = t + delta_t

    mi -= current_flow * delta_t

    t_log.append(t)
    v_log.append(v)
    y_log.append(y)

print(t, Vt, y)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True, figsize = (8, 7))

ax1. plot(t_log, v_log, color = "C0")
ax1.axhline(0, color = "black", linewidth = 0.5)
ax1.set_ylabel("Velocity (m/s)")
ax1.set_title("Velocity time graph")
ax1.legend()
ax1.grid(True)

ax2.plot(t_log, y_log, color = "C0")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("altitude (m)")
ax2.grid(True)

plt.tight_layout()
plt.show()