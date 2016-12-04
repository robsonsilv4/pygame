import pygame
from pygame.locals import *
import sys

pygame.init()

preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
azul = (0, 0, 255)
azul_claro = (0, 255, 255)
roxo = (255, 0, 255)

tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Jogo')


while True:
    for evento in pygame.event.get():
        print(evento)
        if evento.type == QUIT:
            pygame.quit()
            quit()
            sys.exit()
            
    pygame.display.update()
