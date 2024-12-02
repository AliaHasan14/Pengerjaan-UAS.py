import numpy as np
import plotly.graph_objects as go

# Parameter gerakan
v0 = 50  # kecepatan awal dalam m/s
g = 9.81  # percepatan gravitasi dalam m/s^2

# Waktu untuk mencapai tinggi maksimum
t_maks = v0 / g

# Menghitung posisi pada waktu t
t = np.linspace(0, t_maks, 1000)  # waktu dari 0 sampai t_maks
y = v0 * t - 0.5 * g * t**2  # persamaan posisi

# Membuat grafik
fig = go.Figure()

fig.add_trace(go.Scatter(x=t, y=y, mode="lines", name="Simpangan"))

# Kustomisasi tampilan
fig.update_layout(
    title="Gerakan Benda Dilempar Vertikal (NPM Ganjil)",
    xaxis_title="Waktu (detik)",
    yaxis_title="Tinggi (meter)",
    yaxis_range=[0, max(y) + 10]  # Menampilkan tinggi maksimum dengan margin
)
