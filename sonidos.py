import pygame
import sys

# Inicializar los modulos
pygame.init()
pygame.mixer.init()

# Colores

COLOR_BLANCO = pygame.Color(255, 255, 255)

# Ventana
PANTALLA = pygame.display.set_mode((400,400))
PANTALLA.fill(COLOR_BLANCO)
pygame.display.set_caption("Sonidos en pygame")

CONTINUAR = True

# Sonido de fondo
SILBATO = pygame.mixer.music.load("sounds/silbato.ogg")
pygame.mixer.music.play(1,0,0)

# Efectos sonoros
GALLO = pygame.mixer.Sound("sounds/gallo.ogg")
CUERVO = pygame.mixer.Sound("sounds/cuervo.ogg")
BICI = pygame.mixer.Sound("sounds/timbre.ogg")

# Bucle del juego

while CONTINUAR:
    for event in pygame.event.get():
        # Cierra la ventana si se hace click en el boton de cerrar ventana
        if event.type == pygame.QUIT:
            CONTINUAR = False
        # Detectar si se oprimio una tecla
        elif event.type == pygame.KEYDOWN:
            # Si se hace click en la tecla ESC
            if event.key == pygame.K_ESCAPE:
                CONTINUAR == False
            elif event.key == pygame.K_o:
                GALLO.play()
            elif event.key == pygame.K_c:
                CUERVO.play()
            elif event.key == pygame.K_v:
                BICI.play()
            elif event.key == pygame.K_DOWN:
                VOLUMEN = pygame.mixer.music.get_volume() - 0.1
                pygame.mixer.music.set_volume(VOLUMEN)
                GALLO.set_volume(VOLUMEN)
                CUERVO.set_volume(VOLUMEN)
                BICI.set_volume(VOLUMEN)
            elif event.key == pygame.K_UP:

                VOLUMEN = pygame.mixer.music.get_volume() + 0.1
                pygame.mixer.music.set_volume(VOLUMEN)
                GALLO.set_volume(VOLUMEN)
                CUERVO.set_volume(VOLUMEN)
                BICI.set_volume(VOLUMEN)

pygame.display.flip()
