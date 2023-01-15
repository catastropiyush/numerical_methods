#gauss quadrature #general mode
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(2+x**2)
a = 0
b = 3
x_1 = [0]                                       ; w_1 = [2]
x_2 = [-0.577,0.577]                            ; w_2 = [1.000,1.000]
x_3 = [0.000,-0.744,0.744]                      ; w_3 = [0.888,0.555,0.555]  
x_4 = [-0.339,0.339,-0.861,0.861]               ; w_4 = [0.652,0.652,0.347,0.347]
x_5=  [-0.90618,-0.538469,0,0.538469,0.909618]  ; w_5 = [0.236927,0.478629,0.56889,0.478629,0.236927]
integral=0
N=4
if N == 1:
    integral += w_1[0]*(b-a)*0.5*(f((0.5*((b-a)*x_1[0]+(b+a)))))
elif N == 2:
  for i in range(len(x_2)):
      integral += +w_2[i]*(b-a)*0.5*(f((0.5*((b-a)*x_2[i]+(b+a)))))
elif N == 3:
  for i in range(len(x_3)):
      integral += w_3[i]*(b-a)*0.5*(f((0.5*((b-a)*x_3[i]+(b+a)))))
elif N == 4:
    for i in range(len(x_4)):
      integral += w_4[i]*(b-a)*0.5*(f((0.5*((b-a)*x_4[i]+(b+a)))))
else :
    for i in range(len(x_5)):
      integral += w_5[i]*(b-a)*0.5*(f((0.5*((b-a)*x_5[i]+(b+a)))))
print(integral)
