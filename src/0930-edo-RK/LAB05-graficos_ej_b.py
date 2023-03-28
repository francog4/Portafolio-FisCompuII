import numpy as np
import matplotlib.pyplot as plt


#------------------------- Ejercicio a -----------------------------#

def f(u,t, rho=28, beta= 8/3 , sig=10):
    x,y,z = u
    return np.array([sig*(y-x), rho*x-y-x*z, x*y - beta*z ])

tmax=80
h=0.01
t= np.arange(0,tmax,h)

u=np.empty([t.size,3])
u[0]=[0.4,1.2,1]

for n in range(t.size-1):
    K1= f(u[n], t[n])
    K2= f(u[n] + h*0.5*K1, t[n]+0.5*h )
    K3= f(u[n] + h*0.5*K2, t[n]+0.5*h )
    K4= f(u[n] + h*K3, t[n]+h )
    u[n+1]= u[n] + (h/6)*(K1 + 2*K2 + 2*K3 + K4)


#-------------------- Gráficos ejercicio b ---------------------------#

ylabel= ["Razón de convección", "Variación de Temperatura horizontal", "Variación de temperatura vertical"]
colores= ["red","purple","orange"]
for i in range(3):
    plt.figure()
    plt.style.use("bmh")
    plt.xlabel("Tiempo")
    plt.ylabel(str(ylabel[i]))
    plt.plot(t,u[:,i], color=str(colores[i]),linewidth=0.8)
    plt.savefig("ej2_RK_graf0"+str(i)+".pdf")
