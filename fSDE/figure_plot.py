import matplotlib.pyplot as plt


def figure_plot(target, popsize,seed = None):
    A = [target[i][0] for i in range(popsize)]
    B = [target[i][1] for i in range(popsize)]
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(A, B, '*')
    if not seed == None:
        X = [target[i][0] for i in seed]
        Y = [target[i][1] for i in seed]
        plt.plot(X, Y, '^')
    plt.show(block=False)
    return ()
