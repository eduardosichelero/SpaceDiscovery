import pygame
import tkinter as tk
import tkinter.simpledialog as simpledialog
from pygame.locals import *

def open_dialog(event):
    # Abre a caixa de diálogo para inserir o nome da estrela
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    name = simpledialog.askstring("Nome da Estrela", "Insira o nome da estrela:")
    return name

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    star_name = ""
    star_position = (0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                star_name = open_dialog(event)
                star_position = event.pos

        screen.fill((255, 255, 255))  # Preenche a tela com branco
        if star_name:
            # Exibe o nome da estrela e suas coordenadas na tela
            font = pygame.font.Font(None, 36)
            text_name = font.render(star_name, True, (0, 0, 0))
            text_position = font.render(f"({star_position[0]}, {star_position[1]})", True, (0, 0, 0))
            screen.blit(text_name, (star_position[0], star_position[1] + 20))
            screen.blit(text_position, (star_position[0], star_position[1] + 60))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
