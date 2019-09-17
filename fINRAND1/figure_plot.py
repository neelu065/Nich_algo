
import matplotlib.pyplot as plt


def figure_plot(target , popsize , D ):
    A = [target[i][0] for i in range(popsize)]
    B = [target[i][1] for i in range(popsize)]
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.plot(A , B , '*')
    
#    plt.xlim(-(D+1),(D+1))
#    plt.ylim(-(D+1),(D+1))
    
    plt.show(block = False)
    return ()