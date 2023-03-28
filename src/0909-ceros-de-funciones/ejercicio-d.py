import numpy as np
import matplotlib.pyplot as plt


def u(t):
    return np.cos(t) + beta* (np.sin(t))**2

h=0.0001


def ddu(u,t,h):
    return ( u(t+h) - 2*u(t) + u(t-h)) / (h**2)

plt.style.use("bmh")



#plt.subplot(1,2,1)
for beta in np.linspace(0.1,1,10): #con theta igual a 0
    plt.plot(beta,ddu(u,0,h),"o", color="purple")
    plt.ylabel("$u''(\\theta)$")
    plt.xlabel("$\\beta$")



plt.hlines(0.0,0,1.1,color="red")


#--------------------------------------------------------------

c_nt=[0.585, 0.682, 0.758, 0.820, 0.872, 0.917, 0.955, 0.989, 1.020, 1.047]
#plt.subplot(1,2,2)

for i in range(0,10):        #con los ceros no triviales
    a= np.linspace(0.6,1,10)
    beta= a[i]
    plt.plot(beta,ddu(u, c_nt[i], h), "o", color= "brown")






plt.tight_layout()






plt.savefig("ej_d.pdf")








