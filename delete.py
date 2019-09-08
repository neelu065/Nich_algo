
import numpy as np
D = 5
bounds = [(-(D+1),(D+1)) for i in range(D)]
#print(bounds)


for i in range(1,D):
    g = D**3 - D**2
    #print(g)

gp = np.linspace(0,10,20)
print(gp)
for g in gp:
    asp = [max(0,g)]
    asd = sum(asp)
    print(asd)
const_viol = sum(asp)
