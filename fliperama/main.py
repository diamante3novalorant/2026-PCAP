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
from modulos import ler_numero

NOME_DO_DONO = 'Rodz'
OPCOES = ['0', '1']

while True:
    titulo(f'Fliperama do {NOME_DO_DONO} 🤑')
    print('1- Jogo Adivinhe o Número')
    print('0 - Sair do fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        print('Até a Próxima!')
        break
    elif opcao == '1':
        linha()
        jogar_adivinhe()
