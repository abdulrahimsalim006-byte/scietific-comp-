import numpy as np

# High-voltage transmission line adjacency matrix [Hydro Plant, Main Hub, Industrial Zone, Solar Park]
A = np.array([
    [0., 1., 0., 1.],
    [1., 0., 1., 1.],
    [0., 1., 0., 1.],
    [1., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Dominant eigenvalue and eigenvector for structural importance
index = np.argmax(np.real(eigenvalues))
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["Hydro Plant", "Main Grid Hub", "Industrial Zone", "Solar Park"]

print("Grid Node Structural Centrality Scores:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")