def imprimirTriangulo(size):
    """Funcion que imprime en pantalla un triangulo
    formado por digitos del 1 al 9.
    Entradas y restricciones:
    size: debe ser un entero positivo o sea size>0
    size es el tamaño del triangulo
    Salidas: un triangulo con la cantidad de filas
    definidas por size"""
    if type(size) != int or size <=0:
        raise Exception("El tamaño del triangulo debe ser mayor que 0")
    for i in range(1, size+1):
        print(f"{" "*(size-i)}",end="")
        for i2 in range(i, i*2):
            print(f"{i2%10}",end="")
        for i2 in range(i2-1, i-1, -1):
            print(f"{i2%10}",end="")
        print()

        
def main():
    """Programa principal de imprimir triangulo"""
    continuar = True
    while continuar:
        try:
            size= int(input("Escriba de que tamaño quiere que sea su triangulo: "))
            imprimirTriangulo(size)
        except Exception as e:
            print(f"Error: {e}")
            continuar = False
if __name__ == "__main__":
    main()
