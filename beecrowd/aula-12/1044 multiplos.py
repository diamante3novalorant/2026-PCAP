'''
Problema: beecrowd 1044
Data: 2026.04.23
Estudante: Rodrigo Magagnin 
'''

#Objetivo: Ler dois valores inteiros A e B e mostrar se são múltiplos ou não

# --- ANÁLISE (LIAC) ---
# Entrada: O programa recebe 2 valores inteiros
# Processamento: O programa deve calcular se os 2 valores são múltiplos
# Saída: Deve mostrar a exata mensagem "Sao Multiplos" ou "Nao sao Multiplos"
A, B = input().split()
A = int(A)
B = int(B)

if A > B:
 maior = A
 menor = B
else:
 maior = B 
 menor = A

if maior % menor == 0:
 print("Sao Multiplos")
else:
 print("Nao sao Multiplos")

