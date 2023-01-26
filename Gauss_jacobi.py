#Jacobi's Method 
import matplotlib.pyplot as plt
x1=0;x2=0;x3=0;x4=0
data_x1=[];data_x2=[];data_x3=[];data_x4=[]
for i in range (10):
    a=(6+x2-2*x3)/10
    b=(25+x1+x3-3*x4)/11
    c=(-11-2*x1+x2+x4)/10
    d=(15-3*x2+x3)/8
    x1=a;x2=b;x3=c;x4=d
    data_x1.append(x1);data_x2.append(x2);data_x3.append(x3);data_x4.append(x4)
print(x1,x2,x3,x4)
plt.plot (data_x1, label=r'$x_{1}$')
plt.plot (data_x2, label=r'$x_{2}$')
plt.plot (data_x3, label=r'$x_{3}$')
plt.plot (data_x4, label=r'$x_{4}$')
plt.xlabel('Iterations');plt.legend();plt.grid();plt.show()
