from random import *
import tkinter as tk

# Funções de geração de senha
def gerador_str():
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    return choice(alfabeto)

def gerador_int():
    return randint(0, 9)

def gerador_special_str():
    caracteres_especiais = ['!', '°', '?', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '_', '/']
    return choice(caracteres_especiais)

def gerador_universal():
    sorteio = [gerador_int(), gerador_special_str(), gerador_str()]
    return str(choice(sorteio))

# Função para gerar nova senha e atualizar o campo de texto
def gerar_senha():
    nova_senha = ''
    for _ in range(24):  # Gerando 24 caracteres para a senha
        nova_senha += gerador_universal()
    senha_var.set(nova_senha)

# Configuração da interface gráfica
root = tk.Tk()
root.title('Gerador de Senhas')

# Frame para conter o botão e o campo de senha
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Variável de controle para a senha
senha_var = tk.StringVar()

# Campo de texto para exibir a senha
senha_entry = tk.Entry(frame, textvariable=senha_var, font=('Helvetica', 16), width=30)
senha_entry.pack(padx=10, pady=10)

# Botão para gerar nova senha
gerar_button = tk.Button(frame, text='Gerar Nova Senha', command=gerar_senha, font=('Helvetica', 12))
gerar_button.pack(padx=10, pady=10)

# Executar o loop principal da interface gráfica
root.mainloop()
