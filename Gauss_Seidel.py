#Gauss Seidel Iteration 
#Last update:Piyush
import numpy as np
import matplotlib.pyplot as plt
N=10 #number of iterations
# 27x+6y-z=54
# 6x+15y+2z=72
# x+y+54z=110
a=[0]*N
b=[0]*N
c=[0]*N

a[0] = 10.0  
b[0] = -2.0  
c[0] = 3.0
print("Iteration",0,":",a[0],b[0],c[0])
for i in range(1,N):
  a[i] = (1/27)*(54-6*b[i-1]+c[i-1])
  b[i] = (1/15)*(72-6*a[i]-2*c[i-1])
  c[i] = (1/54)*(110-a[i]-b[i])
  print("Iteration",i,":",a[i],b[i],c[i])

plt.plot(a, label=r'$x_{1}$',linewidth=2.0,color='deeppink')
plt.plot(b, label=r'$x_{2}$',linewidth=2.0,color='orchid')
plt.plot(c, label=r'$x_{3}$',linewidth=2.0,color='cornflowerblue')
plt.xlabel(r'$n$')
plt.legend()
plt.grid(color='lightgrey', linestyle='-', linewidth=0.5)

a1 = np.array([[27, 6, -1], [6, 15, 2], [1, 1, 54]])
b1 = np.array([54,72,110])
from scipy import linalg
x = linalg.solve(a1, b1)
# values compared with scipy linalg calc
print('x',a[-1],np.abs(a[-1]-x[0]))
print('y',b[-1],np.abs(b[-1]-x[1]))
print('z',c[-1],np.abs(c[-1]-x[2]))
