import sympy as sy
from sympy.interactive import init_printing
from sympy import *

x, y, z = sy.symbols('x y z')
equacao = '(x**3 - 3*x + 2)*exp(-x/4) - 1'
f = Lambda(x, equacao)
print(f)
print(integrate(f(x), x))
print(integrate(f(x), (x, -1, 1)))
