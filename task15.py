import numpy as np
from scipy.integrate import simpson

# Time in hours and wind farm instantaneous power output (MW)
time_hrs = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_mw = np.array([12.0, 18.5, 29.0, 35.0, 26.5, 19.0, 14.0])

# Integrate power over time using Simpson's rule to compute total MWh
total_energy_mwh = simpson(power_mw, x=time_hrs)

print(f"Total Wind Energy Generated over 12 Hours (Simpson's Rule): {total_energy_mwh:.2f} MWh")