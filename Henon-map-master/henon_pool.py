from numpy import *
from multiprocessing import Pool, cpu_count
from itertools import repeat

l=30
N=10033
xmax=10
eps=1e-5

# pool=Pool()

def Nper(args):
    lamka,be=args
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

	
if __name__ == '__main__':
	
	period=zeros([l,l], dtype=int32)

	lam_min=0
	lam_max=2.0
	b_min=-0.5
	b_max=0.5
	dlam=abs((lam_max-lam_min)/l)
	db=abs((b_max-b_min)/l)
	
	lam = arange(lam_min, lam_max, dlam)
	b = arange(b_min, b_max, db)
	
	p = Pool(cpu_count())
	for k in range(l):
		period[k,:]=p.map(Nper, zip(repeat(lam[k]),b))


	savetxt('henon_pool.txt', period, fmt="%2i")



