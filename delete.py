import matplotlib.pyplot as plt
import numpy as np
D = 5
#bounds = [(-(D+1),(D+1)) for i in range(D)]
## #print(bounds)
##
##
## for i in range(1,D):
##     g = D**3 - D**2
##     #print(g)
##
## gp = np.linspace(0,10,20)
## print(gp)
## for g in gp:
##     asp = [max(0,g)]
##     asd = sum(asp)
##     print(asd)
## const_viol = sum(asp)
#popsize = 20
#
#pop = np.random.rand(popsize,2)
#
#j = 4
#mut = 0.5
#
#idxs = [idx for idx in range(popsize) if idx != j]                  # check to make sure that own index is not selected
#a = pop[np.argmin((pop[j] - pop[i])**2 for i in idxs)]
#b, c = pop[np.random.choice(idxs, 2, replace=False)]             # random choice among popsize excluding current index
#
#mutant = np.clip(a + mut * (b - c), 0, 1)
#
#print(a , b , c)
#print(mutant)

# check for closest point
D = 2
popsize = 10
target = np.random.uniform(-(D+1),(D+1),size = (popsize, D))
trial  = [0 , 0  ]

A = [target[i][0] for i in range(popsize)]
B = [target[i][1] for i in range(popsize)]

plt.figure(2)

plt.xlabel('x')
plt.ylabel('y')
plt.plot(A , B , '*')


ab = []
for n in np.arange(popsize):
    qw =  sum((trial[i] - target[n][i])**2  for i in range(D))
    ab.append(qw)
zx = np.argmin(ab)
print(zx)
print(target[zx])
print(ab[zx])
plt.plot(target[zx][0],target[zx][1],'ro')
plt.plot(trial[0],trial[1],'m^')