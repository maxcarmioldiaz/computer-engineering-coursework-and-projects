import matrices
import random

#Matriz
matriz = []
filas = 20
cols = 20

#Serpiente
head_f = 0
head_c = 0
lenght = 1
viva = True
direccion = "R" # U D R L
manzanas_comidas = 0

MANZANA = -1

VENENO = -2

MANZANA_DORADA = -3

def poner_manzana():
    manzana_f = random.randrange(0, filas)
    manzana_c = random.randrange(0, cols)
    while matriz[manzana_f][manzana_c] != 0:
        manzana_f = random.randrange(0, filas)
        manzana_c = random.randrange(0, cols)
    if random.randrange(0, 101) >= 10: 
        matriz[manzana_f][manzana_c] = MANZANA
    else:
        matriz[manzana_f][manzana_c] = MANZANA_DORADA

def poner_veneno():
    veneno_f = random.randrange(0, filas)
    veneno_c = random.randrange(0, cols)
    while matriz[veneno_f][veneno_c] != 0:
        veneno_f = random.randrange(0, filas)
        veneno_c = random.randrange(0, cols)
    matriz[veneno_f][veneno_c] = VENENO

def siguiente_posicion():
    if direccion == "R":
        return head_f, (head_c + 1) % matrices.cols(matriz)
    if direccion == "L":
        return head_f, (head_c - 1) % matrices.cols(matriz)
    if direccion == "U":
        return (head_f - 1) % matrices.filas(matriz), head_c
    if direccion == "D":
        return (head_f + 1) % matrices.filas(matriz), head_c

def death():
    new_f, new_c = siguiente_posicion()
    if matriz[new_f][new_c] == VENENO and lenght <= 2:
        return True
    return matriz[new_f][new_c] > 0

def cambiar_direccion(nueva_direccion):
    global direccion
    if nueva_direccion in ("U", "D") and direccion in ("L", "R"):
        direccion = nueva_direccion
    elif nueva_direccion in ("L", "R") and direccion in ("U", "D"):
        direccion = nueva_direccion

def avanzar():
    global viva, lenght, head_f, head_c, manzanas_comidas
    if viva:
        if death():
            viva = False
        else:
            new_f, new_c = siguiente_posicion()
            if matriz[new_f][new_c] == MANZANA:
                lenght += 1
                poner_manzana()
                manzanas_comidas = 1
            else:
                manzanas_comidas = 0
            if matriz[new_f][new_c] == VENENO:
                    lenght /= 2
                    poner_veneno()
            if matriz[new_f][new_c] == MANZANA_DORADA:
                lenght += 15
                poner_manzana()
                manzanas_comidas = 1
            else:
                manzanas_comidas = 0
            for f in range(filas):
                for c in range(cols):
                    if matriz[f][c] > 0:
                        matriz[f][c] -= 1
            matriz[new_f][new_c] = lenght
            head_f = new_f
            head_c = new_c

def init():
    global matriz, filas, cols, head_f, head_c, lenght, viva, direccion
    filas = 50
    cols = 50
    matriz = matrices.crearMatriz(filas, cols, 0)
    head_f = filas // 2
    head_c = cols // 2
    lenght = 3
    viva = True
    direccion = "R"
    matriz[head_f][head_c] = lenght
    poner_manzana()
    for i in range(10):
        poner_veneno()
