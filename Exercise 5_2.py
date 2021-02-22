# Script iterates towards min or max value of a given function 
# with a given step of 1
# starting x value of 10
# and imposed iteration quantities in number of 2 

import sympy
x = sympy.Symbol('x')

func = x**4
xx = 2

iterations = 2
func_der = sympy.diff(func)
y_init = func.subs(x, xx)

print(f"Starting values are: \ny = {y_init} \nf'(x) = {func_der.subs(x,xx)} \nx = {xx}")

for i in range(iterations):
    xx_der = func_der.subs(x, xx)
    xx = xx + ( - xx_der)
    y = func.subs(x,xx)
    print(f"\nIteration number {i+1}: \ny = {y} \nf'(x) = {func_der.subs(x,xx)} \nx = {xx}")

'''
# Output:

Starting values are: 
y = 16 
f'(x) = 32 
x = 2

Iteration number 1: 
y = 810000 
f'(x) = -108000 
x = -30

Iteration number 2: 
y = 135897793533936810000 
f'(x) = 5034650126292000 
x = 107970

'''
