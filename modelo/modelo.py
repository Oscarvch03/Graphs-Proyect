import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def df_dt(x, t, a, b, c, d):
    """Función del sistema en forma canónica"""
    dx = a * x[0] - b * x[0] * x[1]
    dy = - c * x[1] + d * x[0] * x[1]
    return np.array([dx, dy])

# Parámetros
a = 10
b = 1
c = 8
d = 1

# Condiciones iniciales
x0 = 10  # Presas # 10
y0 = 2  # Depredadores # 2
conds_iniciales = np.array([x0, y0])

# Condiciones para integración
tf = 20
N = 1000
t = np.linspace(0, tf, N) # Intervalo de tiempo

solucion = odeint(df_dt, conds_iniciales, t, args=(a, b, c, d))
xf = solucion[:, 0]
xfr = [round(i) for i in xf] # Cantidad de presas

yf = solucion[:, 1]
yfr = [round(i) for i in yf] # Cantidad de depredadores

print('xf =', xfr)
print('yf =', yfr)

print('xf min:', min(xfr))
print('yf min:', min(yfr))
print('xf max:', max(xfr))
print('yf max:', max(yfr))

# plt.plot(xf, yf, 'green')
# plt.xlabel('Presa')
# plt.ylabel('Depredador')
# plt.legend(['PresaVsDepredador'])
# plt.savefig("PresaVsDepredador.PNG")

plt.plot(t, xf)
plt.plot(t, yf)
plt.xlabel("Tiempo t")
plt.ylabel("Presa, Depredador")
plt.legend(["Presa", "Depredador"])
plt.savefig("PreYdepVsTiempo.PNG")

plt.show()
