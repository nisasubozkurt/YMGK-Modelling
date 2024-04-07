import numpy as np
import matplotlib.pyplot as plt

# Bernoulli haritası fonksiyonu
def bernoulli_map(x, r):
    return r * x * (1 - x)

# Haritayı çizmek için fonksiyon
def plot_bernoulli_map(r, iterations=1000):
    x = np.linspace(0, 1, 1000)
    y = bernoulli_map(x, r)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'r-', lw=2)
    plt.plot([0, 1], [0, 1], 'k--', lw=1)
    plt.title(f'Bernoulli Haritası (r={r})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

# Harita için r değerini seçin (0 ile 4 arasında bir değer olmalı)
r = 4.6

plot_bernoulli_map(r)