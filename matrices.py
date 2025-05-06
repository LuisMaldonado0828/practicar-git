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
    print(numeros)

crear_matriz(filas,columnas)