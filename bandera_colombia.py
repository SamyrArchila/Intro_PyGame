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
amarrillo = (255,250,0)
azul =  (0,0,255)
rojo =  (255,0,0)


# Crear una superficie
color_amarrillo = pygame.Surface((400, 200))
color_azul = pygame.Surface((400, 300))
color_rojo = pygame.Surface((400, 100))


# Rellenamos la superficie de amarrillo azul y rojo
color_amarrillo.fill((amarrillo))
color_azul.fill((azul))
color_rojo.fill((rojo))

# Inserto o muevo la superficie en la ventana
ventana.blit(color_amarrillo, (0, 0))
ventana.blit(color_azul, (0, 200))
ventana.blit(color_rojo, (0, 300))

# Actualiza la visualizacion de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break 

pygame.quit()