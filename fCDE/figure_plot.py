
import matplotlib.pyplot as plt


def figure_plot(target , popsize ):
    A = [target[i][0] for i in range(popsize)]
    B = [target[i][1] for i in range(popsize)]
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(A , B , '*')
    plt.show(block = False)
    return ()