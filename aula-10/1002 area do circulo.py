'''
Problema: beecrowd 1002
Data: 2026/03/07
Estudante: Rodrigo Magagnin
'''
#Objetivo: Calcular o raio de uma esfera

# --- ANÁLISE (LIAC) ---
#Entrada: um número de ponto flutuante (o raio "r")
#Processamento: aplicar a fórmula do raio da esfera
#Saída: exibir no formato "r = valor" com 3 casa decimais
#float() converte o valor lido para número decimal (ponto flutuante)

# :.4f formata com exatas 4 casas decimais

n = 3.14159
r = float (input())
A = (n*(r**2))
print(f"A={A:.4f}")

