def esRectanguloValido(x1, x2, y1, y2):
    """Procedimiento que evalua si los valores indicados pertenecen a las coordenadas de un rectangulo en un plano cartesiano
    donde los lados del rectangulo son paralelos a los ejes.
    Entradas y restricciones:
    x1: Entero (int) 
    x2: Entero (int)
    x1 tiene que ser menor que x2
    y1: Entero (int)
    y2: Entero (int)
    y1 tiene que ser menor que x2
    Salidas:
    no tiene
    """
def esRectanguloValido(x1, x2, y1, y2):
    if type(x1) != int:
        raise Exception("x1 debe ser entero")
    if type(x2) != int:
        raise Exception("x2 debe ser entero")
    if type(y1) != int:
        raise Exception("y1 debe ser entero")
    if type(y2) != int:
        raise Exception("y2 debe ser entero")

    if x1 >= x2:
        raise Exception("x1 debe ser menor que x2")
    if y1 >= y2:
        raise Exception("y1 debe ser menor que y2")
    
def estaDentro(x1, x2, y1, y2, a1, a2, b1, b2):
    """Funcion que evalua si un rectangulo esta dentro de otro
    Entradas y restricciones:
    x1: Entero (int)
    x2: Entero (int)
    y1: Entero (int)
    y2: Entero (int)
    a1: Entero (int)
    a2: Entero (int)
    b1: Entero (int)
    b2: Entero (int)
    Salida:
    Bool True o False
    """
    return (a1>=x1 and a2<=x2 and b1>=y1 and b2<=y2)
    
def main():
    """Programa principal de esta dentro del rectangulo o no"""
def main():
    while True:
        try:
            x1 = int(input("x1 del primer rectángulo: "))
            x2 = int(input("x2 del primer rectángulo: "))
            y1 = int(input("y1 del primer rectángulo: "))
            y2 = int(input("y2 del primer rectángulo: "))
            esRectanguloValido(x1, x2, y1, y2)
            break
        except ValueError:
            print("Error: ingrese números enteros.")
        except Exception as e:
            print(f"Error: {e}")
    while True:
        try:
            a1 = int(input("x1 del segundo rectángulo: "))
            a2 = int(input("x2 del segundo rectángulo: "))
            b1 = int(input("y1 del segundo rectángulo: "))
            b2 = int(input("y2 del segundo rectángulo: "))
            esRectanguloValido(a1, a2, b1, b2)
            break
        except ValueError:
            print("Error: ingrese números enteros.")
        except Exception as e:
            print(f"Error: {e}")
    if (x1, x2, y1, y2) == (a1, a2, b1, b2):
        print("Los rectángulos son iguales")
    elif estaDentro(x1, x2, y1, y2, a1, a2, b1, b2):
        print("El primer rectángulo está dentro del segundo")
    elif estaDentro(a1, a2, b1, b2, x1, x2, y1, y2):
        print("El segundo rectángulo está dentro del primero")
    else:
        print("Ninguno está dentro del otro")
        
if __name__ == "__main__":
    main()
