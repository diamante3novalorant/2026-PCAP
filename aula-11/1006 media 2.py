'''
Problema: beecrowd 
Data: 2026/04/09
Estudante: Rodrigo Magagnin
'''

#Objetivo: Ler 3 valores como variáveis A, B e C sabendo que A tem peso 2 B tem peso 3 e C tem peso 5

# --- ANÁLISE (LIAC) ---
# Entrada: O arquivo de entrada contém 3 valores com uma casa decimal (float)
# Processamento: Media ponderada 
# Saída: Exibir no formato "MEDIA = valor" com 1 casa decimal

A =  float(input())
B =  float(input())
C =  float(input())

# A tem peso 2, B tem peso 3 e C tem peso 5 a soma dos pesos é 10, então devemos fazer cada número * seu peso e depois dividir tudo por 10 para obter a media ponderada
media = (A * 2 + B * 3 + C * 5) / 10

print(f"MEDIA = {media:.1f}")
