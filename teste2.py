import mysql.connector as mdb
import tkinter as tk

def on_option_select(selected_option):
    # Aqui você pode adicionar a lógica para atualizar o estoque com base na opção selecionada
    print(f"Opção selecionada: {selected_option}")

def consultar_estoque(selected_option, textbox):
    try:
        conexao = mdb.connect(host="localhost", user="root", password="teste", db="comercio")
        cursor = conexao.cursor()

        cursor.execute('SELECT DISTINCT * FROM estoque WHERE setor = %s', (selected_option,))
        estoque = cursor.fetchall()

        if len(estoque) > 0:
            resultado = ""
            for produto in estoque:
                resultado += f'Código do produto: {produto[0]}\n'
                resultado += f'Produto: {produto[1]}\n'
                resultado += f'Setor: {produto[2]}\n'
                resultado += f'Quantidade em estoque: {produto[3]}\n'
                resultado += f'Preço de venda: {produto[4]}\n'
                resultado += f'Data de entrada: {produto[5]}\n\n'
            textbox.configure(state="normal")
            textbox.delete("1.0", "end")
            textbox.insert("1.0", resultado)
            textbox.configure(state="disabled")
        else:
            textbox.configure(state="normal")
            textbox.delete("1.0", "end")
            textbox.insert("1.0", "Nenhum produto encontrado.")
            textbox.configure(state="disabled")
    except mdb.Error as e:
        # Aqui, você pode lidar com exceções de banco de dados, como log de erros ou notificações
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("1.0", f"Erro na consulta: {e}")
        textbox.configure(state="disabled")
    finally:
        if conexao:
            conexao.close()

def toggle_elements():
    textbox_visible.set(not textbox_visible.get())
    button_visible.set(not button_visible.get())
    optionmenu_visible.set(not optionmenu_visible.get())

app = tk.Tk()
app.geometry("400x400")

textbox = tk.Text(app, height=10, width=40)
textbox.place(x=160, y=0)
textbox.configure(state="disabled")

optionmenu = tk.OptionMenu(app, "Opção 1", "Opção 2", "Opção 3")
optionmenu.place(x=160, y=250)

button = tk.Button(app, text="Consultar", command=lambda: consultar_estoque(optionmenu.get(), textbox))
button.place(x=160, y=300)

toggle_button = tk.Button(app, text="Alternar Elementos", command=toggle_elements)
toggle_button.place(x=160, y=350)

textbox_visible = tk.BooleanVar()
textbox_visible.set(False)

button_visible = tk.BooleanVar()
button_visible.set(False)

optionmenu_visible = tk.BooleanVar()
optionmenu_visible.set(False)

app.mainloop()
