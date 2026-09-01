#=======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Fliperama"
# Aula : 20
# Arquivo : modulos.py
# Autor : Rodrigo Magagnin
# Data : 2026.08.04
# Conceitos : 
#=================================================================
def ler_opcao(mensagem,validas):
    resposta = input(mensagem + ": ").strip().upper()
    while resposta not in validas:
        print("Opção inválida! Tenta de novo.")
        resposta = input(mensagem + ": ").strip().upper()
    return resposta

def ler_numero(mensagem, minimo, maximo):
    numeros = []
    for n in range(minimo, maximo + 1):
        numeros.append(str(n))
    return int(ler_opcao(mensagem, numeros))

