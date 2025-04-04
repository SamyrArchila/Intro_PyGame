# Estructura de un juego en pygame

## Inicializacion

como en todo programa en python, se deben importar los modulos o librerias a utilizar.

`import pygame`

- inicializar pygame usando la funcion init(). Inicializa todos los modulos de pygame importados.

``pygame.init()``

## Visualizacion de la ventana

``ventana= pygame.display.set_mode((600,400))``

- set_mode es la funcon encargada de definir el tamaño de la ventana. En el ejemplo se esta definiendo una ventana de 600 pixeles de ancho y 400 pixeles de largo

`pygame.display.set_caption("Mi ventana")`

- set_caption() es la funcion que añade un titulo a la ventana.

### funcion set_mode()

`set_mode(size =(0,0), flags ) = 0, depth = o, display = 0)`

- size = (600,400) : define el tamaño de la ventana
- flags = define uno o mas comportamientos para la ventana

    - Valores:
        - pygame.FULLSCREEN
        - pygame.RESIZABLE
    - Ejemplo:
        - flags = pygame.FULLSCREEN | pygame.RESIZABLE: pantalla completa, dimensiones modificables.

## Bucle del juego - game loop

- Bucle infinito que se interrumpira al cumplir ciertos criterios
- Reloj interno de juego
- En cada iteracion del bucle del juego podemos mover a un personaje, o tener en cuenta que un objeto a alcanzado
a otro, o que se ha cruzado la linea de llegada, lo que quiere decir que la partida ha terminado
- Cada iteracion es una oportunidad para actualizar todo los datos relacionados con el estado actual de la
partida o del juego
- En cada iteracion se realiza las siguentes tareas:
    1. Comprobar que no se alcanzan las condiciones de parada, en cuyo caso se interrumpe el bucle.
    2. Actualizar los recursos necesarios para la iteracion actual.
    3. Obtener las entradas del sistema, o de interaccion con el jugador.
    4. Actualizar todas las entidades que caracterizan el juego
    5. Refrescar la pantalla

## Superficies pygame

- Superficie: 
    - Elemento geometrico
    - Linea, poligono, imagen, texto que se muestra en la pantalla
    - El poligono se puede o no rellenar de color
    - Las Superficie se crea de diferente manera dependiendo del tipo:
        - imagen: image.load()
        - texto: font.render()
        - Superficie generica: pygame.surface
        - Ventana del juego: pygame.display.set_mode() 


# Ejemplo Bandera de Colombia

```Python
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
```

![alt text](image.png)

