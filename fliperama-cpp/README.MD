# Fliperama em C++ (MeuApp v4.0)

## O que é

O fliperama é um projeto criado pelo professor Berssa na matéria PCAP para aperfeiçoar nossas habilidades em Python, C e posteriormente em C++.

Ele consiste em um jogo e outras funcionalidades, como cadastro e listagem de jogadores, além de um sistema que registra quantas partidas cada jogador realizou.

O projeto utiliza dois vetores que crescem automaticamente e um arquivo CSV para armazenar os jogadores e suas respectivas partidas.

## Como compilar e rodar

Para compilar:

```bash
g++ -Wall fliperama.cpp -o fliperama
```

Para executar:

```bash
./fliperama
```

## Arquivos

- `fliperama.cpp` — Código-fonte do projeto.
- `jogadores.csv` — Arquivo que armazena os apelidos dos jogadores e a quantidade de partidas.

## O que mudou do C?

| Operação | Python | C | C++ |
|---|---|---|---|
| Guardar um jogador | `jogadores.append(novo)` | `strcpy(apelidos[qtd], novo)` | `apelidos.push_back(novo)` |
| Comparar apelidos | `==` | `strcmp()` | `==` |
| Descobrir o tamanho | `len(jogadores)` | Contador manual | `apelidos.size()` |
| Abrir arquivo | `open(ARQUIVO, 'w')` | `fopen(ARQUIVO, "w")` | `ofstream arquivo(ARQUIVO)` |
| Ler arquivo | `open(ARQUIVO, 'r')` | `fopen(ARQUIVO, "r")` | `ifstream arquivo(ARQUIVO)` |

**Diferenças:**

- **Adicionar elementos:** em C++ usamos `push_back()`, que adiciona automaticamente um elemento ao final do vetor.
- **Comparar strings:** em C++ podemos utilizar `==` para comparar diretamente duas strings.
- **Descobrir o tamanho:** utilizamos `.size()` para descobrir quantos elementos existem no vetor.
- **Abrir arquivos:** utilizamos `ifstream` para leitura e `ofstream` para escrita, sem precisar fechar manualmente o arquivo.

## O que o C++ decidiu por mim?

- Crescimento automático dos vetores com `push_back()`.
- Comparação de strings utilizando `==`.
- Descoberta automática da quantidade de elementos com `.size()`.
- Abertura e fechamento automático de arquivos com `ifstream` e `ofstream`.
- Manipulação de textos utilizando `string`.
- Controle de partidas utilizando dois vetores paralelos.

## Validação de cadastro

Foi adicionada uma verificação para impedir que o mesmo jogador seja cadastrado mais de uma vez.

A função `buscar()` verifica se o apelido já existe no vetor de jogadores.

Se encontrar o apelido, retorna sua posição. Caso não encontre, retorna `-1`.

A comparação também ignora diferenças entre letras maiúsculas e minúsculas. Assim, `Rodrigo` e `rodrigo` são considerados o mesmo apelido.

## Autoavaliação

| Critério | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilação e Git | A | `fliperama.cpp`, linhas 1 a 23 (estrutura e bibliotecas); compilação com g++ e organização dos arquivos no Git. |
| 2. Cadastro: menu, funções e vetores | A | Linhas 110 a 140 (cadastro, validação de duplicatas e listagem); linhas 180 a 191 (menu); linhas 193 a 215 (controle das opções). |
| 3. Jogo e partidas | A | Linhas 142 a 178 (jogo de adivinhação, identificação do jogador e contagem de partidas). |
| 4. Persistência | A | Linhas 84 a 108 (salvar e carregar jogadores); linhas 197 a 217 (carregamento na entrada e salvamento na saída). |
| 5. Documentação e comparação | A | `README.md`, seções O que é, O que mudou do C?, O que o C++ decidiu por mim? e Autoavaliação. |
