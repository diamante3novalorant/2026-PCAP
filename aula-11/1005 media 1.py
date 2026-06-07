'''
Problema: beecrowd 1005
Data: 2026.04.09
Estudante: Rodrigo Magagnin
'''

#Objetivo: Ler duas notas com pesos diferentes e calcular a média ponderada

# --- ANÁLISE (LIAC) ---
# Entrada: duas notas de ponto flutuante A e B(cada uma em uma linha)
# Processamento: média ponderada = (A * 3.5 + B 7.5) / 11
# Saída: exibir no formato "MÉDIA = valor" com 5 casas decimais

#float(input) - notas podem ter casas decimais
A = float(input())
B = float(input())

# Nota A tem peso 3.5 e Nota B tem peso 7.5
# A soma dos pesos é 11 - divide-se por 11 para obter a média ponderada
media = (A * 3.5 + B * 7.5) / 11

# O  enunciado exige espaço antes e depois do "=" - seguir à risca
print(f"MEDIA = {media:.5f}")

