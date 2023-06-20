import pygame
import winsound
import tkinter
import tkinter.simpledialog as simpledialog
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
pontos = []

def desenhar_linhas():
    if len(pontos) >= 2:
        for i in range(len(pontos) - 1):
            pygame.draw.line(fundo, branco, pontos[i], pontos[i+1], 2)
#Looping Principal
def open_dialog(event):
    # Abre a caixa de diálogo para inserir o nome da estrela
    root = tkinter.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    name = simpledialog.askstring("Nome da Estrela", "Insira o nome da estrela:")
    return name
NomeEstrela = ""
PosicaoEstrela = (0, 0)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            NomeEstrela = open_dialog(evento)
            PosicaoEstrela = evento.pos
            if evento.button == 1:
                x, y = pygame.mouse.get_pos()
                pontos.append((x, y))
    if NomeEstrela:
        pygame.font.Font(None, 20)
        NomeTexto = fonte.render(NomeEstrela, True, branco)
        PosicaoTexto = fonte.render(f"({PosicaoEstrela[1]}, {PosicaoEstrela[0]})", True, branco,0)
        fundo.blit(NomeTexto, (PosicaoEstrela[0], PosicaoEstrela[1] + 0))
        fundo.blit(PosicaoTexto, (PosicaoEstrela[0], PosicaoEstrela[1] + 0))
    
    
    for ponto in pontos:
        pygame.draw.circle(fundo,branco, ponto, 5)
    desenhar_linhas()
    
    
    tela.fill(branco)
    tela.blit(fundo, (0,0))
    texto = fonte.render("Precione ESQ para Fechar o Programa: ",True, branco)
    tela.blit(texto, (1,10))
    pygame.display.update()
pygame.quit()
