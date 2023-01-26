#19 Nov 2022
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
x_ran,y_ran=[],[]
def funci(x):
  return 1/(2+x**2)  
def monte_carlo_integrate(f, a, b, c, d, num_points):
    inside_count = 0
    for i in range(num_points):
        x = uniform(a,b)
        y = uniform(c,d)
        x_ran.append(x);y_ran.append(y)
        if  0 <= y <= f(x):
          inside_count += 1
        elif f(x) <= y <= 0:
          inside_count -= 1
    return inside_count/num_points*(b-a)*(d-c)

print(monte_carlo_integrate(funci,0,3,0,1,1000))
x1=np.linspace(0,10)
plt.figure(figsize=(4,5));
plt.xlim([0,3]); plt.ylim([-1,3])
plt.plot(x1,funci(x1),color='mediumslateblue',Linewidth=3.0)
plt.scatter(x_ran,y_ran,linewidth=0.007,c ="deeppink",alpha=0.3)
