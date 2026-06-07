'''
Problema: beecrowd 1051
Data: 2026.05.14
Estudante: Rodrigo Magagnin
'''

#Objetivo: ler um valor com duas casas decimais e calcular o valor que essa pessoa deve pagar de imposto de renda

# --- ANÁLISE (LIAC) ---
# Entrada: Um valor com duas casas decimais
# Processamento: calcular as porcentagens do salário do pobre cidadão que vão para o governo
# Saída: deve ser "R$ (x)"

A = float(input())
B = 0
C = A
if A > 4500:
    B += ((A - 4500) * 0.28)
    C = (C - (A - 4500))
if A > 3000:
    B += ((C - 3000) * 0.18)
    C = (C - (C - 3000))
if A > 2000:
    B += ((C - 2000) * 0.08)
    C = (C - (C - 2000))
if A < 2000:
    print(f"Isento")
else:
    print(f"R$ {B:.2f}")
