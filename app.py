import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        valor_inicial = float(entry_valor.get())
        
        custo1 = valor_inicial * 0.80
        custo2 = custo1 * 0.80
        custo3 = custo2 * 0.80
        
        diferenca = valor_inicial - custo3
        
        label_custo1.config(text=f"Tabela Fipe (menos 20%): R$ {custo1:.2f}")
        label_custo2.config(text=f"Concerto (menos 20%): R$ {custo2:.2f}")
        label_custo3.config(text=f"Documentação (menos 20%): R$ {custo3:.2f}")
        label_diferenca.config(text=f"Diferença final (40%): R$ {diferenca:.2f}")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora para Leilão")
root.geometry("300x180")

# Entrada do valor inicial
label_valor = tk.Label(root, text="Digite o valor inicial (R$):")
label_valor.pack()

entry_valor = tk.Entry(root)
entry_valor.pack()

# Botão para realizar o cálculo
button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack()

# Labels para mostrar os resultados
label_custo1 = tk.Label(root, text="Tabela Fipe (menos 20%): R$")
label_custo1.pack()

label_custo2 = tk.Label(root, text="Concerto (menos 20%): R$")
label_custo2.pack()

label_custo3 = tk.Label(root, text="Documentação (mais 20%): R$")
label_custo3.pack()

label_diferenca = tk.Label(root, text="Diferença final (40%): R$")
label_diferenca.pack()

# Execução da janela
root.mainloop()