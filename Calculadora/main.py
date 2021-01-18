from calculator_factories import make_root, make_display, make_label, make_buttons
from calculator_function import CalculatorFunction
from calculator_actions import calculate

# Derivar f(x) = (x**3 - 3*x + 2)*exp(-x/4) - 1.
def main():
    root = make_root() # Cria a tela da calculadora
    display = make_display(root, row=1, column=0, columnspan=12, sticky='news')
    display.grid_configure(pady=(0, 10))
    label = make_label(root, row=0, column=0, columnspan=12, sticky='news')
    buttons = make_buttons(root, starting_row=2)

    calculator_function = CalculatorFunction(root, label, display, buttons, calculate)
    calculator_function.start()


if __name__ == '__main__':
    main()