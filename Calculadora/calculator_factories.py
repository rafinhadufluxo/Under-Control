import tkinter as tk
from typing import List

# Cria a janela principal, dando nome e definindo tamanho
def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora Plus Plus')
    root.config(padx=5, pady=5, background='#fff')
    return root

# Cria a Label com o texto "Sem conta ainda" no canto superior direito
def make_label(root, **grid_options) -> tk.Label:
    label = tk.Label(
        root, text='Sem conta ainda',
        anchor='e', justify='right', background='#fff'
    )
    label.grid(**grid_options)
    return label

# Cria o display onde será mostrado os números digitados e o resultado das operações
def make_display(root, **grid_options) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(**grid_options)
    display.config(
        font=('Helvetica', 25, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', _display_control_a)
    return display

# Função criada para executar um evento clicado
def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

# Cria e configura os botões
def make_button(root, text, **grid_options) -> tk.Button:
    btn = tk.Button(root, text=text)
    btn.grid(**grid_options)
    btn.config(
        font=('Helvetica', 15, 'normal'),
        pady=20, background='#f1f2f3', bd=0,
        cursor='hand2', highlightthickness=0,
        highlightcolor='#ccc', activebackground='#ccc',
        highlightbackground='#ccc'
    )
    return btn

# Quais botões terá percorrendo a lista de símbolos
def make_buttons(root, starting_row) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['   7   ', '   8   ', '   9   ', '   +   ', 'Limit x->n+ = .', 'C'],
        ['   4   ', '   5   ', '   6   ', '   -   ', 'Derivar f(x) = .', "Derivar f'(n) = ."],
        ['   1   ', '   2   ', '   3   ', '   *   ', 'Integrar f(x) = .', "Integrar f(x) (-n,+n') = ."],
        ['   0   ', '   (   ', '   )   ', '   /   ', '   **   ', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=starting_row):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = make_button(
                root, text=col_value,
                row=row, column=col_index, sticky='news', padx=8, pady=8,
            )
            button_row.append(btn)
        buttons.append(button_row)
    
    btn = make_button(
        root, text='DICAS (use o da direita da igualdade):       |n| = abs(n)       e^n = exp(n)       cos()       sin()',
        row=row+1, column=0, sticky='news', padx=8, pady=8, columnspan=7
    )
    button_row.append(btn)
    buttons.append(button_row)

    return buttons