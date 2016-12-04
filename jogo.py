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

tela = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Jogo')

imagem = pygame.image.load('beyblade.png')
imagem_x = 10
imagem_y = 10

velocidade = 3
movimento = 'baixo'

fps = pygame.time.Clock()


while True:
    
    tela.fill(preto)
    
    if movimento == 'baixo':
        imagem_y += velocidade
        if imagem_y > 200:
            imagem = pygame.transform.rotate(imagem, 90)
            movimento = 'direita'

    elif movimento == 'direita':
        imagem_x += velocidade
        if imagem_x > 200:
            imagem = pygame.transform.rotate(imagem, 90)
            movimento = 'cima'

    elif movimento == 'cima':
        imagem_y -= velocidade
        if imagem_y < 30:
            imagem = pygame.transform.rotate(imagem, 90)
            movimento = 'esquerda'

    elif movimento == 'esquerda':
        imagem_x -= velocidade
        if imagem_x < 30:
            imagem = pygame.transform.rotate(imagem, 90)
            movimento = 'baixo'
    
    tela.blit(imagem, (imagem_x, imagem_y))
    for evento in pygame.event.get():
        print(evento)
        if evento.type == QUIT:
            pygame.quit()
            quit()
            sys.exit()
            
    pygame.display.update()
    fps.tick(60)
