import matplotlib.pyplot as plt
import numpy as np

# n qiymatlari
n = np.arange(1, 21)

# Funksiyalar
exp = 2 ** n           # 2^n
poly = n ** 2          # n^2
log_exp = np.log2(exp)     # log₂(2^n)
log_poly = np.log2(poly)   # log₂(n^2)

# Grafik chizish
plt.figure(figsize=(14, 6))

# 1-grafik: 2^n vs n^2
plt.subplot(1, 2, 1)
plt.plot(n, exp, label="2^n (Exponential)", color="red", linewidth=2)
plt.plot(n, poly, label="n^2 (Polynomial)", color="blue", linewidth=2)
plt.title("Growth of 2^n vs n^2 (Big O)")
plt.xlabel("n")
plt.ylabel("f(n)")
plt.grid(True)
plt.legend()
plt.yscale("log")  # Logarifmik o‘lchov — farqni yaxshi ko‘rsatadi

# 2-grafik: log(2^n) vs log(n^2)
plt.subplot(1, 2, 2)
plt.plot(n, log_exp, label="log₂(2^n) = n", color="green", linestyle="--")
plt.plot(n, log_poly, label="log₂(n^2) = 2·log₂(n)", color="orange", linestyle="--")
plt.title("Log View: log₂(2^n) vs log₂(n^2)")
plt.xlabel("n")
plt.ylabel("log₂(f(n))")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
