import numpy as np
def mutation1(popsize , j , pop):
    idxs = [idx for idx in range(popsize) if idx != j]                  # check to make sure that own index is not selected
    a, b, c = pop[np.random.choice(idxs, 3, replace=False)]             # random choice among popsize excluding current index
    mutant = np.clip(a + mut * (b - c), 0, 1)
    return mutant
