import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, ttk, Label, Entry, Button, StringVar


def biot_savart(I, r, dl):
    mu_0 = 4 * np.pi * 1e-7
    r_norm = np.linalg.norm(r)
    dl_cross_r = np.cross(dl, r)
    
    campo_magnetico = (mu_0 * I / (4 * np.pi)) * (dl_cross_r / r_norm**3)
    
    return campo_magnetico

def calcular_campos_biot_savart(corrente, dl_z, distancias):
    I = float(corrente)
    dl = np.array([0, 0, float(dl_z)])
    campos = [np.linalg.norm(biot_savart(I, np.array([r, 0, 0]), dl)) for r in distancias]
    
    return campos

def plotar_grafico_biot_savart(distancias, campos):
    plt.plot(distancias, campos, marker='o')
    plt.xlabel('Distância do Fio (m)')
    plt.ylabel('Intensidade do Campo Magnético (T)')
    plt.title('Simulação da Lei de Biot-Savart para um Fio Retilíneo')
    plt.grid(True)

    # Adicionando texto com o valor do campo magnético abaixo do gráfico
    plt.text(0.5, -0.15, f'Intensidade do Campo: {campos[-1]:.4e} T', transform=plt.gca().transAxes, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))
    
    plt.show()

def calcular_e_plotar_biot_savart():
    corrente = corrente_var.get()
    dl_z = dl_z_var.get()
    distancia_inicial = distancia_inicial_var.get()
    distancia_final = distancia_final_var.get()
    passo = 0.1

    distancias = np.arange(float(distancia_inicial), float(distancia_final) + passo, passo)

    campos = calcular_campos_biot_savart(corrente, dl_z, distancias)

    for r, b in zip(distancias, campos):
        print(f"Distância do Fio: {r:.2f} m, Campo Magnético: {b:.6e} T")

    plotar_grafico_biot_savart(distancias, campos)

# Tkinter GUI
root = Tk()
root.title("Lei de Biot-Savart - Simulação")

Label(root, text="Corrente (A):").grid(row=0, column=0)
Label(root, text="Comprimento do segmento de corrente ao longo do eixo z (m):").grid(row=1, column=0)
Label(root, text="Distância Inicial (m):").grid(row=2, column=0)
Label(root, text="Distância Final (m):").grid(row=3, column=0)

corrente_var = StringVar()
dl_z_var = StringVar()
distancia_inicial_var = StringVar()
distancia_final_var = StringVar()

Entry(root, textvariable=corrente_var).grid(row=0, column=1)
Entry(root, textvariable=dl_z_var).grid(row=1, column=1)
Entry(root, textvariable=distancia_inicial_var).grid(row=2, column=1)
Entry(root, textvariable=distancia_final_var).grid(row=3, column=1)

Button(root, text="Calcular e Plotar", command=calcular_e_plotar_biot_savart).grid(row=4, column=0, columnspan=2)

root.mainloop()


