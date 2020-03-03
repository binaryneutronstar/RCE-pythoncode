import math
e=27.2113834
theta=float(input("input theta:"))
phi=float(input("input phi:"))
energy=float(input("input transition energy:"))
k=float(input("input k:"))
l=float(input("input l:"))
m=float(input("input m:"))
alphainv=137.035999
lattconst=5.431021/0.52917721
pi=math.pi
A=math.sqrt(2)*(k*math.cos(phi/180*pi)+m*math.sin(phi/180*pi))
T=(A*math.cos(theta/180*pi)+l*math.sin(theta/180*pi))
S=energy*lattconst/(2*pi*alphainv*e*T)
gamma=math.sqrt(1+S*S)
print("gamma = %f" % gamma)
beta=math.sqrt(1-1./(gamma**2))
print("relativistic beta %f" % beta)
beamene=(gamma-1)*931.494013
print("Beam energy in MeV/u %f" % beamene)
