import numpy as np
import matplotlib.pyplot as plt

def kaplan_yorke_map(x, r):
    return r * x * (1 - x)

def generate_trajectory(x0, r, n):
    trajectory = [x0]
    for _ in range(n):
        x_next = kaplan_yorke_map(trajectory[-1], r)
        trajectory.append(x_next)
    plt.plot(trajectory[:-1], trajectory[1:], 'o', markersize=1)
    plt.xlabel('$x_n$')
    plt.ylabel('$x_{n+1}$')
    plt.title('Kaplan-Yorke Haritası')
    plt.show()
    return trajectory

# Başlangıç değeri
x0 = 0.2

# Sistem parametresi (örneğin)
r = 2.5

# Harita çizimi için nokta sayısı
n = 1000

# Harita oluşturma
generate_trajectory(x0, r, n)