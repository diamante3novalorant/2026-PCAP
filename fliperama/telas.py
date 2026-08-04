#=======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Fliperama"
# Aula : 20
# Arquivo : telas.py
# Autor : Rodrigo Magagnin
# Data : 2026.08.04
# Conceitos : 
#=======================================================================

# Definição da moldura Caracteres e tamnho
CAR = '-'
TAM = 60


# Desenha uma linha na tela
def linha():
    print(CAR * TAM)

linha()

# Função para desenhar um texto entre linhas
def titulo(texto):
    print(texto.center(TAM))
    linha()
