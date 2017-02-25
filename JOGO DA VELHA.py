# Jogo da velha tops

__author__ = "XSyther"
__version__ = "1.0"


def velha():
    print('''
ooooo  oooo ooooooooooo ooooo       ooooo ooooo      o
 888    88   888    88   888         888   888      888
  888  88    888ooo8     888         888ooo888     8  88
   88888     888    oo   888      o  888   888    8oooo88
    888     o888ooo8888 o888ooooo88 o888o o888o o88o  o888o
    ''')


def tabuleiro():
    print("TABULEIRO".center(30))

    print()
    print("          %s | %s | %s" % (table[0], table[1], table[2]))
    print("         ---|---|---")
    print("          %s | %s | %s" % (table[3], table[4], table[5]))  # Posicoes jogaveis
    print("         ---|---|---")
    print("          %s | %s | %s" % (table[6], table[7], table[8]))
    print()


table = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
vezes = 0
ganhou = False
jogador=1
tabuleiro()

while True:

    joga1 = int(input("         JOGADOR %s\nDigite a posicao para jogar: " %jogador))
    if(jogador==1):
        table[joga1 - 1] = "X"
    elif(jogador == 2):
        table[joga1 - 1] = "O"


    vezes += 1

    if (vezes >= 9):
        velha()
        break

    ganhar = (
        table[0] == table[1] == table[2],
        table[3] == table[4] == table[5],
        table[6] == table[7] == table[8],
        # vertical
        table[0] == table[3] == table[6],  # Tava dando erro entao repeti sas porra pra funcionar <3 #POG IS LIFE
        table[1] == table[4] == table[7],
        table[1] == table[4] == table[7],
        table[2] == table[5] == table[8],
        # diagonal
        table[0] == table[4] == table[8],
        table[6] == table[4] == table[2])

    tabuleiro()

    for i in ganhar:
        if (i == True):
            ganhou = True
            print("         Jogador %s Ganhou\n\n" %jogador)
            break
    if (ganhou == True):
        break

    if(jogador==1):
        jogador+=1
    else:
        jogador-=1
