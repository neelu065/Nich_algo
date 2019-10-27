import matplotlib.pyplot as plt
from constrain_const import constrain_const

def figure_plot(target, popsize,Fn,c= None):
    A = [target[i][0] for i in range(popsize)]
    B = [target[i][1] for i in range(popsize)]
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(A, B, '*')
    if 1 <= Fn <= 9:
        value = constrain_const(Fn)  # func which decide the Dimension and parameter(p)
        D = value[0]
        plt.ylim(-(D+1),D+1)
        plt.xlim(-(D+1),D+1)
    if Fn == 11 or Fn == 12:
        plt.ylim(-6,6)
        plt.ylim(-6,6)
    if Fn == 19:
        plt.ylim(-c,c)
        plt.xlim(-c,c)
    plt.show(block=False)
    return ()
