import customtkinter
import customtkinter as ctk
import tkinter as tk
import tkinter
import MySQLdb as mdb
from tkinter import messagebox
from PIL import Image
import mysql.connector
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Configuração da janela principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela = ctk.CTk()
janela.geometry("600x400")
janela.title("DreamCORP")
janela.iconbitmap("D-Logo.ico")
janela.resizable(width=False, height=False)

# Variável global para a janela principal

janela_principal = None
entry_nome = None  # variáveis globais
entry_senha = None
entry_tipo_user = None
entry_tipo_adm = None
option_Var = None

# Função de login de usuário
def login_scc():
    global entry_nome
    global entry_senha
    global entry_tipo_user

    usuario = entry_nome.get()
    senha = entry_senha.get()

    conexao = mdb.connect(host="localhost", user=usuario, password=senha, db="comercio")
    cursor = conexao.cursor()

    # Validação do usuario correto
    try:
        cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND senha=%s", (usuario, senha))
        resultado = cursor.fetchone()

        if resultado:
            janela_principalpcp()

        else:
            messagebox.showinfo("Atenção!", "Usuário ou senha incorreto!")
    except mdb.OperationalError as e:
        messagebox.showerror("Erro de Conexão", f"Erro na conexão ao MySQL: {e}")
    finally:
        if conexao:
            conexao.close()

# Janela pós login
def janela_principalpcp():
    global janela_principal
    if janela:
        janela.withdraw()
    janela_principal = ctk.CTk()
    janela_principal.geometry("600x400")
    janela_principal.iconbitmap("D-Logo.ico")
    janela_principal.title("DreamCO Systems 2.0")
    janela_principal.resizable(width=False, height=False)

    frame_lateral = tk.Frame(janela_principal, width=155, height=400, bg="#212020")
    frame_lateral.place(x=0, y=0)

    optionmenu = ctk.CTkOptionMenu(janela_principal,
                                   values=["Mercearia", "Laticinios", "Limpeza", "Higiene", "Bebidas", "Papelaria",
                                           "Confeitaria"],
                                   width=155,
                                   height=18,
                                   font=("Roboto", 12),
                                   corner_radius=7,
                                   dropdown_font=("Roboto", 12))
    optionmenu.place(x=350, y=450)

    button = ctk.CTkButton(janela_principal,
                           text="Atualizar Estoque",
                           command=lambda: atualizar_estoque(textbox, optionmenu),
                           width=100,
                           height=35,
                           font=("Roboto", 15),
                           fg_color="#212020")
    button.place(x=600, y=550)

    # OptionMenu 1
    botao_mostrar = ctk.CTkButton(janela_principal,
                                  text="Listar estoque",
                                  width=150,
                                  height=15,
                                  font=("Roboto", 13),
                                  fg_color="transparent",
                                  command=lambda: option1(textbox, textbox_visible, button, button_visible, optionmenu, optionmenu_visible))
    botao_mostrar.place(x=3, y=45)

    textbox = ctk.CTkTextbox(janela_principal, width=450, height=250, corner_radius=1) # Widht = largura / height = altura

    # OptionMenu 2
    option_menu2 = ctk.CTkButton(master=janela_principal,
                                 text="Option 2",
                                 width=150,
                                 height=15,
                                 font=("Roboto", 13),
                                 fg_color="transparent",
                                 command=option2)
    option_menu2.place(x=3, y=75) # X > numero maior para esquerda, numero menor para direita / Y > numero menor para cima, numero maior para baixo

    # OptionMenu 3
    option_menu3 = ctk.CTkButton(master=janela_principal,
                                 text="Option 3",
                                 width=150,
                                 height=15,
                                 font=("Roboto", 13),
                                 fg_color="transparent",
                                 command=option2)
    option_menu3.place(x=3, y=105)

# OptionMenu 4
    option_menu4 = ctk.CTkButton(master=janela_principal,
                                 text="Option 4",
                                 width=150,
                                 height=15,
                                 font=("Roboto", 13),
                                 fg_color="transparent",
                                 command=option2)
    option_menu4.place(x=3, y=135)  # X > numero maior para esquerda, numero menor para direita / Y > numero menor para cima, numero maior para baixo

# Botão return
    button_returnlg = ctk.CTkButton(master=janela_principal,
                                    text="Voltar",
                                    width=95,
                                    height=15,
                                    font=("Roboto", 13),
                                    fg_color="transparent",
                                    command=return_janelapcp)
    button_returnlg.place(x=32, y=375)


    janela_principal.mainloop()

