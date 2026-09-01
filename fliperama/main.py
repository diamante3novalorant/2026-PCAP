#=======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Fliperama"
# Aula : 20
# Arquivo : main.py
# Autor : Rodrigo Magagnin
# Data : 2026.08.04
# Conceitos : 
#======================================================================
# Importar funções de arquivos (módulos)
from telas import titulo,linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao
from ppt import jogar_ppt
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores, buscar
from parimpar import jogar_parimpar

NOMES_DOS_JOGOS = ['Adivinhe o Número', 'Pedra-Papel-Tesoura', 'Par ou Impar']

vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()
def mostrar_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')
        
NOME_DO_DONO = 'Rodz'
OPCOES = ['0', '1', '2' , '3', '4']

while True:
    titulo(f'Fliperama do {NOME_DO_DONO} 🤑')
    print('[4] - Jogadores')
    print('[3] - Jogo Par ou ímpar')
    print('[2] - Jogo Pedra, Papel, Tesoura')
    print('[1] - Jogo Adivinhe o Número')
    print('[0] - Sair do fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':

        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        linha()
        titulo('Até a Próxima!')

        break

    if opcao == '4':
        menu_jogadores(jogadores)

    else:
        apelido = input('Digite o apelido do jogador: ').strip().lower()
        i = buscar(jogadores, apelido)
        if i == -1:
            print('Jogador não encontrado.')

        else:
            indice = int(opcao) - 1
            vezes_jogado[indice] = vezes_jogado[indice] + 1
            jogadores[i][2] = str(int(jogadores[i][2]) + 1)
            print('Partida registrada para ' + jogadores[i][1] + '.')

            if opcao == '1':
                jogar_adivinhe()

            elif opcao == '2':
                jogar_ppt()

            elif opcao == '3':
                jogar_parimpar()

            input('Pressione Enter para voltar ao menu...')