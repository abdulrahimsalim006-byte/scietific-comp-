import numpy as np

# First-order RC discharge kinetics: dV/dt = -k * V
V_initial = 400.0  # Volts
k = 0.15           # Discharge constant (1/s)
h = 0.5            # Time step: 0.5 seconds
end_time = 15.0    # 15 seconds

time = np.arange(0, end_time + h, h)
voltage = np.zeros_like(time)
voltage[0] = V_initial

# Euler Integration Loop
for i in range(len(time) - 1):
    dV_dt = -k * voltage[i]
    voltage[i + 1] = voltage[i] + h * dV_dt

print(f"Euler predicted capacitor voltage after 15 seconds: {voltage[-1]:.2f} V")