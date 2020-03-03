import math as m
x=float(input("input x:"))
y=float(input("input y:"))
z=float(input("input z:"))
#convert miller indices to indices in new corrdinate
omega=3./4*m.pi
#phi=3.35
phi=1.3958272811292078+m.pi
#print(m.cos(omega))
#print(m.sin(omega))
#print(m.cos(phi))
#print(m.sin(phi))
X=m.cos(phi)*(x*m.cos(omega)-y*m.sin(omega))+z*m.sin(phi)
Y=x*m.sin(omega)+y*m.cos(omega)
Z=-m.sin(phi)*(x*m.cos(omega)-y*m.sin(omega))+z*m.cos(phi)
print("X",end=" = ")
print(X)
print("Y",end=" = ")
print(Y)
print("Z",end=" = ")
print(Z)
print("")
hX=m.cos(phi)*(1*m.cos(omega)-m.sin(omega))-8*m.sin(phi)
hY=m.sin(omega)+m.cos(omega)
hZ=-m.sin(phi)*(m.cos(omega)-m.sin(omega))-8*m.cos(phi)
print("for h")
print(hX)
print(hY)
print(hZ)
alpha=(X*hX+Y*hY+Z*hZ)/(hX**2+hY**2+hZ**2)
print("alpha",end=" = ")
print(alpha)
gperpX=X-alpha*hX
gperpY=Y-alpha*hY
gperpZ=Z-alpha*hZ
print("gperp",end=" =  ( ")
print(gperpX,end=", ")
print(gperpY,end=", ")
print(gperpZ,end=" )")
print("")
