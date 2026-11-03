# Fliperama em C (MeuApp v3.0)

## O que é
# O fliperama é um projeto criado pelo professor Berssa na matéria PCAP para aperfeiçoar nossas habilidades em Python e posteriormente em C.
# Ele consiste de um jogo e outras coisas, como cadastro e listagem de jogadores.

## Como compilar e rodar
# gcc -Wall fliperama.c -o fliperama
# ./fliperama

## Arquivos
# fliperama.c
# jogadores.csv

## O que mudou do Python?
# Guardar um jogador | jogadores.append(novo) (linha 41 py) | strcpy(apelidos[qtd], novo) (linha 76);
# diferença: .append()  | Controle manual/vetor;
# Comparar apelidos | if jogadores[i][0].strip().lower() == apelido: (linha 71 py) |  if (strcmp(apelidos[i], procurado) == 0) (linha 76)
# diferença | só precisa do == | precisa do strcmp() == 0;
# Abrir sem arquivo | arquivo = open(ARQUIVO, 'w') (linha 124 py) | FILE *arquivo = fopen(ARQUIVO, "w") (linha 140);
# diferença :  pergunta se o arquivo existe | pergunta se conseguiu abrir o arquivo;

## O que o C me obrigou a decidir
# Comparação de strings (if (strcmp(nome, procurado) == 0)),  Adicionar elementos em uma lista (jogadores[qtd] = novo, qtd++;), Descobrir o tamanho de uma lista (int qtd = 0;) Abrir arquivos (FILE *arquivo = fopen("dados.txt", "r"));

## Autoavaliação
| Critério | Conceito que espero | Onde se prova (arquivo e linha)
| 1. Estrutura, compilação e git |Estrutura|A|Tudo foi feito corretamente|
| 2. Cadastro: menu, funções e vetores |menu|A|153 a 161|
| 3. Jogo e partidas |Jogo|A|99 a 126|
| 4. Persistência |persistência|A| 129 a 151|
| 5. Documentação e comparação |Documentação|A|README.MD|
 