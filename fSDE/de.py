import numpy as np
from selection import selection
from constrain_const import constrain_const
from figure_plot import figure_plot
import matplotlib.pyplot as plt
from sort_file import sorttarget
from distance import neighbour, uniquevector,cluster_point


def de(fobj, mut, crossp, popsize, its, Fn):
    # Initilisation
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
        ca = 512  # limits
        bounds = []
        for i in range(D):
            bounds.append((-ca, ca))
        target = np.random.uniform(-ca, ca, size = (popsize, 2))
    
    print('bounds = {}'.format(bounds))
    
    if len(target[0]) == 2:
        plt.title('Initial Uniformly Distributed target vector')
        figure_plot(target, popsize,Fn,ca)

    fitness = np.asarray([fobj(ind, Fn) for ind in target])  # objective func evaluation

    for i in range(its):
        target_sort = sorttarget(Fn, popsize, target, fitness) # call sort function here

        radius = 1  # radius of influence

        ab, s, seed = neighbour(target_sort, popsize, radius, D)   # call distance function here

        # renamed target_sort as target so that further understanding would be easier.
        target = target_sort

        fitness = np.asarray([fobj(ind, Fn) for ind in target])

        for j in range(popsize):

            # Mutation
            if ab[j] == 'false':  # corr to seed
                idxs = [idx for idx in range(len(s)) if s[idx][1] == j]
                
            else:  # corr to neigh_bour points
                idxs = cluster_point(s,target[j]) # call cluster_function here
            
            x = np.random.choice(idxs, 3, replace=False)
            
            a, b, c = [s[item][0] for item in x]

            mutant = a + mut * (b - c)  # using 3 nearest vectors for given target vector

            # Cross-over
            cross_points = np.random.rand(D) < crossp  # result in boolean values
            if not np.any(cross_points):  # check for false value
                cross_points[np.random.randint(0, D)] = True  # Forcing atleast one index to become true.
            trial = np.where(cross_points, mutant, target[j])  # trial vector generator

            f = fobj(trial, Fn)  # trial func evaluation

            # if trial fitness is same as its species seed, then randomly generate new trial vector
            if ab[j] == 'false' and f == fitness[j]:  # if j is seed then compare only eith that species seed
                if  11<= Fn <= 12:
                    trial = np.random.uniform(-(5 + 1), (5 + 1), size=(1, D))
                if 1 <= Fn <=9:
                    trial = np.random.uniform(-(D + 1), (D + 1), size=(1, D))
                if Fn ==19:
                    trial = np.random.uniform(-(ca), (ca), size=(1, D))
                
                f = fobj(trial, Fn)

            if ab[j] == 'true' and np.any(f == fitness[seed]):  # if j is neigh_bour point then compare with all seed
                if  11<= Fn <= 12:
                    trial = np.random.uniform(-(5 + 1), (5 + 1), size=(1, D))
                if 1 <= Fn <=9:
                    trial = np.random.uniform(-(D + 1), (D + 1), size=(1, D))
                if Fn ==19:
                    trial = np.random.uniform(-(10), (10), size=(1, D))
                f = fobj(trial, Fn)

            
            # Selection                                                        # Constrain_implementation

            fitness[j], target[j] = selection(f, fitness[j], target[j], trial,
                                              Fn)  # domination check between trial vector and closest vector

        # create the function from here
        target = uniquevector(s, seed, target)

        fitness = np.asarray([fobj(ind, Fn) for ind in target])

        target_sort = sorttarget(Fn, len(target), target, fitness)
        target = target_sort[0:popsize]
     
    return target, np.asarray([fobj(ind, Fn) for ind in target])
