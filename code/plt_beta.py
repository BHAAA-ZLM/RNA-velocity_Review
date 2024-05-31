import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
c = 0.8
a = 1.0

# Function to solve the system and plot for different values of a
def plot_for_different_c(a, b_values, c, t_span, t_eval, save=False):
    plt.figure(figsize=(15, 5))

    # u-t plane
    plt.subplot(1, 3, 1)
    plt.xlabel('Time (t)')
    plt.ylabel('u(t)')
    plt.title('u(t) vs t')

    # s-t plane
    plt.subplot(1, 3, 2)
    plt.xlabel('Time (t)')
    plt.ylabel('s(t)')
    plt.title('s(t) vs t')

    # u-s plane
    plt.subplot(1, 3, 3)
    plt.xlabel('s(t)')
    plt.ylabel('u(t)')
    plt.title('u(t) vs s(t)')

    # Colors
    colors = plt.cm.viridis(np.linspace(0, 1, len(b_values)))

    for i, b in enumerate(b_values):
        # Solving the system for each value of c
        sol = solve_ivp(lambda t, y: system(t, y, a, b, c), t_span, [0.0, 0.0], t_eval=t_eval)

        t = sol.t
        u = sol.y[0]
        s = sol.y[1]

        color = colors[i]

        # u-t plane
        plt.subplot(1, 3, 1)
        plt.plot(t, u, color=color)

        # s-t plane
        plt.subplot(1, 3, 2)
        plt.plot(t, s, color=color)

        # u-s plane
        plt.subplot(1, 3, 3)
        plt.plot(s, u, label=rf'$\beta={b:.1f}$', color=color)

        # Adding the line u = c * s in u-s plane
        s_line = np.linspace(min(s), max(s), 400)
        u_line = c * s_line
        plt.plot(s_line, u_line, color='black', linestyle='--')

    plt.subplot(1, 3, 3)
    plt.legend()

    plt.tight_layout()
    if save:
        plt.savefig('../figures/plt_diff_beta.png', dpi=300)
    plt.show()



# Defining the system with parameters
def system(t, y, a, b, c):
    u, s = y
    du_dt = a - b * u
    ds_dt = b * u - c * s
    return [du_dt, ds_dt]

# Time span and evaluation points
t_span = [0, 20]
t_eval = np.linspace(t_span[0], t_span[1], 400)

# Range of c values
b_values = np.arange(c, c + 1, 0.1)

# Plot for different c values
plot_for_different_c(a, b_values, c, t_span, t_eval, save=True)
