import numpy as np
from scipy.optimize import root

def inverter_limits(vars):
    p, q = vars
    return [
        p**2 + q**2 - 25.0,      # Apparent power rating: S^2 = P^2 + Q^2 = 25 (5 MVA)
        q - (0.5 * p**2 - 2.0)   # Voltage regulation reactive power curve
    ]

# Solve nonlinear system starting from initial guess [4.0, 3.0]
solution = root(inverter_limits, [4.0, 3.0])

print("Optimal Inverter Operating Point [Active P (MW), Reactive Q (MVAR)]:", np.round(solution.x, 4))
print("Equation Residuals:", np.round(inverter_limits(solution.x), 4))