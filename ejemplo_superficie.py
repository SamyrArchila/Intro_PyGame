# Importamos la libreria pygame
import pygame
import random

# Inicializamos los modulos de pygame
pygame.init()

# Establecer titulo a la ventana
pygame.display.set_caption("COLORES")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# Definimos un color
rojo = random.randint (0,255)
azul = random.randint (0,255)
verde = random.randint (0,255)

color_aleatorio = (rojo, verde, azul)


# Crear una superficie
color_aleatorio = pygame.Surface((200,200))

# Rellenamos la superficie de azul
color_aleatorio.fill((rojo, azul, verde))

# Inserto o muevo la superficie en la ventana
ventana.blit(color_aleatorio, (100,100))

# Actualiza la visualizacion de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break 

pygame.quit()

