import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar

def ampere_law(I, r):
    mu_0 = 4 * np.pi * 1e-7  # Permeabilidade do vácuo
    return (mu_0 * I) / (2 * np.pi * r)

def plot_grafico(corrente, distancia_inicial, distancia_final):
    I = float(corrente)
    distancias = np.arange(float(distancia_inicial), float(distancia_final) + 0.1, 0.1)
    campo_magnetico = [ampere_law(I, r) for r in distancias]

    plt.plot(distancias, campo_magnetico, marker='o')
    plt.xlabel('Distância do Fio (m)')
    plt.ylabel('Intensidade do Campo Magnético (T)')
    plt.title('Simulação da Lei de Ampère para um Fio Retilíneo')
    plt.grid(True)
    plt.show()

def criar_interface():
    root1 = Tk()
    root1.title("Simulação da Lei de Ampère")

    label_corrente = Label(root1, text="Corrente:")
    label_corrente.grid(row=0, column=0)
    entry_corrente = Entry(root1)
    entry_corrente.grid(row=0, column=1)

    label_distancia_inicial = Label(root1, text="Distância Inicial:")
    label_distancia_inicial.grid(row=1, column=0)
    entry_distancia_inicial = Entry(root1)
    entry_distancia_inicial.grid(row=1, column=1)

    label_distancia_final = Label(root1, text="Distância Final:")
    label_distancia_final.grid(row=2, column=0)
    entry_distancia_final = Entry(root1)
    entry_distancia_final.grid(row=2, column=1)

    btn_plotar = Button(root1, text="Iniciar Simulação", command=lambda: plot_grafico(entry_corrente.get(), entry_distancia_inicial.get(), entry_distancia_final.get()))
    btn_plotar.grid(row=3, column=0, columnspan=2)

    root1.mainloop()

# Chamando a função para criar a interface
criar_interface()