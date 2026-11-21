import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Fixed transmission coupling matrix across 3 regional substations (North, Central, South)
A = np.array([
    [6.0, -1.0,  0.0],
    [-1.0, 5.0, -2.0],
    [0.0, -2.0,  4.0]
])

# Power demand vectors across 3 daily load periods [Morning, Afternoon Peak, Night] (MW)
load_periods = [
    np.array([45.0, 38.0, 28.0]),
    np.array([72.0, 65.0, 50.0]),
    np.array([30.0, 24.0, 18.0])
]

# Factor Matrix A once using LU Decomposition
lu, piv = lu_factor(A)

print("Substation Generation Dispatch via LU Decomposition:")
print("-" * 60)

for i, b in enumerate(load_periods, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x
    print(f"Load Period {i} Output (MW):")
    print(f"  North Substation:   {x[0]:.2f}")
    print(f"  Central Substation: {x[1]:.2f}")
    print(f"  South Substation:   {x[2]:.2f}")
    print(f"  Residual Error Norm: {np.linalg.norm(residual):.2e}\n")