import numpy as np
from constrain import const_violation
from selection import selection
from constrain_const import constrain_const
import matplotlib.pyplot as plt


def de(fobj, mut, crossp, popsize, its, Fn):

    value        = constrain_const(Fn)                                         # func which decide the Dimension and parameter(p)
    D            = value[0]
    
    bounds       = [(-(D+1),(D+1)) for i in range(D)]                          # search space
    print('bounds = {}'.format(bounds))
    dimensions = len(bounds)

    # Initilisation
    target = np.random.uniform(-(D+1),(D+1),size = (popsize, dimensions))
    
    # plot to verify the distribution
    A = [target[i][0] for i in range(popsize)]
    B = [target[i][1] for i in range(popsize)]
    plt.figure(1)
    plt.title('Initial Uniformly Distributed target vector')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(A , B , '*')
    plt.show(block = False)

    fitness = np.asarray([fobj(ind) for ind in target])                        # func value evaluation

    for i in range(its):
        for j in range(popsize):

            # Mutation
            idxs = [idx for idx in range(popsize) if idx != j]                 # check to make sure that own index is not selected
            
            if (j != 0 or j != popsize-1):                                     # FINRAND1 Updated
                a = target[np.argmin((target[j] - target[i])**2 for i in [j-1,j+1])]
            else:
                a = target[np.argmin((target[j] - target[i])**2 for i in idxs)]
            
            b, c = target[np.random.choice(idxs, 2, replace=False)]
            mutant = a + mut * (b - c)                                          # just to make sure that value in limit(0,1)


            # Cross-over
            cross_points = np.random.rand(dimensions) < crossp                  # result in boolean values
            if not np.any(cross_points):                                        # check for false value
                cross_points[np.random.randint(0, dimensions)] = True           # Forcing atleast one index to become true.
            trial = np.where(cross_points, mutant, target[j])                   # trail vector generator
                                          
            f = fobj(trial)                                                      # trail func evaluation

            # Constrain_implementation

            # Selection
            fitness[j] , target[j] = selection(f , fitness[j] , target[j] , trial , Fn)



    return target , fitness
