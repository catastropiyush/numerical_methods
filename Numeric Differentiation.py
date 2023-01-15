import numpy as np
import matplotlib.pyplot as plt

x=[] ; y=[]

lower=0 ; upper=10; step=0.2
N=int(((upper-lower)/step))
dy = [0]*N ; back=[0]*N ; forw=[0]*N


def f(x):
  return np.sin(4*x)*np.exp(-x)
for i in range(0,N+1):   
  x_step = lower+i*step
  x.append(x_step)
  y.append(f(x[i]))

for i in range(1,N-1):    
  dy[i]=(y[i+1] - y[i-1]) / (x[i+1] - x[i-1])  #central difference formula
for i in range(1,N):
  back[i]=(y[i] - y[i-1]) / (x[i] - x[i-1])    #backward difference
for i in range(0,N):
  forw[i]=(y[i+1] - y[i]) / (x[i+1] - x[i])    #forward difference


dy[0] = dy[1] + (dy[2]-dy[1])/(x[2]-x[1])*(x[0]-x[1])      
dy[N-1] = dy[N-2] + (dy[N-2]-dy[N-3])/(x[N-2]-x[N-3])*(x[N-1]-x[N-2])

plt.figure(figsize=(5,4))
print('h=',step)
plt.plot(x,y,color='grey',linewidth=2.0,label=r'$f(x)$')
plt.plot(x[:-1],forw,color='orange',linewidth=2.0,label='Forward')
plt.plot(x[1:-1],back[1:],color='blue',linewidth=2.0,label='Backward')
plt.plot(x[:-1],dy,color='deeppink',linewidth=2.0,label='Central')
plt.xlabel('$x$',fontsize=20)
plt.ylabel('$y$')
plt.legend(loc='upper right')
