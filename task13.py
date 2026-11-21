import numpy as np
from scipy.optimize import curve_fit

# Quarters elapsed and regional EV charging demand (MWh)
quarters = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
ev_demand_mwh = np.array([80, 115, 165, 230, 310, 410, 525], dtype=float)

def demand_model(x, a, b, c):
    return a * x**2 + b * x + c

params, _ = curve_fit(demand_model, quarters, ev_demand_mwh)
a, b, c = params

print(f"Fitted EV Demand Model: MWh = {a:.2f}q^2 + {b:.2f}q + {c:.2f}")
print(f"Forecasted EV Charging Demand in Quarter 10: {demand_model(10, a, b, c):.0f} MWh")