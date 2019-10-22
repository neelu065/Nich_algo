from constrain_const import constrain_const
import numpy as np

def const_violation(x , Fn):
    if (Fn >= 1 and Fn <= 9):
        D, P = constrain_const(Fn)                                                  # P = number of constraint
        phi_indv = []                                                               # D = Dimension of the function
        for p in np.arange(P):
            ap = 0
            for d in np.arange(D):
                Cp_old = np.mod(D - (p+1) + (d+1) + 1 , D)
                if Cp_old != 0:
                    Cp = Cp_old
                else:
                    Cp = D
#                print(x)
                ap = ap + (Cp * x[d]) ** 2
                
            gp = D**2 - ap
            phi_indv.append(max(0,gp))
        const_viol = sum(phi_indv)                                               # constraint violation

        return const_viol

# sine function constraint
    if (Fn == 10):
        gp = - np.cos(10*np.pi*x)
        const_viol = max([ 0 , gp ])
        return const_viol



    if (Fn == 11):
         z  = [ 3 , -2.805 , -3.779 , 3.584 ]
        
         e  = [ 2 , 3.131  , -3.283 , -1.848]
        
         g1 = z[0]*x[0] + z[1]*x[0] - z[0]*z[1] + e[0]*x[1] + e[1]*x[1] - e[0]*e[1] -x[0]**2 - x[1]**2
        
         g2 = z[1]*x[0] + z[2]*x[0] - z[1]*z[2] + e[1]*x[1] + e[2]*x[1] - e[1]*e[2] -x[0]**2 - x[1]**2
        
         g3 = z[2]*x[0] + z[3]*x[0] - z[2]*z[3] + e[2]*x[1] + e[3]*x[1] - e[2]*e[3] -x[0]**2 - x[1]**2
        
         g4 = z[3]*x[0] + z[0]*x[0] - z[3]*z[0] + e[3]*x[1] + e[0]*x[1] - e[3]*e[0] -x[0]**2 - x[1]**2
        
         gp = [ g1 , g2 , g3 , g4 ]
        
         phi_indv   = [max(0,gp[i]) for i in range(4)]
         const_viol = sum(phi_indv)
         
         return const_viol
     
         if (Fn == 12):
             g5 =  (x[0] - z[0]) + (x[1] - e[0])
            
             g6 = -(x[0] - z[1]) + (x[1] - e[1])
            
             g7 = -(x[0] - z[2]) - (x[1] - e[2])
            
             g8 =  (x[0] - z[3]) - (x[1] - e[3])
            
             gp = [ g1 , g2 , g3 , g4 , g5 , g6 , g7 , g8 ]
             phi_indv = [max(0,gp[i]) for i in range(8)]
             const_viol = sum(phi_indv)
             return const_viol