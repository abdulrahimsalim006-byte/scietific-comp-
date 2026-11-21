import numpy as np

rng = np.random.default_rng(303)
grid_max_capacity_mw = 500.0
mean_peak_load = 420.0
std_peak_load = 45.0
N_simulations = 100_000

# Simulate 100,000 daily peak grid load scenarios
simulated_loads = rng.normal(mean_peak_load, std_peak_load, N_simulations)

# Count overload events exceeding 500 MW grid capacity
overload_events = simulated_loads > grid_max_capacity_mw
blackout_probability = overload_events.mean()

print(f"Estimated Grid Overload / Blackout Probability: {blackout_probability:.2%}")
print(f"Simulated Overload Days: {overload_events.sum()} out of {N_simulations} days")