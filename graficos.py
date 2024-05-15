import pygame
from clases import Pieza

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (125, 135, 150)
CELESTE = (70, 70, 70)


def dibujar_tablero(ventana, tamano_celda):
    colores = [BLANCO, CELESTE]
    for fila in range(8):
        for columna in range(8):
            color = colores[(fila + columna) % 2]
            pygame.draw.rect(ventana, color, pygame.Rect(columna * tamano_celda, fila * tamano_celda, tamano_celda, tamano_celda))


def dibujar_piezas(ventana, tablero, tamano_celda):
    for fila in range(8):
        for columna in range(8):
            pieza = tablero.tablero[fila][columna]
            if isinstance(pieza, Pieza):
                pieza_color = NEGRO if pieza.color == "negro" else BLANCO
                pieza_contorno = BLANCO if pieza.color == "negro" else NEGRO
                pieza_nombre = pieza.nombre[:2].upper()  # Tomar los dos primeros caracteres para la reina
                fuente = pygame.font.SysFont(None, tamano_celda // 2)
                texto = fuente.render(pieza_nombre, True, pieza_color)
                contorno = fuente.render(pieza_nombre, True, pieza_contorno)
                ventana.blit(contorno, (columna * tamano_celda + tamano_celda // 4 - 1, fila * tamano_celda + tamano_celda // 4 - 1))
                ventana.blit(texto, (columna * tamano_celda + tamano_celda // 4, fila * tamano_celda + tamano_celda // 4))
