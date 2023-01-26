#Last Update:Piyush 
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 100)
def RK4(f_prime, y_0, a, b, h):
    N=int((b-a)/h)  #Number of steps
    x = a ; y = y_0
    x_out,y_out =[],[]
    for i in range(N):
        k1 = h*f_prime(x,y)
        k2 = h*f_prime(x+0.5*h,y+0.5*k1)
        k3 = h*f_prime(x+0.5*h,y+0.5*k2)
        k4 = h*f_prime(x+h,y+k3)

        y = y+ (1/6)*(k1+2*k2+2*k3+k4)   #RK-4 
        x = x + h
        #print(x,y)
        x_out.append(x)
        y_out.append(y)
    return x_out, y_out
def f_prime(x, y):  #Differential equation
  return 50*(np.cos(x)-y)
def solution(x):    #Analytical solution
  return (50/2501)*(np.sin(x)+50*np.cos(x)-50*np.exp(-50*x))  #y(0)=0
x_RK, y_RK = RK4(f_prime, 0, 0, 4, 0.05)
x_RK1, y_RK1 = RK4(f_prime, 0, 0, 4, 0.01)

plt.xlabel(r'$x$');plt.ylabel(r'$y$')
plt.ylim([-1.5,1.5])
plt.plot(x,solution(x),color='black',linewidth=2.0,label='Exact')
plt.plot(x_RK,y_RK,color='deeppink',linewidth=2.0,label='h=0.05')
plt.plot(x_RK1,y_RK1,color='orange',linewidth=2.0,label='h=0.01')
plt.legend(loc='upper right')
