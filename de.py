import numpy as np
from constrain import const_violation
from selection import selection
from constrain_const import constrain_const
import matplotlib.pyplot as plt
def de(fobj, mut, crossp, popsize, its, Fn):
    value        = constrain_const(Fn)                                              # func which decide the Dimension and parameter(p)
    D            = value[0]
    bounds       = [(-(D+1),(D+1)) for i in range(D)]                               # search space
    print('bounds = {}'.format(bounds))
    dimensions = len(bounds)
    # Initilisation
    pop = np.random.uniform(-(D+1),(D+1),size = (popsize, dimensions))

    # plt.plot(pop[0],pop[]'*
    # plt.show()
    # min_b, max_b = np.asarray(bounds).T
    # diff = np.fabs(min_b - max_b)                                               # fabs func to get floating positive difference
    # pop_denorm = min_b + pop * diff
    # print(pop_denorm)
    # plt.plot(pop_denorm,'*')
    # plt.show()                                            # denormalized
    fitness = np.asarray([fobj(ind) for ind in pop])                     # func value evaluation

    for i in range(its):
        for j in range(popsize):

            # Mutation
            idxs = [idx for idx in range(popsize) if idx != j]                  # check to make sure that own index is not selected
            #a, b, c = pop[np.random.choice(idxs, 3, replace=False)]            # random choice among popsize excluding current index

            a = pop[np.argmin((pop[j] - pop[i])**2 for i in idxs)]              # fNRAND1 updated
            b, c = pop[np.random.choice(idxs, 2, replace=False)]

            mutant = a + mut * (b - c)                                          # just to make sure that value in limit(0,1)


            # Cross-over
            cross_points = np.random.rand(dimensions) < crossp                  # result in boolean values
            if not np.any(cross_points):                                        # check for false value
                cross_points[np.random.randint(0, dimensions)] = True           # Forcing atleast one index to become true.
            #trial = np.where(cross_points, mutant, pop[j])
            trial_denorm = np.where(cross_points, mutant, pop[j])
            #trial_denorm = min_b + trial * diff                                 # trail vector generator
            f = fobj(trial_denorm)                                              # trail func evaluation

            # Constrain_implementation
            phi_b = const_violation(trial_denorm  , Fn )
            phi_a = const_violation(pop[j] , Fn )
            # phi_a = 0
            # phi_b = 0
            # Selection
            fitness[j] , pop[j] = selection(phi_a , phi_b , f , fitness[j] , pop[j] , trial)

    return pop , fitness
