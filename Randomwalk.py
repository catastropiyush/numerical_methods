import numpy as np
import matplotlib.pyplot as plt

I = 3
J = 4
N = 50
lattice_n = np.zeros((N, N))
lattice_n[I][J]=1 

for i in range(I,N-1):
  for j in range(J,N-1):
    numbo=np.random.random(1)
    #print(numbo)
    if((numbo >= 0.20)):
      lattice_n[i+1][j] = lattice_n[i][j]
    else:
      lattice_n[i][j+1] = lattice_n[i][j]
      #lattice_n[i][j]   = 0
plt.imshow(lattice_n,cmap='Spectral')
plt.colorbar()
