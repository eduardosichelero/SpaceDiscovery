import math
import pygame
import winsound
from tkinter import simpledialog

pygame.init()

tamanho = (1280, 720)
branco = (255, 255, 255)
fundo = pygame.image.load('fundo1.jpg')
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Projeto Space")
icone = pygame.image.load("space.jpg")
pygame.display.set_icon(icone)
pygame.mixer.music.load("trilha.mp3")
pygame.mixer.music.play(-1)
fonte1 = pygame.font.Font(None, 20)

estrelas = {}
pontos = []
desconhecidos = []

def mostrar_distancias(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distancia, 2)

def desenhar_estrelas():
    for nome, pos in estrelas.items():
        pygame.draw.circle(tela, branco, pos, 4)
        fonte = pygame.font.Font(None, 20)
        texto = fonte.render(nome, True, branco)
        tela.blit(texto, (pos[0] + 15, pos[1] - 10))

    if len(pontos) > 1:
        pygame.draw.lines(tela, branco, False, pontos)
        for (pos1, pos2) in zip(pontos, pontos[1:]):
            try:
                distancia = mostrar_distancias(pos1, pos2)
                x = (pos1[0] + pos2[0]) // 2
                y = (pos1[1] + pos2[1]) // 2
                texto = fonte1.render(str(distancia), True, branco)
                tela.blit(texto, (x, y))
            except ValueError as e:
                print(f"Erro ao calcular distância: {e}")

    if len(desconhecidos) > 1:
        pygame.draw.lines(tela, branco, False, desconhecidos)

def salvar_historico():
    try:
        with open("historico.txt", "w") as arquivo:
            for nome, pos in estrelas.items():
                arquivo.write(f"{nome},{pos[0]},{pos[1]}\n")
    except IOError as e:
        print(f"Erro ao salvar o histórico: {e}")

def carregar_historico():
    estrelas.clear()
    pontos.clear()
    desconhecidos.clear()
    try:
        with open("historico.txt", "r") as arquivo:
            for linha in arquivo:
                valores = linha.strip().split(",")
                if len(valores) == 3:
                    try:
                        nome, x, y = valores
                        pos = (int(x), int(y))
                        estrelas[nome] = pos
                        if nome.startswith("desconhecido"):
                            desconhecidos.append(pos)
                        else:
                            pontos.append(pos)
                    except ValueError as e:
                        print(f"Erro ao carregar histórico: {e}")
    except IOError as e:
        print(f"Erro ao carregar o histórico: {e}")
    desenhar_estrelas()

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            salvar_historico()
            running = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela")
            if not item:
                item = f"desconhecido{pos}"
            estrelas[item] = pos
            if item.startswith("desconhecido"):
                desconhecidos.append(pos)
            else:
                pontos = list(estrelas.values())
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F10:
            estrelas.clear()
            pontos.clear()
            desconhecidos.clear()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F11:
            carregar_historico()

    tela.blit(fundo, (0, 0))
    desenhar_estrelas()
    texto1 = fonte1.render("Pressione ESC para Fechar o Programa:", True, branco)
    texto2 = fonte1.render("Pressione F10 para Apagar os Pontos:", True, branco)
    texto3 = fonte1.render("Pressione F11 para Carregar o Histórico:", True, branco)
    tela.blit(texto1, (1, 10))
    tela.blit(texto2, (1, 28))
    tela.blit(texto3, (1, 45))
    pygame.display.update()

pygame.quit()
