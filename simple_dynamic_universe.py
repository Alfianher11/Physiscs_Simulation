import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameter kosmologis
H0 = 70.0  # Hubble constant dalam (km/s)/Mpc
H0 = H0 / 3.086e19  # Konversi ke satuan 1/s
Omega_m = 0.3  # Parameter densitas materi
Omega_r = 8.4e-5  # Parameter densitas radiasi
Omega_Lambda = 0.7  # Parameter densitas energi gelap

# Fungsi Friedmann
def friedmann(t, a):
    return H0 * np.sqrt(Omega_m / a**3 + Omega_r / a**4 + Omega_Lambda)

# Waktu dalam milyar tahun (Gyr)
t_min = 0  # awal (big bang)
t_max = 50  # batas waktu
time_eval = np.linspace(t_min, t_max, 1000)  # waktu evaluasi

# Integrasi numerik menggunakan Runge-Kutta
sol = solve_ivp(friedmann, [t_min, t_max], [1e-5], t_eval=time_eval)

# Plot hasil
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label='Scale Factor a(t)')
plt.title('Evolution of the Universe')
plt.xlabel('Time (Gyr)')
plt.ylabel('Scale Factor a(t)')
plt.grid(True)
plt.legend()
plt.show()