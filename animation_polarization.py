import math
import numpy as np
pi=math.pi

def rep_lat_vec( k, l, m ):
    gvec=np.array([ -k+m, k+m, l ])
    return gvec

def rep_lat_norm( k, l, m):
    gvec=np.array([ -k+m, k+m, l ])
    g=math.sqrt(gvec[0]**2+gvec[1]**2+gvec[2]**2)
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
import matplotlib.animation as animation
import seaborn as sns
sns.set_style("darkgrid")
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
axon=1
if(axon):
    ax = Axes3D(fig) #make it 3D plot
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-0.3,0.0)
    ax.set_ylim(-0.0,0.2)
    ax.set_zlim(-0.5,0.0)
ims =[]#array for animation

x=[]
y=[]
X=[]
Y=[]
Z=[]
sumX=[]
sumY=[]
sumZ=[]
sumnorm=[]
tempsumX=0
tempsumY=0
tempsumZ=0
gamma=1.53785
alpha2=-7./9
gy=math.sqrt(2)
gz=-7.3
hnorm=6*math.sqrt(2)

#for num in range(10):
#for num in range(100):
for num in range(50):
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

    X.append(Vg*gamma*(num+alpha2)*hnorm)
    Y.append(Vg*gamma*gy)
    Z.append(Vg*gz)

    tempsumX+=Vg*gamma*(num+alpha2)*hnorm
    tempsumY+=Vg*gamma*gy
    tempsumZ+=Vg*gz
    
    sumX.append(tempsumX)
    sumY.append(tempsumY)
    sumZ.append(tempsumZ)
    sumnorm.append(math.sqrt(tempsumX**2+tempsumY**2+tempsumZ**2))
    
    #im = plt.plot(x, y, marker="o", color = "red", linestyle = "--")
    #im =ax.plot(X, Y, Z, marker="o", color = "red", linestyle = "--")
    im =ax.plot(sumX, sumY, sumZ, marker="o", color = "red", linestyle = "--")
    #im =ax.quiver(0,0,0,sumX, sumY, sumZ, color = "red", length = 1, arrow_length_ratio = 0.1)
    ims.append(im)
    
ani =animation.ArtistAnimation(fig, ims, interval=100)
#plt.plot(x,sumnorm, marker="o", color = "red")
#plt.plot(x, y, marker="o", color = "red", linestyle = "--")
plt.show()
#ani.save('animate.gif', writer='imagemagick', dpi = 300)
#ani.save('animate.gif')
#ani.save('animation.gif', writer='pillow')