def option1(textbox, textbox_visible, button, button_visible, optionmenu, optionmenu_visible):
    if textbox_visible.get():
        textbox.place_forget()
        button.place_forget()
        optionmenu.place_forget()
    else:
        textbox.place(x=160, y=0)
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        selected_option = optionmenu.get()
        resultado = query(selected_option)
        textbox.insert("1.0", resultado)
        textbox.configure(state="disabled")

        button.place(x=160, y=300)
        optionmenu.place(x=160, y=250)

    optionmenu_visible.set(not optionmenu_visible.get())
    button_visible.set(not button_visible.get())
    textbox_visible.set(not textbox_visible.get())

textbox_visible = tk.BooleanVar()
textbox_visible.set(False)

button_visible = tk.BooleanVar()
button_visible.set(False)

optionmenu_visible = tk.BooleanVar()
optionmenu_visible.set(False)


def query(selected_option):
    try:
        conexao = mdb.connect(host="localhost", user="root", password="teste", database="comercio")
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM estoque WHERE setor = %s', (selected_option,))
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
            return resultado
        else:
            return "Nenhum produto encontrado."
    except mdb.Error as e:
        return f"Erro na consulta: {e}"
    finally:
        if conexao:
            conexao.close()

def on_option_select(selected_option):
    resultado = query(selected_option)
    return resultado

def atualizar_estoque(textbox, optionmenu):
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    selected_option = optionmenu.get()
    resultado = query(selected_option)
    textbox.insert("1.0", resultado)
    textbox.configure(state="disabled")


def hide_button1(botao, button_visible):
    if button_visible.get():
        botao.place_forget()
    else:
        botao.place(x=0, y=300)
        botao.configure(state="disabled")
    button_visible.set(not textbox_visible.get())
button_visible = tk.BooleanVar()
button_visible.set(False)


def hide_textbox(textbox):
    textbox.pack_forget()

def option2():
    # Criar Função de insert de registro
    popup2 = ctk.CTk()
    popup2.geometry("300x150")
    popup2.title("Janela Pop-up 2")

    popup2.mainloop()

def option3():
    # Criar função de alteração de registro
    popup3 = ctk.CTk()
    popup3.geometry("300x150")
    popup3.title("Janela Pop-up 3")

    popup3.mainloop()


def option5():
    # Criar Função de exportação de registros como arquivo PDF / CSV
    popup4 = ctk.CTk()
    popup4.geometry("300x150")
    popup4.title("Janela Pop-up 4")

    popup4.mainloop()

def option6():
    # Criar Função para atualização de registro
    popup4 = ctk.CTk()
    popup4.geometry("300x150")
    popup4.title("Janela Pop-up 4")

    popup4.mainloop()

# Função de cadastro de usuário
def cadastro():
    # Limpa a tela principal
    for widget in janela.winfo_children():
        widget.destroy()

    global entry_nome
    global entry_senha
    global entry_tipo_user
    global entry_tipo_adm

    # Janela de cadastro
    label_cadastro = ctk.CTkLabel(janela, text="Crie sua conta", font=("Roboto", 20))
    label_cadastro.place(relx=0.48, rely=0.05, anchor=tkinter.CENTER)


    # Campo de entrada para usuário
    entry_nome = ctk.CTkEntry(janela, width=215, placeholder_text="user", height=20, border_width=2, corner_radius=7)
    entry_nome.place(x=180, y=65)

    # Campo de entrada para senha
    entry_senha = ctk.CTkEntry(janela, width=215, placeholder_text="password", height=20, border_width=2, corner_radius=7, show="*")
    entry_senha.place(x=180, y=105)

    # Campo digitar novamente a senha
    entry_senhanv = ctk.CTkEntry(janela, width=215, placeholder_text="password", height=20, border_width=2, corner_radius=7, show="*")
    entry_senhanv.place(x=180, y=140)

    # Menu suspenso para escolher o tipo de usuário
    label_tipo_user = ctk.CTkLabel(janela, text="Tipo de usuário: ")
    label_tipo_user.place(x=180, y=180)

    # Checkbox adm
    check_var = customtkinter.StringVar(value="off")
    entry_tipo_adm = ctk.CTkCheckBox(janela,
                                      text="Admin",
                                      command=check_var,
                                      variable=check_var, onvalue="on", offvalue="off",
                                      checkbox_width=18,
                                      checkbox_height=18)
    entry_tipo_adm.place(x=180, y=215)

    # Checkbox user
    check_var2 = customtkinter.StringVar(value="off")
    entry_tipo_user = ctk.CTkCheckBox(janela,
                                      text="User",
                                      command=check_usr,
                                      variable=check_var2, onvalue="on", offvalue="off",
                                      checkbox_width=18,
                                      checkbox_height=18)
    entry_tipo_user.place(x=265, y=215)

    # Botão de cadastro
    button = ctk.CTkButton(janela,
                           text="Cadastrar",
                           width=160,
                           height=40,
                           command=realizar_cadastro)
    button.place(x=220, y=320)

    # Botão de retorno
    button_return = ctk.CTkButton(master=janela,
                                     text="voltar",
                                     width=95,
                                     height=15,
                                     font=("Roboto", 13),
                                     fg_color="transparent",
                                     command=return_janela)
    button_return.place(x=254, y=365)


