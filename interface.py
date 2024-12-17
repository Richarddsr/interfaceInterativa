import tkinter as tk
from tkinter import messagebox

def packz():
    # Atualiza o texto do label "teste" para indicar que o botão foi clicado
    teste.config(text="Tá funfante")

def criar_interface_place():
    # Cria uma nova janela secundária
    janela_place = tk.Toplevel(root)
    janela_place.title("Gerenciador place()")
    janela_place.geometry("300x300")

    # Adiciona labels usando o gerenciador place()
    tk.Label(
        janela_place, 
        text="Texto 1 gerado com place", 
        font=('Arial', 10, 'bold'),
    ).place(x=50, y=50, width=200, height=30)

    tk.Label(
        janela_place, 
        text="Texto 2 gerado com place",  
        font=('Arial', 10, 'bold')
    ).place(x=50, y=100, width=200, height=30)
    
    def exibirPlace():
        # Exibe uma mensagem de alerta
        messagebox.showwarning("Alerta!!!!!!", "Tá funfante")

    # Adiciona botões usando o gerenciador place()
    tk.Button(
        janela_place, 
        text="Testar", 
        command=exibirPlace
    ).place(x=50, y=200, width=100, height=40)

    tk.Button(
        janela_place, 
        text="Fechar", 
        command=janela_place.destroy
    ).place(x=160, y=200, width=100, height=40)

def criar_interface_grid():
    # Cria uma nova janela secundária
    janela_grid = tk.Toplevel(root)
    janela_grid.title("Grid?!?!?!📐")
    janela_grid.geometry("400x400")

    # Adiciona widgets usando o layout grid()
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
