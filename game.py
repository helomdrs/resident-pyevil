# PYTHON TEXT RPG GAME
#BY HELOÍSA SILVA

# IMPORTANDO BIBLIOTECAS NECESSÁRIAS NO PROJETO #

#cmd para usar linhas de comando
import cmd
#permite a separação do texto em linhas
import textwrap
#para usar comandos do sistema
import sys
#para usar comandos do sistema operacional
import os
#para fazer operações com o tempo de execução
import time
#para utilizar funções de randomização
import random

#tamanho da tela do jogo
screenWidth = 100

# SETACIMA DA CLASSE DO PERSONAGEM # 

#classe iniciada como ela mesma, com os seguintes atributos
class personagem: 
    def __init__(self):
        self.nome = ''
        self.itens = []
        self.localizacao = 'z1'
        self.ganhouJogo = False
        
#criando um objeto do tipo player
player = personagem()

# TELA INICIAL #

#função que permite a seleção de opções do menu
def opcoesTelaInicial():
    #variável que vai guardar o input do usuário
    option = input("> ")
    #se o usuario escreveu "play", chama a função de começar o jogo
    if option.lower() == ("play"):
        iniciarJogo()
    #se o usuário escreveu "help", chama a função de exibir a tela de ajuda
    elif option.lower() == ("help"):
        menuAjuda()
    #se o usuario escreveu "quit", o sistema fechará o jogo
    elif option.lower() == ("quit"):
        sys.exit()
        
    #o sistema roda um loop enquanto nenhuma das três opções for digitada
    #exibindo uma mensagem para o usuário tentar novamente
    while option.lower() not in ['play', 'help', 'quit']:
        print("Opção não reconhecida. Por favor, tente novamente")
        option = input("> ")
        if option.lower() == ("play"):
            iniciarJogo()
        elif option.lower() == ("help"):
            menuAjuda()
        elif option.lower() == ("quit"):
            sys.exit()

#função que vai desenhar a tela inicial
def telaInicial():
    os.system('cls')
    print('############################')
    print('##     SEJA BEM-VINDO     ##')
    print('##      A CTRL+PLAY       ##')
    print('##       AE PYTHON        ##')   
    print('############################')
    print('                            ')
    print('         - PLAY -           ')
    print('         - HELP -           ')
    print('         - QUIT -           ')
    print('     Copyright TM 2020      ')
    opcoesTelaInicial()
    
#função que vai desenhar a tela de ajuda
def menuAjuda():
    os.system('cls')
    print('############################')
    print('##     SEJA BEM-VINDO     ##')
    print('##      A CTRL+PLAY       ##')
    print('##       AE PYTHON        ##')   
    print('############################')
    print('                            ')
    print('- Use cima, baixo, esquerda e direita para se movimentar')
    print('- Digite o seu comando para executá-lo')
    print('- Use "olhar" para inspecionar algo')
    print('- Boa sorte e se divirta!')
    input('> ')
    telaInicial()
       
## MAPA ##   
# ---------------------
# |  z1  |  z2 |  z3  |
# ---------------------
# |  z4  | z5  |  z6  |
# ---------------------
# |  z7  | z8 |   z9  |

#z7 - dentro da delegacia - achou uma espingarda
#z8 - dentro da igreja - chave de carro
#z9 - dentro do hospital - vacina

#variáveis constantes que serão utilizadas no gameplay
NOMEZONA = ''
DESCRICAO = 'DESCRICAO'
AOEXAMINAR = 'examine'
SOLUCIONADO = False
ACIMA = 'acima', 'norte'
ABAIXO = 'abaixo', 'sul'
AESQUERDA  = 'esquerda', 'oeste'
ADIREITA = 'direita', 'leste'

