import numpy as np
import matplotlib.pyplot as plt

#-------------- Ejercicio b -------------------------#
def Lotka_Volterra(P0,D0,mu,tmax,h):
    t= np.arange(0,tmax,h)
    P= np.zeros(len(t))
    D= np.zeros(len(t))
    P[0]=P0
    D[0]=D0
    for n in range(len(t) - 1):
        P[n+1]= P[n] + h * P[n] * (1- D[n])
        D[n+1]= D[n] + h * mu * D[n] * (P[n+1] - 1)
    return t, P, D



#---------------- Ejercicio c ----------------------#

a=Lotka_Volterra(1,5,1,40,0.001)
plt.style.use("bmh")
plt.plot(a[0],a[1],label="Presas")
plt.plot(a[0],a[2], label= "Depredadores")
plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.legend()
def C(P,D,mu):
    return np.log(D) - D + mu * (np.log(P) - P)




#plt.savefig("edo-ej-c.pdf")
plt.figure()



#---------------- Ejercicio d ----------------------#


for D0 in np.linspace(1.1,10,20):
    b=Lotka_Volterra(1, D0, 1, 100, 0.001)
    plt.plot(b[1],b[2])


plt.ylabel("Depredadores")
plt.xlabel("Presas")

#plt.savefig("edo-ej-d.pdf")
plt.figure()


#--------------- Ejercicio e------------------------#


for D0 in np.linspace(1.1,10,20):
    b=Lotka_Volterra(1, D0, 1, 100, 0.001)
    plt.plot(b[0],C(b[1],b[2],1),label="$\\Delta(0)=$"+str(round(D0,2)))
plt.xlabel("Tiempo")
plt.ylabel("C")

plt.tight_layout()

plt.legend(ncol=2,bbox_to_anchor = (1, 1))
#plt.savefig("edo-ej-e.png")









