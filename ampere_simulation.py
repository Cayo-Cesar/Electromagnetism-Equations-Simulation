import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, ttk, Label, Entry, Button, StringVar

def ampere_law(I, r):
    mu_0 = 4 * np.pi * 1e-7
    B = (mu_0 * I) / (2 * np.pi * r)
    return B

def calcular_campos(corrente, distancia_inicial, distancia_final, passo):
    I = float(corrente)
    distancias = np.arange(float(distancia_inicial), float(distancia_final) + passo, passo)
    campos = [ampere_law(I, r) for r in distancias]
    return distancias, campos

def run_simulation(distancias, campos):
    plt.plot(distancias, campos, marker='o')
    plt.xlabel('Distância do Fio (m)')
    plt.ylabel('Intensidade do Campo Magnético (T)')
    plt.title('Simulação da Lei de Ampère para um Fio Retilíneo')
    plt.grid(True)

    # Adicionando texto com o valor do campo magnético abaixo do gráfico
    plt.text(0.5, -0.15, f'Intensidade do Campo: {campos[-1]:.4e} T', transform=plt.gca().transAxes, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))
    
    plt.show()

def calcular_e_plotar():
    corrente = corrente_var.get()
    distancia_inicial = distancia_inicial_var.get()
    distancia_final = distancia_final_var.get()
    passo = 0.1

    distancias, campos = calcular_campos(corrente, distancia_inicial, distancia_final, passo)

    for d, b in zip(distancias, campos):
        print(f"Distância: {d:.2f} m, Campo Magnético: {b:.6e} T")

    run_simulation(distancias, campos)

# Tkinter GUI
root = Tk()
root.title("Lei de Ampère - Simulação")

# Labels and Entry widgets for user input
Label(root, text="Corrente (A):").grid(row=0, column=0)
Label(root, text="Distância Inicial (m):").grid(row=1, column=0)
Label(root, text="Distância Final (m):").grid(row=2, column=0)

corrente_var = StringVar()
distancia_inicial_var = StringVar()
distancia_final_var = StringVar()

Entry(root, textvariable=corrente_var).grid(row=0, column=1)
Entry(root, textvariable=distancia_inicial_var).grid(row=1, column=1)
Entry(root, textvariable=distancia_final_var).grid(row=2, column=1)

# Button to calculate and plot
Button(root, text="Iniciar Simulação", command=calcular_e_plotar).grid(row=3, column=0, columnspan=2)

root.mainloop()

