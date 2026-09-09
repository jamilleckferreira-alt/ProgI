# biblioteca adicional para o comando seguinte
import os

# comando para centralizar a janela
os.environ['SDL_VIDEO_CENTERED'] = '1'

# biblioteca pygamezero
import pgzrun
from pygame import Rect

# passo do jogador
PASSO = 3

# define o labirinto
maze = [
    "#################",
    "###   ###   #####",
    "##     #     ####",
    "#             ###",
    "##           ####",
    "###         #####",
    "####       ######",
    "#####     #######",
    "######   ########",
    "####### #########",
    "#################"
]




# granularidade do labirinto
# cada caracter do labirinto será desenhado VEZES o tamanho da ESCALA
ESCALA = 50

# largura da tela: largura do labirinto VEZES o tamanho da ESCALA
WIDTH = len(maze[0]) * ESCALA

# altura do labirinto: quantidade de elementos no vetor do labirinto (linhas)
# VEZES a ESCALA
HEIGHT = len(maze)* ESCALA

# jogador: retângulo que começa um pouco depois (5) da posição do labirinto
# o tamanho do jogador é 50 (largura) por 30
player = Rect((8 * ESCALA + 10, 8 * ESCALA + 10), (30, 20))

# função que retorna se naquela posição existe ou não parede
def wall_at(x, y):

    # calcula em que posição da matriz o jogador está
    # divide a posição do jogador pela ESCALA,
    # pegando só a parte inteira da divisão
    col = x // ESCALA
    row = y // ESCALA

    # se naquele local houver PARECE, retorna verdadeiro
    # ("colisão": ali tem parede)
    if maze[row][col] == "#":
        return True

    # senão, retorna falso (não tem parede)
    return False

# função que tenta realizar o movimento
def try_move(dx, dy):

    # verifica se um dos quatro cantos está dentro de alguma parede
    '''
    (x1,y1)    (x2, y1)
    c1 ------ c4
    |          |
    |          |
    c2 ------ c3
    (x1,y2)    (x2,y2)

    '''

    # calcula as posições x1, x2, y1, y2
    x1 = player.x + dx
    x2 = player.x + dx + player.width
    y1 = player.y + dy
    y2 = player.y + dy + player.height
    
    # verifica se os pontos estão "dentro" da parede
    c1 = wall_at(x1, y1)
    c2 = wall_at(x2,y1)
    c3 = wall_at(x2,y2)
    c4 = wall_at(x1,y2)
    
    # se nenhum ponto estiver dentro da parede
    if not (c1 or c2 or c3 or c4):
        # movimenta o jogador
        player.x = x1
        player.y = y1

def update():
    
    # se foi apertada a seta esquerda
    if keyboard.left:
        # tenta ir para a esquerda
        try_move(-PASSO, 0)

    if keyboard.right:
        try_move(PASSO, 0)
    if keyboard.up:
        try_move(0, -PASSO)
    if keyboard.down:
        try_move(0, PASSO)

def draw():
    # limpa a tela
    screen.clear()

    # percorrer as linhas do labirinto
    for row in range(len(maze)):

        # percorrer as colunas do labirinto
        for col in range(len(maze[row])):

            # se for parede...
            if maze[row][col] == "#":
                # desenha parede :-)
                wall = Rect(
                    (col * ESCALA, row * ESCALA),
                    (ESCALA, ESCALA)
                )
                screen.draw.filled_rect(
                    wall,
                    (100, 100, 100)
                )

    # desenha o jogador
    screen.draw.filled_rect(player, "green")

# executa o pygme zero
pgzrun.go()

'''
EXERCÍCIOS:
a) mudar a escala do labirinto (valor da variável ESCALA) ✅
b) modificar o labirinto (variável maze) ✅
c) fornecer o labirinto para uma IA e pedir para gerar um labirinto maior

outras melhorias:
https://chatgpt.com/share/6a36f25d-4e18-83e9-a918-1d87a2da7811
'''