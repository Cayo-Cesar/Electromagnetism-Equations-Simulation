# ui.py
from tkinter import Tk, Label, Entry, Button, StringVar
import tkinter as tk
from tkinter import ttk
import numpy as np
from simulations import plot_ampere_simulation, plot_biot_savart_simulation, lorentz_simulation, plot_lorentz_simulation

def criar_interface_ampere():
    root = Tk()
    root.title("Simulação da Lei de Ampère")

    label_corrente = Label(root, text="Corrente:")
    label_corrente.grid(row=0, column=0)
    entry_corrente = Entry(root)
    entry_corrente.grid(row=0, column=1)

    label_distancia_inicial = Label(root, text="Distância Inicial:")
    label_distancia_inicial.grid(row=1, column=0)
    entry_distancia_inicial = Entry(root)
    entry_distancia_inicial.grid(row=1, column=1)

    label_distancia_final = Label(root, text="Distância Final:")
    label_distancia_final.grid(row=2, column=0)
    entry_distancia_final = Entry(root)
    entry_distancia_final.grid(row=2, column=1)

    btn_plotar = Button(root, text="Iniciar Simulação", command=lambda: plot_ampere_simulation(entry_corrente.get(), entry_distancia_inicial.get(), entry_distancia_final.get()))
    btn_plotar.grid(row=3, column=0, columnspan=2)

    root.mainloop()

def criar_interface_biot_savart():
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

    btn_plotar = Button(root, text="Plotar Gráfico", command=lambda: plot_biot_savart_simulation(entry_corrente.get(), entry_dl_z.get(), entry_distancia_inicial.get(), entry_distancia_final.get()))
    btn_plotar.grid(row=4, column=0, columnspan=2)

    root.mainloop()

def criar_interface_lorentz():
    janela = tk.Tk()
    janela.title("Parâmetros da Simulação")

    q_var = tk.DoubleVar(value=1.0)
    m_var = tk.DoubleVar(value=1.0)
    B_var = tk.StringVar(value="0 0 1")
    v0_var = tk.StringVar(value="1 0 0")
    r0_var = tk.StringVar(value="0 0 0")

    ttk.Label(janela, text="Carga (q):").grid(row=0, column=0, padx=10, pady=5)
    ttk.Entry(janela, textvariable=q_var).grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(janela, text="Massa (m):").grid(row=1, column=0, padx=10, pady=5)
    ttk.Entry(janela, textvariable=m_var).grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(janela, text="Campo Magnético (B):").grid(row=2, column=0, padx=10, pady=5)
    ttk.Entry(janela, textvariable=B_var).grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(janela, text="Velocidade Inicial (v0):").grid(row=3, column=0, padx=10, pady=5)
    ttk.Entry(janela, textvariable=v0_var).grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(janela, text="Posição Inicial (r0):").grid(row=4, column=0, padx=10, pady=5)
    ttk.Entry(janela, textvariable=r0_var).grid(row=4, column=1, padx=10, pady=5)

    def iniciar_simulacao():
        q = q_var.get()
        m = m_var.get()
        B = np.array([float(x) for x in B_var.get().split()])
        v0 = np.array([float(x) for x in v0_var.get().split()])
        r0 = np.array([float(x) for x in r0_var.get().split()])
        posicoes, intensidade_campo = lorentz_simulation(q, m, B, v0, r0)
        plot_lorentz_simulation(posicoes, intensidade_campo)
        janela.destroy()

    ttk.Button(janela, text="Iniciar Simulação", command=iniciar_simulacao).grid(row=5, columnspan=2, pady=10)

    janela.mainloop()
