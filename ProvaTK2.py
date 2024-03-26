#tela de login com restriçoes de email e senha
#email deve conter caracter @
#senha deve ser maior que 6 digitos

import tkinter as tk
from tkinter import messagebox

def verificar_login(event=None):
    email = entry_email.get()
    senha = entry_senha.get()

    # Verificar se o e-mail possui "@" e se a senha tem mais de 6 caracteres
    if "@" in email and len(senha) > 6:
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "E-mail ou senha incorretos")


janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry('200x100')


label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

entry_email = tk.Entry(janela)
entry_email.grid(row=0, column=1, padx=5, pady=5)

label_senha = tk.Label(janela, text="Senha:")
label_senha.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

entry_senha = tk.Entry(janela, show="*")
entry_senha.grid(row=1, column=1, padx=5, pady=5)


botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.grid(row=2, columnspan=2, padx=5, pady=5)
janela.bind('<Return>',verificar_login)

janela.mainloop()
