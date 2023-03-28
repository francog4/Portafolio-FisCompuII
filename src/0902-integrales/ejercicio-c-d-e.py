import numpy as np

def f(x):
    return (x-1)*np.exp(x)

def midpoint_simple(f,a,b):
    return (b-a) * f((a+b)*0.5)

limites = np.linspace(0,3,100)

integ = 0

for i in range( len(limites)-1) :
    integ = integ + midpoint_simple(f, limites[i], limites[i+1])


print("Ejercicio 1d: ",midpoint_simple(f, 0, 3))
print("Ejercicio 1e: ",integ)