def esValidoEstar(fila0, columna0):
    """Procedimiento que evalua si la posicion en la que se encuentra el caballo 
    en un tablero de ajedrez es valida
    Entradas y restricciones:
    fila0: numero entero, mayor o igual a 1 y menor o igual a 8
    columna0: numero entero, mayor o igual a 1 y menor o igual a 8
    Salidas:
    no tiene"""
    if type(fila0) != int or fila0 <=0 or fila0>8:
        raise Exception ("La fila debe ser un entero positivo igual o mayor a 1 y menor o igual a 8.")
    if type(columna0) != int or columna0 <=0 or columna0>8:
        raise Exception ("La columna debe ser un entero positivo igual o mayor a 1 y menor o igual a 8.")

def esValidoMover(fila, columna, fila0, columna0):
    """Funcion que evalua si la posicion a la que se mueve el caballo en un tablero de 
    ajedrez respecto a su posicion inicial (fila0, columna0) es valida.
    Entradas y restricciones:
    fila: numero entero, mayor o igual a 1 y menor o igual a 8
    columna: numero entero, mayor o igual a 1 y menor o igual a 8
    Salida: Booleano True o False"""
    if type(fila) != int or fila <=0 or fila>8:
        raise Exception ("La fila debe ser un entero positivo igual o mayor a 1 y menor o igual a 8.")
    if type(columna) != int or columna <=0 or columna>8:
        raise Exception ("La columna debe ser un entero positivo igual o mayor a 1 y menor o igual a 8.")
    diferenciaFila = abs(fila-fila0)
    diferenciaColumna = abs(columna-columna0)
    return diferenciaFila == 2 and diferenciaColumna == 1 or diferenciaFila == 1 and diferenciaColumna == 2
    
    
def main():
    """Programa principal de evaluar si es valido o no el moviimiento del caballo"""
    print("Movimientos validos de un caballo de ajedrez. " \
    "Escriba la posicion actual de la pieza")
    while True:
        try:
            fila0 = int(input("Fila (1-8): "))
            columna0 = int(input("Columna (1-8): "))
            esValidoEstar(fila0, columna0)
            break
        except Exception as e:
            print(f"Error: {e}")
        
    print("Escriba la posicion destino de la pieza")
    while True:
        try:
            fila = int(input("Fila (1-8): "))
            columna = int(input("Columna (1-8): "))
            esValidoEstar(fila, columna)
            break
        except Exception as e:
            print(f"Error: {e}")
            
    if esValidoMover(fila, columna, fila0, columna0):
        print("El movimiento es valido.")
    else:
        print("El movimiento no es valido.")

if __name__ == "__main__":
    main()
