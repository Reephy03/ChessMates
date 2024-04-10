class Pieza:
    def __init__(self, color, nombre):
        self.color = color
        self.nombre = nombre

    def movimientos_validos(self, posicion, tablero):
        # Esta función devolverá una lista de movimientos válidos desde 'posicion'
        movimientos = []
        # Aquí vendrá la lógica para calcular los movimientos válidos basados en la posición de la pieza y el tablero
        return movimientos

    def __str__(self):
        # Devuelve la pieza como string
        return f"{self.color[0]}{self.nombre[0]}"


class Peon(Pieza):
    def __init__(self, color):
        super().__init__(color, "peon")

    def movimientos_validos(self, posicion, tablero):
        movimientos = []
        fila, columna = posicion

        # Definir la dirección del movimiento dependiendo del color del peón
        direccion = -1 if self.color == "negro" else 1
        fila_inicio = 6 if self.color == "negro" else 1

        # Movimiento simple hacia adelante
        if 0 <= fila + direccion < 8:
            if tablero[fila + direccion][columna] == "  ":
                movimientos.append((fila + direccion, columna))

                # Movimiento inicial de dos espacios
                if fila == fila_inicio and tablero[fila + 2 * direccion][columna] == "  ":
                    movimientos.append((fila + 2 * direccion, columna))

        # Capturas diagonales
        for desplazamiento in [-1, 1]:
            col_diagonal = columna + desplazamiento
            if 0 <= col_diagonal < 8:
                if 0 <= fila + direccion < 8 and tablero[fila + direccion][col_diagonal] != "  ":
                    pieza_diagonal = tablero[fila + direccion][col_diagonal]
                    if isinstance(pieza_diagonal, Pieza) and pieza_diagonal.color != self.color:
                        movimientos.append((fila + direccion, col_diagonal))

        return movimientos


class Torre(Pieza):
    def __init__(self, color):
        super().__init__(color, "torre")
        self.ha_movido = False

    def movimientos_validos(self, posicion, tablero):
        movimientos = []
        fila, columna = posicion

        # Movimientos verticales hacia arriba
        for f in range(fila - 1, -1, -1):
            if tablero[f][columna] == "  ":
                movimientos.append((f, columna))
            else:
                # Si hay una pieza, revisa si se puede comer
                if tablero[f][columna].color != self.color:
                    movimientos.append((f, columna))
                break

        # Movimientos verticales hacia abajo
        for f in range(fila + 1, 8):
            if tablero[f][columna] == "  ":
                movimientos.append((f, columna))
            else:
                # Si hay una pieza, revisa si se puede comer
                if tablero[f][columna].color != self.color:
                    movimientos.append((f, columna))
                break

        # Movimientos horizontales hacia la izquierda
        for c in range(columna - 1, -1, -1):
            if tablero[fila][c] == "  ":
                movimientos.append((fila, c))
            else:
                # Si hay una pieza, revisa si se puede comer
                if tablero[fila][c].color != self.color:
                    movimientos.append((fila, c))
                break

        # Movimientos horizontales hacia la derecha
        for c in range(columna + 1, 8):
            if tablero[fila][c] == "  ":
                movimientos.append((fila, c))
            else:
                # Si hay una pieza, revisa si se puede comer
                if tablero[fila][c].color != self.color:
                    movimientos.append((fila, c))
                break

        return movimientos


class Caballo(Pieza):
    def __init__(self, color):
        super().__init__(color, "caballo")

    def movimientos_validos(self, posicion, tablero):
        movimientos = []
        fila, columna = posicion
        # Las posiciones donde el caballo puede moverse
        desplazamientos = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                           (1, -2), (1, 2), (2, -1), (2, 1)]

        for df, dc in desplazamientos:
            f, c = fila + df, columna + dc
            if 0 <= f < 8 and 0 <= c < 8:  # Si está dentro del tablero
                casilla_objetivo = tablero[f][c]
                # Verificar si la casilla está vacía o contiene una pieza
                if casilla_objetivo == "  " or casilla_objetivo.color != self.color:
                    movimientos.append((f, c))

        return movimientos


class Alfil(Pieza):
    def __init__(self, color):
        super().__init__(color, "alfil")

    def movimientos_validos(self, posicion, tablero):
        movimientos = []
        fila, columna = posicion

        # Direcciones diagonales: arriba-izquierda, arriba-derecha, abajo-izquierda, abajo-derecha
        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for df, dc in direcciones:
            f, c = fila, columna
            while True:
                f += df
                c += dc
                if 0 <= f < 8 and 0 <= c < 8:  # Si está dentro del tablero
                    casilla_objetivo = tablero[f][c]
                    # Casilla vacía o pieza enemiga
                    if casilla_objetivo == "  " or casilla_objetivo.color != self.color:
                        movimientos.append((f, c))
                        break
                    else:
                        break
                else:
                    break

        return movimientos


