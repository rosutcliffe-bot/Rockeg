#hohmann transfer calculator
import numpy as np

print("select planet")
print("1. Earth")
print("2. Sun (interplanetary)")
print("3. Kerbin (KSP)")
print("4. Mars")

choice = input("1-4: ")

if choice == "2":
    p = 1.3271244e11
    unit = "Au/km"
    r_body = 0
elif choice == "3":
    p = 3.5316e12
    unit = "meters"
    r_body = 600000
    is_KSP = True
elif choice == "4":
    p = 4.2828e4
    unit = "km"
    r_body = 3389.5
else:
    p = 398600.442
    unit = "km"
    r_body = 6378.1

print(f"\n uusing standard grav parameter (mu) = {p} (units in {unit})\n")

apo1_in = float(input("apoapsis 1: "))
peri1_in = float(input("periapsis 1: "))
apo2_in = int(input("apoapsis 2: "))
peri2_in = int(input("periapsis 2: "))

if is_KSP:
    apo1 = (apo1_in * 1000) + r_body
    peri1 = (peri1_in * 1000) + r_body
    apo2 = (apo2_in * 1000) + r_body
    peri2 = (peri2_in * 1000) + r_body
else:
    apo1 = apo1_in + r_body
    peri1 = peri1_in + r_body
    apo2 = apo2_in + r_body
    peri2 = peri2_in + r_body

a1 = (apo1 + peri1)/2
a2 = (apo2 + peri2)/2

if a2 >= a1:
    r1 = peri1
    r2 = apo2
    direction = "outward"

else:
    r1 = apo1
    r2 = peri2
    direction = "inward"

v1 = np.sqrt(p*(2/r1 - 1/a1))
v2 = np.sqrt(p*(2/r2 - 1/a2))

at = (r1 + r2)/2

vt1 = np.sqrt(p*(2/r1 - 1/at))
vt2 = np.sqrt(p*(2/r2 - 1/at))

delta_v1 = vt1 - v1
delta_v2 = vt2 - v2
sigma_delta_v = np.abs(delta_v1) + np.abs(delta_v2)

tH = np.pi*np.sqrt(at**3/p)

omega_2 = np.sqrt(p/r2**3)
phi_rad = np.pi - omega_2 * tH
phi_deg = np.degrees(phi_rad)
phi_deg = (phi_deg + 180) % 360 - 180

print(f"Delta V: {sigma_delta_v} km/s")
print(f"Flight time: {tH:.4f} sec")
print(f"Phase angle: {phi_deg:.4f}°")

print(f"Transfer direction: {direction}")
print(f"Departure burn at: Radius {r1:.4f} (Velocity: {v1:.4f} -> {vt1:.4f})")
print(f"Arrival burn at: Radius {r2:.4f} (Velocity: {vt2:.4f} -> {v2:.4f})")
print(f"1st buern Δv: {delta_v1:.4f}")
print(f"2nd burn Δv: {delta_v2:.4f}")
print(f"Total Δv: {sigma_delta_v:.4f}")
print(f"Flight time: {tH:.4f} sec")
print(f"Phase angle: {phi_deg:.4f}°")