'''
Problema: beecrowd 1047
Data: 2026.05.14
Estudante: Rodrigo Magagnin
'''

# Objetivo: Calcular a duração de um jogo sabendo a hora de inicio e a hora de fim o jogo dura no mínimo 1m minuto e no maximo 24 horas.

# --- ANÁLISE (LIAC) ---
# Entrada: 4 inteiros na MESMA linha hi mi hf mf(hora/minuto inicial e final)
# Processamento: converter inicio e fim para o total em minutos;
#               se o fim for menor ou igual ao inicio, o jogo "virou a meia-noite"
#                (somar 24h em minutos); converter a duração de volta para horas e minutos
# Saída: "O JOGO DUROU H HORA(S) E M MINUTO(S)"
hi, mi, hf, mf = map(int, input().split())

# Converte tudo para minutos fica muito mais fácil calcular duração 
# trabalhando em uma unica unidade do que em hora minuts separado
tim = (hi* 60) + mi
tfm = (hf * 60) + mf

if tim > tfm:
    ttm = (tfm - tim) + (24 * 60)
else:
    ttm = tfm - tim
if ttm == 0:
    ttm = 24 * 60
print(f"O JOGO DUROU {ttm // 60} HORA(S) E {ttm % 60} MINUTO(S)")
