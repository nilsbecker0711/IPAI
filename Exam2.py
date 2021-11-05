from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def func (x, f):
    return f
def plotGraph(f1, f2 = None):
    xList = np.linspace(-10,10, num = 10000)
    yList1 = func(xList, f1)
    yList2 = func(xList, f2)
    plt.figure(figsize = (20,5))
    plt.plot(xList, yList1, label = "f'(x)")
    plt.plot(xList, yList2, label = "f(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

selection = 0
while selection not in [1,2,3]:
    selection = int(input("1 for computational problem\n2 for equation solving\n3 for finding integrals solving\n"))

problem = input("Enter the problem: ").replace("^", "**").replace(" ","")
x = symbols('x', real = True)

result = ""
if selection == 1:
    result = parse_expr(problem)
    print(problem, "=" , result)

elif selection == 2:
    problem = problem.split("=")
    eq = parse_expr(problem[0], locals()) - parse_expr(problem[1], locals())
    print(eq)
    result = solve(eq, x)
    print("x in", result)
    plot(result[0])
   

else:
    ex = parse_expr(problem, locals())
    result = integrate(ex,x)  
    print("f'(x) =", problem, ', f(x) =', result, "+ C")
    graph = plot(result)
    
