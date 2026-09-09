import random
def isMatriz(M):
    if type(M)!=list:
        return False
    for fila in M:
        if type(fila)!=list:
            return False
        if len(fila)!=len(M[0]):
            return False
        for elemento in fila:
            if type(elemento) not in (int, float):
                return False
    return True

def crearMatriz(filas, cols, valor):
    M=[]
    for f in range(filas):
        fila = []
        for c in range(cols):
            fila.append(valor)
        M.append(fila)
    return M

def createMatrizRandom(filas, cols):
    M=[]
    for f in range(filas):
        fila = []
        for c in range(cols):
            fila.append(random.randint(0,99))
        M.append(fila)
    return M

def sumaMatriz(A,B):
    if not isMatriz(A) or not isMatriz(B):
        raise Exception("A y B deben ser matrices númericas")
    if filas(A)!=filas(B) or cols(A) != cols(B):
        raise Exception ("A y B deben tener las mismas dimensiones")
    C = crearMatriz(filas(A), cols(A), 0)
    for f in range(filas(C)):
                   for c in range(cols(C)):
                       C[f][c]=A[f][c]+B[f][c]
    return C

def filas(M):
    return len(M)

def cols(M):
    return len(M[0])

def restaMatriz(A,B):
    if not isMatriz(A) or not isMatriz(B):
        raise Exception("A y B deben ser matrices númericas")
    if filas(A)!=filas(B) or cols(A) != cols(B):
        raise Exception ("A y B deben tener las mismas dimensiones")
    C = crearMatriz(filas(A), cols(A), 0)
    for f in range(filas(C)):
                   for c in range(cols(C)):
                       C[f][c]=A[f][c]-B[f][c]
    return C

def transpuesta(M):
    if not isMatriz(M):
        raise Exception ("M no es una matriz valida")
    T = crearMatriz(cols(M),filas(M), 0)
    for f in range(filas(T)):
        for c in range(cols(T)):
            T[f][c]=M[c][f]
    return T

def multEscalar(M,e):
    if not isMatriz(M):
        raise Exception("M debe ser matriz válida")
    if type(e) not in (float, int):
        raise Exception("e debe ser un número")
    R= crearMatriz(filas(M),cols(M), 0)
    for f in range(filas(M)):
        for c in range(cols(M)):
            R[f][c]=M[f][c]*e
    return R

def multMatriz(A,B):
    if not isMatriz(A) or not isMatriz(B):
        raise Exception("A y B deben ser un matrices válidas")
    if cols(A) != filas(B):
        raise Exception ("Dimensiones no válidas")
    C = crearMatriz(filas(A),cols(B),0)
    for f in range(filas(A)):
        for c in range(cols(B)):
            valor=0
            for p in range(cols(A)):
                valor+=A[f][p]*B[p][c]
            C[f][c]=valor
    return C