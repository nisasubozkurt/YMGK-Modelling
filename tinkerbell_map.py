import numpy as np
import matplotlib.pyplot as plt


def generate_tinkerbell_map(a, b, c, d, width=100, height=100, x0=0.1, y0=0.1, iterations=10000):
    def tinkerbell_map(x, y):
        xn = x ** 2 - y ** 2 + a * x + b * y
        yn = 2 * x * y + c * x + d * y
        return xn, yn

    map = np.zeros((width, height))

    x, y = x0, y0
    for i in range(iterations):
        x, y = tinkerbell_map(x, y)
        ix, iy = int((x + 2) / 4 * width), int((y + 2) / 4 * height)
        if 0 <= ix < width and 0 <= iy < height:
            map[iy, ix] += 1

    plt.imshow(map, cmap='hot', origin='lower', extent=(-2, 2, -2, 2))
    plt.title('Tinkerbell Haritası')
    plt.colorbar(label='Ziyaret Sayısı')
    plt.show()
    return map


a = 0.9
b = -0.6013
c = 2.0
d = 0.50
map = generate_tinkerbell_map(a, b, c, d)