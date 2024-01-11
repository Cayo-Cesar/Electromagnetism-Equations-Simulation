import math
import tkinter as tk
from tkinter import ttk

def calcular_fem(inducao_magnetica, area, numero_espiras, velocidade_rel, angulo):
    angulo_rad = math.radians(angulo)
    taxa_variacao_fluxo = inducao_magnetica * area * numero_espiras * velocidade_rel * math.cos(angulo_rad)
    fem = -taxa_variacao_fluxo
    return fem

def run_simulation():
    window = tk.Tk()
    window.title("Parâmetros da Simulação de Indução")

    ttk.Label(window, text="Indução Magnética (Tesla):").grid(row=0, column=0, padx=10, pady=5)
    ttk.Label(window, text="Área da Bobina (m²):").grid(row=1, column=0, padx=10, pady=5)
    ttk.Label(window, text="Número de Espiras:").grid(row=2, column=0, padx=10, pady=5)
    ttk.Label(window, text="Velocidade Relativa (m/s):").grid(row=3, column=0, padx=10, pady=5)
    ttk.Label(window, text="Ângulo (graus):").grid(row=4, column=0, padx=10, pady=5)

    parametros = []

    for i in range(5):
        entry_var = tk.DoubleVar()
        ttk.Entry(window, textvariable=entry_var).grid(row=i, column=1, padx=10, pady=5)
        parametros.append(entry_var)

    def iniciar_calculo():
        resultado = calcular_fem(*[entry_var.get() for entry_var in parametros])
        print(f"Força Eletromotriz (f.e.m.): {resultado} Volts")
        window.destroy()

    ttk.Button(window, text="Iniciar Cálculo", command=iniciar_calculo).grid(row=5, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    run_simulation()
