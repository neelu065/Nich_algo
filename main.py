import time
from de import de
from func import *

import matplotlib.pyplot as plt

# Inputs

Fn           = 2                                                               # Function to be evaluated
popsize      = 10
mut          = 0.6
crossp       = 0.7
iter_max     = 5000
func_eval    = func1                                                           # func to be evaluated

# Execution
start = time.time()
a , b  = de(func_eval, mut, crossp, popsize, iter_max, Fn)
end = time.time()

print('Time taken to Execute this code = {} seconds'.format(end - start))

A = [a[i][0] for i in range(popsize)]
B = [a[i][1] for i in range(popsize)]

plt.figure(2)
plt.title('Target vector after {} iteration'.format(iter_max))
plt.xlabel('x')
plt.ylabel('y')
plt.plot(A , B , '*')
plt.show(block = True)
