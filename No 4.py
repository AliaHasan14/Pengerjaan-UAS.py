import numpy as np
import plotly.graph_objects as go
from scipy.integrate import quad

# Definisikan fungsi gaya
def F(x):
    return 2 * x**2 + 4 * x + 2

# Jarak perpindahan
x_max = 30

# Hitung kerja menggunakan integral
work, _ = quad(F, 0, x_max)

# Buat array untuk posisi
x = np.linspace(0, x_max, 1000)
y = F(x)

# Membuat grafik gaya sebagai fungsi posisi
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Gaya (F)"))

# Kustomisasi tampilan
fig.update_layout(
    title="Gaya Tak Konstan sebagai Fungsi Posisi",
    xaxis_title="Posisi (meter)",
    yaxis_title="Gaya (N)",
    yaxis_range=[0, max(y) + 10]  # Menampilkan rentang gaya dengan margin
)

# Menampilkan grafik
fig.show()

# Menampilkan hasil kerja
print(f"Kerja yang dilakukan oleh gaya saat berpindah sejauh {x_max} meter adalah {work:.2f} Joule.")
