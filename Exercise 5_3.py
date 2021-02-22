# Script iterates towards min or max value of a given function 
# with a descent gradient exact line search and unit step size
# starting x value of 10
# and imposed iteration quantities in number of 1

from sympy import solve
import sympy
import math
x = sympy.Symbol('x')
a = sympy.Symbol('a')

func = 2.73**x + 2.73**(-x)
iterations = 1
func_der = sympy.diff(func, x)    # df/dx
x1 = 10                           # x1
p1 = -func_der.subs(x, x1)        # calculating p1 = p(x1) = f'(x1) : function's gradient in x1
y1 = func.subs(x, x1)             # calculating y1 = f(x1)

print(f'Starting values are: \nx1 = {x1} \np1 = {p1}\ny1 = {y1}')


################# gradient descent with unit step size #################

# calculating x2_unitstep with p1 and x1
x2_unitstep = x1 + p1                             # x2_unitstep = -23083.5462371137 
p2_unitstep = -func_der.subs(x, x2_unitstep)      # p2_unitstep = 1.52227819194550E+10068
y2_unitstep = func.subs(x, x2_unitstep)           # y2_unitstep = 1.51575799342078E+10068

print(f'\nAfter one step of gradient descent with unit step size values are: \nx2 = {x2_unitstep} \np2 = {p2_unitstep}\ny2 = {y2_unitstep}')


################# gradient descent with exact line search #################

# solving 0 = f'(x1 + p(x1)*a)/da for alpha
y2 = func.subs(x, x1 + a*p1)            # substituting x with x2 = x1 + a*p1 in f(x)
y2_da = sympy.diff(y2, a)               # calculating df/da
a1 = solve(y2_da, a)                    # solving y2_da for alpha : a1 = [10/23093.5462371137]

# calculating x2 with p1, a1_der and x1
x2 = x1 + a1[0] * p1            # x2 = 0
p2 = -func_der.subs(x, x2)      # p2 = 0 -> reached extreme value    
y2 = func.subs(x, x2)           # y2 = 2

print(f'\nAfter one step of gradient descent with exact line search values are: \nx2 = {x2} \np2 = {p2}\ny2 = {y2}')


'''
# Output:
 
Starting values are: 
x1 = 10 
p1 = -23093.5462371137
y1 = 22994.6324022445

After one step of gradient descent with unit step size values are: 
x2 = -23083.5462371137 
p2 = 1.52227819194550E+10068
y2 = 1.51575799342078E+10068

After one step of gradient descent with exact line search values are: 
x2 = 0.00000000000000
p2 = 0.00000000000000
y2 = 2.00000000000000
'''