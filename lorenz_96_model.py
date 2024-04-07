import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np


def plot_L96_trajectory(N=5, F=8, x0=None, t_range=(0.0, 30.0, 0.01)):
    def L96(x, t):
        d = np.zeros(N)
        for i in range(N):
            d[i] = (x[(i + 1) % N] - x[i - 2]) * x[i - 1] - x[i] + F
        return d

    # Initialize x0 if not provided
    if x0 is None:
        x0 = F * np.ones(N)
        x0[0] += 0.01

    t = np.arange(*t_range)  # Unpack tuple for clarity

    # Solve ODE using odeint
    x = integrate.odeint(L96, x0, t)

    # Create and display the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot(x[:, 0], x[:, 1], x[:, 2])
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$x_3$")
    plt.show()

# Example usage with custom parameters
plot_L96_trajectory(N=3, F=10, x0=[1, 2, 3], t_range=(0.0, 20.0, 0.02))
