# The Heat capacities but after they went to art class
from scipy.integrate import quad   # For quad integration
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors

#Temperatures
T=np.linspace(1,100, 100)
T_e=np.float_(40.10)      #Einstein Temperature
T_d=np.float_(40.00)       #Debye Temperature

def Dulong(T):
    return [1]*len(T)    #Dulong Petit Law C_v=3NK_B;
                         #Normalised it so this is 1.
        
def Einstein(T,T_e):     #Einstein Function
    return ((T_e/T)**2)*(np.exp(T_e/T)/(np.exp(T_e/T)-1)**2)

#Defining the function for the integral in Debye function
def thatintegralindebye(x):
    return ((x**4)*np.exp(x))/((np.exp(x)-1)**2)    
    #Defining the function for the integral part in Debye Function

#Using scipy to integrate the integral and evaluating Debye
def Debye(T,T_d):  
    deby=list()
    for t in T:
        deby.append(3*((t/T_d)**3) *np.float_(quad(thatintegralindebye,0,T_d/t)[0]))
    return (np.array(deby))

plt.figure(figsize=(9, 6))
plt.plot( T, Einstein(T,T_e), linewidth=3,label='$Einstein$',color='deeppink')
#plt.plot( T, Dulong(T), linewidth=3,label='$Dulong-Petit$',color='darkturquoise')
plt.plot( T, Debye(T,T_d),linewidth=3, label='$Debye$',color='mediumorchid')
plt.plot( T,(1e-3)*T**3,label='$T^{3} $',lw=2,color='orange')
#plt.plot( T,100*T**(-2)*np.exp(-(1/T)),label='$T^{2}e^{-1/T} $')
#plt.axvline(x=T_e,label='$T_e$',color='skyblue')
#plt.axvline(x=T_d,label='$T_d$',color='limegreen')
plt.xlim([0,50])
plt.ylim([0,1.1])
plt.xlabel("$T$",fontsize=15)
plt.ylabel("$C/3N k_B$",fontsize=15)
plt.legend(loc='lower right')
plt.show()
