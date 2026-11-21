import numpy as np
from scipy.interpolate import interp1d, CubicSpline

# Solar irradiance (W/m^2) recorded every 2 hours from 06:00 to 18:00
hours = np.array([6, 8, 10, 12, 14, 16, 18], dtype=float)
irradiance = np.array([50.0, 320.0, 680.0, 920.0, 810.0, 410.0, 40.0])

linear = interp1d(hours, irradiance, kind="linear")
cubic = CubicSpline(hours, irradiance)

# Estimate solar irradiance at 11:00 AM
target_hour = 11.0

print(f"Linear Irradiance estimate at 11:00 AM: {float(linear(target_hour)):.2f} W/m^2")
print(f"Cubic Spline Irradiance estimate at 11:00 AM: {float(cubic(target_hour)):.2f} W/m^2")