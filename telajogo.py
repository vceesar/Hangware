import pygame, sys
import random
import pygame_widgets as pw
import pygame as pg

pygame.init()
screenHeight = 500
screenWidth = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Hangware')

btn_font = pygame.font.SysFont("arial", 35)
fonte01 = pygame.font.SysFont("monospace", 24)

palavra = ''
botao = []
tentativaAcerto = []
bonecoHangman = [pygame.image.load('forca.png'), pygame.image.load('cabecaForca.png'),
                 pygame.image.load('corpoForca.png'), pygame.image.load('braco1Forca.png'),
                 pygame.image.load('braco2Forca.png'), pygame.image.load('perna1Forca.png'),
                 pygame.image.load('perna2Forca.png')]

membros = 0
def blit_text(surface, text, pos, font, color=pygame.Color((0,0,0))):
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

