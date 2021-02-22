import sympy

def penalty_method(f, p, k_max, x_variable = 'x', ρ=1, γ=2):

    for k in range(1 , k_max):
        (xx, yy) = newton_method(f, x_variable)
        ρ *= γ
        if p.solve(x, xx) == 0:
            return xx
    return xx

def newton_method(f, k_max, x_variable = 'x', x0=0, y0=0):

    x_variable = sympy.symbols('x')
    
    f_prim = sympy.diff(f, x_variable)                                     # df/dx
    f_bis = sympy.diff(f_prim, x_variable)                                 # df'/dx 
    xx = x0

    for i in range(iterations):                                            # iterating with Newton's Method to get min. 
        xx = float(xx - f_prim.subs(x, xx) / f_bis.subs(x, xx))
        yy = float(f.subs(x, xx))
    
    return (xx, yy)

xx = 0
yy = 0

x = sympy.symbols('x')

p_count = lambda p_count, xx: p_count + 1 if abs(xx) > 2
p_quadratic = q * max( abs(x) - 2, 0) ** 2

f_count = 1 - x ** 2 + q * p_count
f_quadratic = 1 - x ** 2 + q * p_quadratic

xx_count = penalty_method(f_count, p_count, k_max = 10)
xx_quadratic = penalty_method(f_quadratic, p, k_max = 10)


''' 

Count Penalty: 

f(x) = 1 - x ** 2 + ro * p_count(x)
p_count(x) = (|x| > 2)

Book quote: "This penalty will preserve the problem solution for large values of ρ, but it
introduces a sharp discontinuity. Points not inside the feasible set lack gradient
information to guide the search towards feasibility."

In this particular case, if we initiate an algorithm outside of given constraint,
algorithm will go towards -∞ or +∞ as 1 - x ** 2 is minimized there.



Quadratic Penalty:

f(x) = 1 - x ** 2 + ro * p_quadratic(x)
p_quadratic(x) = max(|x|- 2, 0) ** 2

Book qoute: "Quadratic penalties close to the constraint boundary are very small, and may
require ρ to approach infinity before the solution ceases to violate the constraints."

In this particular case, partial derivatives are proportional to penalties, therefore partial derivatives
are large where penalties are large, which may cause problems for optimizing methods.
On the other hand, if we have small penalties, penalized interval may be not suficiently penalized,
which could lead to obtainng wrong solution.

'''