#Diagonal Dominance checker
#make a code for determining the spectral radius of a matrix
import numpy as np 
import matplotlib.pyplot as plt
A = np.array([[6,-2,10],[1,-5,2],[-1,2,8]])
tick = [0]*len(A)
N=len(np.sum(np.abs(A), axis=1))
sum_row=np.sum(np.abs(A), axis=1)
for i in range(0,N):
  if(np.abs(A[i][i])>(sum_row[i]-np.abs(A[i][i]))):
    tick[i]='Yes'
  else:
    tick[i]='No'
print(tick) 
