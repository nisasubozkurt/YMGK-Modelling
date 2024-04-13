from django.db import models
import numpy as np

# Create your models here.
def lorenz96_model(N, F, dt, num_steps):
    """
    Lorenz 96 modelini çalıştırır ve verileri döndürür.
    
    Argümanlar:
    N : int
        Değişken sayısı.
    F : float
        Forcing term.
    dt : float
        Zaman adımı.
    num_steps : int
        Toplam adım sayısı.
    
    Dönüş:
    numpy.ndarray
        Modelin ürettiği veri.
    """
    data = np.zeros((N, num_steps))
    x = np.random.rand(N) * 2 - 1  # Başlangıç koşulları
    for t in range(num_steps):
        for i in range(N):
            data[i, t] = x[i] + (x[(i + 1) % N] - x[i - 2]) * x[i - 1] - x[i] + F
        x += dt * data[:, t]
    return data

def bernoulli_map(x, r):
    """
    Bernoulli haritasını hesaplayan fonksiyon.
    
    Argümanlar:
    x : float
        Mevcut x değeri.
    r : float
        Bernoulli haritasının parametresi.
    
    Dönüş:
    float
        Bir sonraki x değeri.
    """
    return r * x * (1 - x)