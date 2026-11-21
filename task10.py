from scipy.optimize import root_scalar

# Utility Solar Project: -$1,500k initial build cost, 4 years of electricity sales ($100k units)
cash_flows = [-15.0, 4.0, 5.0, 5.5, 4.5]

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)

# Newton-Raphson Method
newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)

print(f"Solar Farm Internal Rate of Return (IRR): {newton.root:.6%}")
print(f"Net Present Value at IRR: {npv(newton.root):.6f}")