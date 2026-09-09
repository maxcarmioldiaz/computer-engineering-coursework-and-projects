from time import time
from random import randint
import matplotlib.pyplot as plt

INCREMENTO = 2000

def lista_random(n):
    return [randint(0, 10000) for x in range(n)]

def bubble_sort(L):
    if type(L) != list:
        raise Exception("L debe ser una lista")
    n=0
    intercambios = True
    while intercambios == True and n<len(L)-1:
        intercambios = False
        for i in range(len(L)-n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                intercambios = True
        n += 1
    return L

def selection_sort(L):
    #restricciones
    for n in range(len(L)-1):
        pos_menor = menor(L, n)
        L[n], L[pos_menor] = L[pos_menor], L[n]
    return L
def menor(L, inicio):
    pos_menor = inicio
    for i in range(inicio + 1, len(L)):
        if L[i] < L[pos_menor]:
            pos_menor = i
    return pos_menor

def insertion_sort(L):
    #restricciones
    for iter in range(1, len(L)):
        i = iter
        while i > 0 and L[i] < L[i-1]:
            L[i], L[i-1] = L[i-1], L[i]
            i -= 1
    return L

def merge_sort(L):
    #restricciones
    return merge_sortAux(L)
def merge_sortAux(L):
    if len(L) < 2:
        return L
    izquierda = merge_sortAux(L[:len(L)//2])
    derecha = merge_sortAux(L[len(L)//2:])
    return merge(izquierda, derecha)
def merge(izq, der):
    L = []
    while izq != [] and der != []:
        if izq[0] <= der[0]:
            L.append(izq.pop(0))
        else:
            L.append(der.pop(0))
    L.extend(der if izq == [] else izq)
    return L

def quick_sort(L):
    #restricciones
    return quick_sortAux(L)
def quick_sortAux(L):
    if len(L) < 2:
        return L
    pivote = L.pop(len(L)//2)
    menores = [x for x in L if x < pivote]
    mayores = [x for x in L if x >= pivote]
    return quick_sortAux(menores) + [pivote] + quick_sortAux(mayores)

def medir_promedio(funcion, n):
    tiempos = []
    for i in range(10):
        L = lista_random(n)
        inicio = time()
        funcion(L)
        tiempos.append(time()-inicio)
    promedio = sum(tiempos) / 10
    return promedio
    
def lista_promedios(funcion):
    valores_n = []
    lista = []
    n = 100
    if funcion == merge_sort or funcion == quick_sort:
        while n <= 1000000:
            prom = medir_promedio(funcion, n)
            print(f"{funcion.__name__}: 10 pruebas de {n} elementos. Promedio: {prom}")
            valores_n.append(n)
            lista.append(prom)
            n += 100000
    else:
        while n <= 20000:
            prom = medir_promedio(funcion, n)
            print(f"{funcion.__name__}: 10 pruebas de {n} elementos. Promedio: {prom}")
            valores_n.append(n)
            lista.append(prom)
            n += INCREMENTO
    return valores_n, lista

bubbleSortN, bubbleSortT = lista_promedios(bubble_sort)
print("")
selectionSortN, selectionSortT = lista_promedios(selection_sort)
print("")
insertionSortN, insertionSortT = lista_promedios(insertion_sort)
print("")
mergeSortN, mergeSortT = lista_promedios(merge_sort)
print("")
quickSortN, quickSortT = lista_promedios(quick_sort)

plt.plot(bubbleSortN, bubbleSortT, label="bubbleSort")
plt.plot(selectionSortN, selectionSortT, label="selectionSort")
plt.plot(insertionSortN, insertionSortT, label="insertionSort")
plt.plot(mergeSortN, mergeSortT, label="mergeSort")
plt.plot(quickSortN, quickSortT, label="quickSort")

plt.xlabel("Cantidad de datos")
plt.ylabel("Segundos")
plt.title("Algoritmos de Ordenamiento")
plt.legend()
plt.show()
