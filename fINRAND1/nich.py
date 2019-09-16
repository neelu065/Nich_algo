# fDE

#mutation
a, b, c = pop[np.random.choice(idxs, 3, replace=False)]                       # random choice among popsize excluding current index
#selection
fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn)




# fNRAND1

#mutation
all_sum = []
for n in idxs:
    indv_sum =  sum((target[j][i] - target[n][i])**2  for i in range(D))
    all_sum.append(indv_sum)
ind = np.argmin(all_sum)
a = target[ind]                                                    # here only two position vector are randomly selected in nature
b, c = target[np.random.choice(idxs, 2, replace=False)]
#selection
fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn) 



#fINRAND1

#mutation
all_sum = []
            
if (j == 0 or j == popsize-1):
    idxs = [idx for idx in range(popsize) if idx != j]
    
    for n in idxs:
        indv_sum =  sum((target[j][i] - target[n][i])**2  for i in range(D))
        all_sum.append(indv_sum)
    ind = np.argmin(all_sum)
   
else:
    
    for n in [j-1,j+1]:
        indv_sum =  sum((target[j][i] - target[n][i])**2  for i in range(D))
        all_sum.append(indv_sum)
    
    ind = np.where(np.argmin(all_sum) == 0 , j-1 , j+1)

a = target[ind]                                                    # three different vectors are generated.
b, c = target[np.random.choice(idxs, 2, replace=False)]            # here only two position vector are randomly selected in nature

#selection
fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn)


# fCDE

 # process to find the closest target vector for this iteration trial vector
all_sum = []
for n in np.arange(popsize):
    
    indv_sum = sum((trial[i] - target[n][i])**2  for i in range(D))
    all_sum.append(indv_sum)

ind  = np.argmin(all_sum)
x_n  = target[ind]
f_xn = fitness[ind]
# Selection                                                        # Constrain_implementation
fitness[j] , target[j] = selection(f , f_xn , x_n , trial , Fn)    # domination check between trial vector and closest vector



#fNCDE

