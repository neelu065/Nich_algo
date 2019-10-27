import numpy as np
from selection import selection
from constrain_const import constrain_const
from figure_plot import figure_plot
import matplotlib.pyplot as plt

def de(fobj, mut, crossp, popsize, its, Fn, ca):

    # Initilisation
    np.random.seed(20)
    if 1 <= Fn <= 9:
        value = constrain_const(Fn)  # func which decide the Dimension and parameter(p)
        D = value[0]
        bounds = []
        for i in range(D):
            bounds.append((-(D + 1), (D + 1)))
        target = np.random.uniform(-(D + 1), (D + 1), size=(popsize, D))
    
    if Fn == 11 or Fn == 12:
        D = 2
        bounds = []
        for i in range(D):
            bounds.append((-(5 + 1), (5 + 1)))
        target = np.random.uniform(-(5 + 1), (5 + 1), size=(popsize, 2))
    
    
    if Fn == 19:
        D = 2
        bounds = []
        for i in range(D):
            bounds.append((-ca, ca))
        target = np.random.uniform(-ca, ca, size = (popsize, 2))
    
    print('bounds = {}'.format(bounds))
    
    if len(target[0]) == 2:
        plt.title('Initial Uniformly Distributed target vector')
        figure_plot(target, popsize,Fn,ca)
    fitness = np.asarray([fobj(ind, Fn) for ind in target])                        # func value evaluation

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
                                          
            f = fobj(trial, Fn)                                                    # trial func evaluation

            # Selection                                                        # Constrain_implementation
            fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn)    # domination check between trial vector and closest vector

    return target , fitness
