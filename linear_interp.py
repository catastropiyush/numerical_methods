import numpy as np
import matplotlib.pyplot as plt
#x = [1,2,3]
#y = [3,2,9]
sumX,sumX2,sumY,sumXY = 0,0,0,0
data=np.loadtxt('poing.txt')
x  = data[:,0]
y  = data[:,1]
n  = len(x)
for i in range(n):
    sumX =  sumX  + x[i]
    sumX2 = sumX2 + x[i]*x[i]
    sumY =  sumY  + y[i]
    sumXY = sumXY + x[i]*y[i]
b = (n*sumXY-sumX*sumY)/(n*sumX2-sumX*sumX)
a = (sumY - b*sumX)/n

print('y', '=', a, '+', b,'x')
xco=np.linspace(x[0],x[-1],100)
plt.xlim([0,100])
plt.ylim([280,320])
plt.xlabel('$Time [ps]$',fontsize=12)
plt.ylabel('$T [K]$',fontsize=12)
plt.plot(x,y,linewidth=2.0,color='#DA3287')
plt.plot(xco,a+b*xco,linewidth=1.3,color='#9932CC')
