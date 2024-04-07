import numpy as np
import matplotlib.pyplot as plt


def logistic_map(r, x0, num_steps):
    x = np.zeros(num_steps)
    x[0] = x0
    for i in range(1, num_steps):
        x[i] = r * x[i - 1] * (1 - x[i - 1])

    # Logistic Haritasını çiz
    plt.plot(x, 'b-', label='Logistic Haritası')
    plt.title('Logistic Haritası (r={})'.format(r))
    plt.xlabel('Adım')
    plt.ylabel('Popülasyon Oranı')
    plt.legend()
    plt.show()
    return plt



# Parametreler
r = 3.9  # Büyüme oranı
x0 = 0.5  # Başlangıç koşulu
num_steps = 100  # Adım sayısı

# Logistic Haritasını hesapla
population = logistic_map(r, x0, num_steps)
