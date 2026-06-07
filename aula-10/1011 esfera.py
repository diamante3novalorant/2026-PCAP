'''
Problema: beecrowd 1011
Data: 2026/03/07
Estudante: Rodrigo Magagnin
'''
#Objetivo:Ler o raio de uma esfera e calcular seu volume com a formula (4/3) * pi *R³

# --- ANÁLISE (LIAC) ---
#Entrada: um número de ponto flutuante (o raio R)
#Processamento: aplicar a fórmula do volume da esfera
#Saída: exibir no formato "VOLUME = valor" com 3 casa decimais
#float() converte o valor lido para número decimal (ponto flutuante)
R = float(input())

# O enunciado pede para atribuir pi como constante
pi = 3.14159

#4.0/3 garante divisão decimal (não inteira)
# R**3 R ao cubo R³
V = (4.0 / 3) *pi * R ** 3

# :.3f formata com exatas 3 casas decimais

print(f"VOLUME = {V:.3f}")

 
