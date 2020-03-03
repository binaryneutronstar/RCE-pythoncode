import math
import numpy as np
pi=math.pi

def rep_lat_vec( k, l, m ):
    gvec=np.array([ -k+m, k+m, l ])
    return gvec

def rep_lat_norm( k, l, m):
    gvec=np.array([ -k+m, k+m, l ])
    g=math.sqrt(float(gvec[0]**2+gvec[1]**2+gvec[2]**2))
    return g



def Sklm( k, l, m ):
    return 2*math.cos(pi*(2*m+l)/4.)*(1+math.cos(pi*(k+l+m)))

def DebyeWaller( k, l, m ):
    g=rep_lat_norm( k, l, m)
    u=0.075e-10 #thermal vibration amplitude
    W=2*pi*pi*u*u*g*g
    return W

alpha=np.array([ 0.1, 0.55, 0.35 ])
beta =np.array([ 6.0, 1.2,  0.3  ])

twopiaTF=0.20681

def Sum( k, l, m ):
    sum=0
    g=rep_lat_norm( k, l, m )
    for i in range(3):
        sum=alpha[i]/(beta[i]/twopiaTF**2+g**2)
    return sum


import matplotlib.pyplot as plt
x=[]
y=[]

for num in range(10):
#for num in range(100):
    k=num+1
    l=-8*num+7
    m=num
    print(np.array([k,l,m]))
    gvec=rep_lat_vec( k, l, m )
    g=rep_lat_norm( k, l, m )
    print("gvec",end=" = ")
    print(gvec)
    print("g norm",end=" = ")
    print(g)

    Vg=math.exp(-DebyeWaller( k, l, m ))*Sklm( k, l, m )*Sum( k, l, m )
    print("Vg",end=" = ")
    print(Vg)
    x.append(num)
    y.append(Vg)

plt.plot(x, y, marker="o", color = "red", linestyle = "--")
plt.show()
