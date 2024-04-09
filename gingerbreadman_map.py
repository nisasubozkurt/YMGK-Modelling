import matplotlib.pyplot as plt

def plot_gingerbread_map(iterations=10000, x_start=0.1, y_start=0.1):
    def gingerbread_map(x, y):
        x_next = 1 - y + abs(x)
        y_next = x
        return x_next, y_next

    x = x_start
    y = y_start

    x_points = [x]
    y_points = [y]

    for _ in range(iterations):
        x, y = gingerbread_map(x, y)
        x_points.append(x)
        y_points.append(y)

    plt.figure(figsize=(8, 8))
    plt.plot(x_points, y_points, 'o-', markersize=1, alpha=0.5)
    plt.title('Gingerbread Man Haritası')
    plt.show()

# 1000 iterasyon ve varsayılan başlangıç noktası için çizim
plot_gingerbread_map()
