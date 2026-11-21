import numpy as np
from scipy.optimize import minimize

# Objective: Minimize Generation Cost = 50 * Solar_units + 80 * Hydro_units ($)
def dispatch_cost(z):
    solar, hydro = z
    return 50 * solar + 80 * hydro

# Constraint: 15 * Solar + 25 * Hydro >= 300 MWh regional demand
def demand_constraint(z):
    solar, hydro = z
    return 15 * solar + 25 * hydro - 300

constraints = {"type": "ineq", "fun": demand_constraint}
bounds = [(0, None), (0, None)]

solution = minimize(dispatch_cost, x0=[10, 10], method="SLSQP", bounds=bounds, constraints=constraints)

print("Optimization Success:", solution.success)
print(f"Optimal Solar Dispatch Units: {solution.x[0]:.1f}")
print(f"Optimal Hydro Dispatch Units: {solution.x[1]:.1f}")
print(f"Minimum Generation Cost: ${solution.fun:.2f}")