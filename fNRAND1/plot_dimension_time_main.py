import time
from de import de
from func import fobj
from figure_plot import figure_plot
import matplotlib.pyplot as plt
import concurrent.futures
# Inputs
def func( Dimension_number ):
    Time = []
    for i in range(Dimension_number):
        Fn = 20  # Function to be evaluated
        Dimension = i+1
        
        popsize = 20
        mut = 0.9
        crossp = 0.9
        iter_max = 1500
        func_eval = fobj  # func to be evaluated
        ca = 512
        
        # Execution
        start = time.time()
        target, fitness = de(func_eval, mut, crossp, popsize, iter_max, Fn, ca, Dimension)
        end = time.time()
        Time.append(end - start)
        print('Time taken to Execute this code = {} seconds'.format(end - start))
        
        #        if len(target[0]) == 2:
        #            plt.title('Target vector after {} iteration'.format(iter_max))  # plot for reference
        #            figure_plot(target, popsize, Fn ,ca)  # comment if unnecessary
        
    return Time

Max_Dimension=100

Time = func( Max_Dimension )


with open('plot_dimension_time_taken.csv','w') as f:
    f.write("Dimension \t\t Time Taken(seconds) \n")
    for i in range(Max_Dimension):
        f.write('{} \t\t\t {} \n'.format( i+1 , Time[i]))

plt.figure()
plt.plot(range(1,Max_Dimension+1) , Time, '-')
plt.xlabel('Dimensions')
plt.ylabel('Time Taken (sec)')
plt.title('Time Taken for Various Dimension (fNRAND1)')
plt.grid()
plt.savefig('plot_dimension_time_taken.png', dpi = 300)
plt.show()