'''
Problema: beecrowd 1046
Data: 2026.05.14
Estudante: Rodrigo Magagnin
'''

# Objetivo: Calcular a duração de um jogo sabendo a hora de inicio e a hora de fim o jogo dura no mínimo 1 hora e no maximo 24 horas.

# --- ANÁLISE (LIAC) ---
# Entrada: 2 inteiros na MESMA linha hi  hf (hora inicial e final)
# Processamento: converter inicio e fim para o total de horas
#               se o fim for menor ou igual ao inicio, o jogo "durou 24 horas"
# Saída: "O JOGO DUROU H HORA(S)"

hi, hf = map(int, input().split())
ti = (hi * 60)
tf = (hf * 60)
if ti > tf:
    tt = (tf - ti) + (24 * 60)
else:
    tt = tf - ti

if tt == 0:
    tt = 24 * 60
print(f"O JOGO DUROU {tt // 60} HORA(S)")
