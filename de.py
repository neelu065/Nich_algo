import numpy as np
from mutation import *
from selection import *
def de(fobj, bounds, mut, crossp, popsize, its):
    dimensions = len(bounds)
    # Initilisation
    pop = np.random.rand(popsize, dimensions)
    min_b, max_b = np.asarray(bounds).T
    diff = np.fabs(min_b - max_b)                                               # fabs func to get floating positive difference
    pop_denorm = min_b + pop * diff                                             # denormalized
    fitness = np.asarray([fobj(ind) for ind in pop_denorm])                     # func value evaluation
    best_idx = np.argmin(fitness)                                               # index with min func value
    best = pop_denorm[best_idx]                                                 # corr func value
    for i in range(its):
        for j in range(popsize):
            # Mutation
            idxs = [idx for idx in range(popsize) if idx != j]                  # check to make sure that own index is not selected
            a, b, c = pop[np.random.choice(idxs, 3, replace=False)]             # random choice among popsize excluding current index
            mutant = np.clip(a + mut * (b - c), 0, 1)                           # just to make sure that value in limit(0,1)
            #mutant = mutation1(popsize , j , pop)
            # Cross-over
            cross_points = np.random.rand(dimensions) < crossp                  # result in boolean values
            if not np.any(cross_points):                                        # check for false value
                cross_points[np.random.randint(0, dimensions)] = True           # Forcing atleast one index to become true.
                trial = np.where(cross_points, mutant, pop[j])
                trial_denorm = min_b + trial * diff                             # trail vector generator
                f = fobj(trial_denorm)                                          # trail func evaluation
                # Selection

                if f < fitness[j]:
                    fitness[j] = f                                              # compare with previous generation
                    pop[j] = trial
                    if f < fitness[best_idx]:                                   # check for best vector
                        best_idx = j                                            # compare with previous index
                        best = trial_denorm
    return best, fitness[best_idx]                                              # retun best vector and its func value
