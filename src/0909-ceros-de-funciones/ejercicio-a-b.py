import numpy as np
import matplotlib.pyplot as plt

#be = np.linsoace(0.1,1,10)

def u(t):
    return np.cos(t) + beta* (np.sin(t))**2

h=0.0001
t=np.linspace(0, np.pi/2, 100)

def du(u,t,h):
    return (u(t+h) - u(t)) / h

plt.style.use("bmh")

plt.hlines(0.0,0,1.5,color="red")

for beta in  np.linspace(0.1,1,10):
    plt.plot(t,du(u,t,h),label="$\\beta=$"+str(round(beta,2)))


for beta in np.linspace(0.6,1,5):
    a=0.5
    b=1.2
    for i in range(20):
        c= 0.5*(a+b)
        condicion = du(u,a,h)*du(u,c,h)

        if condicion<0:
            b=c
        else:
            a=c
    plt.plot(c,du(u,c,h),"o",color="black")
    print("para beta="+str(beta)+" el cero no trivial es: "+str(c))

plt.xlabel("$\\theta$")
plt.ylabel("$u'(\\theta)$")

plt.legend()

#plt.savefig("graficoo.pdf")