#dicionário com as informações de cada zona
mapaCidade = {
    'z1' : {
        NOMEZONA: 'Centro',
        DESCRICAO: 'Centro da cidade, com várias lojas e parques',
        AOEXAMINAR: 'Todas as lojas foram saqueadas, algumas queimadas. Os parques estão cheios de pássaros mortos.',
        SOLUCIONADO: False,
        ACIMA: 'none',
        ABAIXO: 'z4',
        AESQUERDA: 'none',
        ADIREITA: 'z2',
    }, 
    'z2' : {
        NOMEZONA: 'Suburbio',
        DESCRICAO: 'Grande área residencial da cidade',
        AOEXAMINAR: 'Algumas casas estão abertas, outras estão lacradas de maneira improvidada. Está tudo silencioso até demais.',
        SOLUCIONADO: False,
        ACIMA: 'none',
        ABAIXO: 'z5',
        AESQUERDA: 'z1',
        ADIREITA: 'z3',
    },
    'z3' : {
        NOMEZONA: 'Delegacia',
        DESCRICAO: 'Maior Departamento Policial da cidade, centro de operações policiais',
        AOEXAMINAR: 'O prédio está depredado, várias viaturas posicionadas como barreira se encontram pegando fogo ou quebradas, há um barulho de murmurio vindo de dentro do prédio',
        SOLUCIONADO: False,
        ACIMA: 'none',
        ABAIXO: 'z6',
        AESQUERDA: 'z2',
        ADIREITA: 'none',
    },
    'z4' : {
        NOMEZONA: 'Igreja',
        DESCRICAO: 'Maior centro religioso da cidade, com um grande salão.',
        AOEXAMINAR: 'Barricadas improvidadas cercam a igreja, mas parte dela está caída. Os vidros e as portas também foram lacradas com madeira. Não dá ver nada dentro do prédio.',
        SOLUCIONADO: False,
        ACIMA: 'z1',
        ABAIXO: 'z7',
        AESQUERDA: 'none',
        ADIREITA: 'z5',
    },
    'z5' : {
        NOMEZONA: 'Hospital',
        DESCRICAO: 'Hospital público da cidade.',
        AOEXAMINAR: 'Muitas ambulâncias cercam o local, há sangue e materiais hospitalares jogado pelo chão. Algumas entradas estão lacradas de maneira improvidsada.',
        SOLUCIONADO: False,
        ACIMA: 'z2',
        ABAIXO: 'z8',
        AESQUERDA: 'z4',
        ADIREITA: 'z6',
    },
    'z6' : {
        NOMEZONA: 'Prefeitura',
        DESCRICAO: 'O maior prédio da cidade, a prefeitura com fórum e câmara municipal.',
        AOEXAMINAR: 'Há uma grande barricada cercando o prédio, com algumas partes destruídas. Várias viaturas e carros também estão amontoados. Há barulhos de passos dentro do prédio.',
        SOLUCIONADO: False,
        ACIMA: 'z3',
        ABAIXO: 'z9',
        AESQUERDA: 'z5',
        ADIREITA: 'none',
    },
    'z7' : {
        NOMEZONA: 'Sala do Delegado',
        DESCRICAO: 'A sala está toda revirada, com mesas dispostas como se fossem uma barreira para a janela, há jornais espalhados pelo chão.',
        AOEXAMINAR: 'O jornal diz que pessoas atacaram outras, comendo-as. Você encontrou uma espingarda debaixo dos papéis, com apenas uma bala.',
        SOLUCIONADO: False,
        ACIMA: 'z4',
        ABAIXO: 'none',
        AESQUERDA: 'none',
        ADIREITA: 'z8',
    },
    'z8' : {
        NOMEZONA: 'Salão Comunitário',
        DESCRICAO: 'O cheio de sangue e pessoas mortas é forte, há muitos objetos espalhos pelo chão.',
        AOEXAMINAR: 'Você encontrou uma chave de um carro que estava lá fora. Uma pessoa (se isso pode ser chamado de pessaoa) está te atacando!',
        SOLUCIONADO: False,
        ACIMA: 'z5',
        ABAIXO: 'none',
        AESQUERDA: 'z7',
        ADIREITA: 'z9',
    },
    'z9' : {
        NOMEZONA: 'Laboratório',
        DESCRICAO: 'O laboratório está todo revirado e destruído, mas uma caixa permanece segura dentro de uma, a porta não está trancada.',
        AOEXAMINAR: 'Você encontrou uma vacina, mas apenas uma.',
        SOLUCIONADO: False,
        ACIMA: 'z6',
        ABAIXO: 'none',
        AESQUERDA: 'z8',
        ADIREITA: 'none',
    }
}

