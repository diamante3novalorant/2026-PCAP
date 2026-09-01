from os.path import exists
from telas import titulo, linha
from modulos import ler_opcao

ARQUIVO = 'jogadores.csv'
#==========================================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Fliperama"
# Aula : 22
# Arquivo : jogadores.py
# Autor : Rodrigo Magagnin
# Data : 2026.09.01
# Conceitos : Registro como lista de campos, cadatro com linha de listas, cadastrar,
#             listar, buscar, alterar, excluir, persistência em arquivo .csv
#==========================================================================================
#
#==========================================================================================
# O QUE ESTE ARQUIVO É?
# A quarta gaveta do projeto. O telas.py cuida do que aparece, o modulos cuida do que o 
# progama pergunta, o placar.py cuida de quantas partidas cada jogo teve, e o jogadores.py
# cuida de quem jogou.
#
# O REGISTRO
# Cada jogador é uma lista de três campos, sempre nesta ordem:
#       Indice 0 => apelido / 1 => nome / 2 => partidas
#     E o cadastro é uma lista dessas listas.
#==========================================================================================


def cadastrar(jogadores):
    titulo('NOVO JOGADOR')

    apelido = input('Apelido (sem espaços):').strip().lower()
    nome = input('Nome completo: ').strip()

    novo = [apelido, nome, '0']
    jogadores.append(novo)

    print('Jogador ' + apelido + ' cadastrado.')
    linha()

def listar(jogadores):
    titulo('JOGADORES CADASTRADOS')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastrado ainda.')
    else:
        for jogador in jogadores:
            print(jogador[0] + '|' + jogador[1] + '|' + jogador [2] + ' partidas')

    linha()


def buscar(jogadores, apelido):
    # Devolve a POSIÇÃO do jogador na lsta, ou -1 se não achar.
    for i in range(len(jogadores)):
        if jogadores[i][0] == apelido:
            return i


    return -1

def alterar(jogadores):
    listar(jogadores)

    apelido = input('Apelido de quem vai mudar de nome: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Não achei ninguém com esse apelido.')
    else:
        print('Nome atual: ' + jogadores[i][1])
        jogadores[i][1] = input('Nome novo: ').strip()
        print('Pronto. Agora e ' + jogadores [i][1] + '.')

    linha()

def excluir(jogadores):
    listar(jogadores)

    apelido = input('Apelido de quem vai sair do cadastro: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Não achei ninguém com esse apelido')
    else:
        print('Vou apagar o cadastro de ' + jogadores[i][1] + '.')
        print('[1] Confirmar')
        print('[2] Deixar como está')
        certeza = ler_opcao('Sua escolha', ['1', '2'])

        if certeza == '1':
            jogadores.pop(i)
            print('Cadastro apagado.')
        else:
            print('Nada foi apagado')

    linha()


def salvar_jogadores(jogadores):
    arquivo = open(ARQUIVO, 'w')

    for jogador in jogadores:
        arquivo.write(jogador[0] + ',' + jogador[1] + ',' + jogador[2] + '\n')

    arquivo.close()

def carregar_jogadores():
    if not exists(ARQUIVO):
        return []
    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    lidos = []
    for linhas_lida in linhas:
        campos = linhas_lida.strip().split(',')
        lidos.append(campos)

    return lidos

def menu_jogadores(jogadores):
    while True:
        titulo('CADASTRO DE JOGADORES')
        print('[1] Cadastrar jogador')
        print('[2] Listar jogadores')
        print('[3] Alterar nome')
        print('[4] Excluir jogador')
        print('[0] Voltar ao fliperama')
        linha()

        opcao = ler_opcao('Tua escolha', ['0', '1', '2', '3', '4'])

        if opcao == '0':
            break
        elif opcao == '1':
            cadastrar(jogadores)
            salvar_jogadores(jogadores)
        elif opcao == '2':
            listar(jogadores)
            salvar_jogadores(jogadores)
        elif opcao == '3':
            alterar(jogadores)
            salvar_jogadores(jogadores)
        else:
            excluir(jogadores)
            salvar_jogadores(jogadores)
        