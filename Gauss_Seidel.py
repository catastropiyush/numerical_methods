#Gauss Seidel Iteration 
#Last update:Piyush
N=5 #number of iterations
# 27x+6y-z=54
# 6x+15y+2z=72
# x+y+54z=110
x=0;y=0;z=0
for i in range(N):
  x = (1/27)*(54-6*y+z)
  y = (1/15)*(72-6*x-2*z)
  z = (1/54)*(110-x-y)
print('x',x)
print('y',y)
print('z',z)
