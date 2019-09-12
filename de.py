import numpy as np
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
            
            a, b, c = target[np.random.choice(idxs, 3, replace=False)]
            mutant = a + mut * (b - c)                                          # just to make sure that value in limit(0,1)


            # Cross-over
            cross_points = np.random.rand(dimensions) < crossp                  # result in boolean values
            if not np.any(cross_points):                                        # check for false value
                cross_points[np.random.randint(0, dimensions)] = True           # Forcing atleast one index to become true.
            trial = np.where(cross_points, mutant, target[j])                   # trial vector generator
                                          
            f = fobj(trial)                                                     # trial func evaluation
            
            ind = np.argmin((trial - target[i])**2 for i in range(popsize))   
           
            x_n = target[ind]                                                   # closest position vector
            print(x_n)
            f_xn = fitness[ind]
            # Constrain_implementation

            # Selection
            fitness[j] , target[j] = selection(f , f_xn , x_n , trial , Fn)    # domination check between trial vector and closest vector

    return target , fitness
