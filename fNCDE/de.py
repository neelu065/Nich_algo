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
   

    fitness = np.asarray([fobj(ind , Fn) for ind in target])                        # func value evaluation

    for i in range(its):
        for j in range(popsize):

            # Mutation
            idxs = [idx for idx in range(popsize) if idx != j]

            all_sum = []                                                       # list which hold distances from trial vector
            for n in idxs:
                indv_sum =  sum((target[j][i] - target[n][i])**2  for i in range(D))
                all_sum.append(indv_sum)

            min_ind = []
                                                                               # list which hold index corr to mini distance
            for m in range(10):
                indx = np.argmin(all_sum)
                min_ind.append(indx)
                all_sum[indx] = max(all_sum) + 1                                 # replaced that number with max number 
                                                                               # so that it wont come into consideration anymore

            a , b , c = target[np.random.choice( min_ind , 3 , replace=False)]

            mutant = a + mut * (b - c)                                         # using 3 nearest vectors for given target vector

            # Cross-over
            cross_points = np.random.rand(D) < crossp                          # result in boolean values
            if not np.any(cross_points):                                       # check for false value
                cross_points[np.random.randint(0, D)] = True                   # Forcing atleast one index to become true.
            trial = np.where(cross_points, mutant, target[j])                  # trial vector generator

            f = fobj(trial, Fn)                                                # trial func evaluation

            # process to find the closest target vector for this iteration trial vector
            all_set = []
            for n in range(popsize):

                indv_sum = sum((trial[i] - target[n][i])**2  for i in range(D))
                all_set.append(indv_sum)

            ind  = np.argmin(all_set)
            x_n  = target[ind]
            f_xn = fitness[ind]

            # Selection                                                        # Constrain_implementation
            fitness[j] , target[j] = selection(f , f_xn , x_n , trial , Fn)    # domination check between trial vector and closest vector

    return target , fitness
