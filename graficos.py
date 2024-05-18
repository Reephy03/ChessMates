import pygame
from clases import Pieza

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (125, 135, 150)
CELESTE = (70, 70, 70)
ROJO = (255, 0, 0)


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


def dibujar_menu_promocion(ventana, color, tamano_celda):
    opciones = ['Reina', 'Torre', 'Alfil', 'Caballo']
    ventana.fill(GRIS)
    fuente_pregunta = pygame.font.SysFont(None, tamano_celda // 2)
    fuente_opciones = pygame.font.SysFont(None, tamano_celda // 2)
    pregunta = "¿A qué pieza quieres promocionar el peón?"
    texto_pregunta = fuente_pregunta.render(pregunta, True, NEGRO if color == 'blanco' else BLANCO)
    ventana.blit(texto_pregunta, (tamano_celda // 2, tamano_celda // 2))

    for i, opcion in enumerate(opciones):
        texto = fuente_opciones.render(opcion, True, NEGRO if color == 'blanco' else BLANCO)
        ventana.blit(texto, (tamano_celda // 2, (i + 2) * tamano_celda))
    pygame.display.flip()


def obtener_eleccion_promocion(ventana, tamano_celda):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return None
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fila = pos[1] // tamano_celda - 2
                if 0 <= fila < 4:
                    return ['Reina', 'Torre', 'Alfil', 'Caballo'][fila]


def mostrar_mensaje(ventana, mensaje, tamano_celda):
    ventana.fill(GRIS)
    fuente_mensaje = pygame.font.SysFont(None, tamano_celda // 3)

    # Dividir el mensaje en varias líneas si es necesario
    palabras = mensaje.split()
    lineas = []
    linea_actual = palabras[0]

    for palabra in palabras[1:]:
        if fuente_mensaje.size(linea_actual + " " + palabra)[0] < ventana.get_width() - tamano_celda:
            linea_actual += " " + palabra
        else:
            lineas.append(linea_actual)
            linea_actual = palabra
    lineas.append(linea_actual)

    # Renderizar cada línea
    for i, linea in enumerate(lineas):
        texto_mensaje = fuente_mensaje.render(linea, True, ROJO)
        ventana.blit(texto_mensaje, (tamano_celda // 2, tamano_celda // 2 + i * (tamano_celda // 3)))

    pygame.display.flip()

    # Esperar a que el usuario presione una tecla para continuar
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return None
            elif evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.KEYDOWN:
                esperando = False