import re
import math
import sympy as sy
from sympy import *
from sympy.interactive import init_printing
init_printing(pretty_print=True)

def calculate(equation: str) -> str:
    print("Equação: ", equation)

    x, y, z = sy.symbols('x y z')

    if 'Limit x->' in equation:
        f = Lambda(x, equation[14:-1])
        successfully_solved_equation = limit(f(x), x, int(equation[9]), str(equation[10]))

    if 'Derivar' in equation:
        if "f'(" in equation:
            f = Lambda(x, equation[16:-1])
            f1 = Lambda(x, diff(f(x),x))
            successfully_solved_equation = f1(int(equation[11:12]))
        elif "f(" in equation:
            f = Lambda(x, equation[15:-1])
            successfully_solved_equation = sy.diff(f(x), x)

    if 'Integrar' in equation:
        if "f(x) (" in equation:
            f = Lambda(x, equation[25:-1])
            print("f: ", f)
            successfully_solved_equation = integrate(f(x), (x, equation[15:17], equation[18:20]))
        elif "f(x) =" in equation:
            f = Lambda(x, equation[16:-1])
            successfully_solved_equation = integrate(f(x), x)
    
    print("Resultado: ", successfully_solved_equation)
    return str(successfully_solved_equation)
