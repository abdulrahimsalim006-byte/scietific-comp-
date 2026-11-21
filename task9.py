import numpy as np
from scipy.optimize import root_scalar

# Energy storage equilibrium: Charge rate balances nonlinear grid discharge
def storage_balance(E):
    return E - 30 - 12 * np.exp(-E / 25)

# Bisection Method
solution = root_scalar(storage_balance, bracket=[25, 45], method="bisect", xtol=1e-10)

# Fixed-Point Iteration: E = 30 + 12 * exp(-E/25)
def g(E):
    return 30 + 12 * np.exp(-E / 25)

E_guess = 35.0
for _ in range(100):
    E_new = g(E_guess)
    if abs(E_new - E_guess) < 1e-10:
        break
    E_guess = E_new

print(f"Equilibrium Storage Level (Bisection): {solution.root:.6f} MWh")
print(f"Equilibrium Storage Level (Fixed-Point): {E_guess:.6f} MWh")