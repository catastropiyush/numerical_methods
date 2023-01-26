import matplotlib.pyplot as plt 
import numpy as np
import numpy.polynomial.hermite as Herm
import math
m=1.0
w=1.0
hbar=1.0
dx = 0.05
x_lim =12
x = np.arange(-x_lim,x_lim,dx)

def hermite(x, n):
    xi = np.sqrt(m*w/hbar)*x
    herm_coeffs = np.zeros(n+1)
    herm_coeffs[n] = 1
    return Herm.hermval(xi, herm_coeffs)
  
def wavefunction(x,n):
    xi = np.sqrt(m*w/hbar)*x
    psi = 1./math.sqrt(2.**n * math.factorial(n))*(m*w/(np.pi*hbar))**(0.25)*np.exp(- xi**2 / 2) * hermite(x,n)
    return psi

plt.plot(x, stationary_state(x,3)**2,linewidth=2.0,color='#0ABAB5')
plt.plot(x, stationary_state(x,1)**2,linewidth=2.0,color='#A020F0')
plt.xlabel(r"x")
plt.ylabel(r"$\psi(x)$")
plt.show()
