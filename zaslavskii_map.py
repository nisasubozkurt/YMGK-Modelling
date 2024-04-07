import numpy as np
import matplotlib.pyplot as plt

def zaslavskii_rotation_map(x, y, a, k):
    x_new = x + y + k * np.sin(2 * np.pi * y)
    y_new = y - a * np.sin(2 * np.pi * x)
    return x_new, y_new

def plot_zaslavskii_map(a, k, iterations):
    # Başlangıç koordinatları
    x, y = 0.1, 0.1

    # Değerleri saklamak için dizi
    x_values, y_values = [x], [y]

    # İterasyonları yap
    for _ in range(iterations):
        x, y = zaslavskii_rotation_map(x, y, a, k)
        x_values.append(x)
        y_values.append(y)

    # Sonuçları çiz
    plt.scatter(x_values, y_values, s=1, c='b')
    plt.title('Zaslavskii Rotation Map')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Örnek kullanım
plot_zaslavskii_map(a=0.1, k=0.1, iterations=10000)
