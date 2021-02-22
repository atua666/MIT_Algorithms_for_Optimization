import sympy as sp
x = sp.symbols('x')

### Defining Dominates Function - A method for checking whether x dominates x' ###
def dominates(y, y_prim):
    if all(y_ <= y_prim_ for y_, y_prim_ in zip(y, y_prim)) and any(y_ < y_prim_ for y_, y_prim_ in zip(y, y_prim)):
        return True
    else:
        return False

### Defining Naive Pareto Function - checking whether values are dominated or not, returns not dominated values ###
### A method for generating a Pareto frontier using randomly sampled design points xs and their multiobjective values ys.
### Both the Pareto optimal design points and their objective values are returned.

def naive_pareto(xs, ys):
    
    pareto_xs, pareto_ys = [], []
    
    for (x,y) in zip(xs,ys):        
        if not any(dominates(y_prim, y) for y_prim in ys):
            pareto_xs.append(x)
            pareto_ys.append(y)
    
    return (pareto_xs, pareto_ys)
   
### Solving task ###
# input
f_1 = - (x - 2) * sp.sin(x)
f_2 = - ((x + 3) ** 2) * sp.sin(x)
x_list = [-5, -3, -1, 1, 3, 5]
yy1 = []
yy2 = []

# calculating values vector for f1 and f2
for xx in x_list:
    yy1.append(float(f_1.subs(x, xx)))
    yy2.append(float(f_2.subs(x, xx)))

# usign Naive Pareto's function for generating Pareto Frontier
yy = list(zip(yy1, yy2))
result = naive_pareto(x_list, yy)
res_sort = result[1]
res_sort.sort()

##### PLOTTING Pareteo Frontier #####
import matplotlib.pyplot as plt

fig = plt.figure(1,figsize=(10,8))
ax1 = fig.add_subplot(111)

# annotating points and pareto frontier
for (a,b,c) in zip(x_list,yy1,yy2):
    plt.annotate('x = ' + str(a), (b+0.15,c), color='black', fontsize='large', fontweight='bold')
plt.annotate('Pareto Frontier', (-2.5,-5), color='red', fontsize='large', fontweight='bold')

# scattering all points obtained from (y1, y2)
ax1.scatter(yy1, yy2, color='blue')

# figure details
plt.suptitle('Pareto Frontier', fontsize='large', fontweight='bold')
plt.ylabel('y1')
plt.xlabel('y2')

# ploting pareto frontier
ax1.plot([d[0] for d in res_sort], [d[1] for d in res_sort], color='red')
plt.show()

'''
#Output:
attached as an image
'''