## INTERATIVIDADE DO JOGO ##

#função para mostrar a localização do jogador no mapa
def mostrarLocalizacao():
    print('===================================')
    print(mapaCidade[player.localizacao][NOMEZONA].upper())
    print(mapaCidade[player.localizacao][DESCRICAO])
    print('===================================')

#função para pegar a ação do usuário
def prompt():
    print('\n' + '=================================')
    print('O que você gostaria de fazer?')
    acao = input('> ')
    acoesAceitaveis = ['andar', 'mover', 'examinar', 'sair', 'inspecionar', 'olhar', 'interagir']
    while acao.lower() not in acoesAceitaveis:
        print('Ação desconhecida. Por favor, tente novamente. \n')
        acao.input('> ')
    if acao.lower() == 'sair':
        sys.exit()
    elif acao.lower() in ['andar', 'mover']:
        moverPlayer(acao.lower())
    elif acao.lower() in ['inspecionar', 'olhar', 'examinar', 'interagir']:
        playerExaminar(acao.lower())

#função de mover o personagem principal
def moverPlayer(acao):
    pergunta = "Para onde você gostaria de se mover? \n"
    movimento = input(pergunta)
    if movimento in ['acima', 'norte']:
        if mapaCidade[player.localizacao][ACIMA] == 'none':
            print('\nNão é possível ir por aí, escolha outro caminho')
            prompt()
        else:
            destino = mapaCidade[player.localizacao][ACIMA]
            gerenciadorMovimento(destino)
    elif movimento in ['abaixo', 'sul']:
        if mapaCidade[player.localizacao][ABAIXO] == 'none':
            print('\nNão é possível ir por aí, escolha outro caminho')
            prompt()
        else:
            destino = mapaCidade[player.localizacao][ABAIXO]
            gerenciadorMovimento(destino)
    elif movimento in ['esquerda', 'oeste']:
        if mapaCidade[player.localizacao][AESQUERDA] == 'none':
            print('\nNão é possível ir por aí, escolha outro caminho')
            prompt()
        else:
            destino = mapaCidade[player.localizacao][AESQUERDA]
            gerenciadorMovimento(destino)
    elif movimento in ['direita', 'leste']:
        if mapaCidade[player.localizacao][ADIREITA] == 'none':
            print('\nNão é possível ir por aí, escolha outro caminho')
            prompt()
        else:
            destino = mapaCidade[player.localizacao][ADIREITA]
            gerenciadorMovimento(destino)
        
#função que gerencia o movimento do personagem principal
def gerenciadorMovimento(destino):
    player.localizacao = destino
    mostrarLocalizacao()

