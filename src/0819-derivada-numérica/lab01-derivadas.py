
import numpy as np
import matplotlib.pyplot as plt

h = np.geomspace(0.1,1e-20,300)

e_t = 2**(-52)

def f(x):
    return np.sqrt(x)

def deriv2(f,x,h):
    return (f(x+h) - 2*f(x) + f(x-h))/(h**2)

def ddf(x):
    return -0.25*x**(-1.5)

y= [0.1,1,np.pi/3]


for i in np.array(y):
    err = np.abs( ddf(i) - deriv2(f,i,h) )
    plt.style.use("bmh")
    plt.figure()
    plt.loglog(h,err)
    plt.title("Para x="+str(i))
    plt.xlabel("$h$")
    plt.ylabel("Error relativo")
    #plt.savefig("graf"+str(i)+"_deriv.pdf")
    print("cuando x="+str(i)+"el valor de h para que el error sea minimo es h="+str(h[np.argmin(err)]))


def d4f(x):
    return -( 15/ ( 16 * x**(7/2) ) )

for i in np.array(y):

    err_a = (h**2 / 12) * np.abs( d4f(i) ) + (4*e_t / h**2) * np.abs( f(i) )
    plt.show()
    plt.loglog(h,err_a,color="brown")
    plt.title("Para x="+str(i))
    plt.xlabel("$h$")
    plt.ylabel("Error relativo analítico")
    #plt.savefig("graf"+str(i)+"_deriv.pdf")
    print("cuando x="+str(i)+"el mínimo h="+str(h[np.argmin(err_a)]))


