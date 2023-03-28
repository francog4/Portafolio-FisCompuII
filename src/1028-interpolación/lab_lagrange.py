import numpy as np
import matplotlib.pyplot as plt


datos= np.genfromtxt("data-manchas.txt")
año= datos[118:,0]
manchas= datos[118:,1]


plt.style.use("bmh")


#---------------- polinomio de lagrange --------#

for m in range(51):
    año2 = año[m*4:5+m*4]
    manchas2 = manchas[m*4:5+m*4]

    N= len(año2)

    def f(x):
        pol = 0.0
        for i in range(N):
            Li = manchas2[i]
            for j in range(N):
                if j != i:
                    Li = Li * (x-año2[j]) / (año2[i] - año2[j])
            pol= pol + Li
        return(pol)

    x= np.linspace(np.min(año2), np.max(año2), 300)
    y= f(x)

    plt.plot(x,y, linewidth=1.2,color="darkorange")

plt.title("Método de los polinomios de Lagrange")
plt.plot(año,manchas,".",color="navy")
plt.xlabel("Año")
plt.ylabel("Número de manchas")

#plt.xlim(1821,1825)
#plt.ylim(0,12)

#plt.savefig("acercamiento.pdf")


#plt.savefig("lagrange1.pdf")
plt.show()


#--------------------------------------------#
#--------------------------------------------#
#--------------------------------------------#







