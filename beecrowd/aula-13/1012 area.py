'''
Problema: beecrowd 1012
Data: 2026.05.07
Estudante: Rodrigo Magagnin 
'''

#Objetivo: Escrever um programa que leia três valores de dupla precisão A, B e C que deve calcular e mostrar: a área do triângulo retângulo, a área do circulo de Raio C 

# --- ANÁLISE (LIAC) ---
# Entrada: O programa recebe três valores com float
# Processamento: Calcular as áreas das formas que se pede
# Saída: Deverá conter 5 linhas de dados, cada uma corresponde a uma das áreas sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. Ele deve ser apresentado com 3 linhas após a casa decimal.
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
triangulo = (A * C) / 2
circulo = pi * (C ** 2)
trapézio = ((A + B) * C) / 2
quadrado = B ** 2
retângulo = A * B
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapézio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retângulo:.3f}")
