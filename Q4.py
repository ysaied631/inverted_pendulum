import sympy as sym
import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

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

# Using float() as transfer function requires this
a_value = float(a.subs([(M, M_value), (m, m_value)]))
b_value = float(b.subs([(M, M_value), (m, m_value), (g, g_value)]))
c_value = float(c.subs([(M, M_value), (m, m_value), (g, g_value), (ell, ell_value)]))
d_value = float(d.subs([(M, M_value), (m, m_value), (g, g_value), (ell, ell_value)]))

n_points = 500
t_final = 0.2
t_span = np.linspace(0, t_final, n_points)

# Input signal
input_signal = np.sin(100 * t_span**2)

# Transfer function
tf_Gs = ctrl.TransferFunction([-c_value], [1, 0, -d_value])
tf_Gx = ctrl.TransferFunction([a_value, 0, (-a_value * d_value) + (b_value * c_value)], [1, 0, -d_value, 0, 0])

# Using forced_response instead of step_response to fix error thrown
response_t_Gs, response_y_Gs, response_x_Gs = ctrl.forced_response(tf_Gs, t_span, input_signal)
response_t_Gx, response_y_Gx, response_x_Gx = ctrl.forced_response(tf_Gx, t_span, input_signal)

# Plot graphs
plt.plot(response_t_Gs, response_y_Gs)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Angle of the Rod (rad)')
plt.show()

plt.plot(response_t_Gx, response_y_Gx)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Horizontal Position of the Car (m)')
plt.show()