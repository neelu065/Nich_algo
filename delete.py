# bounds=[]
# D = 1
# for i in range(5):
#     bounds.append([-(D+1),(D+1)])

import numpy as np
D = 5
bounds = [(-(D+1),(D+1)) for i in range(D)]
print(bounds)
