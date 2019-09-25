import matplotlib.pyplot as plt
import numpy as np
from constrain_const import constrain_const
from func import fobj
Fn = 3
popsize      = 5
value        = constrain_const(Fn)                                         # func which decide the Dimension and parameter(p)
D            = value[0]
target = np.random.uniform(-(D+1),(D+1),size = (popsize , D))
fitness = np.asarray([fobj(ind , Fn) for ind in target])
def const_violation(x , Fn):
    if (Fn >= 1 or Fn <= 9):
        D, P = constrain_const(Fn)                                                  # P = number of constraint
        phi_indv = []                                                               # D = Dimension of the function
        for p in np.arange(P):
            ap = 0
            for d in np.arange(D):
                Cp_old = np.mod(D - (p+1) + (d+1) + 1 , D)
                if Cp_old != 0:
                    Cp = Cp_old
                else:
                    Cp = D
                
                ap = ap + (Cp * x[d]) ** 2
            
            gp = D**2 - ap
            phi_indv.append(max(0,gp))
        const_viol = sum(phi_indv)                                               # constraint violation

    return const_viol
#a = [const_violation(target[i],Fn) for i in range(popsize)]
#print(a)
b=[] ; c = []; e=[] ; f=[]                                                      # b is list of fitness value
for i in range(popsize):                                                        # c= list of violated values
    ans = const_violation(target[i],Fn)                                           # d= cpoy of b for reference 
    if ans == 0:                                                                  # e= index of feasible fitness value
        b.append(fitness[i])                                                    # f = index of violated values
        e.append(i)
    else:
        c.append(ans)
        f.append(i)
feas_sort = []    ;  feas_ind=[]
d = b.copy()    ; g=c.copy()  
b.sort() ;        c.sort()
target_sort = []
for i in range(len(b)):
    indx = d.index(b[i])
    target_indx = e[indx]
    target_sort.append(target[target_indx])
    #print(target_indx)
    print(target[target_indx] , target_indx)  
print('infeasible')
for i in range(len(c)):
    indx = g.index(c[i])
    target_indx = f[indx]
    target_sort.append(target[target_indx])
#    print(target_indx)
    print(target[target_indx] , target_indx)                                                                 # list which hold index corr to mini distance
#for m in range(len(b)):
#    indx = np.argmin(b)
#    feas_sort.append(b[indx])
#    feas_ind.append(indx)
#    b[indx] = max(b) + 1 
#target_feas_sort = target[feas_ind]


#infeas_sort =[] ; infeas_ind = []
#for n in range(len(c)):
#    indx = np.argmin(c)
#    infeas_sort.append(c[indx])
#    infeas_ind.append(indx)
#    c[indx] = max(c) + 1
#target_infeas_sort = target[infeas_ind]
##print(np.min(b))
print('compare min_ind and d variable\nfeasible sorted out, concentrate on infeasible once')
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
#D = 2
#popsize = 5
#target = np.random.uniform(-(D+1),(D+1),size = (popsize, D))
#trial  = [0 , 0  ]
#
#A = [target[i][0] for i in range(popsize)]
#B = [target[i][1] for i in range(popsize)]
#
#plt.figure(2)
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.plot(A , B , '*')
#
#
#ab = []
#for n in np.arange(popsize):
#    qw =  sum((trial[i] - target[n][i])**2  for i in range(D))
#    ab.append(qw)
#zx = np.argmin(ab)
#print(zx)
#print(target[zx])
#print(ab[zx])
#plt.plot(target[zx][0],target[zx][1],'ro',label = 'target')
#
#plt.plot(trial[0],trial[1],'m^',label = 'trial')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#
#plt.show()
