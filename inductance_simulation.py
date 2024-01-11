import math
import tkinter as tk
from tkinter import ttk

def calcular_indutancia(numero_espiras, permeabilidade_magnetica, area_secao_transversal, comprimento):
    indutancia = (numero_espiras ** 2) * permeabilidade_magnetica * area_secao_transversal / comprimento
    return indutancia

def run_simulation():
    window = tk.Tk()
    window.title("Parâmetros da Simulação de Indutância")

    ttk.Label(window, text="Número de Espiras:").grid(row=0, column=0, padx=10, pady=5)
    ttk.Label(window, text="Permeabilidade Magnética (H/m):").grid(row=1, column=0, padx=10, pady=5)
    ttk.Label(window, text="Área da Seção Transversal (m²):").grid(row=2, column=0, padx=10, pady=5)
    ttk.Label(window, text="Comprimento do Núcleo (m):").grid(row=3, column=0, padx=10, pady=5)

    parametros = []

    for i in range(4):
        entry_var = tk.DoubleVar()
        ttk.Entry(window, textvariable=entry_var).grid(row=i, column=1, padx=10, pady=5)
        parametros.append(entry_var)

    def iniciar_calculo():
        resultado = calcular_indutancia(*[entry_var.get() for entry_var in parametros])
        print(f"A indutância da bobina é: {resultado} Henrys")
        window.destroy()

    ttk.Button(window, text="Iniciar Cálculo", command=iniciar_calculo).grid(row=4, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    run_simulation()
