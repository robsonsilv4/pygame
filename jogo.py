import pygame
from pygame.locals import *

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

tela.fill(azul_claro)

um_pixel = pygame.PixelArray(tela)
um_pixel[3][3] = preto

while True:
    for evento in pygame.event.get():
        print(evento)
        if evento.type == QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update()
