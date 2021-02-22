# import sympy
from sympy.abc import x

func = x ** 2 + x ** 4             # function
iterations = 10                    # number of iterations to perform
f_prim = sympy.diff(func, x)       # df/dx
f_bis = sympy.diff(f_prim, x)      # df'/dx 
xx0 = -4                           # x0
xx1 = -3                           # x1


#################### NEWTON'S METHOD ####################
x_NM = []
y_NM = []
fp_NM = []
xx = xx1

for i in range(iterations):
    yy = func.subs(x, xx)
    x_NM.append(float(xx))
    y_NM.append(float(yy))
    fp_NM.append(float(f_prim.subs(x, xx)))
    xx = xx - f_prim.subs(x, xx) / f_bis.subs(x, xx)
  
    
#################### SECANT METHOD ####################
x_SM = []
y_SM = []
fp_SM = []
xx_k_minus_1 = xx0
xx_k = xx1

for i in range(iterations):
    yy_k = func.subs(x, xx_k)
    x_SM.append(float(xx_k))
    y_SM.append(float(yy_k))
    fp_SM.append(float(f_prim.subs(x, xx_k)))
    f_bis_est_k = ( f_prim.subs(x, xx_k) - f_prim.subs(x, xx_k_minus_1) ) / (xx_k - xx_k_minus_1)
    xx_k_minus_1 = xx_k
    xx_k = xx_k - f_prim.subs(x, xx_k) / f_bis_est_k

    
#################### Plotting Results ####################
import matplotlib.pyplot as plt

### Graph 1
plt.plot(list(range(1,iterations+1)), y_NM, list(range(1,iterations+1)), y_SM)
plt.suptitle('Function Values on each Iteration')
plt.yscale('log')
plt.ylabel('f')
plt.xlabel('Iteration')
plt.show()

### Graph 2
x_NM_0 = []
fp_NM_0 = []
x_SM_0 = []
fp_SM_0 = []

for i in range(iterations):
    x_NM_0.append(x_NM[i])
    x_NM_0.append(x_NM[i])
    
    fp_NM_0.append(0)
    fp_NM_0.append(fp_NM[i])
    
    x_SM_0.append(x_SM[i])
    x_SM_0.append(x_SM[i])
    
    fp_SM_0.append(0)
    fp_SM_0.append(fp_SM[i])

plt.plot(x_NM_0, fp_NM_0, x_SM_0, fp_SM_0)
plt.suptitle('f(x)')
plt.ylabel('f')
plt.xlabel('x')
plt.show()

'''
Output Graphs attached as seperate pictures
'''