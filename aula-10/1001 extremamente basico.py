
'''
Problema: Beecrowd - 1001
Data: 2026/03/07
Estudante: Rodrigo Magagnin
'''
#Objetivo: Ler dois inteiros em variáveis A e B e calcular a soma em X

#--- Análise (LIAC) ---
#Entrada: dois numeros inteiros, um em cada linha
#Processamento: A soma de A e B e armazenar em X
#Saída: Exibir a soma entre os dois valores no formato "X = valor"

#int() converte o texto lido para número inteiro
#input() lê o valor fornecido
#int(input()) lê e converte em uma única instrução

A = int(input())
B = int(input())
X = A+B
#f-string: insere o valor de X dentro do texto com chaves {}
print(f"X = {X}" )
