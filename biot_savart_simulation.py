import numpy as np
import matplotlib.pyplot as plt

def biot_savart(I, r, dl):
    mu_0 = 4 * np.pi * 1e-7  # Permeabilidade do vácuo
    r_norm = np.linalg.norm(r)
    dl_cross_r = np.cross(dl, r)
    
    campo_magnetico = (mu_0 * I / (4 * np.pi)) * (dl_cross_r / r_norm**3)
    
    return campo_magnetico

# Parâmetros da simulação
I = 16.0  # Corrente elétrica no fio

# Distâncias de 0.1 a 5.0 em passos de 0.1
distancias = np.arange(0.1, 5.1, 0.1)

# Vetor que representa o elemento de comprimento do fio (ao longo do eixo Z)
dl = np.array([0, 0, 1e-3])

# Calcular a intensidade do campo magnético para cada distância
campo_magnetico = [np.linalg.norm(biot_savart(I, np.array([r, 0, 0]), dl)) for r in distancias]

# Plotar o gráfico
plt.plot(distancias, campo_magnetico, marker='o')
plt.xlabel('Distância do Fio (m)')
plt.ylabel('Intensidade do Campo Magnético (T)')
plt.title('Simulação da Lei de Biot-Savart para um Fio Retilíneo')
plt.grid(True)
plt.show()