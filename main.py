import pygame
from clases import Tablero
from graficos import dibujar_tablero, dibujar_piezas

# Inicializa Pygame
pygame.init()

# Constantes
ANCHO, ALTO = 600, 600  # Reducir el tamaño de la ventana
DIMENSIONES = 8
TAMANO_CELDA = ANCHO // DIMENSIONES
FPS = 30

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (125, 135, 150)
CELESTE = (70, 70, 70)
ROJO = (255, 0, 0)

# Crear la ventana
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("ChessMates")


def main():
    reloj = pygame.time.Clock()
    tablero = Tablero()

    activo = True
    pieza_seleccionada = None
    inicio = None

    while activo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fila = pos[1] // TAMANO_CELDA
                columna = pos[0] // TAMANO_CELDA
                if pieza_seleccionada:
                    fin = (fila, columna)
                    if tablero.mover_pieza(inicio, fin):
                        pieza_seleccionada = None
                        inicio = None
                    else:
                        pieza_seleccionada = None
                        inicio = None
                else:
                    pieza_seleccionada = tablero.tablero[fila][columna]
                    inicio = (fila, columna)

        dibujar_tablero(VENTANA, TAMANO_CELDA)
        dibujar_piezas(VENTANA, tablero, TAMANO_CELDA)
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
