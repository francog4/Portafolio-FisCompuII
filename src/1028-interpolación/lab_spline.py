import numpy as np
import matplotlib.pyplot as plt
from GaussianElimination import Resolver
import spline as sp


datos= np.genfromtxt("data-manchas.txt")
año= datos[118:,0]
manchas= datos[118:,1]


csp = sp.cspline(año, manchas)
x = np.linspace( np.min(año), np.max(año), 10000, endpoint=False)
plt.plot(x, csp(x),color="darkorange")
plt.plot(año,manchas, ".", color="navy")

plt.title("Método de spline cúbica")
plt.xlabel("Año")
plt.ylabel("Número de manchas")


#plt.savefig("sp.pdf")
plt.show()




