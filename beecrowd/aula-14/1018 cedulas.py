'''
Problema: beecrowd 1018
Data: 2026.05.14
Estudante: Rodrigo Magagnin 
'''

#Objetivo: Ler um valor monetário e decompô-lo no MENOR número possível
#                  de notas (100, 50, 20, 10, 5, 2 , 1) 


# --- ANÁLISE (LIAC) ---
# Entrada: um valor monetário inteiro
# Processamento: Separar o total nos números de cada nota
# Saída: lista formatada de notas na ordem do maior para o menor valor

n = int(input())
print(n)
n100 = n // 100; n = n % 100
n50 = n // 50; n = n % 50
n20 = n // 20; n = n % 20
n10 = n // 10; n = n % 10
n05 = n // 5; n = n % 5
n02 = n // 2; n = n % 2
n01 = n


#Saída formatada

print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n05} nota(s) de R$ 5,00')
print(f'{n02} nota(s) de R$ 2,00')
print(f'{n01} nota(s) de R$ 1,00')