def playerExaminar(acao):
    if mapaCidade[player.localizacao][SOLUCIONADO]:
        print("Não há nada mais de interessante aqui.")
    else:
        print(mapaCidade[player.localizacao][AOEXAMINAR])
        mapaCidade[player.localizacao][SOLUCIONADO] = True
        if mapaCidade[player.localizacao][NOMEZONA] == 'Sala do Delegado':
            if 'Espingarda' in player.itens == False:
                player.itens.append('Espingarda')
                print('\nVocê coletou a Espingarda. \n')
        if mapaCidade[player.localizacao][NOMEZONA] == 'Salão Comunitário':
            if 'Chave de Carro' in player.itens == False:
                player.itens.append('Chave de Carro')
                print('\nVocê coletou a Chave do Carro. \n')
                time.sleep(0.5)
                if 'Espingarda' in player.itens:
                    print('Atirar na pessoa que o ataca?\n')
                    acao = input('> ')
                    if acao.lower in ['atirar', 'sim']:
                        print('\nVocê matou quem te atacava, liberando o caminho até o carro. Você fugiu da cidade no carro o mais rápido possível.')
                        gameOver('fugiu')
                    elif acao.lower in ['fugir', 'não', 'não atirar']:
                        print('\nVocê não atirou em quem te atacava e acabou sendo mordido!')
                        if 'Vacina' in player.itens:
                            print('Usar a Vacina em si mesmo?\n')
                            acao = input('> ')
                            if acao.lower in ['usar', 'sim']:
                                print('\nVocê utilizou a vacina em si mesmo. Mas essa história ainda está longe de acabar.')
                                gameOver('não infectado')
                            elif acao.lower in ['não', 'não usar']:
                                print('\nVocê não utilizou a vacina em si mesmo. Uma raiva incontrolável já toma conta de sua mente.')
                                gameOver('infectado')
                else:
                    print('Você tentou fugir da pessoa que o atacava, mas ele foi mais rápido e você acabou sendo mordido.\n')
                    gameOver('infectado')
        if mapaCidade[player.localizacao][NOMEZONA] == 'Laboratório':
            if 'Vacina' in player.itens == False:
                player.itens.append('Vacina')
                print('\nVocê coletou a vacina.')
                print('\nVárias pessoas loucas invadiram a sala em que você está')
                time.sleep(0.5)
                print('\nE elas estão te atacando!')
                if 'Espingarda' in player.itens:
                    print('Atirar nas pessoas que o ataca?\n')
                    acao = input('> ')
                    if acao.lower in ['atirar', 'sim']:
                        print('\nVocê matou algumas pessoas, mas eles eram muitos e você acabou sendo mordido mesmo assim!')
                        time.sleep(0.5)
                        print('\nVocê quer usar a vacina que conseguiu?')
                        acao = input('> ')
                        if acao.lower in ['sim', 'usar']:
                            print('\nVocê usou a vacina em si mesmo.')
                            if 'Chave do Carro' in player.itens:
                                gameOver('fugiu')
                            else:
                                gameOver('não infectado')
                        elif acao.lower in ['não', 'não usar']:
                            print('\nVocê não usou a vacina em si mesmo, sabendo que não lhe resta muito tempo de vida.')
                            time.sleep
                            if 'Chave do Carro'in player.itens:
                                gameOver('fugiu infectado')
                else:
                    print('\nVocê conseguiu fugir daqueles que te atacam com a vacina')
                    if 'Chave do Carro' in player.itens:
                        gameOver('fugiu com vacina')
                    else:
                        gameOver('não infectado')
                    
                
# FUNCIONAMENTO DO JOGO #

#função de game over
def gameOver(causa):
    return
    
#loop principal do jogo
def loopPrincipal():
    while player.ganhouJogo is False:
        prompt()

        #fazer verificações aqui
        
#função de começar devidamente o jogo
def iniciarJogo():
    os.system('cls')
    
    #Pega a informação do nome do usuario
    pergunta1 = "Olá estranho, qual o seu nome? \n"
    #loop que cria efeito de digitação
    for char in pergunta1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    #guarda o nome do player através do input
    player.nome = input('> ')
    
    #diz o nome ao usuario
    mensagem1 = "Olá, " + player.nome
    #loop que cria efeito de digitação
    for char in mensagem1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    mensagem2 = "\nVejo que está acordado, finalmente! \nAlgo muito estranho aconteceu nesta cidade, mas tenho muito medo de ir lá fora.... \nEspera, você vai? Então é melhor tomar muito, muito cuidado!\n"
    for char in mensagem2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    
    input('> ')
    os.system('cls')
    mostrarLocalizacao()
    loopPrincipal()
        
        
#chama a tela inicial
telaInicial()