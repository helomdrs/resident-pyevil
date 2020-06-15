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

# SETUP DA CLASSE DO PERSONAGEM # 

#classe iniciada como ela mesma, com os seguintes atributos
class personagem: 
    def __init__(self):
        self.nome = ''
        self.vida = 0
        self.magia = 0
        self.poderes = []
        self.localizacao = 'z0'
        
#criando um objeto do tipo player
player = personagem()

# TELA INICIAL #

#função que permite a seleção de opções do menu
def titleScreenSelecions():
    #variável que vai guardar o input do usuário
    option = input("> ")
    #se o usuario escreveu "play", chama a função de começar o jogo
    if option.lower() == ("play"):
        startGame()
    #se o usuário escreveu "help", chama a função de exibir a tela de ajuda
    elif option.lower() == ("help"):
        helpMenu()
    #se o usuario escreveu "quit", o sistema fechará o jogo
    elif option.lower() == ("quit"):
        sys.exit()
        
    #o sistema roda um loop enquanto nenhuma das três opções for digitada
    #exibindo uma mensagem para o usuário tentar novamente
    while option.lower() not in ['play', 'help', 'quit']:
        print("Opção não reconhecida. Por favor, tente novamente")
        option = input("> ")
        if option.lower() == ("play"):
            startGame()
        elif option.lower() == ("help"):
            helpMenu()
        elif option.lower() == ("quit"):
            sys.exit()

#função que vai desenhar a tela inicial
def titleScreen():
    os.system('clear')
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
    titleScreenSelecions()
    
#função que vai desenhar a tela de ajuda
def helpMenu():
    os.system('clear')
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
    
# FUNCIONAMENTO DO JOGO #
    
#função de começar devidamente o jogo
def startGame():
    print('Jogo iniciado')
    
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
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT  = 'left', 'west'
RIGH = 'right', 'east'

#dicionário dos lugares que o jogador vai passar?
lugaresVisitados = {'z1': False, 'z2': False, 'z3': False, 'z4': False, 'z5': False, 'z6': False}

#dicionário com as informações de cada zona
mapaCidade = {
    'z1' : {
        ZONENAME : 'Centro',
        DESCRIPTION : 'Centro da cidade, com várias lojas e parques',
        EXAMINATION : 'Todas as lojas foram saqueadas, algumas queimadas. Os parques estão cheios de pássaros mortos.',
        SOLVED : False,
        UP : 'none',
        DOWN : 'z4',
        LEFT  : 'none',
        RIGH : 'z2',
    }, 
    'z2' : {
        ZONENAME : 'Suburbio',
        DESCRIPTION : 'Grande área residencial da cidade',
        EXAMINATION : 'Algumas casas estão abertas, outras estão lacradas de maneira improvidada. Está tudo silencioso até demais.',
        SOLVED : False,
        UP : 'none',
        DOWN : 'z5',
        LEFT  : 'z1',
        RIGH : 'z3',
    },
    'z3' : {
        ZONENAME : 'Delegacia',
        DESCRIPTION : 'Maior Departamento Policial da cidade, centro de operações policiais',
        EXAMINATION : 'O prédio está depredado, várias viaturas posicionadas como barreira se encontram pegando fogo ou quebradas, há um barulho de murmurio vindo de dentro do prédio',
        SOLVED : False,
        UP : 'none',
        DOWN : 'z6',
        LEFT  : 'z2',
        RIGH : 'none',
    },
    'z4' : {
        ZONENAME : 'Igreja',
        DESCRIPTION : 'Maior centro religioso da cidade, com um grande salão.',
        EXAMINATION : 'Barricadas improvidadas cercam a igreja, mas parte dela está caída. Os vidros e as portas também foram lacradas com madeira. Não dá ver nada dentro do prédio.',
        SOLVED : False,
        UP : 'z1',
        DOWN : 'z7',
        LEFT  : 'none',
        RIGH : 'z5',
    },
    'z5' : {
        ZONENAME : 'Hospital',
        DESCRIPTION : 'Hospital público da cidade.',
        EXAMINATION : 'Muitas ambulâncias cercam o local, há sangue e materiais hospitalares jogado pelo chão. Algumas entradas estão lacradas de maneira improvidsada.',
        SOLVED : False,
        UP : 'z2',
        DOWN : 'z8',
        LEFT  : 'z4',
        RIGH : 'z6',
    },
    'z6' : {
        ZONENAME : 'Prefeitura',
        DESCRIPTION : 'O maior prédio da cidade, a prefeitura com fórum e câmara municipal.',
        EXAMINATION : 'Há uma grande barricada cercando o prédio, com algumas partes destruídas. Várias viaturas e carros também estão amontoados. Há barulhos de passos dentro do prédio.',
        SOLVED : False,
        UP : 'z3',
        DOWN : 'z9',
        LEFT  : 'z5',
        RIGH : 'none',
    },
    'z7' : {
        ZONENAME : 'Sala do Delegado',
        DESCRIPTION : 'A sala está toda revirada, com mesas dispostas como se fossem uma barreira para a janela, há jornais espalhados pelo chão.',
        EXAMINATION : 'O jornal diz que pessoas atacaram outras, comendo-as. Você encontrou uma espingarda debaixo dos papéis.',
        SOLVED : False,
        UP : 'z4',
        DOWN : 'none',
        LEFT  : 'none',
        RIGH : 'z8',
    },
    'z8' : {
        ZONENAME : 'Salão Comunitário',
        DESCRIPTION : 'O cheio de sangue e pessoas mortas é forte, há muitos objetos espalhos pelo chão.',
        EXAMINATION : 'Você encontrou uma chave de um carro que estava lá fora. Uma pessoa (se isso pode ser chamado de pessaoa) está te atacando!',
        SOLVED : False,
        UP : 'z5',
        DOWN : 'none',
        LEFT  : 'z7',
        RIGH : 'z9',
    },
    'z9' : {
        ZONENAME : 'Laboratório',
        DESCRIPTION : 'O laboratório está todo revirado e destruído, mas uma caixa permanece segura dentro de uma, a porta não está trancada.',
        EXAMINATION : 'Você encontrou uma vacina, mas apenas uma.',
        SOLVED : False,
        UP : 'z6',
        DOWN : 'none',
        LEFT  : 'z8',
        RIGH : 'none',
    }
}

## INTERATIVIDADE DO JOGO ##

#função para mostrar a localização do jogador no mapa
def printLocation():
    print('\n' + ('#' * (4 + len(player.localizacao))))
    print('# ' + player.localizacao.upper() + ' #')
    print('# ' + mapaCidade[player.localizacao][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(player.localizacao))))
    
#location = belo horizonte - 13 letras
##################
# belo horizonte #
# UHFUFUAHDADNJKASDKAJS #
##################

#função para pegar a ação do usuário
def prompt():
    print('\n' + '=================================')
    print('O que você gostaria de fazer?')
    acao = input('> ')
    acoesAceitaveis = ['andar', 'mover', 'examinar', 'sair', 'inspecionar', 'olhar', 'interagir']
    while acao.lower() not in acoesAceitaveis:
        print('Ação desconhecida. Por favor, tente novamente. \n')
        acao.input('> ')
