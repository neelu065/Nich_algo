import time
from de import de
from func import func3
from figure_plot import figure_plot
import matplotlib.pyplot as plt

# Inputs

Fn           = 11                                                               # Function to be evaluated
popsize      = 20
mut          = 0.65
crossp       = 0.65
iter_max     = 1000
func_eval    = func3                                                           # func to be evaluated

# Execution
start = time.time()
a , b = de(func_eval, mut, crossp, popsize, iter_max, Fn)
end = time.time()

print('Time taken to Execute this code = {} seconds'.format(end - start))

if len(a[0]) == 2:
    plt.title('Target vector after {} iteration'.format(iter_max))             # plot for reference 
    figure_plot(a , popsize )                                                  # comment if unnecessary
    plt.show()