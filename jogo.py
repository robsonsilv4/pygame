import pygame
from pygame.locals import *

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('')

while True:
    for evento in pygame.event.get():
        print(evento)
        if evento.type == QUIT:
            pygame.quit()
            
    pygame.display.update()
