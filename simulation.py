# importar o módulo pgzrun para rodar o jogo
import pgzrun

# criar um "ator"
quad = Actor('quadrado.png')
# definir posição do ator (x, y)
quad.pos = 300, 200

# criar uma "base"
base = Actor('base.png')
# definir a posição da base
base.pos = 400, 400

# definir largura e altura da janela
WIDTH = 800
HEIGHT = 600

# método que vai desenhar os atores na tela
def draw():
    # limpar a tela
    screen.clear()
    # desenhar os atores
    quad.draw()
    base.draw()

# método que vai atualizar a posição dos atores
def update():
    # se o ator NÃO colidiu com a base...
    if not quad.colliderect(base):
        # o ator continua "caindo"
        quad.top += 1        

# executar o jogo
pgzrun.go()

''' EXERCÍCIOS:

a) aumentar a velocidade de queda do quadrado
b) mudar a posição inicial do quadrado (colocar o quadrado mais alto)
c) mudar a posição da base (colocar a base mais para baixo)
d) mudar as figuras da base e do quadrado
e) colocar 2 quadrados caindo ao mesmo tempo

Para fazer as atividades a seguir, você deverá buscar na Internet/IA
como realizá-las no pygame zero:

f) alterar a cor de fundo da janela
===> "como alterar a cor de fundo da janela no pygame zero"
g) centralizar a janela na tela
===> "como centralizar a janela no pygame zero"
h) colocar um título na janela
===> "como colocar um título na janela no pygame zero"

'''