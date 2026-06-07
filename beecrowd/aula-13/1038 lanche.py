'''
Problema: beecrowd 1038
Data: 2026.05.07
Estudante: Rodrigo Magagnin
'''

#Objetivo: Escreva um programa que leia o código e a quantidade de um item A seguir calcule e mostre o valor da conta a pagar


# --- ANÁLISE (LIAC) ---
# Entrada: O programa recebe 2 valores inteiros correspondentes ao código e à quantidade de um item
# Processamento: O produto do valor do item e a quantidade dele
# Saída: A saida deve conter a mensagem "Total:R$" seguido pelo valor com 2 casas após o ponto decimal
A, B = input().split()
A = int(A)
B = int(B)

if A == 1:
   t = B * 4.00
elif A == 2:
   t = B * 4.50
elif A == 3:
   t = B * 5.00
elif A == 4:
   t = B * 2.00
elif A == 5:
   t = B * 1.50  


print(f"Total: R$ {t:.2f}")
