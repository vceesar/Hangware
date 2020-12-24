#---------------TRABALHO REALIZADO POR VICTOR CESAR, AUGUSTO ROSASCO E EDUARDO ATANES ------------------------------------------#
import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
import pygame
import pygame_widgets as pw
from pygame.locals import *
import random

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Hangware')
screenHeight = 500
screenWidth = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
#----------------Musica------------------------------
pygame.mixer.init()
pygame.mixer.music.load("data/musicafundo.wav")
pygame.mixer.music.play(-1)
#-----------------Fontes-----------------------------
font1 = pygame.font.SysFont(None, 20)
font2 = pygame.font.Font("data/DK Hangman's Delight.otf",100)
font3 = pygame.font.Font("data/DK Hangman's Delight.otf",50)
font4 = pygame.font.SysFont(None, 50)
font5 = pygame.font.SysFont(None, 40)
btn_font = pygame.font.SysFont("arial", 25)
fonte01 = pygame.font.SysFont("monospace", 24)
fonteinstrucoes = pygame.font.SysFont('arial', 25)
#------------------------------------------------------
#Configuracoes tela jogo
palavra = ''
botao = []
tentativaAcerto = []
bonecoHangman = [pygame.image.load('data/forca.png'), pygame.image.load('data/cabecaForca.png'),
                 pygame.image.load('data/corpoForca.png'), pygame.image.load('data/braco1Forca.png'),
                 pygame.image.load('data/braco2Forca.png'), pygame.image.load('data/perna1Forca.png'),
                 pygame.image.load('data/perna2Forca.png')]

membros = 0
#--------------------------MENU---------------------------------------------------------
def desenhartexto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
def main_menu():
    while True:
        screen.fill((200, 255, 255))
        desenhartexto("Desenvolvivo por Victor Cesar, Augusto Rosasco, Eduardo Atanes",font1,(245, 177, 49),screen,0,0)
        desenhartexto("@Universidade Presbiteriana Mackenzie", font1, (245,177,49), screen, 530,0)
        desenhartexto("Para pausar a musica aperte M e despausar N", font1, (245,177,49), screen,500,480)
        desenhartexto('Hangware', font2, (245, 177, 49), screen, 250, 70)


        mx, my = pygame.mouse.get_pos()

        textjogar = font4.render("Jogar", False,(255,255,255))
        textinstrucoes = font5.render("Como Jogar", False, (255, 255, 255))
        button_1 = pygame.Rect(300,210,200,50)
        button_2 = pygame.Rect(300,350,200,50)
        if button_1.collidepoint((mx, my)):
            if click:
                main_jogo()
        if button_2.collidepoint((mx, my)):
            if click:
                main_instrucoes()
        pygame.draw.rect(screen, (245, 177, 49), button_1)
        pygame.draw.rect(screen, (245, 177, 49), button_2)
        screen.blit(textjogar, (350,220))
        screen.blit(textinstrucoes,(320,362))

        click = False
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
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
#----------------------------------------------------------------------------------------------------
#-------------------------INSTRUCOES------------------------------------------------------------------
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


text = "Na tela Inicial (MENU), o Jogador terá dois botões, sendo eles o de Jogar e o de Como Jogar \n" \
       "Na tela de Jogar, Será apresentado uma descrição, sendo este, respectivo de um Malware. O usuário deverá utilizar o teclado interativo para assim, acertar ou errar o malware sorteado. \n" \
       "Caso acerte, este será levado para uma tela sendo Parabenizado! \n" \
       "Caso erre 6 letras, este será um GameOver, e consequentemente será levado para uma tela de Erro!. \n" \
       "Caso queira, poderá ou voltar ao menu, ou continuar jogando."

def desenhartexto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_instrucoes():
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
        blit_text(screen, text,(20,20), fonteinstrucoes)

        botaoinstrucoes = pw.Button(
            screen, 10, 430, 100, 50, text='Menu',
            fontSize=20, margin=20,
            inactiveColour=(245, 177, 50),
            pressedColour=(255,255,255), radius=20,
            onClick=lambda: main_menu()
        )
        botaoinstrucoes.listen(pygame.event.get())
        botaoinstrucoes.draw()
        pygame.display.flip()
    pygame.quit()
#----------------------------------------------------------------------------------------------
#-----------------------------TELA DE JOGO-----------------------------------------------------
def malwareAleatorio():
    palavras_discricao = {
        1: ["Computer worm",
            "É um malware que se replica e seu objetivo primário é infectar outros computadores, duplicando-se enquanto já está dentro de um sistema infectado"],
        2: ["trojan horse", "Um tipo de malware que engana os usuários ao se parecer com um programa legitimo"],
        3: ["Ransomware",
            "É uma forma de malware que sequestra os dados do computador, criptografando-os e, em seguida, pede resgate em moedas virtuais, como o Bitcoin"],
        4: ["rootkits",
            "É uma coleção de malwares que dão acesso não autorizado ao computador infectado. Ele consegue disfarçar sua presença no sistema ao enganar os antivirus"],
        5: ["keylogger",
            "É um tipo de malware que monitora todas as teclas que estão sendo clicadas pelo usuário e armazena-as, assim conseguindo informações pessoais como senhas"],
        6: ["grayware",
            "São aplicações indesejadas que causam uma piora de desempenho no computador e não são considerados de fato malwares"],
        7: ["fileless malware",
            "É um malware que utiliza programas legitimos para infectar um computador. Por não depender de arquivos, ele não deixa rastros no sistema, tornando um desafio para os ativirus encontrarem e removerem a ameaça do sistema"],
        8: ["adware", "Ele se disfarça de softwares legitimos e causa popups ao acessar os browsers"],
        9: ["malvertising",
            "É um malware que utiliza propagandas maliciosas para espalhar mais malwares, geralmente colocando suas propagandas em sites considerados como 'confiáveis'"],
        10: ["spyware",
             "É um malware que coleta informações sobre a pessoa ou organização que tem o computador infectado e manda essas informações ao agressor, comos senhas e informações do cartão de crédito"]
    }

    i = random.choice(list(palavras_discricao))

    return palavras_discricao[i]


