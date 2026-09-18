# Fliperama do Rodrigo 

Um fliperama de terminal com três joguinhos simples, um placar que não esquece e um registro que não esquece de quem se cadastra,
projeto da disciplina PCAP 1º ano de Informática


# O que ele faz?

São três jogos pelo menu: o Adivinhe o Nº, o Pedra papel tesoura e o par ou impar.
O placar conta quantas vezes cada jogo foi jogado e continua mesmo depois de fechar o programa.
cadastro de jogadores, Podendo criar, excluir, alterar e listar.

# Como eu rodo o jogo?

escrevendo no teu terminal o seguinte:
cd fliperama (Para sair da main e entrar no repositório fliperama)
python3 main.py (Para rodar a main.py do fliperama).
(Escrever python3 main.py equivale a apertar o botão de iniciar lá em cima)

# Os arquivos:
main.py: O arquivo que dá vida ao jogo, nele encontram-se todas as funções criadas.
telas.py: Ferramentas visuais.
modulos.py: As ferramentas lógicas.
jogadores.py: O cadastro de quem joga o fliperama, tem várias funções, como excluir, alterar, etc.
jogadores.csv: Guarda os Jogadores.
placar.py: Vê o número de vezes que cada jogo foi jogado e manda pro .csv guardar.
placar.csv: Guarda os Placares do jogo.
ppt.py: O jogo pedra papel tesoura do fliperama.
parimpar.py: O jogo par ou impar do fliperama.
adivinhe.py: O jogo adivinhe o número do fliperama.
meujogo.py: Meu jogo autoral (Jogo da Forca).
README.MD: Documentação do repositório.
README-meujogo.MD: Documentação do meujogo.py.

A função 'ler_texto' fica no módulos porque mesmo não sendo uma função lógica ficando ali ela ajuda na organização
geral do repositório, porque a meu ver não faz sentido do nada um 'ler_texto' gigante no meio do jogadores.py quando
tenho um arquivo feito pra guardas esse tipo de função.

# AUTOAVALIAÇÃO
Mereço um C, pois fiz tudo o básico pedido não tenho nada feito a mais além do pedido, então nem tenho linhas para provar merecer uma nota melhor.

# IA
Sim, usei um pouco de IA na parte do meu jogo em algumas coisas que eu tinha um pouco de dúvidas,
porém garanto que sei de tudo que escrevi e pra que serve no código.

def listar(jogadores):

    # Exibe os jogadores ordenados pelo número de partidas.

    titulo('JOGADORES CADASTRADOS')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastrado ainda.')
    else:
        jogadores.sort(key=lambda jogador: int(jogador[2]), reverse=True)

        for jogador in jogadores[:10]:
            print(jogador[0] + '|' + jogador[1] + '|' + jogador[2] + ' partidas')

essa foi uma das partes que usei ia por exemplo, mas após uma leve pesquisa descobri pra que serve cada
coisa nessa parte, por exemplo:
A parte key=lambda serve pra personalizar a ordem de ordenação dos elementos.
