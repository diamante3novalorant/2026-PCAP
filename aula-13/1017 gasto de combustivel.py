'''
Problema: beecrowd 1017
Data: 2026/05/07
Estudante: Rodrigo Magagnin
'''

#Objetivo: Calcular e mostrar o gasto de combustivel em uma viagem

# --- ANÁLISE (LIAC) ---
# Entrada: Dois inteiros
# Processamento: Tempo gasto vezes velocidade média para obter a distância percorrida 
# Saída: Imprimir a quantdade gasta de litros com três números após o ponto decimal
A = int(input())
B = int(input())
C = (A * B) / 12
print(f"{C:.3f}")
