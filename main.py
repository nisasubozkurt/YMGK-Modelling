import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lotka_volterra(alpha, beta, gamma, delta, prey_initial, predator_initial):
    # Zaman noktaları
    t = np.linspace(0, 100, 1000)

    # Başlangıç koşulları
    y0 = [prey_initial, predator_initial]

    # Lotka-Volterra diferansiyel denklemleri
    def model(y, t):
        prey, predator = y
        dydt = [alpha * prey - beta * prey * predator,
                gamma * prey * predator - delta * predator]
        return dydt

    # Diferansiyel denklemleri çöz
    sol = odeint(model, y0, t)

    # Grafik
    plt.figure(figsize=(10, 6))
    plt.plot(t, sol[:, 0], label='Av Popülasyonu')
    plt.plot(t, sol[:, 1], label='Yırtıcı Popülasyonu')
    plt.xlabel('Zaman')
    plt.ylabel('Popülasyon')
    plt.title('Lotka-Volterra Modeli: Yırtıcı ve Av Popülasyonları')
    plt.legend()
    plt.grid(True)
    plt.show()

# Kullanıcıdan parametreleri al
alpha = float(input("Av büyüme hızını girin (alpha): "))
beta = float(input("Yırtıcı oranını girin (beta): "))
gamma = float(input("Yırtıcı büyüme hızını girin (gamma): "))
delta = float(input("Yırtıcı ölüm hızını girin (delta): "))
prey_initial = float(input("Başlangıç av popülasyonunu girin: "))
predator_initial = float(input("Başlangıç yırtıcı popülasyonunu girin: "))

# Fonksiyonu çağır
lotka_volterra(alpha, beta, gamma, delta, prey_initial, predator_initial)
