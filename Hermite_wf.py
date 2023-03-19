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

def hermite(x, n):         #Hermite function
    if (n==1):
      return 2*x
    elif n==2:
      return 4*x**2-2
    elif n==3 :
      return 8*x**3-12*x
    elif n==4:
      return 16*x**4-48*x**2+12
    elif n==5:
      return 32*x**5-160*x**3+120*x
  
def wavefunction(x,n):
    xi = np.sqrt(m*w/hbar)*x
    wavi = 1./math.sqrt(2.**n*math.factorial(n))*(m*w/(np.pi*hbar))**(0.25)*np.exp(-xi**2/2)*hermite(x,n)
    return wavi

plt.plot(x, stationary_state(x,2)**2,linewidth=2.0,color='#0ABAB5')
plt.plot(x, stationary_state(x,1)**2,linewidth=2.0,color='#A020F0')
plt.xlabel(r"x")
plt.ylabel(r"$\psi^{2}(x)$")
