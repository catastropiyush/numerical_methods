#Last update:Piyush   8 Aug 2022
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,4,100)             
def euler_explicit(f_prime, y_0, a, b, h):#defining the euler method 
    N=int((b-a)/h)        #Number of steps
    x = a ; y = y_0       #Initial Values to the equation y(0) and x(0)
    x_out,y_out =[],[]
    for i in range(N):
        y = y + h*f_prime(x, y)  #y_n+1 = y_n + h * f
        x = x + h
        x_out.append(x)   
        y_out.append(y)
    return x_out, y_out
def solution(x):
  return np.exp(x/2)*np.sin(5*x)
def f_prime(x, y):
  return -0.5*np.exp(x/2)*np.sin(5*x)+5*np.exp(x/2)*np.cos(5*x)+y
   #return y*np.exp(y)+np.exp(y)
x_euler, y_euler = euler_explicit(f_prime, 0, 0, 3, 0.1)  #call the function and store the values in x and y
#plt.xlim([0,2])#plt.ylim([0.7,1.1])
plt.figure(figsize=(7,6))
plt.plot(x,solution(x),linewidth=3.0,color='mediumslateblue',label='Exact')
plt.plot(x_euler,y_euler,linewidth=3.0,color='orchid',label='Euler-Explicit')
plt.xlabel(r'$x$',fontsize=15);plt.ylabel(r'$y$',fontsize=15)
plt.legend(loc='upper right')
