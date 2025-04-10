import pygame
import sys
import math
import random

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
negro = (0,0,0)
blanco = (255,255,255)
cian = (0,255,255)
color_aleatorio = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
 
pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("TRABAJO")


clock = pygame.time.Clock()

XX = MOVIMIENTO = 3

while True: 
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(negro)

    pygame.draw.rect(ventana,blanco, ((50,100), (400,350)), 1)

    fuente_arial = pygame.font.SysFont("Arial", 25, 2, 1)
    texto = fuente_arial.render("Colegio San Jose De Guanenta", 1, blanco)
    ventana.blit(texto,(60,30))

    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto = fuente_arial.render("Especialidad de Sistemas", 1, blanco)
    ventana.blit(texto,(100,65))

    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto = fuente_arial.render("Samyr Alejandro Archila Guiza", 1, blanco)
    ventana.blit(texto,(5,475))

    for i in range(100):

        lineas1 = random.randint(50,450)
        lineas2 = random.randint(100,450)
        lineas3 = random.randint(50,450)
        lineas4 = random.randint(100,450)

        color_aleatorio = (random.randint(0,255), random.randint(0, 255),random.randint(0, 255))

        pygame.draw.line(ventana, color_aleatorio,(lineas1,lineas2),(lineas3,lineas4))

    pygame.display.flip()


























    


