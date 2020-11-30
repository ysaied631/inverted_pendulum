import sympy as sym

# Symbols declaration
M, m, g, ell, x1, x2, x3, x4, F = sym.symbols('M, m, g, ell, x1, x2, x3, x4, F')

# Functions
phi = 4 * m * ell * x4**2 * sym.sin(x3) + 4 * F - 3 * m * g * sym.sin(x3) * sym.cos(x3)
phi /= 4 * (M + m) - 3 * m * sym.cos(x3)**2

psi = -3 * (m * ell * x4**2 * sym.sin(x3) * sym.cos(x3) + F * sym.cos(x3) - (M + m) * g * sym.sin(x3))
psi /= ell * (4 * (M + m) - 3 * m * sym.cos(x3)**2)

sym.pprint(phi)
sym.pprint(psi)

# Derivatives
dphi_F = phi.diff(F)
dphi_x3 = phi.diff(x3)
dphi_x4 = phi.diff(x4)

dpsi_F = psi.diff(F)
dpsi_x3 = psi.diff(x3)
dpsi_x4 = psi.diff(x4)

# Equilibrium
F_eq = 0
x3_eq = 0
x4_eq = 0


# Function to simplify subbing in equilibrium values to each derivative
def evaluate_at_equilibrium(f):
    return f.subs([(F, F_eq), (x3, x3_eq), (x4, x4_eq)])


# Substitute equilibrium values
dphi_F_eq = evaluate_at_equilibrium(dphi_F)
dphi_x3_eq = evaluate_at_equilibrium(dphi_x3)
dphi_x4_eq = evaluate_at_equilibrium(dphi_x4)
dpsi_F_eq = evaluate_at_equilibrium(dpsi_F)
dpsi_x3_eq = evaluate_at_equilibrium(dpsi_x3)
dpsi_x4_eq = evaluate_at_equilibrium(dpsi_x4)

# Print partial derivatives
sym.pprint(dphi_F_eq)
sym.pprint(dphi_x3_eq)
sym.pprint(dphi_x4_eq)
sym.pprint(dpsi_F_eq)
sym.pprint(dpsi_x3_eq)
sym.pprint(dpsi_x4_eq)

# Print LaTex
print(sym.latex(phi))
print(sym.latex(psi))
print(sym.latex(dphi_F_eq))
print(sym.latex(dphi_x3_eq))
print(sym.latex(dphi_x4_eq))
print(sym.latex(dpsi_F_eq))
print(sym.latex(dpsi_x3_eq))
print(sym.latex(dpsi_x4_eq))