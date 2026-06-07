'''
Problema: beecrowd 1035
Data: 2026/04/23
Estudante: Rodrigo Magagnin
'''

#Objetivo: Leia 4 valores inteiros e calcule as respectivas somas entre eles e mostre os valores aceitos e nao aceitos

# --- ANÁLISE (LIAC) ---
# Entrada: O programa recebe quatro valores inteiros
# Processamento: Somente as somas entre os valores
# Saída: O programa deve exibir exatamente "Valores aceitos" e "Valores nao aceitos"

A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
if B > C and D > A and (D + C > A + B) and C and D > 0 and A % 2 == 0:
    print(f"Valores aceitos")
else:
    print(f"Valores nao aceitos")
