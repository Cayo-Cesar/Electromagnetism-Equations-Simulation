# main.py
from ui import criar_interface_ampere, criar_interface_biot_savart, criar_interface_lorentz
import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Simulações Físicas")

    ttk.Label(root, text="Escolha uma Simulação:").grid(row=0, column=0, padx=10, pady=5)

    ttk.Button(root, text="Lei de Ampère", command=criar_interface_ampere).grid(row=1, column=0, padx=10, pady=5)
    ttk.Button(root, text="Lei de Biot-Savart", command=criar_interface_biot_savart).grid(row=2, column=0, padx=10, pady=5)
    ttk.Button(root, text="Força de Lorentz", command=criar_interface_lorentz).grid(row=3, column=0, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
