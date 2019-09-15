import numpy as np
from selection import selection
from constrain_const import constrain_const
from figure_plot import figure_plot
import matplotlib.pyplot as plt

def de(fobj, mut, crossp, popsize, its, Fn):

    value        = constrain_const(Fn)                                         # func which decide the Dimension and parameter(p)
    D            = value[0]
    bounds       = [(-(D+1),(D+1)) for i in range(D)]                          # search space
    print('bounds = {}'.format(bounds))
    
    # Initilisation
    target = np.random.uniform(-(D+1),(D+1),size = (popsize, D))
    
    if len(target[0]) == 2:
        plt.title('Initial Uniformly Distributed target vector')
        figure_plot(target , popsize )
   
    fitness = np.asarray([fobj(ind) for ind in target])                        # func value evaluation

    for i in range(its):
        for j in range(popsize):

            # Mutation
            idxs = [idx for idx in range(popsize) if idx != j]                 # check to make sure that own index is not selected
            
            all_sum = []
            for n in idxs:
                indv_sum =  sum((target[j][i] - target[n][i])**2  for i in range(D))
                all_sum.append(indv_sum)
            ind = np.argmin(all_sum)
            a = target[ind]                                                    # here only two position vector are randomly selected in nature
            b, c = target[np.random.choice(idxs, 2, replace=False)]
            
            mutant = a + mut * (b - c)                                         
            
            # Cross-over
            cross_points = np.random.rand(D) < crossp                          # result in boolean values
            if not np.any(cross_points):                                       # check for false value
                cross_points[np.random.randint(0, D)] = True                   # Forcing atleast one index to become true.
            trial = np.where(cross_points, mutant, target[j])                  # trial vector generator
                                          
            f = fobj(trial)                                                    # trial func evaluation

            # Selection                                                        # Constrain_implementation
            fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn)    # domination check between trial vector and closest vector

    return target , fitness, ind
