import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    nome = entrada_nome.get()
    messagebox.showinfo("Saudação", f"Ola , {nome} bem vindo!")

janela = tk.Tk()

janela.title("Ola Tkinter")
janela.geometry("300x150")

rotulo_nome = tk.Label(janela, text="Digite seu nome: ")
rotulo_nome.pack(pady=5)

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem)
botao.pack(pady=20)

janela.mainloop()