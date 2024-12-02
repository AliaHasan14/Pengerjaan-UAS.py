import numpy as np
import matplotlib.pyplot as plt

# Konstanta pegas
k = 60  # dalam N/m

# Rentang posisi x dari 0 hingga 0.5 meter dengan langkah 0.02 meter
x_values = np.arange(0, 0.5, 0.02)

# Menghitung gaya F(x) menggunakan hukum Hooke
F_values = -k * x_values  # F(x) = -kx

# Visualisasi grafik gaya F(x) terhadap posisi x
plt.plot(x_values, F_values, marker='o', color='r', linestyle='-')
plt.title('Grafik Gaya F(x) pada Pegas terhadap Posisi x')
plt.xlabel('Posisi x (meter)')
plt.ylabel('Gaya F(x) (N)')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Garis horizontal di y=0
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Garis vertikal di x=0
plt.show()
