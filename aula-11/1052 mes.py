'''
Problema: beecrowd 1052
Data: 2026/04/09
Estudante: Rodrigo Magagnin
'''

#Objetivo: Ler um inteiro e informar qual mês ele é

# --- ANÁLISE (LIAC) ---
# Entrada: um inteiro representando o mês
# Processamento: Comparar o inteiro lido com cada codigo da tabela usando if/elif/else
# Saída: mostrar o mês correspondente em inglês com a primeira letra em maiusculo

# mês sempre é um inteiro (int)
N = int(input())

# Estrutura if/elif/else: testa cada condição em sequência 
# Apenas o primeiro bloco verdadeiro é executado - os demais são ignorados
if N == 1:
    print("January")
elif N == 2:
    print("February")
elif N == 3:
    print("March")
elif N == 4:
    print("April")
elif N == 5:
    print("May")
elif N == 6:
    print("June")
elif N == 7:
    print("July")
elif N == 8:
    print("August")
elif N == 9:
    print("September")
elif N == 10:
    print("October")
elif N == 11:
    print("November")
elif N == 12:
    print("December")


