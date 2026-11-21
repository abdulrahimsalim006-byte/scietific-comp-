import numpy as np
from scipy.integrate import solve_ivp

# Reservoir water head depletion ODE during peak generation: dH/dt = -k * H
def head_depletion(t, H):
    k = 0.06  # Outflow depletion coefficient
    return [-k * H[0]]

t_eval = np.linspace(0, 12, 200)
# Initial reservoir water head: 85.0 meters
solution = solve_ivp(head_depletion, (0, 12), [85.0], t_eval=t_eval)

print(f"Remaining reservoir head at Hour 12: {solution.y[0, -1]:.2f} meters")
print("SciPy Solver Success:", solution.success)