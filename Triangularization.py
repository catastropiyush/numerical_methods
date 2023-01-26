import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 3, 5], 
    [2, -1, -3],
    [4, 5, -1]])
B = np.array([[14],[3],[7]])
N=len(A)
k1 = [(A[i][0]/A[0][0]) for i in range(1,N)]
for i in range(0,N):
  A[1][i] = A[1][i] - k1[0]*A[0][i]
  A[2][i] = A[2][i] - k1[1]*A[0][i]
print("A")
print(A)

print("B");print(B)
#B[0][0]=(-1)*(B[1][0]-k1[0]*B[0][0])
B[1][0]=(-1)*(B[1][0]-k1[0]*B[0][0])
B[2][0]=(-1)*(B[2][0]-k1[1]*B[1][0])
B[2][0]=B[2][0]-k2[0]*B[1][0]

print("B");print(B)
#k2 = [(A[k][1]/A[1][1]) for k in range(2,N)]

for l in range(0,N):
  A[1][l]=-A[1][l]
  A[2][l]=-A[2][l] 
#print(A)
for j in range(1,N):
  A[2][j]=A[2][j]-k2[0]*A[1][j]
print("Triangularization")
print(A)

x      = [0]*(len(A))
x[-1]  = B[N-1][0]/A[N-1][N-1]
x
