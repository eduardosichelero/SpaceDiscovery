import pygame
import winsound
import random
pygame.init()
tamanho = (800,600)
branco = (255,255,255)
vermelho = (255,0, 0)
preto = (0,0,0)
clock = pygame.time.Clock()
tela =  pygame.display.set_mode( tamanho )
pygame.display.set_caption("FlappyBird do Marcão")
running = True
posicaoXBolinha = 0
posicaoYBolinha= 300
flappy = pygame.image.load("flappybird.png")
pac = pygame.image.load("pac.png")
pacOriginal = pygame.image.load("pac.png")
flappyOriginal = pygame.image.load("flappybird.png")
pygame.display.set_icon(flappy)
fundo = pygame.image.load("fundo.jpg")
velocidadeBolinha = 1
posicaoXBolinhaV = 400
movimentoBolinhaVX = 0
movimentoBolinhaVY = 0
posicaoYBolinhaV = 300
direita = True
pygame.mixer.music.load("trilha.mp3")
pygame.mixer.music.play(-1)
pacSound = pygame.mixer.Sound("pac.mp3")
pygame.mixer.Sound.play(pacSound)
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoBolinhaVX = -5
            flappy = flappyOriginal
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoBolinhaVX = 5
            flappy = pygame.transform.flip(flappy, True,False)
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoBolinhaVX = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoBolinhaVX = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoBolinhaVY = -5

        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoBolinhaVY = 5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoBolinhaVY = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoBolinhaVY = 0


        
        

    tela.fill(branco)
    tela.blit(fundo, (0,0))

    tela.blit(pac, (posicaoXBolinha,posicaoYBolinha))
    #pygame.draw.circle(tela,preto,(posicaoXBolinha,posicaoYBolinha),30)

    if posicaoXBolinha >= 800:
        direita = False
        velocidadeBolinha = velocidadeBolinha + 1
        pygame.mixer.Sound.play(pacSound)
        posicaoYBolinha = random.randint(0,600)
        pac = pygame.transform.flip(pac, True,False)
        #winsound.Beep(500,300)
    elif posicaoXBolinha <= 0:
        direita = True
        pac = pacOriginal
        pygame.mixer.Sound.play(pacSound)
        velocidadeBolinha = velocidadeBolinha + 1
        #winsound.Beep(500,300)

    if direita :
        posicaoXBolinha = posicaoXBolinha + velocidadeBolinha
    else:
        posicaoXBolinha = posicaoXBolinha - velocidadeBolinha
    
    
    if posicaoXBolinhaV < 0:
        posicaoXBolinhaV = 0
    elif posicaoXBolinhaV > 700:
        posicaoXBolinhaV = 700
    else:
        posicaoXBolinhaV = posicaoXBolinhaV + movimentoBolinhaVX

    if posicaoYBolinhaV < 0:
        posicaoYBolinhaV = 0
    elif posicaoYBolinhaV > 550:
        posicaoYBolinhaV = 550
    else:
        posicaoYBolinhaV = posicaoYBolinhaV + movimentoBolinhaVY
    
    #pygame.draw.circle(tela, vermelho, (posicaoXBolinhaV,posicaoYBolinhaV) , 30 )
    tela.blit(flappy, (posicaoXBolinhaV,posicaoYBolinhaV))

    pixelXFlappy = list(range(posicaoXBolinhaV, posicaoXBolinhaV+100))
    pixelYFlappy = list(range(posicaoYBolinhaV, posicaoYBolinhaV+56))
    pixelXPac = list(range(posicaoXBolinha, posicaoXBolinha+100))
    pixelYPac = list(range(posicaoYBolinha, posicaoYBolinha+117))

    totalPixelAltura = len(list(set(pixelYFlappy) & set(pixelYPac) ))
    totalPixelLargura = len(list(set(pixelXFlappy) & set(pixelXPac) ))
    
    if totalPixelAltura > 12: 
        if totalPixelLargura> 28: 
            running =False

    pygame.display.update()
    clock.tick(60)
pygame.quit()
