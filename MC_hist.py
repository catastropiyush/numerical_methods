monty=[] 
N=500   #number of times
N1 =500 #number of points
def funci(x):
  return 1/(2+x**2)
for k in range(0,N):    
  monty.append(monte_carlo_integrate(funci,0,2,0,1,N1))
sum=0
for i in range(0, len(monty)):    
   sum = sum + monty[i];     
average=sum/len(monty)
print(average)
plt.hist(monty,histtype='stepfilled',color='darkorange',alpha=0.8,edgecolor='black', bins=20)
plt.title(N1)
plt.axvline(average,color='red')
