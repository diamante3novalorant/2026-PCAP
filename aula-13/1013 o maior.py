'''
Problema: beecrowd 1013
Data: 2026.05.07
Estudante: Rodrigo Magagnin
'''

#Objetivo: Faça um programa que pega três valores lidos escolhe o maior seguido da mensagem "eh o maior"

# --- ANÁLISE (LIAC) ---
# Entrada: Três inteiros
# Processamento: A fórmula (A + B + ABS(A - B))
#                           -------------------
#                                     2
# Saída: Imprima o maior dos três valores lidos seguido da mensagem "eh o maior"

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
MAB = (A + B + abs(A - B)) / 2
MABC = int(MAB + C + abs(MAB - C)) / 2
print(f"{MABC:.0f} eh o maior")

