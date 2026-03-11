def obtener_dimensiones():
    """Obtiene las dimensiones de una matriz del usuario"""
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            if filas <= 0 or columnas <= 0:
                print("Las dimensiones deben ser positivas")
                continue
            return filas, columnas
        except ValueError:
            print("Error: Ingrese números enteros válidos")

def obtener_matriz(filas, columnas, numero_matriz):
    """Obtiene los datos de una matriz del usuario"""
    matriz = []
    print(f"\nIngrese los datos de la matriz {numero_matriz}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"Elemento [{i}][{j}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número válido")
        matriz.append(fila)
    return matriz

def multiplicar_matrices(A, B):
    """Multiplica dos matrices"""
    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])
    
    resultado = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

def mostrar_matriz(matriz):
    """Muestra una matriz de forma legible"""
    for fila in matriz:
        print([f"{valor:.2f}" for valor in fila])

# Programa principal
print("=== MULTIPLICACIÓN DE MATRICES ===\n")

print("Matriz 1:")
filas_1, columnas_1 = obtener_dimensiones()

print("\nMatriz 2:")
filas_2, columnas_2 = obtener_dimensiones()

# Verificar si se pueden multiplicar
if columnas_1 != filas_2:
    print(f"\nError: No se pueden multiplicar. Las columnas de la matriz 1 ({columnas_1}) deben ser iguales a las filas de la matriz 2 ({filas_2})")
else:
    matriz_1 = obtener_matriz(filas_1, columnas_1, 1)
    matriz_2 = obtener_matriz(filas_2, columnas_2, 2)
    
    resultado = multiplicar_matrices(matriz_1, matriz_2)
    
    print("\n=== RESULTADO ===")
    mostrar_matriz(resultado)