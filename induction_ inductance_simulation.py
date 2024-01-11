import math

def calcular_fem(inducao_magnetica, area, numero_espiras, velocidade_rel, angulo):
    # Converte o ângulo para radianos
    angulo_rad = math.radians(angulo)
    
    # Calcula a taxa de variação do fluxo magnético
    taxa_variacao_fluxo = inducao_magnetica * area * numero_espiras * velocidade_rel * math.cos(angulo_rad)
    
    # Fórmula da f.e.m. induzidaimport math

def calcular_indutancia(numero_espiras, permeabilidade_magnetica, area_secao_transversal, comprimento):
    indutancia = (numero_espiras ** 2) * permeabilidade_magnetica * area_secao_transversal / comprimento
    return indutancia

def calcular_fem(inducao_magnetica, area, numero_espiras, velocidade_rel, angulo):
    angulo_rad = math.radians(angulo)
    taxa_variacao_fluxo = inducao_magnetica * area * numero_espiras * velocidade_rel * math.cos(angulo_rad)
    fem = -taxa_variacao_fluxo
    return fem

# Menu de escolha
print("Escolha a operação:")
print("1. Calcular Indutância")
print("2. Calcular Força Eletromotriz (f.e.m.)")
opcao = int(input("Digite o número da operação desejada (1 ou 2): "))

if opcao == 1:
    # Solicita dados para calcular a indutância
    numero_espiras_indutancia = int(input("Digite o número de espiras da bobina: "))
    permeabilidade_magnetica = float(input("Digite a permeabilidade magnética do material do núcleo (em H/m): "))
    area_secao_transversal = float(input("Digite a área da seção transversal do núcleo (em metros quadrados): "))
    comprimento = float(input("Digite o comprimento do núcleo (em metros): "))

    # Calcula a indutância
    indutancia_calculada = calcular_indutancia(numero_espiras_indutancia, permeabilidade_magnetica, area_secao_transversal, comprimento)
    
    # Exibe o resultado
    print(f"A indutância da bobina é: {indutancia_calculada} Henrys")

elif opcao == 2:
    # Solicita dados para calcular a f.e.m.
    inducao_magnetica = float(input("Digite a indução magnética (em Tesla): "))
    area = float(input("Digite a área da bobina (em metros quadrados): "))
    numero_espiras_fem = int(input("Digite o número de espiras da bobina: "))
    velocidade_rel = float(input("Digite a velocidade relativa entre a bobina e o ímã (em metros por segundo): "))
    angulo = float(input("Digite o ângulo entre o vetor da área da bobina e o campo magnético (em graus): "))

    # Calcula a f.e.m. induzida
    fem_induzida = calcular_fem(inducao_magnetica, area, numero_espiras_fem, velocidade_rel, angulo)
    
    # Exibe o resultado
    print(f"Força Eletromotriz (f.e.m.): {fem_induzida} Volts")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

   

# Solicita dados ao usuário
inducao_magnetica = float(input("Digite a indução magnética (em Tesla): "))
area = float(input("Digite a área da bobina (em metros quadrados): "))
numero_espiras = int(input("Digite o número de espiras da bobina: "))
velocidade_rel = float(input("Digite a velocidade relativa entre a bobina e o ímã (em metros por segundo): "))
angulo = float(input("Digite o ângulo entre o vetor da área da bobina e o campo magnético (em graus): "))

# Calcula a f.e.m. induzida
fem_induzida = calcular_fem(inducao_magnetica, area, numero_espiras, velocidade_rel, angulo)

# Exibe o resultado
print(f"Força Eletromotriz (f.e.m.): {fem_induzida} Volts")
