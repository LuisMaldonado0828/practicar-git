# Hacer matriz en python
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

#Crear matriz
def crear_matriz(filas, columnas):
    numeros = []
    for i in range(filas):
        row = []
        for j in range(columnas):
            row.append(int((input((f"Introduce el primer valor en la posición fila: {i} columna: {j}: ")))))
        numeros.append(row)
    return numeros

matrix = crear_matriz(filas,columnas)

#Mostrar matriz 
def mostrar_matriz(matrix):
    print("La matriz introducida es: ")
    for i in range(len(matrix)):
        print(matrix[i])

mostrar_matriz(matrix)