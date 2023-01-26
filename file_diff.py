import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt('water_md.txt')
x  = data[:,1]  ;  y  = data[:,5]
N=len(x)
dy = [0]*N;
for i in range(1,N-1):    
  dy[i]=(y[i+1] - y[i-1]) / (x[i+1] - x[i-1])  #central difference formula

dy[0] = dy[1] + (dy[2]-dy[1])/(x[2]-x[1])*(x[0]-x[1])                 
dy[N-1] = dy[N-2] + (dy[N-2]-dy[N-3])/(x[N-2]-x[N-3])*(x[N-1]-x[N-2]) 
plt.figure(figsize=(8,6))
plt.plot(x,y,color='grey',linewidth=1.5,label=r'$E_{kin}$')
plt.plot(x[:],dy,color='deeppink',linewidth=1.5,label='Central')
plt.xlabel('$Time [fs]$',fontsize=15)
plt.ylabel('$y$',fontsize=15)
plt.legend(loc='upper right')
