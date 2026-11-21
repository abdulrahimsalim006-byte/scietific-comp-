import numpy as np

# Service years and usable grid battery capacity (MWh)
years = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
capacity_mwh = np.array([100.0, 97.5, 94.6, 91.2, 87.1, 82.3, 76.8])
degradation_rate = np.zeros_like(capacity_mwh)

# Forward, Central, and Backward Finite Differences
degradation_rate[0] = (capacity_mwh[1] - capacity_mwh[0]) / (years[1] - years[0])
for i in range(1, len(years) - 1):
    degradation_rate[i] = (capacity_mwh[i + 1] - capacity_mwh[i - 1]) / (years[i + 1] - years[i - 1])
degradation_rate[-1] = (capacity_mwh[-1] - capacity_mwh[-2]) / (years[-1] - years[-2])

for yr, cap, rate in zip(years, capacity_mwh, degradation_rate):
    print(f"Year {yr:.0f}: Capacity = {cap:.1f} MWh, Degradation Rate = {rate:.2f} MWh/yr")