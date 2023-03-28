import numpy as np
import matplotlib.pyplot as plt

for i in range(20):
    for N in np.linspace(50,20000,20, int):

        x=np.random.rand(int(N))
        y=np.random.rand(int(N))

        mx=-np.random.rand(int(N))
        my=-np.random.rand(int(N))

        xx=np.concatenate( [ mx,x,mx,x] ) /2
        yy=np.concatenate( [ my,y,y,my] ) /2


        xa= []
        ya= []


        for n in range(len(xx)):

            r = np.sqrt(xx[n]**2 + yy[n]**2)

            if r<0.5:

                xa.append(xx[n])
                ya.append(yy[n])

        A_cuadrado = len(xx)
        A_circ = len(xa)

        pi = 4 * A_circ / A_cuadrado


        plt.plot(N*4,pi,".")



plt.style.use("bmh")
plt.plot([0,80000],[np.pi,np.pi], color="black", label="$\pi$")

plt.xlabel("Cantidad de números generados aleatoriamente")
plt.ylabel("Valor obtenido para $\pi$")

plt.legend()

plt.savefig("puntos_pi.pdf")

plt.show()





print(pi)
plt.figure(figsize=(5,5))
plt.plot(xa,ya,".")


pi = 4 * A_circ / A_cuadrado

print(pi)

plt.xlabel("$xa$", fontsize=20)
plt.ylabel("$ya$", fontsize=20)

#plt.savefig("circunf_pi.pdf")
plt.show()