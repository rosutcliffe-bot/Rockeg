import numpy as np
g = 9.8067
rho_0 = 1.225
H = 8400
Cd = 1.0
A = np.pi * 1.85**2

m_init = 26000
Fthrust = 760000
mass_flow_rate = 300
delta_t = 0.1

def simulate_burn(ignition_altitiude):
    rho = rho_0 * np.exp(-ignition_altitude/H)
    v = np.sqrt(
        2 * m_init * g / (rho * A * Cd)
    )

    h = ignition_altitude
    m = m_init
    t = 0.0

    log = {
        "t": [], "h": [], "v": [],
        "a": [], "m": []
    }

    while h > 0 and m > 0:
        rho = rho_0 * np.esp(-max(h, 0) / H)
        drag = 0.5 * rho * Cd * A * v**2

        acceleration = g - (drag + Fthrust) / m

        log["t"].append(t)
        log["h"].append(h)
        log["v"].append(v)
        log["a"].append(acceleration)
        log["m"].append(m)

        v_new = v + acceleration * delta_t
        h_new = h - v * delta_t

        if v_new <= 0:
            log["stopped_altitude"] = h_new
            log["stopping_time"] = t + delta_t
            log["impact_speed"] = None
            return log

        if h_new <= 0:
            impact_fraction = h/max(v * delta_t, 1e-12)
            log["impact_speed"] = v + acceleration * (
                impact_fraction * delta_t
            )
            log["stopped_altitude"] = None
            return log

        v = v_new
        h = h_new
        m -= mass_flow_rate
        t += delta_t

    return log