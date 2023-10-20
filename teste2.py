import tkinter as tk
from tkinter import ttk

# Crie a janela principal
janela_principal = tk.Tk()
janela_principal.title("Exemplo de TabView")

# Crie um widget Notebook para conter as guias
notebook = ttk.Notebook(janela_principal)

# Crie guias individuais
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Adicione guias ao notebook
notebook.add(tab1, text="Guia 1")
notebook.add(tab2, text="Guia 2")

# Adicione widgets aos tabs
label1 = tk.Label(tab1, text="Conteúdo da Guia 1")
label1.pack(padx=10, pady=10)

label2 = tk.Label(tab2, text="Conteúdo da Guia 2")
label2.pack(padx=10, pady=10)

# Empacote o notebook
notebook.pack(padx=10, pady=10)

# Inicie o loop principal
janela_principal.mainloop()
