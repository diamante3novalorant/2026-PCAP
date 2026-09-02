import random
from telas import titulo, linha


def jogar_forca():

    linha()

    print('=== JOGO DA FORCA ===')

    palavras = [
        'python',
        'jogo',
        'computador',
        'fliperama',
        'programacao'
    ]

    palavra = random.choice(palavras)

    letras_acertadas = []

    tentativas = 6

    while tentativas > 0:

        palavra_mostrada = ''

        for letra in palavra:

            if letra in letras_acertadas:
                palavra_mostrada = palavra_mostrada + letra
            else:
                palavra_mostrada = palavra_mostrada + '_'

        print()
        print('Palavra:', palavra_mostrada)
        print('Tentativas restantes:', tentativas)

        if '_' not in palavra_mostrada:

            linha()

            titulo("YOU'RE A WINNER!")

            linha()

            return

        letra = input('Digite uma letra: ').strip().lower()

        if len(letra) != 1:

            print('Opção inválida! Digite apenas uma letra.')

        elif letra in letras_acertadas:

            print('Você já tentou essa letra.')

        elif letra in palavra:

            print('Acertou!')

            letras_acertadas.append(letra)

        else:

            print('Errou!')

            letras_acertadas.append(letra)

            tentativas = tentativas - 1

    linha()

    titulo("YOU'RE A LOSER!")

    linha()

    print('A palavra era:', palavra)

    linha()