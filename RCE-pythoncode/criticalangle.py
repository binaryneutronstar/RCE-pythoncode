import math as math
K=int(input("input K:"))
L=int(input("input L:"))
M=int(input("input M:"))
#convert Miller indeces to the usual Miller indices
k=M-K
l=K+M
m=L
a=5.431e-10#a is the lattice constant
d=1/((k/a)**2+(l/a)**2+(m/a)**2)
d=math.sqrt(d)
#distance between plane is the inverce of the length of the reciprocal lattice vector
print("distance between the crystalline planes")
print(d*1e10)
print("result in angstrome")
if( (2*M+L)%4==2 ):
    print("2M+L = 4j+2, so you need to check it")
print("now let's calculate the critical angle")
E=float(input("input beam energy:"))
Z2=int(input("input the atomic number of the projectile ion (Ar=18):"))
phi=math.sqrt(d*1e10/1.56779*Z2/18*391.0/E)*0.17
print(phi)
print("mrad")
print("lets calculate critical angle based on MC simulation")

print("here we assume thermal vibration amplitude 0.15 angstrom")
rho1=0.15
al1=0.1
al2=0.55
al3=0.35
bet1=6.0
bet2=1.2
bet3=0.3
aTF=1.123
xi=rho1/aTF
eta=d*1e10/aTF
print("assume aTF is")
print(aTF)
print("xi is")
print(xi)
print("eta is")
print(eta)
fps1=(bet1/al1)*math.exp(-1*bet1*xi)+(bet2/al2)*math.exp(-1*bet2*xi)+(bet3/al3)*math.exp(-1*bet3*xi)
fps2=(bet1/al1)*math.exp(-1*bet1*(eta-xi))+(bet2/al2)*math.exp(-1*bet2*(eta-xi))+(bet3/al3)*math.exp(-1*bet3*(eta-xi))
fps3=(bet1/al1)*math.exp(-1*bet1*eta/2)+(bet2/al2)*math.exp(-1*bet2*eta/2)+(bet3/al3)*math.exp(-1*bet3*eta/2)
P=math.sqrt(fps1+fps2-2*fps2)
print("P is")
print(P)
print("critical angle is")
print(0.76*P*phi)
print("mrad")
