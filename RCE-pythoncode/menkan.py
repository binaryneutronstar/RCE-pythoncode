import math as math
K=int(input("input K:"))
L=int(input("input L:"))
M=int(input("input M:"))
#convert Miller indeces to the usual Miller indices
k=M-K
l=K+M
m=L
print("k,l,m")
print(k)
print(l)
print(m)
a=5.431e-10#a is the lattice constant
d=1/((k/a)**2+(l/a)**2+(m/a)**2)
d=math.sqrt(d)
#distance between plane is the inverce of the length of the reciprocal lattice vector
print(d*1e10)
print("result in angstrome")
if( (2*M+L)%4==2 ):
    print("2M+L = 4j+2, so you need to check it")
