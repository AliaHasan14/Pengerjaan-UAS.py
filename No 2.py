import numpy as np
import matplotlib.pyplot as plt

# Parameter gerak harmonik sederhana
A = 0.05  # amplitudo dalam meter (5 cm)
T = 10    # periode dalam detik
t_maks = 50  # waktu total bergerak

# Menentukan array waktu
t = np.linspace(0, t_maks, 1000)

# Menentukan persamaan posisi sebagai fungsi waktu
y = A * np.sin((2 * np.pi / T) * t)

# Plot grafik posisi terhadap waktu
plt.figure(figsize=(10, 5))
plt.plot(t, y, color="b", linestyle="-", label="Posisi (y) = A * sin(2π/T * t)")
plt.xlabel("Waktu (detik)")
plt.ylabel("Posisi Simpangan (meter)")
plt.title("Grafik Gerak Harmonis Sederhana")
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Garis horizontal di y=0
plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Garis vertikal di x=0
plt.show()
