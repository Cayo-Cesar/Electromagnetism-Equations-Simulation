import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import tkinter as tk
from tkinter import ttk

#Definições da Interface Gráfica

def executar_simulacao(q, m, B, v0, r0):
    posicoes, forcas = lorentz_simulation(q, m, B, v0, r0)  # Recebe as posições e as forças
    intensidade_forca = np.linalg.norm(forcas, axis=1)  # Calcula a intensidade da força em cada passo
    plot_lorentz_simulation(posicoes, intensidade_forca)  # Passa a intensidade da força para a função de plotagem
def obter_parametros():
   
    janela = tk.Tk()
    janela.title("Parâmetros da Simulação")

    q_var = tk.DoubleVar()
    m_var = tk.DoubleVar()
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
        executar_simulacao(q, m, B, v0, r0)
        janela.destroy()  

    ttk.Button(janela, text="Iniciar Simulação", command=iniciar_simulacao).grid(row=5, columnspan=2, pady=10)

    janela.mainloop()

# A função lorentz_simulation simula a trajetória de uma partícula carregada em um campo magnético B.
# A força que a partícula experimenta é a força de Lorentz, que é o produto cruzado da velocidade da partícula e o campo magnético.
# A força de Lorentz é dada por F = qvB sin(theta), onde q é a carga da partícula, v é a velocidade, B é o campo magnético e theta é o ângulo entre v e B.

def lorentz_simulation(q, m, B, v0, r0, dt=0.01, num_steps=1000):
    posicoes = []
    forcas = []  # Lista para armazenar as forças
    r = r0
    v = v0
    
    for _ in range(num_steps):
        F = q * np.cross(v, B)
        forcas.append(F)  # Adiciona a força atual à lista de forças
        a = F / m
        v = v + a * dt
        r = r + v * dt
        posicoes.append(r.copy())

    return np.array(posicoes), np.array(forcas)  # Retorna as posições e as forças

def plot_lorentz_simulation(posicoes, intensidade_forca):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(posicoes[:, 0], posicoes[:, 1], posicoes[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Simulação da Força de Lorentz')

    # Adicionar texto com a intensidade da força
    ax.text2D(0.05, 0.95, f'Intensidade da Força: {intensidade_forca[-1]} N', transform=ax.transAxes)

    plt.show()
    
obter_parametros()