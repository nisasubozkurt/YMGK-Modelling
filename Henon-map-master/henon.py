from numpy import *

l=100
N=10033
xmax=10
eps=1e-5

def Nper(lamka,be):
    x=zeros(N)

    x[0]=0.03
    x[1]=0.01

    Nl=10000

    for h in range(2,N):   
        if abs(x[h-1])>xmax:
            return 0 
        else: 
            x[h]=1-(lamka*(x[h-1]*x[h-1]))-(be*x[h-2])
    
    
    for f in range(1,33):
        if abs(x[f+10000]-x[10000])<eps:
            return f

    return 33


lam=zeros(l)
b=zeros(l)
period=zeros([l,l], dtype=int32)


lam[0]=0
lam[l-1]=2.0
b[0]=-0.5
b[l-1]=0.5
dlam=abs((lam[l-1]-lam[0])/l)
db=abs((b[l-1]-b[0])/l)

  
for i in range(l):
    lam[i]=lam[0]+i*dlam
    b[i]=b[0]+i*db

for k in range(l):
    for j in range(l):
        period[k][j]=Nper(lam[k],b[j])


savetxt('henon.txt', period, fmt="%2i")



