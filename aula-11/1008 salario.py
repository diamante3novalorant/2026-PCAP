'''
Problema: beecrowd 1008
Data: 2026/04/09
Estudante: Rodrigo Magagnin
'''

#Objetivo: Escrever um programa que leia número, horas trabalhadas e quanto recebe por hora de cada funcionário

# --- ANÁLISE (LIAC) ---
# Entrada: O programa recebe 2 inteiros e 1 número com 2 casas decimais
# Processamento: O programa deve calcular o produto das horas trabalhadas com o valor recebido por hora
# Saída: O programa deve exibir o número e salário do funcionário, escrito exatamente com "NUMBER = " para número do funcionário e "SALARY = U$ " deve haver um espaço em branco entre o "=" e o resultado

# 2 números inteiros e 1 número decimal
N = int(input())
H = int(input())
VPH = float(input())

print(f"NUMBER = {N}")
print(f"SALARY = U$ {H*VPH:.2f}")