def  check_adm():
    adm = entry_tipo_adm()

def check_usr():
    user = entry_tipo_user()


# Função para realizar o cadastro
def realizar_cadastro():
    nome = entry_nome.get()
    senha = entry_senha.get()
    tipo_user = entry_tipo_user.get()

    conexao = mdb.connect(host="localhost", user="root", password="teste", db="comercio")
    cursor = conexao.cursor()

    try:
        # Criar o usuário
        cursor.execute(f"CREATE USER '{nome}'@'localhost' IDENTIFIED BY %s", (senha,))
        # Conceder privilégios
        cursor.execute("GRANT ALL PRIVILEGES ON *.* TO %s@'localhost'", (nome,))
        # Inserir na tabela usuarios
        cursor.execute("INSERT INTO usuarios (usuario, senha, tipo_user) VALUES (%s, %s, %s)", (nome, senha, tipo_user))
        # Atualizar privilégios
        cursor.execute("FLUSH PRIVILEGES")

        conexao.commit()
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
    except mdb.Error as e:
        conexao.rollback()
        messagebox.showerror("Erro de Cadastro", f"Erro ao cadastrar: {e}")
    finally:
        if conexao:
            conexao.close()


# Função para retornar à janela principal
def return_janela():
    for widget in janela.winfo_children():
        widget.destroy()
    criar_widgets()

# Função para retornar a janela principal ( Pós login)
def return_janelapcp():
    global janela_principal
    if janela_principal:
        janela_principal.destroy()  # Destroi a janela secundária
        if janela:
            janela.deiconify()

# Função para criar a interface inicial
def criar_widgets():

    global entry_nome   # Declare a variável como global para todo o código
    global entry_senha
    global entry_tipo_user

    frame_login = tk.Frame(janela, width=300, height=250, bg="#212020")  # Define o fundo do frame como "blue"
    frame_login.place(x=138, y=70)

    # Texto superior da janela
    labelusr = ctk.CTkLabel(master=janela,
                            text="Faça seu login",
                            font=("Roboto", 20))
    labelusr.place(relx=0.48, rely=0.05, anchor=tkinter.CENTER)

    # Campo de entrada de usuário
    entry_nome = ctk.CTkEntry(master=janela,
                              placeholder_text="user",
                              width=215,
                              height=20,
                              border_width=2,
                              corner_radius=7)
    entry_nome.place(x=180, y=120)

    # Campo de entrada de senha
    entry_senha = ctk.CTkEntry(master=janela,
                               placeholder_text="password",
                               width=215,
                               height=20,
                               border_width=2,
                               corner_radius=7,
                               show="*")
    entry_senha.place(x=180, y=160)

    # Botão de login
    button = ctk.CTkButton(master=janela,
                           text="Login",
                           width=120,
                           height=20,
                           command=login_scc)
    button.place(x=225, y=218)

    # Botão de cadastro
    button_cadastro = ctk.CTkButton(master=janela,
                                     text="Usuário novo? Cadastre-se!",
                                     width=120,
                                     height=20,
                                     font=("Roboto", 15),
                                     fg_color="transparent",
                                     command=cadastro)
    button_cadastro.place(x=185, y=355)

    img = ctk.CTkImage(dark_image=Image.open("Minorias.sh.png"), size=(138, 138))
    label_img = ctk.CTkLabel(master=janela, text=None, image=img)
    label_img.place(x=0, y=270)

criar_widgets()

janela.mainloop()
janela_principal.mainloop()