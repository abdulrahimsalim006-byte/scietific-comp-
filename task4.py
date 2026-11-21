import numpy as np

# 4 Wind Turbine coordinates [East (km), North (km)]
turbine_coords = np.array([
    [1.0, 2.0],
    [4.0, 2.0],
    [4.0, 6.0],
    [1.0, 6.0]
])

# 60-degree rotation to align with prevailing seasonal wind direction
angle = np.deg2rad(60)
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

# Wake-spacing scaling matrix (1.4x crosswind spacing, 0.9x downwind spacing)
scale = np.array([
    [1.4, 0.0],
    [0.0, 0.9]
])

transformation = rotation @ scale
new_coords = turbine_coords @ transformation.T

print("Original Turbine Coordinates [East, North]:\n", turbine_coords)
print("\nComposite Transformation Matrix:\n", np.round(transformation, 4))
print("\nRealigned Turbine Coordinates:\n", np.round(new_coords, 2))
print("\nTransformation Determinant:", round(np.linalg.det(transformation), 4))