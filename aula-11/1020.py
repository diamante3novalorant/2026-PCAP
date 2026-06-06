'''
Problema: beecrowd 1020
Data: 2026/04/09
Estudante: Rodrigo Magagnin
'''

#Objetivo: descrever o objetivo

# --- ANÁLISE (LIAC) ---
# Entrada: Leia um valor inteiro correspondente à idade de uma pessoa em dias e a informe em dias, anos e meses
# Processamento: Ele deve trazer o valor de dias para anos, meses e dias
# Saída: Deve ser exibido exatamente como "X ano(s), X mes(s) X dia(s)"

D = int(input())
Ano = D // 365
D = D % 365
Mês = D // 30
Dia = D % 30
print(f"{Ano} ano(s)")
print(f"{Mês} mes(es)")
print(f"{Dia} dia(s)")
