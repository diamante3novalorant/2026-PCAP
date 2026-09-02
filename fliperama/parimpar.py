#=======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Fliperama"
# Aula : 23
# Arquivo : parimpar.py
# Autor : Rodrigo Magagnin
# Data : 2026.09.01
# Conceitos : Jogo par ou impar, nele o jogador deve escolher um numero
# e depois dizer se quer par ou impar, para vencer a soma final deve ser
# o resuiltado de sua escolha, seja ela par ou impar
#======================================================================
from modulos import ler_opcao
from telas import titulo, linha
import random


def jogar_parimpar():

    print('=== PAR OU ÍMPAR - MELHOR DE 3 ===')

    vitorias_jogador = 0
    vitorias_computador = 0
    rodada = 1

    while vitorias_jogador < 2 and vitorias_computador < 2:

        linha()
        print('--- RODADA', rodada, '---')

        numero_jogador = ler_opcao('Digite um número de 1 a 10',['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

        jogador = int(numero_jogador)

        escolha = ler_opcao('Você escolhe PAR ou ÍMPAR',['PAR','par', 'ÍMPAR','impar', 'ímpar','IMPAR'])

        if escolha == 'IMPAR': 
            escolha == 'ÍMPAR'
        if escolha == 'par':
            escolha == 'PAR'
        computador = random.randint(1, 10)

        soma = jogador + computador

        linha()
        print('Você jogou:', jogador)
        print('O computador jogou:', computador)
        print('Soma:', soma)

        if soma % 2 == 0:
            resultado = 'PAR'
        else:
            resultado = 'ÍMPAR'

        print('Resultado:', resultado)

        if escolha == resultado:

            print('Você venceu a rodada!')
            vitorias_jogador = vitorias_jogador + 1

        else:

            print('O bot venceu a rodada!')
            vitorias_computador = vitorias_computador + 1

        linha()
        print('Placar:')
        print('Você:', vitorias_jogador)
        print('Bot:', vitorias_computador)

        rodada = rodada + 1

    linha()
    print('=== FIM DA PARTIDA ===')
    linha()

    if vitorias_jogador == 2:
        titulo("YOU'RE A WINNER!")
    else:
        titulo("YOU'RE A LOSER!")