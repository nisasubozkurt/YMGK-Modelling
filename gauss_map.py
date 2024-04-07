import matplotlib.pyplot as plt

def gauss_map(x, r):
    return r * x * (1 - x)

def generate_map(x0, r, n):
    map_values = [x0]
    for _ in range(n):
        x0 = gauss_map(x0, r)
        map_values.append(x0)
    plt.plot(map_values[:-1], map_values[1:], '.', markersize=1)
    plt.xlabel('x_n')
    plt.ylabel('x_{n+1}')
    plt.title(f"Gauss Map (r={r})")
    plt.show()
    return plt

# Başlangıç noktası ve kaos parametresi
x0 = 0.2
r = 3.9
# Kaç adım yapılacağı
n = 10000

# Gauss haritasını oluştur
map_values = generate_map(x0, r, n)

