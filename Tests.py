import pygame
import winsound
import tkinter 
pygame.init()

#Parte Visual da Janela
tamanho = (1280,720)
branco = (255,255,255)
fonte = pygame.font.Font(None, 20)
fundo = pygame.image.load('fundo1.jpg')
tela =  pygame.display.set_mode( tamanho )
pygame.display.set_caption("Projeto Space")
icone = pygame.image.load("space.jpg")
pygame.display.set_icon(icone)
pygame.mixer.music.load("trilha.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Exemplo de Captura de Cliques")
pontos = []
nomes = []
running = True
VERMELHO = (255, 0, 0)

def desenhar_linhas():
    if len(pontos) >= 2:
        for i in range(len(pontos) - 1):
            pygame.draw.line(fundo, branco, pontos[i], pontos[i+1], 2)
#Looping Principal
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                x, y = pygame.mouse.get_pos()
                pontos.append((x, y))
    for ponto in pontos:
        pygame.draw.circle(fundo, VERMELHO, ponto, 5)
    desenhar_linhas()
    
    tela.fill(branco)
    tela.blit(fundo, (0,0))
    texto = fonte.render("Precione ESQ para Fechar o Programa: ",True, branco)
    tela.blit(texto, (1,10))
    pygame.display.update()
pygame.quit()

