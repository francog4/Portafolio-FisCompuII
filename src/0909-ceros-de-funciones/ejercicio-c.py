import numpy as np
import matplotlib.pyplot as plt

c_nt=[0.585, 0.682, 0.758, 0.820, 0.872, 0.917, 0.955, 0.989, 1.020, 1.047]
beta= np.linspace(0.6,1,10)

plt.style.use("bmh")
plt.plot(beta,c_nt,color="black",linewidth=0.4)
plt.plot(beta, c_nt, "o",color="purple")
plt.xlabel("$\\beta$")
plt.ylabel("$\\theta_{nt}$")

#plt.savefig("graf_ejc.pdf")