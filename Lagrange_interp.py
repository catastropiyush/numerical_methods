#Lagrange Interpolation 
#Last update:Piyush
import numpy as np
import matplotlib.pyplot as plt
#x=[1,1.5,2,3.2,4.5]    #If you have a dataset
#y=[5,8.2,9.2,11,16]
N = 10
x = np.zeros((N))       #If you want a functional form
y = np.zeros((N))
for i in range(len(x)):
  a = i/2
  x[i]=a
  y[i]=np.sin(a)
#xp = float(input('Enter interpolation point: '))
xp = 2.75; yp = 0
for i in range(len(x)):
    prod = 1
    for j in range(len(x)):
      if i != j:
            prod = prod * (xp - x[j])/(x[i] - x[j])
    yp = yp + prod * y[i] 
print('Interpolated value at %.3f is %.3f.' % (xp, yp))
plt.scatter(x,y,label='Data')
plt.plot(x,y,linewidth=1.5,color='red')
plt.xlabel(r'$x$');plt.ylabel(r'$y$')
plt.scatter(xp,yp,label='Interpolated')
plt.legend(loc='lower right')
