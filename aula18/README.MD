##Jogo Par ou Ímpar

Este é um dos jogos do projeto Fliperama, feito em Python.

A ideia é jogar Par ou Ímpar contra o computador. O jogador escolhe par ou ímpar e depois escolhe um número de 0 a 10. O computador sorteia outro número e os dois são somados.

##Como funciona

O programa pergunta:

Escolha par ou impar:


Depois pede um número entre 0 e 10.

O computador sorteia seu número usando:

computador = random.randint(0, 10)


No final, os dois números são somados e vemos se o resultado é par ou ímpar.

Função quem_venceu()

A decisão do vencedor foi colocada em uma função separada:

def quem_venceu(soma, aposta):


Ela recebe a soma dos números e a aposta do jogador.

Primeiro verifica se a soma é par ou ímpar. Depois compara com a escolha do jogador e retorna:

Você ganhou!


ou:

O computador ganhou!


A função principal chama assim:

print(quem_venceu(soma, escolha))


Separei essa parte porque achei mais organizado deixar a função principal cuidando da partida e outra função cuidando somente da decisão de quem venceu.

Validações

O programa verifica se:

o jogador escolheu par, impar ou ímpar;

o número está entre 0 e 10;

o que foi digitado como número realmente é um número.

Conceitos usados

Neste jogo foram usados:

if e else;

while;

input();

try e except;

random;

funções;

parâmetros e return.

Esse jogo faz parte do projeto Fliperama da disciplina de Pensamento Computacional, Algoritmos e Programação.