import matplotlib.pyplot as plt
import numpy as np


# Python code to demonstrate working of 
# nlargest() and nsmallest() 

# importing "heapq" to implement heap queue 
import heapq 
D = 2

popsize = 20

# initializing list 
#li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1] 

# using heapify() to convert list into heap 
#heapq.heapify(li1) 

# using nlargest to print 3 largest numbers 
## prints 10, 9 and 8 
#print("The 3 largest numbers in list are : ",end="") 
#print(heapq.nlargest(3, li1)) 
#
## using nsmallest to print 3 smallest numbers 
## prints 1, 3 and 4 
#print("The 3 smallest numbers in list are : ",end="") 
#print(heapq.nsmallest(3, li1)) 
D = 2

popsize = 20
target = np.random.uniform(-(D+1),(D+1),size = (popsize, D))
for j in range(1):

    # Mutation
    idxs = [idx for idx in range(popsize) if idx != j]                 # check to make sure that own index is not selected
    
    all_sum = []
    
       
    for n in idxs:
        indv_sum =  sum((target[j][i] - target[n][i])**2  for i in range(D))
        all_sum.append(indv_sum)
    #print("The 3 smallest numbers in list are : ",end="") 
    a  = heapq.nsmallest(3, all_sum)
    print(np.argmin(all_sum))
#    indiv = []
#    for ab in range(7):
#        noun = np.argmin(all_sum)
#        indiv.append(noun)
#        #all_sum.remove(all_sum[noun])
#    print('min_indx :{}'.format(indiv))
#    print('all_sum :{}'.format(all_sum))
#    a , b , c = target[np.random.choice(indiv, 3, replace=False)]
#    print(a)
       #all_sum.remove(all_sum[index])
#        ind = np.where(index == 0 , j-1 , j+1)
#bounds = [(-(D+1),(D+1)) for i in range(D)]
## #print(bounds)
##
##
## for i in range(1,D):
##     g = D**3 - D**2
##     #print(g)
##
## gp = np.linspace(0,10,20)
## print(gp)
## for g in gp:
##     asp = [max(0,g)]
##     asd = sum(asp)
##     print(asd)
## const_viol = sum(asp)
#popsize = 20
#
#pop = np.random.rand(popsize,2)
#
#j = 4
#mut = 0.5
#
#idxs = [idx for idx in range(popsize) if idx != j]                  # check to make sure that own index is not selected
#a = pop[np.argmin((pop[j] - pop[i])**2 for i in idxs)]
#b, c = pop[np.random.choice(idxs, 2, replace=False)]             # random choice among popsize excluding current index
#d = np.argmin((pop[j] - pop[i])**2 for i in idxs)
#mutant = np.clip(a + mut * (b - c), 0, 1)
#
#print(a , b , c)
#print(mutant)

# check for closest point
#D = 2
#popsize = 5
#target = np.random.uniform(-(D+1),(D+1),size = (popsize, D))
#trial  = [0 , 0  ]
#
#A = [target[i][0] for i in range(popsize)]
#B = [target[i][1] for i in range(popsize)]
#
#plt.figure(2)
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.plot(A , B , '*')
#
#
#ab = []
#for n in np.arange(popsize):
#    qw =  sum((trial[i] - target[n][i])**2  for i in range(D))
#    ab.append(qw)
#zx = np.argmin(ab)
#print(zx)
#print(target[zx])
#print(ab[zx])
#plt.plot(target[zx][0],target[zx][1],'ro',label = 'target')
#
#plt.plot(trial[0],trial[1],'m^',label = 'trial')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#
#plt.show()
       