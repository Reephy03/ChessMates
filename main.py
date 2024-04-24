from clases import Tablero


def main():
    tablero = Tablero()
    while True:
        tablero.mostrar()

        movimiento = input(f"Turno del jugador {tablero.turno_actual}. Introduce tu movimiento: ")
        inicio, fin = tablero.interpretar_movimiento(movimiento)
        if inicio is None or fin is None:  # Verifica si la entrada es inválida
            continue  # Continúa con el siguiente ciclo del bucle si es inválido

        tablero.mover_pieza(inicio, fin)

        if tablero.jaque_mate(tablero.turno_actual):
            print(f"Jaque Mate! Ganador: {tablero.turno_actual}.")
            break
        elif tablero.esta_en_jaque(tablero.turno_actual):
            print("\033[91m¡Cuidado! Tu rey está en jaque.\033[0m")


if __name__ == "__main__":
    main()