class Rey(Pieza):
    def __init__(self, color):
        super().__init__(color, "rey")
        self.ha_movido = False

    def movimientos_validos(self, posicion, tablero):
        movimientos = []
        fila, columna = posicion
        # Posibles movimientos del rey en todas las direcciones
        desplazamientos = [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]

        for df, dc in desplazamientos:
            f, c = fila + df, columna + dc

            if 0 <= f < 8 and 0 <= c < 8:  # Si está dentro del tablero
                casilla_objetivo = tablero[f][c]
                # Casilla vacia o comer pieza
                if casilla_objetivo == "  " or casilla_objetivo.color != self.color:
                    movimientos.append((f, c))

        return movimientos


class Reina(Pieza):
    def __init__(self, color):
        super().__init__(color, "reina")

    def movimientos_validos(self, posicion, tablero):
        movimientos = []
        fila, columna = posicion
        # Direcciones: vertical, horizontal y diagonal
        direcciones = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 1),
                       (1, -1), (1, 0), (1, 1)]

        for df, dc in direcciones:
            f, c = fila, columna
            while True:
                f += df
                c += dc
                if 0 <= f < 8 and 0 <= c < 8:
                    casilla_objetivo = tablero[f][c]
                    # Casilla vacía o pieza enemiga
                    if casilla_objetivo == "  " or casilla_objetivo.color != self.color:
                        movimientos.append((f, c))
                        break
                    else:
                        break
                else:
                    break

        return movimientos


