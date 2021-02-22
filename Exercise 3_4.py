# calculating a function

func = x - 1

def f_prim(p, func = func):
    import sympy
    x = sympy.Symbol('x')
    return func.subs(x, p)


# Checking interval starting and ending point sign and doubling it if condition of opposite sings is not met

def bracket_sign_change(f_prim, a, b, k = 2):

    if a > b:
        a, b = b, a
        return (a,b)
    
    center, half_width = ( b + a ) / 2, ( b - a ) / 2 
    
    while f_prim(a) * f_prim(b) > 0:
        half_width *= k
        a = center - half_width
        b = center + half_width
        
    return (a,b)

# main function, aproximating root of x - 1

def bisection(f_prim, a, b, ϵ):
    
    if a > b:
        a, b = b, a
        return (a, b)
    
    ya, yb = f_prim(a), f_prim(b)
    
    if ya == 0:
        b = a
        return (a,b)
    
    if yb == 0:
        a = b
        return (a,b)
    
    while b - a > ϵ:
        print(f'{a, b}')
        x = (a + b) / 2
        y = f_prim(x)
        
        if y == 0:
            a, b = x, x
            
        elif y*ya >= 0:
            a = x
            
        else:
            b = x
        
        
    return (a,b)

# Executing Three Steps of a Bisection Method
a, b = 0 , 1000 # starting interval
func = x - 1 # function
ϵ = 150 #width interval tolerance
a, b = bracket_sign_change(f_prim, a, b)
a, b = bisection(f_prim, a, b, ϵ) # ϵ equals to 150 to excute 3 steps
a, b

### Three steps are:
#(0, 1000)
#	first
#(0, 500.0)
#	second
#(0, 250.0)
#	third
#(0, 125.0)
