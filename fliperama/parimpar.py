#=======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Fliperama"
# Aula : 20
# Arquivo : parimpar.py
# Autor : Rodrigo Magagnin
# Data : 2026.08.18
# Conceitos : 
#======================================================================

import random
def jogar_parimpar():
    print('=== PAR OU ÍMPAR ===')

    jogador = int(input('Digite um número: '))

    escolha = input('Você escolhe PAR ou ÍMPAR? ').strip().lower()

    computador = random.randint(0, 10)

    soma = jogador + computador

    print('Você jogou:', jogador)
    print('O computador jogou:', computador)
    print('Soma:', soma)

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    print('Resultado:', resultado)

    if escolha == resultado:
        print('Você venceu!')
    else:
        print('O bot venceu!')
