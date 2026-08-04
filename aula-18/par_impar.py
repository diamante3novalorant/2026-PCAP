# ════════════════════════════════════════════════════════════
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Rodrigo Magagnin
# Data       : 2026.06.25
# ════════════════════════════════════════════════════════════
import random

numero = random.randint(0, 5)
pp = 0
pm = 0
entrada = input("Par ou Ímpar? ")
escolha = entrada.lower().strip()
opcoes = ["par", "impar", "ímpar"]

jogada = int(input("Escolha um Número: ")) 
opcoesnumeros = [0, 1, 2, 3, 4, 5]
if jogada not in opcoesnumeros and opcoes:
    print("Jogada Inválida")
    pm = pm + 1
jogadamaquina = numero
print("A máquina jogou: ", jogadamaquina)
def soma(jogadamaquina, jogada): 
    carambolas = (jogadamaquina + jogada) % 2
    if carambolas == 1:
        return "impar"
    else:
        return "par"
blabla = soma(jogadamaquina, jogada)
def winner(escolha, resultado):
    if escolha == resultado:
        return "jogador"
    return "maquina"
resultado = soma(jogadamaquina, jogada)
vencedor = winner = (escolha, resultado)
if vencedor == "jogador":
    print("Tu venceu")
    pp = pp + 1
else:
    print("Perdeu pro bot kk")
    pm = pm + 1


    
