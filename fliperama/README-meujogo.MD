Jogo da Forca
Sobre o jogo
O Jogo da Forca é um jogo simples em Python onde o computador escolhe uma palavra aleatória e o jogador precisa descobrir a palavra, tentando uma letra por vez.

O jogador possui 6 tentativas. A cada letra errada, uma tentativa é perdida. Se conseguir descobrir todas as letras antes de acabar as tentativas, o jogador vence.

Fundamentos usados
random
É usado para escolher uma palavra aleatória da lista:

palavra = random.choice(palavras)

Lista
usei uma lista para armazenar as palavras possíveis:

palavras = ['python', 'jogo', 'computador', 'fliperama', 'programacao']

Também é usada uma lista para guardar as letras que o jogador já acertou:

letras_acertadas = []

while
O while faz o jogo funcionar enquanto o jogador ainda tiver tentativas:

while tentativas > 0:

for
O for olha cada letra da palavra para mostrar quais letras já foram descobertas:

for letra in palavra:

if, elif e else
São utilizados para verificar as situações do jogo, como:

Se o jogador acertou a letra.
Se a letra já foi escolhida.
Se a letra está errada.
Se o jogador venceu ou perdeu.
input()
É utilizado para receber a letra escolhida pelo jogador:

letra = input('Digite uma letra: ')

append()
Adiciona uma letra à lista de letras já utilizadas:

letras_acertadas.append(letra)

Função
O jogo inteiro fica dentro de uma função chamada jogar_forca():

def jogar_forca():

Isso permite chamar o jogo pelo menu principal do fliperama.

Objetivo
O objetivo do jogo é praticar conceitos básicos de Python, como:

Variáveis
Listas
Funções
Condições
Laços de repetição
Entrada de dados
Biblioteca random