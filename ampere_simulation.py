import numpy as np
import matplotlib.pyplot as plt

def ampere_law(I, r):
    mu_0 = 4 * np.pi * 1e-7  # Permeabilidade do vácuo
    return (mu_0 * I) / (2 * np.pi * r)

# Parâmetros da simulação
I = 1.0  # Corrente elétrica no fio

# Distâncias de 0.1 a 5.0 em passos de 0.1
distancias = np.arange(0.1, 5.1, 0.1)

# Calcular a intensidade do campo magnético para cada distância
campo_magnetico = [ampere_law(I, r) for r in distancias]

# Plotar o gráfico
plt.plot(distancias, campo_magnetico, marker='o')
plt.xlabel('Distância do Fio (m)')
plt.ylabel('Intensidade do Campo Magnético (T)')
plt.title('Simulação da Lei de Ampère para um Fio Retilíneo')
plt.grid(True)
plt.show()


