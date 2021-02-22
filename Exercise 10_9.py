# import sympy
import sympy 
from sympy import * 
x, a, b, x_t, x_s = sympy.symbols('x, a, b, x_t, x_s')

iterations = 5                               # iterations quantity for Newton's Method
ab = [1,10]                                  # constraint
func = sympy.sin( 4 / x )                    # function
e = 2.718281828459045

t_x = ( b + a ) / 2 + ( b - a ) / 2 * ( 2 * x_t / (1 + x_t ** 2))  # x with x^
s_x = a + (b - a) / (1 + sympy.exp(-x_s) )                             

func_t = func.subs(x, t_x).subs( { a : ab[0] , b : ab[1] } )
func_s = func.subs(x, s_x).subs( { a : ab[0] , b : ab[1] } )


#################### GOLDEN SECTION SEARCH ####################

def golden_section_search(f, x_name, a, b, n):         # funtcion searching for interval with the lowest value  in it
    φ = (1 + 5 ** 0.5 ) / 2                            # f - funtcion, x_name - name of a variable in f function
    ρ = φ - 1                                          # interval which should be searched [a, b] with n function evalutations
    d = ρ * b + (1 - ρ) * a
    yd = f.subs(x_name, d)
    
    for i in range(n):
        c = ρ * a + (1 - ρ) * b
        yc = f.subs(x_name, c)
        if yc < yd:
            b, d, yd = d, c, yc
        else:
            a, b = b, c

    if a < b:
        return (a, b)
    else: 
        return (b, a)

    
#################### NEWTON's METHOD for T-TRANSFORM ####################

f_t_prim = sympy.diff(func_t, x_t)                                     # df/dx
f_t_bis = sympy.diff(f_t_prim, x_t)                                    # df'/dx 

ab_t = golden_section_search(func_t, x_t, -1000, 1000, 100)            # Searching through interval [-1000, 1000] with 100 steps

# Newton's Method 

xx_t = ab_t[0]/2+ab_t[1]/2                                             # inintial x value - middle of interval provided by golden section search
yy_t = func_t.subs(x_t, xx_t)                                          # f(initial x) - initial y value
print('T-Transform Iterations: ')
print(f'{xx_t}, {yy_t}')

for i in range(iterations):                                            # iterating with Newton's Method to get min. 
    xx_t = float(xx_t - f_t_prim.subs(x_t, xx_t) / f_t_bis.subs(x_t, xx_t))
    yy_t = float(func_t.subs(x_t, xx_t))
    print(f'{xx_t}, {yy_t}')

    
#################### NEWTON's METHOD for SIGMOID TRANSFORM ####################

f_s_prim = sympy.diff(func_s, x_s)                                     # df/dx
f_s_bis = sympy.diff(f_s_prim, x_s)                                    # df'/dx 

ab_s = golden_section_search(func_s, x_s, -1000, 1000, 100)            # Searching through interval [-1000, 1000] with 100 steps

xx_s = ab_s[0]/2+ab_s[1]/2                                             # inintial x value - middle of interval provided by golden section search
yy_s = func_s.subs(x_s, xx_s)                                          # f(initial x) - initial y value

print('\nSigmoid Transform Iterations: ')
print(f'{xx_s}, {yy_s}')

for i in range(iterations):                                            # iterating with Newton's Method to get min. 
    xx_s = float((xx_s - f_s_prim.subs(x_s, xx_s) / f_s_bis.subs(x_s, xx_s)))    
    yy_s = float((func_s.subs(x_s, xx_s)))
    print(f'{xx_s}, {yy_s}')
   
x_result_t = t_x.subs( { x_t : xx_t, a : ab[0] , b : ab[1] } )
x_result_s = s_x.subs( { x_s : xx_s, a : ab[0] , b : ab[1] } )
y_result_t = func.subs(x, x_result_t) 
y_result_s = func.subs(x, x_result_s)

print(f'\nT-Transform converges with 2 steps, achieving local minimum at:')
print(f'(x_t, y_t) = ({xx_t}, {yy_t}) thus (x, y) = ({x_result_t}, {y_result_t})')
print(f"\nSigmoid Transform, regardless of iteration's accuracy, doesn't have a solution.")
print(f'Minimum can only be reached as x approches minus infinity: ')
print(f'[-∞ , {yy_s}] thus (x, y) = ({x_result_s}, {y_result_s})')

'''
#Output:

T-Transform Iterations: 
-0.9999999884337497, -0.756802495307926
-0.9999999999999999, -0.7568024953079282
-1.0, -0.7568024953079282
-1.0, -0.7568024953079282
-1.0, -0.7568024953079282
-1.0, -0.7568024953079282

Sigmoid Transform Iterations: 
-236.06797749978972, -0.756802495307928
-237.06797749978972, -0.7568024953079282
-238.06797749978972, -0.7568024953079282
-239.06797749978972, -0.7568024953079282
-240.06797749978972, -0.7568024953079282
-241.06797749978972, -0.7568024953079282

T-Transform converges with 2 steps, achieving global minimum at:
(x_t, y_t) = (-1.0, -0.7568024953079282) thus (x, y) = (1.00000000000000, -0.756802495307928)

Sigmoid Transform, regardless of iteration's accuracy, doesn't have a solution.
Global minimum can only be reached as x approches minus infinity: 
[-∞ , -0.7568024953079282] thus (x, y) = (1.00000000000000, -0.756802495307928)

'''