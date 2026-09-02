#=======================================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Fliperama"
# Aula : 20
# Arquivo : main.py
# Autor : Rodrigo Magagnin
# Data : 2026.08.04
# Conceitos : é o cérebro do jogo, tudo começa aqui
#======================================================================
# Importar funções de arquivos (módulos)
from telas import titulo,linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao
from ppt import jogar_ppt
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores, buscar, registrar_partida
from parimpar import jogar_parimpar
from meujogo import jogar_forca
NOMES_DOS_JOGOS = ['Adivinhe o Número', 'Pedra-Papel-Tesoura', 'Par ou Impar','Jogo da Forca']

vezes_jogado = carregar_placar()

while len(vezes_jogado) < len(NOMES_DOS_JOGOS):
    vezes_jogado.append(0)

jogadores = carregar_jogadores()
def mostrar_placar():
    titulo('PLACAR')
    for i in range(len(NOMES_DOS_JOGOS)):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')
        
NOME_DO_DONO = 'Rodz'
OPCOES = ['0', '1', '2', '3', '4','5']

while True:
    titulo(f'Fliperama do {NOME_DO_DONO} 🤑')
    print('[5] - Jogadores')
    print('[4] - Jogo da Forca (Meu jogo)')
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

    if opcao == '5':
        menu_jogadores(jogadores)

    else:
            indice = int(opcao) - 1
            vezes_jogado[indice] = vezes_jogado[indice] + 1
            jogador = registrar_partida(jogadores)
            if jogador == -1:
                continue

            salvar_placar(vezes_jogado)
            salvar_jogadores(jogadores)

            if opcao == '1':
                jogar_adivinhe()

            elif opcao == '2':
                jogar_ppt()

            elif opcao == '3':
                jogar_parimpar()

            elif opcao == '4':
                jogar_forca()

            input('Pressione Enter para voltar ao menu...')