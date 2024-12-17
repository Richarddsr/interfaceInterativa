import tkinter as tk
from tkinter import messagebox

# Função simples para atualizar o texto de um label
def packz():
    # Modifica o texto do label "teste" para mostrar que o botão foi clicado
    # Isso demonstra como podemos alterar dinamicamente os widgets
    teste.config(text="Tá funfante")

# Função para criar uma interface usando o gerenciador de layout place()
def criar_interface_place():
    # Cria uma janela secundária (Toplevel) que é filha da janela principal
    # Isso permite criar interfaces adicionais sem fechar a janela original
    janela_place = tk.Toplevel(root)
    janela_place.title("Gerenciador place()")  # Define o título da janela
    janela_place.geometry("300x300")  # Define o tamanho da janela

    # Criando labels usando o gerenciador place()
    # place() permite posicionar widgets com coordenadas x e y precisas
    # Útil para layouts que precisam de posicionamento exato
    tk.Label(
        janela_place, 
        text="Texto 1 gerado com place",  # Texto do label
        font=('Arial', 10, 'bold'),  # Estilização da fonte
    ).place(x=50, y=50, width=200, height=30)  # Posicionamento preciso

    tk.Label(
        janela_place, 
        text="Texto 2 gerado com place",  
        font=('Arial', 10, 'bold')
    ).place(x=50, y=100, width=200, height=30)
    
    # Função interna para exibir uma mensagem de alerta
    # Demonstra o uso de messagebox para interações com o usuário
    def exibirPlace():
        # showwarning() exibe uma caixa de diálogo de aviso
        messagebox.showwarning("Alerta!!!!!!", "Tá funfante")

    # Criando botões usando place()
    # Cada botão tem um texto e uma ação (command) associada
    tk.Button(
        janela_place, 
        text="Testar",  # Texto do botão
        command=exibirPlace  # Ação ao clicar no botão
    ).place(x=50, y=200, width=100, height=40)

    tk.Button(
        janela_place, 
        text="Fechar",  # Texto do botão
        command=janela_place.destroy  # Fecha a janela atual
    ).place(x=160, y=200, width=100, height=40)

# Função para criar uma interface usando o gerenciador de layout grid()
def criar_interface_grid():
    # Cria uma nova janela secundária
    janela_grid = tk.Toplevel(root)
    janela_grid.title("Grid?!?!?!📐")  # Título divertido para a janela
    janela_grid.geometry("400x400")

    # Adiciona widgets usando o layout grid()
    # grid() organiza widgets em linhas e colunas, similar a uma planilha
    # Útil para layouts mais organizados e responsivos
    tk.Label(
        janela_grid, 
        text="Texto 1 gerado com grid", 
        font=('cardinal', 10, 'bold')
    ).grid(row=2, column=0, padx=50, pady=5, sticky='e')

    tk.Label(
        janela_grid, 
        text="Texto 2 gerado com grid", 
        font=('Arial', 10, 'bold')
    ).grid(row=3, column=0, padx=50, pady=5, sticky='e')

    # Adiciona botões usando grid layout
    tk.Button(
        janela_grid, 
        text="Testar", 
        command=mostrar_dados
    ).grid(row=4, column=0, columnspan=2, pady=10)

    tk.Button(
        janela_grid, 
        text="Fechar", 
        command=janela_grid.destroy
    ).grid(row=5, column=0, columnspan=2, pady=10)

# Função para mostrar dados
def mostrar_dados():
    # Exibe uma mensagem de informação
    messagebox.showinfo("Alerta⚠️⚠️⚠️⚠️", "Tá funfante")

# Janela principal
root = tk.Tk()
root.title("Interface interativa")
root.geometry("800x600")
root.configure(bg="white")

# Widgets da janela principal
label1 = tk.Label(root, text="Pack?!?!!? 😨", font=("Arial", 10), bg="white", fg="black")
label1.pack(pady=10, fill=tk.X)

tk.Button(root, text="Testar button com pack", command=packz).pack(padx=20, pady=20)

textin = tk.Label(root, text="Grid!?!?!?!😨", font=("Arial", 10), bg="white", fg="black")
textin.pack(padx=5, pady=5)

tk.Button(root, text="Abrir Grid Layout", command=criar_interface_grid).pack(padx=20, pady=20)

textin = tk.Label(root, text="P-Place!?!!?!?😰😱😱", font=("Arial", 10), bg="white", fg="black")
textin.pack(padx=5, pady=5)

tk.Button(root, text="Abrir Place Layout", command=criar_interface_place).pack(padx=20, pady=20)

