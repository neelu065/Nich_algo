import numpy as np
from constrain import const_violation
from selection import selection

def de(fobj, bounds, mut, crossp, popsize, its, Fn):
    dimensions = len(bounds)
    # Initilisation
    pop = np.random.rand(popsize, dimensions)
    min_b, max_b = np.asarray(bounds).T
    diff = np.fabs(min_b - max_b)                                               # fabs func to get floating positive difference
    pop_denorm = min_b + pop * diff                                             # denormalized
    fitness = np.asarray([fobj(ind) for ind in pop_denorm])                     # func value evaluation

    for i in range(its):
        for j in range(popsize):

            # Mutation
            idxs = [idx for idx in range(popsize) if idx != j]                  # check to make sure that own index is not selected
            a, b, c = pop[np.random.choice(idxs, 3, replace=False)]             # random choice among popsize excluding current index
            mutant = np.clip(a + mut * (b - c), 0, 1)                           # just to make sure that value in limit(0,1)

            # Cross-over
            cross_points = np.random.rand(dimensions) < crossp                  # result in boolean values
            if not np.any(cross_points):                                        # check for false value
                cross_points[np.random.randint(0, dimensions)] = True           # Forcing atleast one index to become true.
            trial = np.where(cross_points, mutant, pop[j])
            trial_denorm = min_b + trial * diff                                 # trail vector generator
            f = fobj(trial_denorm)                                              # trail func evaluation

            # Constrain_implementation
            phi_b = const_violation(trial_denorm  , Fn )
            phi_a = const_violation(pop_denorm[j] , Fn )

            # Selection
            fitness[j] , pop[j] = selection(phi_a , phi_b , f , fitness[j] , pop[j] , trial)

    return pop , fitness
