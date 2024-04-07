import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lorenz(t, xyz, sigma, rho, beta):
    x, y, z = xyz
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

def lorenz_plt(sigma = 10.0,rho = 28.0,beta = 8.0 / 3.0):
    initial_conditions = [1.0, 1.0, 1.0]

    # Zaman aralığı
    t_span = (0, 100)
    t_eval = np.linspace(*t_span, 10000)

    # Diferansiyel denklemlerin çözümü
    sol = solve_ivp(lorenz, t_span, initial_conditions, args=(sigma, rho, beta), t_eval=t_eval)

    # Sonuçları al
    x, y, z = sol.y

    # Görselleştirme
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='b', alpha=0.7, linewidth=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Lorenz Çekicisi')
    plt.show()

lorenz_plt()