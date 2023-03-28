import numpy as np
import matplotlib.pyplot as plt
from GaussianElimination import Resolver

datos= np.genfromtxt("data-manchas.txt")
año= datos[118:,0]
manchas= datos[118:,1]


plt.style.use("bmh")


#------------------ Vandermonde ----------------#

for m in range(51):
    año2 = año[m*4:5+m*4]
    manchas2 = manchas[m*4:5+m*4]

    dim = año2.size

    vandermonde = np.ones( [dim,dim] )

    for i in range(1,dim):
        vandermonde[:,i]= año2**i

    #print(vandermonde)

    a = Resolver(vandermonde, manchas2)


    def p(x,a):

        pol=0.0
        for n in range(len(a)):
            pol= pol + a[n] * x**n

        return pol


    X = np.linspace(np.min(año2), np.max(año2), 100)


    y=p(X,a)

    plt.plot(X,y,linewidth=1.5, color="darkorange")
    plt.plot(año2,manchas2,".", color="navy")


plt.title("Método de la inversión de la matriz de Vandermonde")
plt.xlabel("Año")
plt.ylabel("Número de manchas")


#   plt.savefig("vandermonde.pdf")
plt.show()