import time
from de import de
from func import fobj
from figure_plot import figure_plot
import matplotlib.pyplot as plt

# Inputs

Fn = 3  # Function to be evaluated
popsize = 20
mut = 0.5
crossp = 0.7
iter_max = 50
func_eval = fobj  # func to be evaluated

# Execution
start = time.time()
target, fitness = de(func_eval, mut, crossp, popsize, iter_max, Fn)
end = time.time()

print('Time taken to Execute this code = {} seconds'.format(end - start))

if len(target[0]) == 2:
    plt.title('Target vector after {} iteration'.format(iter_max))  # plot for reference
    figure_plot(target, popsize)  # comment if unnecessary
    plt.show()