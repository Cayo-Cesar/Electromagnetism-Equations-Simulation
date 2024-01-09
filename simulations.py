# simulations.py
import numpy as np
import matplotlib.pyplot as plt

def ampere_law(I, r):
    mu_0 = 4 * np.pi * 1e-7
    return (mu_0 * I) / (2 * np.pi * r)

def plot_ampere_simulation(corrente, distancia_inicial, distancia_final):
    I = float(corrente)
    distancias = np.arange(float(distancia_inicial), float(distancia_final) + 0.1, 0.1)
    campo_magnetico = [ampere_law(I, r) for r in distancias]

    plt.plot(distancias, campo_magnetico, marker='o')
    plt.xlabel('Distância do Fio (m)')
    plt.ylabel('Intensidade do Campo Magnético (T)')
    plt.title('Simulação da Lei de Ampère para um Fio Retilíneo')
    plt.grid(True)
    plt.show()

def biot_savart(I, r, dl):
    mu_0 = 4 * np.pi * 1e-7
    r_norm = np.linalg.norm(r)
    dl_cross_r = np.cross(dl, r)
    
    campo_magnetico = (mu_0 * I / (4 * np.pi)) * (dl_cross_r / r_norm**3)
    
    return campo_magnetico

def plot_biot_savart_simulation(corrente, dl_z, distancia_inicial, distancia_final):
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

def lorentz_simulation(q, m, B, v0, r0, dt=0.01, num_steps=1000):
    posicoes = []
    r = r0
    v = v0
    
    for _ in range(num_steps):
        F = q * np.cross(v, B)
        a = F / m
        v = v + a * dt
        r = r + v * dt
        posicoes.append(r.copy())

    intensidade_campo = np.linalg.norm(B)
    return np.array(posicoes), intensidade_campo

def plot_lorentz_simulation(posicoes, intensidade_campo):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(posicoes[:, 0], posicoes[:, 1], posicoes[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Simulação da Força de Lorentz')

    ax.text2D(0.05, 0.95, f'Intensidade do Campo: {intensidade_campo}', transform=ax.transAxes)

    plt.show()