def atualizaTela():
    global tentativaAcerto
    global bunecoHangman
    global membros
    global descrição
    screen.fill((200, 255, 255))
    # Buttons
    for i in range(len(botao)):
        if botao[i][4]:
            pygame.draw.circle(screen, (0, 0, 0), (botao[i][1], botao[i][2]), botao[i][3])
            pygame.draw.circle(screen, botao[i][0], (botao[i][1], botao[i][2]), botao[i][3] - 2)

            label = fonte01.render(chr(botao[i][5]), 1, (0, 0, 0))
            screen.blit(label, (botao[i][1] - (label.get_width() / 2), botao[i][2] - (label.get_height() / 2)))

    espaco = espacamentoPalavras(palavra, tentativaAcerto)
    label1 = fonte01.render(espaco, 1, (0, 0, 0))
    rect = label1.get_rect()
    length = rect[2]
#Blita ____ ____ ____
    screen.blit(label1, (screenWidth / 2 - length / 2, 320))

    foto = bonecoHangman[membros]
#Blita Forca e partes do corpo
    screen.blit(foto, (screenWidth / 2 - foto.get_width() / 2 + 20, 70))
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    blit_text(screen, descrição, (0, 0), myfont)


#------------Botao Voltar Menu---------------------#
    botaoJogoVoltar = pw.Button(
                screen, 0, 200, 80, 40, text='Menu',
                fontSize=20, margin=20,
                inactiveColour=(245, 177, 50),
                pressedColour=(255,255,255), radius=20,
                onClick=lambda: main_menu()
            )
    botaoJogoVoltar.listen(pygame.event.get())
    botaoJogoVoltar.draw()
    pygame.display.update()

def forca(tentativaAcerto):
    global palavra
    if tentativaAcerto.lower() not in palavra.lower():
        return True
    else:
        return False


def espacamentoPalavras(palavra, tentativaAcerto=[]):
    espacoPalavra = ''
    letrasCertas = tentativaAcerto
    for x in range(len(palavra)):
        if palavra[x] != ' ':
            espacoPalavra += '_ '
            for i in range(len(letrasCertas)):
                if palavra[x].upper() == letrasCertas[i]:
                    espacoPalavra = espacoPalavra[:-2]
                    espacoPalavra += palavra[x].upper() + ' '
        elif palavra[x] == ' ':
            espacoPalavra += ' '
    return espacoPalavra


def pressionarBotao(x, y):
    for i in range(len(botao)):
        if x < botao[i][1] + 20 and x > botao[i][1] - 20:
            if y < botao[i][2] + 20 and y > botao[i][2] - 20:
                return botao[i][5]
    return None


def fimJogo(vencedor=False):
    perdeuTexto = 'VOCÊ ERROU! Pressione qualquer botão para continuar'
    ganhouTexto = 'VOCÊ ACERTOU!'
    atualizaTela()
    pygame.time.delay(1000)
    screen.fill((200, 255, 255))

    if vencedor == True:
        label = btn_font.render(ganhouTexto, 1, (0, 0, 0))
    else:
        label = btn_font.render(perdeuTexto, 1, (0, 0, 0))

    wordTxt = btn_font.render(palavra.upper(), 1, (0, 0, 0))
    wordWas = btn_font.render('O Malware era: ', 1, (0, 0, 0))

    screen.blit(wordTxt, (screenWidth / 2 - wordTxt.get_width() / 2, 295))
    screen.blit(wordWas, (screenWidth / 2 - wordWas.get_width() / 2, 245))
    screen.blit(label, (screenWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    again = True
    while again:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                again = False
    recomecarJogo()


def recomecarJogo():
    global membros
    global tentativaAcerto
    global botao
    global palavra
    global descrição
    for i in range(len(botao)):
        botao[i][4] = True

    membros = 0
    tentativaAcerto = []
    palavra_descricao = malwareAleatorio()
    palavra = palavra_descricao[0]
    descrição = palavra_descricao[1]



increase = round(screenWidth / 13)
for i in range(26):
    if i < 13:
        y = 405
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 450
    botao.append([(245, 177, 49), x, y, 20, True, 65 + i])

palavra_descricao = malwareAleatorio()
palavra = palavra_descricao[0]
descrição = palavra_descricao[1]


def main_jogo():
    global membros
    emJogo = True
    while emJogo:
        atualizaTela()
        pygame.time.delay(10)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                emJogo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    emJogo = False
                if evento.key == pygame.K_m:
                    pygame.mixer.music.pause()
                if evento.key == pygame.K_n:
                    pygame.mixer.music.unpause()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                clickPos = pygame.mouse.get_pos()
                letra = pressionarBotao(clickPos[0], clickPos[1])
                if letra != None:
                    tentativaAcerto.append(chr(letra))
                    botao[letra - 65][4] = False
                    if forca(chr(letra)):
                        if membros != 5:
                            membros += 1
                        else:
                            fimJogo()
                    else:
                        print(espacamentoPalavras(palavra, tentativaAcerto))
                        if espacamentoPalavras(palavra, tentativaAcerto).count('_') == 0:
                            fimJogo(True)

    pygame.quit()


#----------------------------------------------------------------------------------------------
#-------------------Chamada das Funcoes--------------------------------------------------------
main_menu()
