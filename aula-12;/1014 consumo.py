'''
Problema: beecrowd 1014
Data: 2026/04/23
Estudante: Rodrigo Magagnin
'''

#Objetivo: Calcular o consumo médio de um automóvel em km/l

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro X representando distância e um numero float Y representando o gasto de combustivel
# Processamento: Consumo = X (Distância)/ Y (Total Gasto)
# Saída: Consumo com 3 casas decimais seguido de "km/l"

# Lê a distância total percorrida em km (tipo inteiro)
X = int(input())

# Lê o total de combustível gasto em litros (tipo ponto flutuante)
Y = float(input())

# Calcula o consumo médio: quilôtros dividido por litros
consumo = X / Y

# Exibe o resultado com três casas decimais e a unidade km/l
print(f"{consumo:.3f} km/l")

