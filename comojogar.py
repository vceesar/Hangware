import pygame, sys
import random
import pygame_widgets as pw
import pygame as pg

from pygame.locals import *

pygame.init()
screenHeight = 500
screenWidth = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Hangware')

btn_font = pygame.font.SysFont("arial", 25)
fonteGanhou = pygame.font.SysFont("monospace", 25)
fontePerdeu = pygame.font.SysFont('arial', 25)

def blit_text(surface, text, pos, font, color=pygame.Color((245, 177, 49))):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


text = "Na tela Inicial (MENU), o Jogador tera dois botoes, sendo eles o de Jogar e o de Como Jogar \n" \
       "Na tela de Jogar, Sera apresentado uma descricao, sendo este, respectivo de um Malware. O usuario devera utilizar o teclado interativo para assim, acertar ou errar o malware sorteado. \n" \
       "Caso acerte, este sera levado para uma tela sendo Parabenizado! " \
       "Caso erre 6 palavras, este sera um GameOver, e consequentemente sera levado para uma tela de Erro!, Caso queira, podera ou voltar ao menu, ou continuar tentando acertar o malware."

def desenhartexto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
click = False

def execComoJogar():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    pygame.mixer.music.pause()
                if event.key == pygame.K_n:
                    pygame.mixer.music.unpause()

        screen.fill((200, 255, 255))
        blit_text(screen, text,(20,20), btn_font)

        botaovoltar01 = pw.Button(
            screen, 10, 430, 100, 50, text='Menu',
            fontSize=20, margin=20,
            inactiveColour=(245, 177, 50),
            pressedColour=(255,255,255), radius=20,
            onClick=lambda: ""
        )
        events = pg.event.get()
        botaovoltar01.listen(events)
        botaovoltar01.draw()
        pygame.display.flip()
    pygame.quit()





