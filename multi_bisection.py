import numpy as np
import matplotlib.pyplot as plt
import random
a = []
b = []
gap = 1
x=np.linspace(-5,10,200)
def f(x):     #function
  return x**3-3*x+1
for i in range(5):
  c=random.randrange(-5, 5)
  a.append(c)
  b.append(c+gap)
  #print(np.sign(f(a[i])))
print("a:",a)
print("b:",b)


corn=[]
for i in range(len(a)):
  if (np.sign(f(a[i])) * np.sign(f(b[i]))) > 0 :
     corn.append(i)   
for i in range(len(corn)):
  a.pop(corn[i])
  b.pop(corn[i])
print("a:",a)
print("b:",b)


#Last update:Piyush
import numpy as np
import matplotlib.pyplot as plt
def bisectionhaitaakat(f, a, b, sehlo): 
    if (np.sign(f(a)))*(np.sign(f(b))) > 0:
          print("can't do it") 
    mid = (a + b)/2 #midpoint #sehlo is tolerance  
    if np.abs(f(mid)) < sehlo:     #jab tak root mil jaye
        return mid   #root mil gaya that's it
    elif np.sign(f(a)) == np.sign(f(mid)):
        return bisectionhaitaakat(f, mid, b,sehlo)
    elif np.sign(f(b)) == np.sign(f(mid)):
        return bisectionhaitaakat(f, a, mid,sehlo)
        
x=np.linspace(-5,5,100)
def f(x):
   return x**3-3*x+1            #yeh raha function
plt.xlabel('x');plt.ylabel('y')
plt.xlim([-3,3.0]);plt.ylim([-5,5])
plt.axhline(0, color='grey',linestyle='--',linewidth=2)

for i in range(len(a)):
  root= bisectionhaitaakat(f,a[i],b[i], 1e-5)   #function call kiya
  print("root =", root)
  #print("f(root) =", f(root)) #ideally f(root) has to be zero
plt.plot(x,f(x),'-',linewidth=3.0)
plt.axvline(root,color='red',linewidth=1.5)
