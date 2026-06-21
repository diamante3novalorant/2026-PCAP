#=======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Pedra-Papel-Tesoura"
# Arquivo : ppt.py
# Autor : Rodrigo Magagnin
# Data : 2026.06.21
#=======================================================================

import random

# === Sub-rotina: decide o resultado de UMA rodada e devolve um texto ===
def resultado(jogador, maquina):
     #Testa caso a caso; 1º retorno que bater já encerra a função
    if jogador == maquina:
        return "empate"

    if jogador == "pedra" and maquina == "tesoura":
        return "jogador"
    
    if jogador =="pedra" and maquina == "lagarto":
        return "jogador"

    if jogador == "papel" and maquina == "pedra":
        return "jogador"

    if jogador == "papel" and maquina == "spock":
        return "jogador"
    
    if jogador == "tesoura" and maquina == "papel":
        return "jogador"
    
    if jogador =="tesoura" and maquina == "lagarto":
        return "jogador"
     
    if jogador == "lagarto" and maquina == "spock":
        return "jogador"
    
    if jogador == "lagarto" and maquina == "papel":
        return "jogador"
    
    if jogador == "spock" and maquina == "tesoura":
        return "jogador"
    
    if jogador == "spock" and maquina == "pedra":
        return "jogador"

    return "maquina"


# === Programa principal: joga as rodadas e cuida do placar ===
opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]

pontos_jogador = 0
pontos_maquina = 0

for rodada in range(1, 6):
    print("---Rodada", rodada, "---")

    jogada_maquina = random.choice(opcoes)

    # leitura enxuta: ler + .lower() + .strip()em uma linha só
    jogada_jogador = input("Tua jogada: ").lower().strip()
    print("A máquina jogou:", jogada_maquina)
    if jogada_jogador not in opcoes:
        print("Jogada inválida! Você perdeu a rodada.")
        pontos_maquina = pontos_maquina + 1
    else:
        quem = resultado(jogada_jogador, jogada_maquina) # chamamos a sub-rotina

        if quem == "empate":
            print("Empate!")
        elif quem == "jogador":
            print("Tu ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
        else:
            print("A máquina ganhou a rodada!")
            pontos_maquina = pontos_maquina + 1

print("Placar final => Você:", pontos_jogador, "| Máquina:", pontos_maquina)
if pontos_maquina > pontos_jogador:
    print("Perdeu pro bot KKKKKKKKKKKKKKKKKKKKKK")
if pontos_jogador > pontos_maquina:
    print("Parabéns, tu ganhou!")
if pontos_jogador == pontos_maquina:
    print("Empate!")
