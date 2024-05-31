import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
a = 0
b = 1
c = 0.6

# System of differential equations
def system(t, y):
u, s = y
du_dt = a - b * u
ds_dt = b * u - c * s
return [du_dt, ds_dt]

# Initial conditions
u0 = 1
s0 = 1 / 0.6

# Time span
t_span = [0, 20]
t_eval = np.linspace(t_span[0], t_span[1], 400)

# Solving the system
sol = solve_ivp(system, t_span, [u0, s0], t_eval=t_eval)

# Extracting the results
t = sol.t
u = sol.y[0]
s = sol.y[1]

# Plotting
plt.figure(figsize=(15, 5))

# u-t plane
plt.subplot(1, 3, 1)
plt.plot(t, u, label='u(t)')
plt.xlabel('Time (t)')
plt.ylabel('u(t)')
plt.title('u(t) vs t')
plt.legend(loc = 'lower right')

# s-t plane
plt.subplot(1, 3, 2)
plt.plot(t, s, label='s(t)', color='orange')
plt.xlabel('Time (t)')
plt.ylabel('s(t)')
plt.title('s(t) vs t')
plt.legend(loc = 'lower right')

# u-s plane
plt.subplot(1, 3, 3)
plt.plot(s, u, label='u(t) vs s(t)', color='green')
plt.xlabel('s(t)')
plt.ylabel('u(t)')
plt.title('u(t) vs s(t)')
plt.legend(loc = 'lower right')

# Adding the line u = c * s
s_line = np.linspace(min(s), max(s), 400)
u_line = c * s_line
plt.plot(s_line, u_line, label='u = c * s', color='red', linestyle='--')
plt.legend()

plt.tight_layout()
plt.savefig('../figures/plt_ode_a0b1c0.6.png', dpi=300)
plt.show()
