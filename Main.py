import pygame
import winsound
pygame.init()

#Parte Visual da Janela
tamanho = (1280,720)
cor = (255,255,255)
fundo = pygame.image.load('fundo1.jpg')
tela =  pygame.display.set_mode( tamanho )
pygame.display.set_caption("Projeto Space")
icone = pygame.image.load("space.jpg")
pygame.display.set_icon(icone)
pygame.mixer.music.load("trilha.mp3")
pygame.mixer.music.play(-1)


#Looping Principal
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    tela.fill(cor)
    tela.blit(fundo, (0,0))
    pygame.display.update()
pygame.quit()