# Label para teste de funcionalidade
teste = tk.Label(root, text="", font=("Arial", 10), bg="white", fg="black")
teste.pack(padx=20, pady=20)

# Executa o loop principal
root.mainloop()
import tkinter as tk
from tkinter import messagebox

# 🔄 Função simples para atualizar dinamicamente um label
def packz():
    # 🖌️ Modifica o texto do label, mostrando como widgets podem ser alterados
    teste.config(text="Tá funfante")

# 🪟 Função para criar uma interface usando o gerenciador de layout place()
def criar_interface_place():
    # 🆕 Cria uma janela secundária que é filha da janela principal
    # 🌈 Permite criar interfaces adicionais sem fechar a janela original
    janela_place = tk.Toplevel(root)
    janela_place.title("Gerenciador place()") # 🏷️ Define o título da janela
    janela_place.geometry("300x300")  # 📏 Define o tamanho da janela

    # 🏷️ Criando labels usando o gerenciador place()
    # 📍 place() permite posicionamento preciso de widgets
    # 🎯 Útil para layouts que precisam de coordenadas exatas
    tk.Label(
        janela_place, 
        text="Texto 1 gerado com place",  # 💬 Texto do label
        font=('Arial', 10, 'bold'),  # 🖋️ Estilização da fonte
    ).place(x=50, y=50, width=200, height=30)  # 📐 Posicionamento preciso

    tk.Label(
        janela_place, 
        text="Texto 2 gerado com place",  
        font=('Arial', 10, 'bold')
    ).place(x=50, y=100, width=200, height=30)
    
    # 🚨 Função interna para exibir uma mensagem de alerta
    # 📢 Demonstra interações com o usuário
    def exibirPlace():
        # ⚠️ showwarning() exibe uma caixa de diálogo de aviso
        messagebox.showwarning("Alerta!!!!!!", "Tá funfante")

    # 🔘 Criando botões usando place()
    # 🖱️ Cada botão tem texto e ação associada
    tk.Button(
        janela_place, 
        text="Testar",  # 🏷️ Texto do botão
        command=exibirPlace  # 🎬 Ação ao clicar no botão
    ).place(x=50, y=200, width=100, height=40)

    tk.Button(
        janela_place, 
        text="Fechar",  # 🚪 Texto do botão
        command=janela_place.destroy  # 🔒 Fecha a janela atual
    ).place(x=160, y=200, width=100, height=40)

# ... (resto do código permanece igual)import tkinter as tk
from tkinter import messagebox

# 🔄 Função simples para atualizar dinamicamente um label
def packz():
    # 🖌️ Modifica o texto do label, mostrando como widgets podem ser alterados
    teste.config(text="Tá funfante")

# 🪟 Função para criar uma interface usando o gerenciador de layout place()
def criar_interface_place():
    # 🆕 Cria uma janela secundária que é filha da janela principal
    # 🌈 Permite criar interfaces adicionais sem fechar a janela original
    janela_place = tk.Toplevel(root)
    janela_place.title("Gerenciador place()") # 🏷️ Define o título da janela
    janela_place.geometry("300x300")  # 📏 Define o tamanho da janela

    # 🏷️ Criando labels usando o gerenciador place()
    # 📍 place() permite posicionamento preciso de widgets
    # 🎯 Útil para layouts que precisam de coordenadas exatas
    tk.Label(
        janela_place, 
        text="Texto 1 gerado com place",  # 💬 Texto do label
        font=('Arial', 10, 'bold'),  # 🖋️ Estilização da fonte
    ).place(x=50, y=50, width=200, height=30)  # 📐 Posicionamento preciso

    tk.Label(
        janela_place, 
        text="Texto 2 gerado com place",  
        font=('Arial', 10, 'bold')
    ).place(x=50, y=100, width=200, height=30)
    
    # 🚨 Função interna para exibir uma mensagem de alerta
    # 📢 Demonstra interações com o usuário
    def exibirPlace():
        # ⚠️ showwarning() exibe uma caixa de diálogo de aviso
        messagebox.showwarning("Alerta!!!!!!", "Tá funfante")

    # 🔘 Criando botões usando place()
    # 🖱️ Cada botão tem texto e ação associada
    tk.Button(
        janela_place, 
        text="Testar",  # 🏷️ Texto do botão
        command=exibirPlace  # 🎬 Ação ao clicar no botão
    ).place(x=50, y=200, width=100, height=40)

    tk.Button(
        janela_place, 
        text="Fechar",  # 🚪 Texto do botão
        command=janela_place.destroy  # 🔒 Fecha a janela atual
    ).place(x=160, y=200, width=100, height=40)

# ... (resto do código permanece igual)