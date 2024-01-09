import tkinter as tk
from tkinter import ttk
from ampere_simulation import criar_interface as criar_interface_ampere
from biot_savart_simulation import criar_interface as criar_interface_biot_savart
from lorentz_simulation import obter_parametros as obter_parametros_lorentz

def abrir_interface_ampere():
    criar_interface_ampere()

def abrir_interface_biot_savart():
    criar_interface_biot_savart()

def abrir_interface_lorentz():
    obter_parametros_lorentz()

def main():
    root = tk.Tk()
    root.title("Simulações Físicas")

    ttk.Label(root, text="Escolha uma Simulação:").grid(row=0, column=0, padx=10, pady=5)

    ttk.Button(root, text="Lei de Ampère", command=lambda: abrir_interface_ampere()).grid(row=1, column=0, padx=10, pady=5)
    ttk.Button(root, text="Lei de Biot-Savart", command=lambda: abrir_interface_biot_savart()).grid(row=2, column=0, padx=10, pady=5)
    ttk.Button(root, text="Força de Lorentz", command=lambda: abrir_interface_lorentz()).grid(row=3, column=0, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
