import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button

def biot_savart(I, r, dl):
    mu_0 = 4 * np.pi * 1e-7  # Permeabilidade do vácuo
    r_norm = np.linalg.norm(r)
    dl_cross_r = np.cross(dl, r)
    
    campo_magnetico = (mu_0 * I / (4 * np.pi)) * (dl_cross_r / r_norm**3)
    
    return campo_magnetico

def plotar_grafico(corrente, dl_z, distancia_inicial, distancia_final):
    I = float(corrente)
    dl = np.array([0, 0, float(dl_z)])
    distancias = np.arange(float(distancia_inicial), float(distancia_final) + 0.1, 0.1)
    campo_magnetico = [np.linalg.norm(biot_savart(I, np.array([r, 0, 0]), dl)) for r in distancias]

    plt.plot(distancias, campo_magnetico, marker='o')
    plt.xlabel('Distância do Fio (m)')
    plt.ylabel('Intensidade do Campo Magnético (T)')
    plt.title('Simulação da Lei de Biot-Savart para um Fio Retilíneo')
    plt.grid(True)
    plt.show()

def criar_interface():
    root = Tk()
    root.title("Simulação da Lei de Biot-Savart")

    label_corrente = Label(root, text="Corrente:")
    label_corrente.grid(row=0, column=0)
    entry_corrente = Entry(root)
    entry_corrente.grid(row=0, column=1)

    label_dl_z = Label(root, text="Comprimento do Fio (dl_z):")
    label_dl_z.grid(row=1, column=0)
    entry_dl_z = Entry(root)
    entry_dl_z.grid(row=1, column=1)

    label_distancia_inicial = Label(root, text="Distância Inicial:")
    label_distancia_inicial.grid(row=2, column=0)
    entry_distancia_inicial = Entry(root)
    entry_distancia_inicial.grid(row=2, column=1)

    label_distancia_final = Label(root, text="Distância Final:")
    label_distancia_final.grid(row=3, column=0)
    entry_distancia_final = Entry(root)
    entry_distancia_final.grid(row=3, column=1)

    btn_plotar = Button(root, text="Plotar Gráfico", command=lambda: plotar_grafico(entry_corrente.get(), entry_dl_z.get(), entry_distancia_inicial.get(), entry_distancia_final.get()))
    btn_plotar.grid(row=4, column=0, columnspan=2)

    root.mainloop()

# Chamando a função para criar a interface
criar_interface()
