#Spline Interpolation Piyush Oct 12,2022
#3:33 spline ho gaya
import numpy as np
import matplotlib.pyplot as plt

#input data
x=[1,3,4,5,9] ; y=[2,5,8,7,15]
N=len(x)-1

h =[0]*N   ; H =[0]*N   #x diff and y diff
b =[0]*N   ; d =[0]*N

for i in range(0,N):
  h[i]=x[i+1]-x[i]
  H[i]=y[i+1]-y[i]
A = np.zeros((5,5))
print("h");print(h)
print("H");print(H)

A[0][0]=1; A[N,N]=1 #Boundary conditions

#Constructing A
for w in range(1,N):
  A[w][w+1]   = h[w]
for k in range(0,N-1):
  A[k+1][k]   = h[k]
for l in range(1,N):
  A[l][l] = 2*(A[l][l-1]+A[l][l+1])
print("Matrix A");print(A)

B=np.zeros((5,1))
for s in range(1,len(B)-1):
  B[s][0]=3*((H[s]/h[s])-(H[s-1]/h[s-1]))
print("Matrix B");print(B)

#Thomas Algorithm to solve tridiagonal matrix
gamma  = [0]*N
rho    = [0]*(N+1)
gamma[0] = A[0][1]/A[0][0]
rho[0]   = B[0][0]/A[0][0]

for o in range(1,N):
  gamma[o]=A[o][o+1]/(A[o][o]-gamma[o-1]*A[o][o-1])
for z in range(1,N+1):
   rho[z]=(B[z][0]-rho[z-1]*A[z][z-1])/(A[z][z]-gamma[z-1]*A[z][z-1])
print("rho");print(rho)
print("gamma"); print(gamma)

c=[0]*(N+1)
c[-1]=rho[-1]
for t in reversed(range(0,N)):
  c[t]=rho[t]-gamma[t]*c[t+1]
print("c");print(c)

#calculate coefficients
b = [(H[g]/h[g])-(h[g]/3)*(2*c[g]+c[g+1]) for g in range(0,N)]
print("b");print(b)
d = [(c[e+1]-c[e])/(3*h[e]) for e in range(0,N)]
print("d");print(d)
