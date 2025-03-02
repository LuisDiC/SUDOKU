# Definir el tablero de Sudoku como una lista de listas (9x9)
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Función para imprimir el tablero de Sudoku
def imprimir_tablero(tablero):
    for fila in range(9):
        if fila % 3 == 0 and fila != 0:
            print("- - - - - - - - - - - -")
        for columna in range(9):
            if columna % 3 == 0 and columna != 0:
                print(" | ", end="")
            if columna == 8:
                print(tablero[fila][columna])
            else:
                print(str(tablero[fila][columna]) + " ", end="")

# Función para encontrar una celda vacía en el tablero
def encontrar_vacio(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)  # fila, columna
    return None

# Función para comprobar si es válido colocar un número en una posición
def es_valido(tablero, numero, posicion):
    # Comprobar fila
    for i in range(9):
        if tablero[posicion[0]][i] == numero and posicion[1] != i:
            return False

    # Comprobar columna
    for i in range(9):
        if tablero[i][posicion[1]] == numero and posicion[0] != i:
            return False

    # Comprobar cuadrado 3x3
    caja_x = posicion[1] // 3
    caja_y = posicion[0] // 3
    for i in range(caja_y * 3, caja_y * 3 + 3):
        for j in range(caja_x * 3, caja_x * 3 + 3):
            if tablero[i][j] == numero and (i, j) != posicion:
                return False

    return True

# Función que resuelve el Sudoku usando backtracking
def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True
    else:
        fila, columna = vacio

    for i in range(1, 10):
        if es_valido(tablero, i, (fila, columna)):
            tablero[fila][columna] = i

            if resolver_sudoku(tablero):
                return True

            tablero[fila][columna] = 0

    return False

# Ejecutar el solucionador y mostrar el tablero resuelto
imprimir_tablero(tablero)
resolver_sudoku(tablero)
print("\nSudoku Resuelto:")
imprimir_tablero(tablero)