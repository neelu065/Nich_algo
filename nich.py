# fDE

#mutation
a, b, c = pop[np.random.choice(idxs, 3, replace=False)]                       # random choice among popsize excluding current index
#selection
fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn)




# fNRAND1

#mutation
a = target[np.argmin((target[j] - target[i])**2 for i in idxs)]                # here only two position vector are randomly selected in nature
b, c = target[np.random.choice(idxs, 2, replace=False)]
#selection
fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn) 



#fINRAND1

#mutation
if (j != 0 or j != popsize-1):                                    
    a = target[np.argmin((target[j] - target[i])**2 for i in [j-1,j+1])]
else:
    a = target[np.argmin((target[j] - target[i])**2 for i in idxs)]
    
b, c = target[np.random.choice(idxs, 2, replace=False)]
#selection
fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn)


# fCDE

 