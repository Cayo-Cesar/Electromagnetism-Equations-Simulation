import numpy as np
import matplotlib.pyplot as plt

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

def main():
    # Solicita entrada do usuário
    corrente = input("Digite a corrente (em Amperes): ")
    dl_z = input("Digite o comprimento do segmento de corrente ao longo do eixo z (em metros): ")
    distancia_inicial = input("Digite a distância inicial do ponto de observação ao longo do eixo x (em metros): ")
    distancia_final = input("Digite a distância final do ponto de observação ao longo do eixo x (em metros): ")
    passo = 0.1

    # Cria um array de distâncias usando np.arange
    distancias = np.arange(float(distancia_inicial), float(distancia_final) + passo, passo)

    # Calcula os campos magnéticos usando a Lei de Biot-Savart
    campos = calcular_campos_biot_savart(corrente, dl_z, distancias)

    # Exibe o resultado
    for r, b in zip(distancias, campos):
        print(f"Distância do Fio: {r:.2f} m, Campo Magnético: {b:.6e} T")

    # Plota o gráfico
    plotar_grafico_biot_savart(distancias, campos)

if __name__ == "__main__":
    main()
