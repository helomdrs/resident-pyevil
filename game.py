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
        self.vida = 0
        self.magia = 0
        self.poderes = []
        self.localizacao = 'z0'
        
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
    opcoesTelaInicial()
    
#função que vai desenhar a tela de ajuda
def menuAjuda():
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
def iniciarJogo():
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
NOMEZONA = ''
DESCRICAO = 'DESCRICAO'
AOEXAMINAR = 'examine'
SOLUCIONADO = False
ACIMA = 'ACIMA', 'north'
ABAIXO = 'ABAIXO', 'south'
AESQUERDA  = 'left', 'west'
ADIREITA = 'right', 'east'

#dicionário dos lugares que o jogador vai passar?
lugaresVisitados = {'z1': False, 'z2': False, 'z3': False, 'z4': False, 'z5': False, 'z6': False}

#dicionário com as informações de cada zona
mapaCidade = {
    'z1' : {
        NOMEZONA : 'Centro',
        DESCRICAO : 'Centro da cidade, com várias lojas e parques',
        AOEXAMINAR : 'Todas as lojas foram saqueadas, algumas queimadas. Os parques estão cheios de pássaros mortos.',
        SOLUCIONADO : False,
        ACIMA : 'none',
        ABAIXO : 'z4',
        AESQUERDA  : 'none',
        ADIREITA : 'z2',
    }, 
    'z2' : {
        NOMEZONA : 'Suburbio',
        DESCRICAO : 'Grande área residencial da cidade',
        AOEXAMINAR : 'Algumas casas estão abertas, outras estão lacradas de maneira improvidada. Está tudo silencioso até demais.',
        SOLUCIONADO : False,
        ACIMA : 'none',
        ABAIXO : 'z5',
        AESQUERDA  : 'z1',
        ADIREITA : 'z3',
    },
    'z3' : {
        NOMEZONA : 'Delegacia',
        DESCRICAO : 'Maior Departamento Policial da cidade, centro de operações policiais',
        AOEXAMINAR : 'O prédio está depredado, várias viaturas posicionadas como barreira se encontram pegando fogo ou quebradas, há um barulho de murmurio vindo de dentro do prédio',
        SOLUCIONADO : False,
        ACIMA : 'none',
        ABAIXO : 'z6',
        AESQUERDA  : 'z2',
        ADIREITA : 'none',
    },
    'z4' : {
        NOMEZONA : 'Igreja',
        DESCRICAO : 'Maior centro religioso da cidade, com um grande salão.',
        AOEXAMINAR : 'Barricadas improvidadas cercam a igreja, mas parte dela está caída. Os vidros e as portas também foram lacradas com madeira. Não dá ver nada dentro do prédio.',
        SOLUCIONADO : False,
        ACIMA : 'z1',
        ABAIXO : 'z7',
        AESQUERDA  : 'none',
        ADIREITA : 'z5',
    },
    'z5' : {
        NOMEZONA : 'Hospital',
        DESCRICAO : 'Hospital público da cidade.',
        AOEXAMINAR : 'Muitas ambulâncias cercam o local, há sangue e materiais hospitalares jogado pelo chão. Algumas entradas estão lacradas de maneira improvidsada.',
        SOLUCIONADO : False,
        ACIMA : 'z2',
        ABAIXO : 'z8',
        AESQUERDA  : 'z4',
        ADIREITA : 'z6',
    },
    'z6' : {
        NOMEZONA : 'Prefeitura',
        DESCRICAO : 'O maior prédio da cidade, a prefeitura com fórum e câmara municipal.',
        AOEXAMINAR : 'Há uma grande barricada cercando o prédio, com algumas partes destruídas. Várias viaturas e carros também estão amontoados. Há barulhos de passos dentro do prédio.',
        SOLUCIONADO : False,
        ACIMA : 'z3',
        ABAIXO : 'z9',
        AESQUERDA  : 'z5',
        ADIREITA : 'none',
    },
    'z7' : {
        NOMEZONA : 'Sala do Delegado',
        DESCRICAO : 'A sala está toda revirada, com mesas dispostas como se fossem uma barreira para a janela, há jornais espalhados pelo chão.',
        AOEXAMINAR : 'O jornal diz que pessoas atacaram outras, comendo-as. Você encontrou uma espingarda debaixo dos papéis.',
        SOLUCIONADO : False,
        ACIMA : 'z4',
        ABAIXO : 'none',
        AESQUERDA  : 'none',
        ADIREITA : 'z8',
    },
    'z8' : {
        NOMEZONA : 'Salão Comunitário',
        DESCRICAO : 'O cheio de sangue e pessoas mortas é forte, há muitos objetos espalhos pelo chão.',
        AOEXAMINAR : 'Você encontrou uma chave de um carro que estava lá fora. Uma pessoa (se isso pode ser chamado de pessaoa) está te atacando!',
        SOLUCIONADO : False,
        ACIMA : 'z5',
        ABAIXO : 'none',
        AESQUERDA  : 'z7',
        ADIREITA : 'z9',
    },
    'z9' : {
        NOMEZONA : 'Laboratório',
        DESCRICAO : 'O laboratório está todo revirado e destruído, mas uma caixa permanece segura dentro de uma, a porta não está trancada.',
        AOEXAMINAR : 'Você encontrou uma vacina, mas apenas uma.',
        SOLUCIONADO : False,
        ACIMA : 'z6',
        ABAIXO : 'none',
        AESQUERDA  : 'z8',
        ADIREITA : 'none',
    }
}

## INTERATIVIDADE DO JOGO ##

#função para mostrar a localização do jogador no mapa
def mostrarLocalizacao():
    print('\n' + ('#' * (4 + len(player.localizacao))))
    print('# ' + player.localizacao.upper() + ' #')
    print('# ' + mapaCidade[player.localizacao][DESCRICAO] + ' #')
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
