from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x', real = True)
f = x**7 - 10*x**6 +42*x**5 + 128*x**4 - 800*x**3 + 1300*x**2 - 670*x

der1 = f.diff(x)
der2 = f.diff(x, 2)

extrema = [N(extrema) for extrema in (solve(der1, x))]
print("Extrema:",extrema)
maxima = []
for toCheck in extrema:
    if (der2.replace(x, toCheck) < 0):
        maxima.append(toCheck)
print("Maxima:", maxima)
for maximum in maxima:
    print("Maximum: (" + str(maximum) + '|' + str(f.replace(x, maximum))+ ")")

def f(x):
    return x**7 - 10*x**6 +42*x**5 + 128*x**4 - 800*x**3 + 1300*x**2 - 670*x

#plotting:
xList = np.linspace(-5,5, num = 10000)
yList = f(xList)
print(yList)
plt.figure(figsize = (10,5))
plt.plot(xList, yList, label = "f(x)")
for maximum in maxima:
    plt.plot(maximum,f(maximum),'ro', label = "maximum")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()