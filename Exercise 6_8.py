# importing sympy functions
import sympy
from sympy.matrices import Matrix, Inverse
x1, x2 = sympy.symbols('x1, x2')

XX1 = Matrix([0, 0])	                                             # Sarting point at the origin XX1= [0,0]
FUNC =  (x1 + 1) ** 2 + (x2 + 3) ** 2 + 4            				 # Function
F_PRIM = Matrix([[sympy.diff(FUNC, x1)] , [sympy.diff(FUNC, x2)]]) 	 # Derivating FUNC with respect to x1 and than x2
H = Matrix([[sympy.diff(F_PRIM[0], x1), sympy.diff(F_PRIM[1], x1)], [sympy.diff(F_PRIM[0], x2), sympy.diff(F_PRIM[1], x2)]])     # Derivating F_PRIM with respect to x1 and than x2, becuase of quadratic funstion Hessian is obtained


#################### NEWTON'S METHOD ####################
XX2 = XX1 - Inverse(H) * F_PRIM.subs( { x1 : XX1[0] , x2 : XX1[0]} ) # XX2 = [-1, -3]

print(f"Function is quadratic therefore converges in one step. Hessian = {H} is positive therefore X2 = {XX2} is function's minimum")


'''
#Output:
Function is quadratic therefore converges in one step. Hessian = [2, 0, 0, 2] is positive therefore X2 = [-1, -3] is function's minimum.
'''