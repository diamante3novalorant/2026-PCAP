#=================================================================================================================
# Disciplina : Pensamento Computacional, Algorítmos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o Número"
# Arquivo    : advinhe.py
# Autor      : Rodrigo Magagnin
# Data       : 2026.06.07
#=================================================================================================================

import random

def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input(f"Seu palpite (1 a {maximo}): "))

        if palpite == numero_secreto:
            print("Parabéns Você venceu!.")
            return True  # termina o nível
        elif palpite < numero_secreto:
            print("Muito baixo!!")
        else:
            print("Muito alto!!")

        chances -= 1
        print("Chances restantes:", chances)
    
    print(f"Fim de jogo! O número era {numero_secreto}.")
    return False  # nao ganhou

# Lista de níveis: [nome, máximo, chances]

niveis = [
    ["Fácil", 10, 3],
    ["Médio", 100, 5],
    ["Impossível", 1000, 10],
]

for nivel in niveis:
    print(f"Nível: {nivel[0]} (1 a {nivel[1]}, {nivel[2]} chances)")
    venceu = jogar(nivel[1], nivel[2])
    if not venceu:
        print("Você perdeu! Fim de jogo.")
        break
else:
    print("Parabéns! Você venceu todos os níveis!")
