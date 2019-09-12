
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
j =5
D = 2
target = np.random.uniform(-(D+1),(D+1),size = (20, 2))
trial  = np.random.uniform(-(D+1),(D+1),size = (20, 2))


diff = np.argmin((target[i]-trial[i])**2 for i in range(20))

print(diff)