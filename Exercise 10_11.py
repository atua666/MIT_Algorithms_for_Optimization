# import sympy
import sympy 
from sympy import * 
x_1, x_2, x_3 = sympy.symbols('x_1, x_2, x_3')

func_constr = x_1 ** 3 + x_2 ** 2 + x_3
constraint = x_1 + 2 * x_2 + 3 * x_3 - 6
x1_constr = solve(constraint, x_1)
x2_constr = solve(constraint, x_2)
x3_constr = solve(constraint, x_3)

func_unconstr_x1 = func_constr.subs(x_1, x1_constr[0])
func_unconstr_x2 = func_constr.subs(x_2, x2_constr[0])
func_unconstr_x3 = func_constr.subs(x_3, x3_constr[0])

print("In order to make this function unconstrained, constraining equation need to be solved for one of it's variables:") 
print(f'x_1 = {x1_constr}')
print(f'x_2 = {x2_constr}')
print(f'x_3 = {x3_constr}')
print('\nAnd than substituted in the main function. This way we get unconstrained function with only two variables:')
print(f'Unconstrained function, x_1 substituted: {func_unconstr_x1}')
print(f'Unconstrained function, x_2 substituted: {func_unconstr_x2}')
print(f'Unconstrained function, x_3 substituted: {func_unconstr_x3}')


'''
#Output:

In order to make this function unconstrained, constraining equation need to be solved for one of it's variables:
x_1 = [-2*x_2 - 3*x_3 + 6]
x_2 = [-x_1/2 - 3*x_3/2 + 3]
x_3 = [-x_1/3 - 2*x_2/3 + 2]

And than substituted in the main function. This way we get unconstrained function with only two variables:
Unconstrained function, x_1 substituted: x_2**2 + x_3 + (-2*x_2 - 3*x_3 + 6)**3
Unconstrained function, x_2 substituted: x_1**3 + x_3 + (-x_1/2 - 3*x_3/2 + 3)**2
Unconstrained function, x_3 substituted: x_1**3 - x_1/3 + x_2**2 - 2*x_2/3 + 2

'''