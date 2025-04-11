import pygame
import sys

negro = (0, 0, 0)
blanco = (255, 255, 255)
gris = (124, 130, 133)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde_oscuro = (45, 87, 44)
cian = (0, 255, 255)
azul_claro = (100, 149, 237)
amarillo = (255, 250, 0)
rosa_palido = (255, 182, 193)
cafe = (150, 75, 0)


pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("MI DIBUJO ANIMADO")


clock = pygame.time.Clock()

rueda = pygame.Surface((70, 70), pygame.SRCALPHA)
pygame.draw.circle(rueda, cian, (35, 35), 35)


angulo = 0
via_x = 0  
velocidad_via = 3 

while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(azul_claro)

    # Texto en la pantalla
    fuente_arial = pygame.font.SysFont("Arial", 25, True, True)
    texto = fuente_arial.render("Colegio San Jose De Guanenta", True, blanco)
    ventana.blit(texto, (60, 30))

    texto = fuente_arial.render("Especialidad de Sistemas", True, blanco)
    ventana.blit(texto, (100, 65))

    texto = fuente_arial.render("Samyr Alejandro Archila Guiza", True, blanco)
    ventana.blit(texto, (5, 475))

    # Parte delantera del tren
    pygame.draw.circle(ventana, azul, (120, 300), 35)

    # Parte principal del tren
    pygame.draw.rect(ventana, blanco, ((50, 100), (400, 350)), 1)
    pygame.draw.rect(ventana, rojo, (150, 250, 200, 100))

    # Chimenea y ventanas
    pygame.draw.rect(ventana, verde_oscuro, (135, 253, 15, 100))
    pygame.draw.rect(ventana, verde_oscuro, (110, 245, 25, 118))
    pygame.draw.rect(ventana, gris, (165, 200, 30, 50))
    pygame.draw.rect(ventana, gris, (150, 185, 60, 25))
    pygame.draw.rect(ventana, gris, (225, 150, 120, 100))
    pygame.draw.rect(ventana, blanco, (240, 160, 90, 80))
    pygame.draw.rect(ventana, gris, (200, 130, 160, 25))
    pygame.draw.rect(ventana, gris, (215, 115, 130, 25))
    pygame.draw.rect(ventana,gris,(52, 330, 395, 115))


    via_x -= velocidad_via  
    if via_x <= -50:  
        via_x = 0
    
    for i in range(100, 500, 50):  
        pygame.draw.rect(ventana, amarillo, (via_x + i, 380, 10, 24))

    # Cara del tren
    pygame.draw.circle(ventana, amarillo, (290, 200), 30)         # cara
    pygame.draw.circle(ventana, blanco, (280, 190), 7)            # ojo izq
    pygame.draw.circle(ventana, blanco, (300, 190), 7)            # ojo der
    pygame.draw.circle(ventana, negro, (300, 190), 3)             # pupila izq
    pygame.draw.circle(ventana, negro, (280, 190), 3)             # pupila der
    pygame.draw.circle(ventana, rojo, (290, 210), 8)              # boca

    # Código de rueda
    angulo += 5  
    rueda_rotada = pygame.transform.rotate(rueda, angulo)

    rueda_izquierda = rueda_rotada.get_rect(center=(180, 350))
    ventana.blit(rueda_rotada, rueda_izquierda.topleft)

    rueda_derecha = rueda_rotada.get_rect(center=(320, 350))
    ventana.blit(rueda_rotada, rueda_derecha.topleft)

    rueda_central = rueda_rotada.get_rect(center=(250, 350))
    ventana.blit(rueda_rotada, rueda_central.topleft)

    # Partes adicionales en las ruedas
    pygame.draw.rect(ventana, verde_oscuro, (260, 340, 50, 24))
    pygame.draw.rect(ventana, verde_oscuro, (185, 340, 50, 24))


    






























    pygame.display.flip()