import matplotlib.pyplot as plt

def plot_complex_squared_map(real_range=10, imag_range=10, num_points=100):
    def complex_squaring(z):
        real_part = z.real ** 2 - z.imag ** 2
        imag_part = 2 * z.real * z.imag
        return complex(real_part, imag_part)

    real_values = [i * real_range / num_points for i in range(-num_points, num_points)]
    imag_values = [i * imag_range / num_points for i in range(-num_points, num_points)]

    complex_points = [complex(real, imag) for real in real_values for imag in imag_values]
    squared_points = [complex_squaring(z) for z in complex_points]

    real_parts = [z.real for z in squared_points]
    imag_parts = [z.imag for z in squared_points]

    # Scatter plot oluşturma
    plt.figure(figsize=(8, 6))
    plt.scatter(real_parts, imag_parts, s=5)
    plt.xlabel('Gerçel Bölüm')
    plt.ylabel('Sanal Bölüm')
    plt.title('Karmaşık Sayı Karesi Haritası')
    plt.grid(True)
    plt.show()


# Fonksiyonu çağırarak haritayı çizdirme
plot_complex_squared_map()

