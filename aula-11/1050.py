'''
Problema: beecrowd 1050
Data: 16/04/26
Estudante: Rodrigo Magagnin
'''

#Objetivo: Ler um DDD e informar a qual cidade ele pertence

# --- ANÁLISE (LIAC) ---
# Entrada: um inteiro representando o DDD
# Processamento: Comparar o DDD lido co cada codigo da tabela usando if/elif/else
# Saída: nome da cidade correspondente, ou "DDD não cadastrado" se não encontrada

# DDD sempre é um inteiro (int)
DDD = int(input())

# Estrutura if/elif/else: testa cada condição em sequência 
# Apenas o primeiro bloco verdadeiro é executado - os demais são ignorados
if DDD == 61:
    print("Brasilia")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("Sao Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitoria")
elif DDD == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")
