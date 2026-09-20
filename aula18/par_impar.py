# ════════════════════════════════════════════════════════════
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Rodrigo Magagnin
# Data       : 2026.06.25
# ════════════════════════════════════════════════════════════
import random


def quem_venceu(soma, aposta):
    """Decide quem venceu com base na soma e na aposta do jogador."""

    if soma % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'

    if resultado == aposta or (resultado == 'impar' and aposta == 'ímpar'):
        return 'Você ganhou!'
    else:
        return 'O computador ganhou!'


def par_ou_impar():
    """Executa uma partida de Par ou Ímpar contra o computador."""

    print('===== PAR OU ÍMPAR =====')

    while True:
        escolha = input('Escolha par ou impar: ').strip().lower()

        if escolha in ['par', 'impar', 'ímpar']:
            break

        print('Escolha inválida. Digite par ou impar.')

    while True:
        try:
            jogador = int(input('Digite um número de 0 a 10: '))

            if 0 <= jogador <= 10:
                break

            print('Digite um número entre 0 e 10.')
        except ValueError:
            print('Digite apenas números.')

    computador = random.randint(0, 10)
    soma = jogador + computador

    print(f'Tu escolheu: {escolha}')
    print(f'Teu número: {jogador}')
    print(f'Número do computador: {computador}')
    print(f'Soma: {soma}')

    print(quem_venceu(soma, escolha))


par_ou_impar()
