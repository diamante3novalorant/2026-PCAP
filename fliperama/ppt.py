#=======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Fliperama"
# Aula : 20
# Arquivo : ppt.py
# Autor : Rodrigo Magagnin
# Data : 2026.08.11
# Conceitos : 
#======================================================================
#sorteia um numero aleatorio
from random import randint

# importa funções titulo e linha
from telas import titulo, linha

from modulos import ler_opcao
# pedra == posição 0, papel == 1 e tesoura == 2
JOGADAS = ['PEDRA', 'PAPEL', 'TESOURA']
#Define o vencedor
def quem_vence(jogador, computador):
    if jogador == computador:
        return "empate"
    if jogador == (computador + 1) % 3:
        return "jogador"
    return "maquina"
def mostrar_jogadas():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')
    linha()

def jogar_ppt():
    titulo('PEDRA - PAPEL -TESOURA')

    pontos_jogador = 0
    pontos_maquina = 0

    while pontos_jogador < 2 and pontos_maquina < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao('Tua jogada',['0','1','2']))
        maquina = randint(0, 2)

        print('Tu jogou ' + JOGADAS[jogador] + '-')
        print('Computador jogou ' + JOGADAS[maquina] + '-')

        resultado = quem_vence(jogador, maquina)

        if resultado == 'empate':
            print('Empate! Ninguém vence')
        elif resultado == 'jogador':
            print('Parabéns! Tu venceu a rodada')
            pontos_jogador += 1
        elif resultado == 'maquina':
            print('A maquina venceu a rodada')
            pontos_maquina += 1

        linha()
        print(f'Placar: Jogador {pontos_jogador} X {pontos_maquina} Computador')
        linha()

    if pontos_jogador > pontos_maquina:
        titulo("YOU'RE A WINNER!")
    else:
        titulo("YOU'RE A LOSER!")

