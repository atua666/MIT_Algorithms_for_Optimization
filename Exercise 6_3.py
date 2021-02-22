import sympy
from sympy import solve
from sympy.matrices import Matrix, Inverse
from sympy.abc import x, y, a

X1 = Matrix([1, 1])
X = Matrix([x, y])                        # Creating variables matrix X = [x, y]
H = Matrix([[1,0],[0,1000]])              # Creating Hessian Matrix

FUNC = 0.5 * X.T * H * X                  # Function provided in the exercise description


#################### NEWTON'S METHOD ####################

F_PRIM = Matrix([0, 0])                   # Setting up empty matrix for X_PRIM
F_PRIM[0] = FUNC.diff(X[0])               # deriving FUNC with respect to x and y separatelly   
F_PRIM[1] = FUNC.diff(X[1])               # F_PRIM = [[1.0*x], [1000.0*y]] = H * X

F_BIS = Matrix([[0, 0], [0, 0]])          # Setting up empty matrix for X_BIS
F_BIS[0] = F_PRIM[0].diff(X[0])           # deriving F_PRIM with respect to x and y separatelly  
F_BIS[1] = F_PRIM[1].diff(X[0])
F_BIS[2] = F_PRIM[0].diff(X[1])
F_BIS[3] = F_PRIM[1].diff(X[1])           # F_BIS = [[1,0],[0,1000]] = H

X2 = X - Inverse(F_BIS) * F_PRIM          # X2 = [0, 0], cnvergence in one step

print("Newton's Method")
print(f"  Newton's Method converges in one step, X2 = {list(X2)}\n")


#################### GRADIENT DESCENT ####################

X2_gd = X1 - F_PRIM.subs( { X[0] : X1[0] , X[1] : X1[1] } )
X3_gd = X2_gd - F_PRIM.subs( { X[0] : X2_gd[0] , X[1] : X2_gd[1] } )
print("Gradient Descent Method")
print(f"  After first step of Gradient Descent Method X2 = {list(X2_gd)}")
print(f"  After second step of Gradient Descent Method X3 = {list(X3_gd)}")
print("  Gradient Descent Method Diverges.\n")


#################### CONJUGATE DESCENT ####################

### First Step ###
# starting with a direction of a steepest descent d1 = - df (X1):
D1 = - F_PRIM.subs( { X[0] : X1[0] , X[1] : X1[1] } )
# substituting x with X2_cd = X1 + a * D1 in f(x):
FUNC_a1 = FUNC.subs( { X[0] : X1[0] + a * D1[0] , X[1] : X1[1] + a * D1[1] } )
# calculating df/da:
FUNC_a1_da = sympy.diff(FUNC_a1, a) 
# solving FUNC_a1_da for alpha:
a1 = solve(FUNC_a1_da, a) 
# calculating x2 with D1, a1 and x1
X2_cd = X1 + a1[a] * D1            # X2_cd = [0.998999999001000, -9.98999999168859e-7]

### Second Step ###
# starting with a direction of a steepest descent d1 = - df (X1):
D2 = - F_PRIM.subs( { X[0] : X2_cd[0] , X[1] : X2_cd[1] } )
# substituting X with X3_cd = X2_cd + a * D2 in f(x):
FUNC_a2 = FUNC.subs( { X[0] : X2_cd[0] + a * D2[0] , X[1] : X2_cd[1] + a * D2[1] } )
# calculating df/da:
FUNC_a2_da = sympy.diff(FUNC_a2, a)
# solving FUNC_a2_da for alpha:
a2 = solve(FUNC_a2_da, a) 
# calculating X3_cd with D2, a2 and X2_cd
X3_cd = X2_cd + a2[a] * D2                      # X3_cd = [0.000997003995341639, 0.000997003995174181]

print("Conjugate Descent Method")
print(f"  After first step of Conjugate Descent Method X2 = {list(X2_cd)}")
print(f"  After second step of conjugate Descent Method X3 = {list(X3_cd)}")
print("  Conjugate Descent converges to minimum in second step.\n")

'''

# Output:

Newton's Method
  Newton's Method converges in one step, X2 = [0, 0]

Gradient Descent Method
  After first step of Gradient Descent Method X2 = [0, -999.000000000000]
  After second step of Gradient Descent Method X3 = [0, 998001.000000000]
  Gradient Descent Method Diverges.

Conjugate Descent Method
  After first step of Conjugate Descent Method X2 = [0.998999999001000, -9.98999999168859e-7]
  After second step of conjugate Descent Method X3 = [0.000997003995341639, 0.000997003995174181]
  Conjugate Descent converges to minimum in second step.

'''