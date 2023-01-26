#Last update:Piyush
import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(-5,10,200)

def f(x):     #function
  return x**3-3*x+1
def f_prime(x):   #first derivative
  return 3*x**2-3
def newtoroot(f, df, x0, tol):  #newton raphson method
    if abs(f(x0)) < tol:
        return x0
    else:
        print(x0)
        return newtoroot(f, df, x0 - f(x0)/df(x0), tol)

result = newtoroot(f,f_prime, -1.3, 1e-5) 
print("root =", result)
plt.figure(figsize=(6,4));plt.xlim([-5,5]);plt.ylim([-5,10])
plt.plot(x,f(x),label=r'$f(x)$',linewidth=2.0,color='deeppink')
plt.axvline(x=result,color='black',linewidth=1.3);plt.axhline(y=0,color='grey')
plt.legend(fontsize='12')