class Tablero:
    def __init__(self):
        self.tablero = [["  " for _ in range(8)] for _ in range(8)]
        self.inicializar_piezas()
        self.turno_actual = "blanco"

    def cambiar_turno(self):
        self.turno_actual = "negro" if self.turno_actual == "blanco" else "blanco"

    def inicializar_piezas(self):
        # Coloca las piezas en el tablero.
        self.tablero[0][0] = Torre("blanco")
        self.tablero[0][7] = Torre("blanco")
        self.tablero[0][1] = Caballo("blanco")
        self.tablero[0][2] = Alfil("blanco")
        self.tablero[0][3] = Reina("blanco")
        self.tablero[0][4] = Rey("blanco")
        self.tablero[0][5] = Alfil("blanco")
        self.tablero[0][6] = Caballo("blanco")
        self.tablero[7][0] = Torre("negro")
        self.tablero[7][7] = Torre("negro")
        self.tablero[7][1] = Caballo("negro")
        self.tablero[7][2] = Alfil("negro")
        self.tablero[7][3] = Reina("negro")
        self.tablero[7][4] = Rey("negro")
        self.tablero[7][5] = Alfil("negro")
        self.tablero[7][6] = Caballo("negro")

        for i in range(8):
            self.tablero[1][i] = Peon("blanco")
            self.tablero[6][i] = Peon("negro")

    def interpretar_movimiento(self, movimiento):
        movimiento = movimiento.lower()
        if movimiento in ["enroque corto", "enroque largo"]:
            inicio = "e1" if self.turno_actual == "negro" else "e8"
            fin = "g1" if movimiento == "enroque corto" else "c1"
            fin = fin if self.turno_actual == "negro" else fin.replace("1", "8")
        else:
            partes = movimiento.split()
            if len(partes) != 2:
                print("Formato inválido. Usa 'c1 e4' o 'enroque corto/largo'.")
                return None, None
            inicio, fin = partes

        try:
            fila_inicio, col_inicio = 8 - int(inicio[1]), "abcdefgh".index(inicio[0])
            fila_fin, col_fin = 8 - int(fin[1]), "abcdefgh".index(fin[0])
        except (ValueError, IndexError):
            print("Movimiento no válido. Usa el formato 'c1 e4'.")
            return None, None

        return (fila_inicio, col_inicio), (fila_fin, col_fin)

    def mostrar(self):
        print("  a  b  c  d  e  f  g  h")
        print("  -----------------------")
        for i, fila in enumerate(self.tablero):
            fila_str = " ".join(str(casilla) if isinstance(casilla, Pieza) else "  " for casilla in fila)
            print(f"{8 - i}|{fila_str}|{8 - i}")
        print("  -----------------------")
        print("  a  b  c  d  e  f  g  h")

    def validar_pieza_seleccionada(self, inicio):
        pieza = self.tablero[inicio[0]][inicio[1]]
        if not pieza or not isinstance(pieza, Pieza):  # Verificar que selecciono una pieza
            print("No has seleccionado ninguna pieza.")
            return False

        if pieza.color != self.turno_actual:  # Verificar que es el turno correcto
            print("No es tu turno.")
            return False

        return True

    def es_movimiento_valido(self, inicio, fin):
        pieza = self.tablero[inicio[0]][inicio[1]]

        if not self.validar_pieza_seleccionada(inicio):  # Verificar si selecciono una pieza correcta
            return False

        movimientos = pieza.movimientos_validos(inicio, self.tablero)
        print(f"Movimientos válidos desde {inicio}: {movimientos}")
        if fin in movimientos:
            return True
        return False

    def mover_pieza(self, inicio, fin):
        print(f"Intentando mover de {inicio} a {fin}")

        pieza = self.tablero[inicio[0]][inicio[1]]

        if not self.validar_pieza_seleccionada(inicio):  # Verificar si selecciono una pieza correcta
            return

        # Manejar el enroque
        if isinstance(pieza, Rey) and (fin == (0, 6) or fin == (0, 2) or fin == (7, 6) or fin == (7, 2)):
            if self.es_enroque_valido(inicio, fin):
                self.realizar_enroque(inicio, fin)
                return

        # Verificar si el movimiento es válido y no pone al rey en jaque
        if not self.es_movimiento_valido(inicio, fin):
            print("Movimiento no válido, intenta de nuevo.")
            return

        # Mover la pieza y verificar jaque
        pieza_destino_original = self.tablero[fin[0]][fin[1]]
        self.tablero[fin[0]][fin[1]] = pieza
        self.tablero[inicio[0]][inicio[1]] = "  "
        if self.esta_en_jaque(self.turno_actual):
            self.tablero[inicio[0]][inicio[1]] = pieza
            self.tablero[fin[0]][fin[1]] = pieza_destino_original
            print("\033[91mNo puedes realizar ese movimiento, tu rey estaría en jaque.\033[0m")
        else:
            self.cambiar_turno()

    def es_enroque_valido(self, inicio, fin):
        pieza = self.tablero[inicio[0]][inicio[1]]

        # Verificar si la pieza es un rey y si no se ha movido
        if not isinstance(pieza, Rey) or pieza.ha_movido:
            return False

        # Dirección del enroque (1 para enroque corto, -1 para enroque largo)
        direccion = 1 if fin[1] > inicio[1] else -1

        # Verificar que el espacio entre el rey y la torre está libre
        for i in range(1, 3 if direccion == 1 else 4):
            if self.tablero[inicio[0]][inicio[1] + i * direccion] != "  ":
                return False

        # Verificar que la torre en la esquina correspondiente no se ha movido
        torre_pos = 7 if direccion == 1 else 0
        torre = self.tablero[inicio[0]][torre_pos]
        if not isinstance(torre, Torre) or torre.ha_movido:
            return False

        for i in range(0, 3):
            casilla_rey = (inicio[0], inicio[1] + i * direccion)
            if self.esta_en_jaque(casilla_rey, pieza.color):
                return False

        return True

    def esta_en_jaque(self, color):
        # Encuentra la posición del rey
        pos_rey = None
        for f in range(8):
            for c in range(8):
                pieza = self.tablero[f][c]
                if isinstance(pieza, Rey) and pieza.color == color:
                    pos_rey = (f, c)
                    break
            if pos_rey:
                break

        # Verifica si alguna pieza enemiga puede atacar al rey
        color_oponente = "blanco" if color == "negro" else "negro"
        for f in range(8):
            for c in range(8):
                pieza = self.tablero[f][c]
                if isinstance(pieza, Pieza) and pieza.color == color_oponente:
                    if pos_rey in pieza.movimientos_validos((f, c), self.tablero):
                        return True
        return False

    def realizar_enroque(self, inicio, fin):
        direccion = 1 if fin[1] > inicio[1] else -1
        fila_rey = inicio[0]

        # Mover el rey
        self.tablero[fila_rey][fin[1]] = self.tablero[fila_rey][inicio[1]]
        self.tablero[fila_rey][inicio[1]] = "  "

        # Mover la torre
        col_torre_origen = 7 if direccion == 1 else 0
        col_torre_destino = fin[1] - direccion

        self.tablero[fila_rey][col_torre_destino] = self.tablero[fila_rey][col_torre_origen]
        self.tablero[fila_rey][col_torre_origen] = "  "

        self.cambiar_turno()
