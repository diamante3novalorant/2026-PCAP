'''
Problema: Beecrowd - 1004
Data: 2026/03/07
Estudante: Rodrigo Magagnin
'''
#Objetivo: Ler dois inteiros em variáveis A e B e calcular a o produto em PROD

#--- Análise (LIAC) ---
#Entrada: dois numeros inteiros, um em cada linha
#Processamento: O produto de A e B e armazenar em PROD
#Saída: Exibir o produto entre os dois valores no formato "PROD = valor"

#int() converte o texto lido para número inteiro
#input() lê o valor fornecido
#int(input()) lê e converte em uma única instrução


A = int(input())
B = int(input())
PROD = A*B
print(f"PROD = {PROD}" )
