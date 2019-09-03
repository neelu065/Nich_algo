from de import de
from func import *

bounds = [(-4.5, 4.5), (-4.5,4.5)]  # search space

a, b = de(func1, bounds)

print(a, b)
