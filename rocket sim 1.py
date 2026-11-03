#rocket sim 1
import matplotlib.pyplot as plt
import numpy as np

p = 1.2105
#p0 = 1.225, p250 = 1.196
Cd = 0.6
A = 0.001089 * 3.14159265358979323
m = 0.5
g = 9.808
delta_t = 0.1
Fgrav = m * g
t_burn = 2
burn_steps = round(t_burn/delta_t)

print("1")

def simulate(F_burn, verbose = False):
    v = 0
    y = 0
    t_hist = [0, 0]
    v_hist = [0, 0]
    y_hist = [0, 0]
    
    for i in range(100):
        Fthrust = F_burn if i < burn_steps else 0
        Fdrag = 0.5 * p * v * abs(v) * Cd * A
        a = (Fthrust - Fdrag - Fgrav) / m

        v = v + a * delta_t
        y = y + v * delta_t

        t_hist.append((i + 1) * delta_t)
        v_hist.append(v)
        y_hist.append(y)

        if i + 1 >= burn_steps and v <= 0:
            break

    return np.array(t_hist), np.array(v_hist), np.array(y_hist)

print("1")

target = 250
tol = 0.1
lo = Fgrav
hi = 200

for n in range(100):
    F_burn = (lo + hi) / 2
    apogee = simulate(F_burn)[2].max()
    print(f"run {n}: thrust = {F_burn:.5f}N, apogee = {apogee:.5f}m")
    if abs(apogee - target) < tol:
        break
    if apogee > target:
        hi = F_burn
    else:
        lo = F_burn

print("1")

t, v, y = simulate(F_burn)
print(f"\nThrust needed for {target}m with a {t_burn}s burn at {F_burn:.5f}N")
print(f"Apogee: {y.max():.5f}m at t = {t[np.argmax(y)]:.1f}s")
print(f"max veloctiy: {v.max():.5f} m/s")
#simulate(F_burn, verbose = True)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True, figsize = (8, 7))

ax1.plot(t, v, color = "C0")
ax1.axvline(t_burn, color = "gray", linestyle = "--", label = "Burnout")
ax1.axhline(0, color = "black", linewidth = 0.5)
ax1.set_ylabel("Velocity (m/s)")
ax1.set_title("Velocity time graph")
ax1.legend()
ax1.grid(True)

ax2.plot(t, y, color = "C1")
ax2.axvline(t_burn, color = "gray", linestyle = "--")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("altitude (m)")
ax2.grid(True)

plt.tight_layout()
plt.show()

print("1")