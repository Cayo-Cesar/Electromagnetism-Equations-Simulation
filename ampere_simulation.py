import numpy as np
import matplotlib.pyplot as plt

def ampere_law(I, r):
    mu_0 = 4 * np.pi * 1e-7
    B = (mu_0 * I) / (2 * np.pi * r)
    return B

def calcular_campos(corrente, distancia_inicial, distancia_final, passo):
    I = float(corrente)
    distancias = np.arange(float(distancia_inicial), float(distancia_final) + passo, passo)
    campos = [ampere_law(I, r) for r in distancias]
    return distancias, campos

def plotar_grafico(distancias, campos):
    plt.plot(distancias, campos, marker='o')
    plt.xlabel('Distância do Fio (m)')
    plt.ylabel('Intensidade do Campo Magnético (T)')
    plt.title('Simulação da Lei de Ampère para um Fio Retilíneo')
    plt.grid(True)

    # Adicionando texto com o valor do campo magnético abaixo do gráfico
    plt.text(0.5, -0.15, f'Intensidade do Campo: {campos[-1]:.4e} T', transform=plt.gca().transAxes, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))
    
    plt.show()

def main():
    # Solicita entrada do usuário
    corrente = input("Digite a corrente (em Amperes): ")
    distancia_inicial = input("Digite a distância inicial (em metros): ")
    distancia_final = input("Digite a distância final (em metros): ")
    passo = 0.1

    # Calcula os campos magnéticos
    distancias, campos = calcular_campos(corrente, distancia_inicial, distancia_final, passo)

    # Exibe o resultado
    for d, b in zip(distancias, campos):
        print(f"Distância: {d:.2f} m, Campo Magnético: {b:.6e} T")

    # Plota o gráfico
    plotar_grafico(distancias, campos)

if __name__ == "__main__":
    main()
