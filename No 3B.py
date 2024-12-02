import numpy as np
import plotly.graph_objects as go

# Parameter gerakan
v0 = 50  # kecepatan awal dalam m/s
g = 9.81  # percepatan gravitasi dalam m/s^2

# Waktu untuk mencapai tinggi maksimum
t_maks = v0 / g

# Menghitung posisi pada waktu t untuk NPM genap (sampai kembali ke posisi awal)
total_time = 2 * t_maks  # total waktu sampai kembali ke posisi awal
t_genap = np.linspace(0, total_time, 1000)  # waktu dari 0 sampai total_time
y_genap = v0 * t_genap - 0.5 * g * t_genap**2  # persamaan posisi

# Membuat grafik untuk NPM genap
fig_genap = go.Figure()
fig_genap.add_trace(go.Scatter(x=t_genap, y=y_genap, mode="lines", name="Simpangan (NPM Genap)"))
fig_genap.update_layout(
    title="Gerakan Benda Dilempar Vertikal (NPM Genap)",
    xaxis_title="Waktu (detik)",
    yaxis_title="Tinggi (meter)",
    yaxis_range=[0, max(y_genap) + 10]  # Menampilkan tinggi maksimum dengan margin
)
