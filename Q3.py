import sympy as sym

# Symbols declaration
M, m, g, ell, x1, x2, x3, x4, F = sym.symbols('M, m, g, ell, x1, x2, x3, x4, F', real=True, positive=True)

# Functions
phi = 4 * m * ell * x4**2 * sym.sin(x3) + 4 * F - 3 * m * g * sym.sin(x3) * sym.cos(x3)
phi /= 4 * (M + m) - 3 * m * sym.cos(x3)**2

psi = -3 * (m * ell * x4**2 * sym.sin(x3) * sym.cos(x3) + F * sym.cos(x3) - (M + m) * g * sym.sin(x3))
psi /= ell * (4 * (M + m) - 3 * m * sym.cos(x3)**2)

# Derivatives
dphi_F = phi.diff(F)
dphi_x3 = phi.diff(x3)
dphi_x4 = phi.diff(x4)

dpsi_F = psi.diff(F)
dpsi_x3 = psi.diff(x3)
dpsi_x4 = psi.diff(x4)

# Variables
F_eq = 0
x3_eq = 0
x4_eq = 0
M_value = 0.3
m_value = 0.1
ell_value = 0.35
g_value = 9.81


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

# constants
a = dphi_F_eq
b = -dphi_x3_eq
c = -dpsi_F_eq
d = dpsi_x3_eq

# Symbols declaration, w = omega
a, b, c, d = sym.symbols('a, b, c, d', real=True, positive=True)
s, t = sym.symbols('s, t')
w = sym.symbols('w', real=True)

# Transfer function declaration
Gs = - c / (s**2 - d)
Gx = ((a * s**2) - (a * d) + (b * c)) / s**2 / (s**2 -d)

# Impulse, Step and Frequency
Fs_impulse = 1
Fs_step = 1 / s
Fs_frequency = w / (s**2 + w**2)

# Gs
impulse_X3s_Gs = Gs * Fs_impulse
impulse_x3t_Gs = sym.inverse_laplace_transform(impulse_X3s_Gs, s, t)

step_X3s_Gs = Gs * Fs_step
step_x3t_Gs = sym.inverse_laplace_transform(step_X3s_Gs, s, t)

frequency_X3s_Gs = Gs * Fs_frequency
frequency_x3t_Gs = sym.inverse_laplace_transform(frequency_X3s_Gs, s, t, w)

# Gx
impulse_X1s_Gx = Gx * Fs_impulse
impulse_x1t_Gx = sym.inverse_laplace_transform(impulse_X1s_Gx, s, t)

step_X1s_Gx = Gx * Fs_step
step_x1t_Gx = sym.inverse_laplace_transform(step_X1s_Gx, s, t)

frequency_X1s_Gx = Gx * Fs_frequency
frequency_x1t_Gx = sym.inverse_laplace_transform(frequency_X1s_Gx, s, t, w)

# Print the expressions
sym.pprint(impulse_x3t_Gs.simplify())
sym.pprint(step_x3t_Gs.simplify())
sym.pprint(frequency_x3t_Gs.simplify())
sym.pprint(impulse_x1t_Gx.simplify())
sym.pprint(step_x1t_Gx.simplify())
sym.pprint(frequency_x1t_Gx.simplify())

# Print LaTex
print(sym.latex(impulse_x3t_Gs.simplify()))
print(sym.latex(step_x3t_Gs.simplify()))
print(sym.latex(frequency_x3t_Gs.simplify()))
print(sym.latex(impulse_x1t_Gx.simplify()))
print(sym.latex(step_x1t_Gx.simplify()))
print(sym.latex(frequency_x1t_Gx.simplify()))