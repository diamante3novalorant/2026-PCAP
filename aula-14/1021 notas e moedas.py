'''
Problema: beecrowd 1021
Data: 2026.05.14
Estudante: Rodrigo Magagnin
'''

#Objetivo: Ler um valor monetário e decompô-lo no MENOR número possível
#                  de notas (100, 50, 20, 10, 5, 2 , 1) e moedas (0.50, 0.25, 0.10, 0.05, 0.01)


# --- ANÁLISE (LIAC) ---
# Entrada: um valor monetário com 2 casas decimais
# Processamento: separar parte inteira e parte decimal
# Saída: lista formatada de notas e moedas, na ordem do maior para o menor valor

n,m = input().split(".")

n = int(n)
m = int(m)

# // é a divisão dos inteiros (descarta o decimal)
# % é o resto da divisão
n100 = n // 100; n = n % 100
n50 = n // 50; n = n % 50
n20 = n // 20; n = n % 20
n10 = n // 10; n = n % 10
n05 = n // 5; n = n % 5
n02 = n // 2; n = n % 2
n01 = n

# Decomposição dos cents em moedas - mesma coisa só que em centavos
m50 = m // 50; m = m % 50
m25 = m // 25; m = m % 25
m10 = m // 10; m = m % 10
m05 = m // 5; m = m % 5
m01 = m

#Saída formatada
print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n05} nota(s) de R$ 5.00')
print(f'{n02} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{n01} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m05} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01')

