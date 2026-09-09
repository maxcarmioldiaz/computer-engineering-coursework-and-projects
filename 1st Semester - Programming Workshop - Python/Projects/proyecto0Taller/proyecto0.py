ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
def codificacion(texto, alfabetoCodificado):
    """Función que recibe el texto y lo modifica tomando como parametros
    el texto y el alfabeto codificado de la funcion/cifrado que se encuentre
    Entradas:
        -texto:texto a modificar
        -alfabetoCodificado: alfabeto con las modificaciones de su cifrado aplicadas
    Salidas:
        -el texto codificado
    Restricciones:
        -ninguna"""
    texto = texto.split()
    textoCodificado = []
    for i in range (0, len(texto)):
        palabra = ""
        for letra in texto[i]:
            palabra += alfabetoCodificado[ALFABETO.index(letra)]
        textoCodificado.append(palabra)
    textoCodificado = " ".join(textoCodificado)
    return textoCodificado
def decodificacion(texto, alfabetoCodificado):
    """Función que recibe el texto y lo modifica tomando como parametros
    el texto y el alfabeto codificado de la funcion/cifrado que se encuentre
    Entradas:
        -texto:texto a modificar
        -alfabetoCodificado: alfabeto con las modificaciones de su cifrado aplicadas
    Salidas:
        -el texto decodificado
    Restricciones:
        -ninguna"""
    texto = texto.split()
    textoDecodificado = []
    for i in range (0, len(texto)):
        palabra = ""
        for letra in texto[i]:
            palabra += ALFABETO[alfabetoCodificado.index(letra)]
        textoDecodificado.append(palabra)
    textoDecodificado = " ".join(textoDecodificado)
    return textoDecodificado
def esTextoValido(texto, caracteresExtra = ""):
    """Funcion booleana que dice si un string es un texto valido
    para codificar o decodificar.
    Entradas: Texto a analizar
    Salidas: True si el texto contiene solo letras, espacios y tiene al menos
    un caracter, False si no.
    Restricciones: texto debe ser un string.
    """
    if type(texto) != str:
        raise Exception ("texto debe ser un string.")
    if texto == "":
        return False
    caracteresValidos = " aábcdeéfghiíjklmnñoópqrstuúüvwxyz" + caracteresExtra
    for letra in texto:
        if letra.lower() not in caracteresValidos:
            return False
    return True
def limpiarTexto(texto):
    """Función que lee el texto dado por el usuario, lo
    convierte a minúsculas y elimina tildes y espacios al final y el inicio del mensaje.
    Entradas:
        -texto: Mensaje dado por el usuario.
    Salidas:
        -texto ya limpio sin mayúsculas ni tildes. 
    Restricciones:
        -texto debe ser de tipo \"str\". """
    if type(texto) != str:
        raise Exception("Texto debe ser un string.")
    texto = texto.lower()
    texto = texto.strip()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")
    return texto
def cesarCod(texto, desplazamiento):
    """Función que codifica el texto dado utilizando cifrado césar
    con el desplazamiento indicado. Este cifrado consiste en sustituir cada letra
    del texto original, reemplazandola por otra letra que se encuentre desplazada
    cierta cantidad de posiciones más adelante en el alfabeto.
    Entradas:
        -texto: Mensaje dado por el usuario a codificar con el cifrado, sin mayúsculas ni tildes.
        -desplazamiento: Número entero que indica cuanto se desplaza el alfabeto hacia adelante
        creando un \"nuevo\" alfabeto que es el que se utiliza a la hora de codificar el mensaje (texto).
    Salidas:
        -texto codificado en cifrado césar.
    Restricciones:
        -desplazamiento debe ser un número entero.
        -texto debe ser de tipo \"str\". """
    if type(desplazamiento) != int:
        raise Exception("Desplazamiento debe ser un valor entero.")
    texto = limpiarTexto(texto)
    desplazamiento %= 27
    alfabetoCodificado = ALFABETO[desplazamiento:] + ALFABETO[:desplazamiento]
    textoCodificado = codificacion(texto, alfabetoCodificado)
    return textoCodificado
def cesarDec(texto, desplazamiento):
    """Función que decodifica el texto dado utilizando cifrado césar
    con el desplazamiento indicado. Este cifrado consiste en sustituir cada letra
    del texto original, reemplazandola por otra letra que se encuentre desplazada
    cierta cantidad de posiciones más adelante en el alfabeto.
    Entradas:
        -texto: Mensaje dado por el usuario a decodificar con el cifrado, sin mayúsculas ni tildes.
        -desplazamiento: Número entero que indica cuanto se desplaza el alfabeto hacia adelante
        creando un \"nuevo\" alfabeto que es el que se utiliza a la hora de decodificar el mensaje (texto).
    Salidas:
        -texto decodificado del cifrado césar.
    Restricciones:
        -desplazamiento debe ser un número entero.
        -texto debe ser de tipo \"str\".
        """
    if type(desplazamiento) != int:
        raise Exception("Desplazamiento debe ser un valor entero.")
    texto = limpiarTexto(texto)
    desplazamiento = -desplazamiento
    textoDecodificado = cesarCod(texto, desplazamiento)
    return textoDecodificado
def alfabetoCodificadoMono(palabra):
    """Funcion que genera el alfabeto codificado para la funcion monoCod y monoDec
    Entradas:
        -palabra: palabra dada por el usuario la cual se agrega al inicio del alfabetoCodificado
    Salidas: 
        -el alfabetoCodificado para este tipo de cifrado
    Restricciones:
        -ninguna"""
    palabraClave = []
    alfabetoCodificado = ALFABETO
    for letra in palabra:
        if letra not in palabraClave:
            palabraClave.append(letra)
        if letra in ALFABETO:
            alfabetoCodificado = alfabetoCodificado.replace(letra, "")
    palabraClave= "".join(palabraClave)
    alfabetoCodificado = palabraClave + alfabetoCodificado
    return alfabetoCodificado
def monoCod(texto, palabra):
    """Función que codifica el texto dado utilizando cifrado monoalfabético 
    con palabra clave. En este cifrado el orden del alfabeto se obtiene a partir
    de una palabra clave, usando esta al inicio del alfabeto. En caso de que la palabra
    clave tenga letras repetidas estas se eliminan.
    Entradas:
        -texto: Mensaje dado por el usuario a codificar con el cifrado, sin mayúsculas ni tildes.
        -palabra: Palabra clave dada por el usuario que se utiliza para crear un \"nuevo\" alfabeto que 
        es el utlizado a la hora de codificar el mensaje (texto).
    Salidas:
        -texto codificado con el cifrado monoalfabético con palabra clave.
    Restricciones:
        -texto debe ser de tipo \"str\".
        -palabra debe ser de tipo \"str\".
        """
    if type(texto) != str or type(palabra) != str:
        raise Exception ("El texto y la palabra deben ser strings")
    texto = limpiarTexto(texto)
    alfabetoCodificado = alfabetoCodificadoMono(palabra)
    textoCodificado = codificacion(texto, alfabetoCodificado)
    return textoCodificado
def monoDec(texto, palabra):
    """Función que decodifica el texto dado utilizando cifrado monoalfabético 
    con palabra clave. En este cifrado el orden del alfabeto se obtiene a partir
    de una palabra clave, usando esta al inicio del alfabeto. En caso de que la palabra
    clave tenga letras repetidas estas se eliminan.
    Entradas:
        -texto: Mensaje dado por el usuario a decodificar con el cifrado, sin mayúsculas ni tildes.
        -palabra: Palabra clave dada por el usuario que se utiliza para crear un \"nuevo\" alfabeto que 
        es el utlizado a la hora de decodificar el mensaje (texto).
    Salidas:
        -texto codificado con el cifrado monoalfabético con palabra clave.
    Restricciones:
        -texto debe ser de tipo \"str\".
        -palabra debe ser de tipo \"str\".
        """
    if type(texto) != str or type(palabra) != str:
        raise Exception ("El texto y la palabra deben ser strings")
    texto = limpiarTexto(texto)
    alfabetoCodificado = alfabetoCodificadoMono(palabra)
    textoDecodificado = decodificacion(texto, alfabetoCodificado)
    return textoDecodificado
def vignereCod(texto, palabra):
    """Función que codifica el texto dado utilizando cifrado Vigenère. Este cifrado hace una correspondencia
    numerica del 0 al 26 con las letras del alfabeto de la a a la z respectivamente. Utiliza una palabra clave.
    La codificación consiste en que al valor de la primer letra del mensaje a codificar se le suma el valor
    de la primer letra de la palabra clave, y se hace esto por cada una de las letras. Cada suma crea un nuevo valor
    y este valor se relaciona con una letra del alfabeto diferente, creando así el mensaje codificado.
    Entradas:
        -texto: Mensaje dado por el usuario a codificar con el cifrado, sin mayúsculas ni tildes.
        -palabra: Palabra clave dada por el usuario que se utiliza para crear nuevos valores mediante
        la suma con los valores asignados a las letras del mensaje a codificar.
    Salidas:
        -texto codificado con el cifrado vigenère.
    Restricciones:
        -texto debe ser de tipo \"str\".
        -palabra debe ser de tipo \"str\".
        """
    if type(texto) != str or type(palabra) != str:
        raise Exception ("El texto y la palabra deben ser strings")
    texto = limpiarTexto(texto)
    valoresPalabra = [ALFABETO.index(letra) for letra in palabra]
    valoresMensaje = [ALFABETO.index(letra) for letra in texto if letra != ' ']
    k = 0
    for i in range(len(valoresMensaje)):
        valoresMensaje[i] = valoresMensaje[i] + valoresPalabra[k]
        if valoresMensaje[i] > len(ALFABETO) - 1:
            valoresMensaje[i] = valoresMensaje[i] - len(ALFABETO)
        k += 1
        if k >= len(valoresPalabra):
            k = 0
    j = 0
    textoCodificado = []
    for letra in texto:
        if letra == ' ':
            textoCodificado.append(' ')
        else:
            textoCodificado.append(ALFABETO[valoresMensaje[j]])
            j += 1
    return "".join(textoCodificado)
def vignerDec(texto, palabra):
    """Función que decodifica el texto dado utilizando cifrado Vigenère. Este cifrado hace una correspondencia
    numerica del 0 al 26 con las letras del alfabeto de la a a la z respectivamente. Utiliza una palabra clave.
    La decodificación consiste en que al valor de la primer letra del mensaje codificado se le resta el valor
    de la primer letra de la palabra clave, y se hace esto por cada una de las letras. Cada resta da el valor 
    asignado a cada una de las letras del mensaje original, dando así el mensaje decodificado.
    Si alguna de las restas da un numero negativo, se cuenta de derecha a izquierda apartir del 26 
    con el valor del negativo.
    Entradas:
        -texto: Mensaje dado por el usuario a decodificar con el cifrado, sin mayúsculas ni tildes.
        -palabra: Palabra clave dada por el usuario que se utiliza para crear nuevos valores mediante
        la resta con los valores asignados a las letras del mensaje a decodificar.
    Salidas:
        -texto decodificado con el cifrado vigenère.
    Restricciones:
        -texto debe ser de tipo \"str\".
        -palabra debe ser de tipo \"str\".
        """
    if type(texto) != str or type(palabra) != str:
        raise Exception ("El texto y la palabra deben ser strings")
    valoresPalabra = [ALFABETO.index(letra) for letra in palabra]
    valoresMensaje = [ALFABETO.index(letra) for letra in texto if letra != ' ']
    k = 0
    for i in range(len(valoresMensaje)):
        valoresMensaje[i] = valoresMensaje[i] - valoresPalabra[k]
        if valoresMensaje[i] < 0:
            valoresMensaje[i] = valoresMensaje[i] + len(ALFABETO)
        k += 1
        if k >= len(valoresPalabra):
            k = 0
    j = 0
    textoCodificado = []
    for letra in texto:
        if letra == ' ':
            textoCodificado.append(' ')
        else:
            textoCodificado.append(ALFABETO[valoresMensaje[j]])
            j += 1
    return "".join(textoCodificado)
def matrizPlayfair(palabra):
    """Funcion que genera la matriz de letras para el cifrado PlayFair modificado
    Entradas:
        -palabra: palabra dada por el usuario la cual se agrega al inicio de la matriz
    Salidas: 
        -la matriz de letras para el cifrado PlayFair modificado
    Restricciones:
        -ninguna"""
    matriz = []
    extras = ["1", "2", "3"]
    for letra in palabra:
        if letra not in matriz:
            matriz.append(letra)
    for letra in ALFABETO:
        if letra not in matriz:
            matriz.append(letra)
    for num in extras:
        matriz.append(num)
    return matriz
def posicionMatriz(letra, matriz):
    """Funcion que devuelve la posicion de una letra dada en la matriz del cifrado PlayFair modificado
    Entradas:
        -matriz: matriz de letras para el cifrado PlayFair modificado
        -letra: letra a la cual se le quiere encontrar su posicion en la matriz
    Salidas: 
        -la posicion de la letra dada en la matriz del cifrado PlayFair modificado
    Restricciones:
        -ninguna"""
    indice = matriz.index(letra)
    fila = indice // 5
    columna = indice % 5
    return fila, columna

def codificarPareja(letra1, letra2, matriz):
    """Funcion que codifica una pareja de letras dada utilizando la matriz del cifrado PlayFair modificado
    Entradas:
        -matriz: matriz de letras para el cifrado PlayFair modificado
        -letra1: primera letra de la pareja a codificar
        -letra2: segunda letra de la pareja a codificar
    Salidas: 
        -la pareja de letras codificada utilizando la matriz del cifrado PlayFair modificado
    Restricciones:
        -ninguna"""
    fila1, columna1 = posicionMatriz(letra1, matriz)
    fila2, columna2 = posicionMatriz(letra2, matriz)
    #Caso 2
    if fila1 == fila2:
        letraCodificada1 = matriz[fila1 * 5 + (columna1 + 1) % 5]
        letraCodificada2 = matriz[fila2 * 5 + (columna2 + 1) % 5]
    #Caso 3
    elif columna1 == columna2:
        letraCodificada1 = matriz[((fila1 + 1) % 6) * 5 + columna1]
        letraCodificada2 = matriz[((fila2 + 1) % 6) * 5 + columna2]
    #Caso 1
    else:
        letraCodificada1 = matriz[fila1 * 5 + columna2]
        letraCodificada2 = matriz[fila2 * 5 + columna1]
    return letraCodificada1, letraCodificada2
def decodificarPareja(letra1, letra2, matriz):
    """Funcion que decodifica una pareja de letras dada utilizando la matriz del cifrado PlayFair modificado
    Entradas:
        -matriz: matriz de letras para el cifrado PlayFair modificado
        -letra1: primera letra de la pareja a decodificar
        -letra2: segunda letra de la pareja a decodificar
    Salidas: 
        -la pareja de letras decodificada utilizando la matriz del cifrado PlayFair modificado
    Restricciones:
        -ninguna"""
    fila1, columna1 = posicionMatriz(letra1, matriz)
    fila2, columna2 = posicionMatriz(letra2, matriz)
    #Caso 2
    if fila1 == fila2:
        letraDecodificada1 = matriz[fila1 * 5 + (columna1 - 1) % 5]
        letraDecodificada2 = matriz[fila2 * 5 + (columna2 - 1) % 5]
    #Caso 3
    elif columna1 == columna2:
        letraDecodificada1 = matriz[((fila1 - 1) % 6) * 5 + columna1]
        letraDecodificada2 = matriz[((fila2 - 1) % 6) * 5 + columna2]
    #Caso 1
    else:
        letraDecodificada1 = matriz[fila1 * 5 + columna2]
        letraDecodificada2 = matriz[fila2 * 5 + columna1]
    return letraDecodificada1, letraDecodificada2
def prepararPalabra(palabra):
    """Función que toma una palabra y la prepara para el cifrado PlayFair:
    separa letras repetidas consecutivas con '1' y si queda impar agrega '1' al final.
    Entradas:
        -palabra: string con la palabra a preparar.
    Salidas:
        -lista de parejas de caracteres listas para codificar.
    Restricciones:
        -ninguna"""
    letras = []
    for i in range(len(palabra)):
        letras.append(palabra[i])
        if i < len(palabra) - 1 and palabra[i] == palabra[i + 1]:
            letras.append("1")
    if len(letras) % 2 != 0:
        letras.append("1")
    parejas = []
    for i in range(0, len(letras), 2):
        parejas.append((letras[i], letras[i + 1]))  
    return parejas
  
def playfairCod(texto, palabra):
    """Función que codifica el texto dado utilizando cifrado PlayFair modificado. En este cifrado
    se genera una matriz de letras que se usa para sustituir las letras de dos en dos, la matriz
    consiste en 5 columnas y 6 filas, dando un total de 30 espacios, solo con las letras no se logra
    completar la matriz por lo que en los ultimos 3 espacios se sustituyen por 1, 2 y 3 respectivamente.
    Se separan las letras del mensaje en parejas, en caso de que alguna palabra tenga letras repetidas consecutivamente
    se separan con un \"1\" y si la cantidad de letras es impar la ultima letra se agrupa con el numero \"1\"
    las sustituciones se realizan según en que posiciones de la matriz se encuentran cada pareja de letras.
    Entradas:
        -texto: Mensaje dado por el usuario a codificar con el cifrado, sin mayúsculas ni tildes.
        -palabra: Palabra clave dada por el usuario .
    Salidas:
        -texto codificado con el cifrado PlayFair modificado.
    Restricciones:
        -texto debe ser de tipo \"str\".
        -palabra debe ser de tipo \"str\".
        """
    if type(texto) != str or type(palabra) != str:
        raise Exception ("El texto y la palabra deben ser strings")
    if palabra == "":
        raise Exception ("La palabra clave no puede ser vacía.")
    texto = limpiarTexto(texto)
    palabra = limpiarTexto(palabra)
    matriz = matrizPlayfair(palabra)
    palabras = texto.split()
    palabrasCodificadas = []
    for pal in palabras:
        parejas = prepararPalabra(pal)
        palabraCod = ""
        for (a, b) in parejas:
            palabraCod += "".join(codificarPareja(a, b, matriz))
        palabrasCodificadas.append(palabraCod)
    return " ".join(palabrasCodificadas)
def eliminarNumeros(texto):
    """Función que elimi los números separados ("1", "2", "3") del texto dado, para preparar el texto a 
    decodificar con el cifrado PlayFair modificado
    Entradas: 
        -texto: string con la palabra ya decodificada que puede contener números.
    Salidas:
        -texto sin los números separados ("1", "2", "3") del texto dado.
    Restricciones:
        -ninguna""" 
    textoLimpio = ""
    for i in texto:
        if i not in "123":
            textoLimpio += i
    return textoLimpio
def playfairDec(texto, palabra):
    """Función que decodifica el texto dado utilizando cifrado PlayFair modificado. En este cifrado
    se genera una matriz de letras que se usa para sustituir las letras de dos en dos, la matriz
    consiste en 5 columnas y 6 filas, dando un total de 30 espacios, solo con las letras no se logra
    completar la matriz por lo que en los ultimos 3 espacios se sustituyen por 1, 2 y 3 respectivamente.
    Se separan las letras del mensaje en parejas, en caso de que alguna palabra tenga letras repetidas consecutivamente
    se separan con un \"1\" y si la cantidad de letras es impar la ultima letra se agrupa con el numero \"1\"
    las sustituciones se realizan según en que posiciones de la matriz se encuentran cada pareja de letras.
    Entradas:
        -texto: Mensaje dado por el usuario a decodificar con el cifrado, sin mayúsculas ni tildes.
        -palabra: Palabra clave dada por el usuario .
    Salidas:
        -texto decodificado con el cifrado PlayFair modificado.
    Restricciones:
        -texto debe ser de tipo \"str\".
        -palabra debe ser de tipo \"str\".
        """
    if type(texto) != str or type(palabra) != str:
        raise Exception ("El texto y la palabra deben ser strings")
    if palabra == "":
        raise Exception ("La palabra clave no puede ser vacía.")
    palabra = limpiarTexto(palabra)
    matriz = matrizPlayfair(palabra)
    palabras = texto.split()   
    palabrasDecodificadas = []
    for pal in palabras:
        if len(pal) % 2 != 0:
            raise Exception ("El mensaje a decodificar no es válido, cada palabra debe tener una cantidad par de caracteres.")
        palabraDec = ""
        for i in range(0, len(pal), 2):
            palabraDec += "".join(decodificarPareja(pal[i], pal[i + 1], matriz))
        palabraDec = eliminarNumeros(palabraDec)
        palabrasDecodificadas.append(palabraDec)
    return " ".join(palabrasDecodificadas)
def railfenceCod(texto):
    """Función que codifica el texto dado utilizando cifrado Railfence. En este cifrado el texto
    original se escribe en zigzag, los caracteres se agrupan por filas, lo que genera la nueva posición 
    de cada caracter en el mensaje codificado. Luego el texto se divide en grupos de 5 caracteres
    separados por espacios, dando así el mensaje codificado.
    Entradas:
        -texto: Mensaje dado por el usuario a codificar con el cifrado.
    Salidas:
        -texto codificado con el cifrado Railfence.
    Restricciones:
        -texto debe ser de tipo \"str\".
        """
    if type(texto) != str:
        raise Exception("El texto debe ser un string")
    texto = texto.replace(" ", "-")
    textoCodificado = ""
    while len(texto) % 4 != 0:
        texto += "-"
    texto = texto[::4] + texto[1::2] + texto[2::4]
    for i in range(len(texto)):
        textoCodificado += texto[i]
        if (i + 1) % 5 == 0 and i != len(texto) - 1:
           textoCodificado += " "
    return textoCodificado
def railfenceDec(texto):
    """Función que decodifica el texto dado utilizando cifrado Railfence. Para la decodificacion
    se eliminan los espacios en blanco del texto, vuelve a separar el mensaje en 4 partes iguales 
    dejando 1 parte en la primer linea, 2 partes en la segunda y 1 parte en la ultima. 
    Para la reconstrucción del mensaje se toma a la vez un carácter de la primer línea, la segunda, la tercera
    y la segunda otra vez, esto hasta haber reconstruido el mensaje. Ya reconstruido el mensaje se reemplazan
    los guiones por espacios en blanco.
    Entradas:
        -texto: Mensaje dado por el usuario a decodificar con el cifrado, sin mayúsculas ni tildes.
    Salidas:
        -texto decodificado con el cifrado Railfence.
    Restricciones:
        -texto debe ser de tipo \"str\".
        """
    if type(texto) != str:
        raise Exception("El texto ebe ser un string")
    texto = texto.replace(" ", "")
    cantFila1 = 0
    cantFila2 = 0
    cantFila3 = 0
    for i in range(len(texto)):
        if i % 4 == 0:
            cantFila1 += 1
        elif i % 2 == 0:
            cantFila3 += 1
        else:
            cantFila2 += 1
    fila1 = texto[:cantFila1]
    fila2 = texto[cantFila1:cantFila1 + cantFila2]
    fila3 = texto[cantFila1 + cantFila2:]
    i1 = 0
    i2 = 0
    i3 = 0
    textoDecodificado = ""
    for i in range(len(texto)):
        if i % 4 == 0:
            textoDecodificado += fila1[i1]
            i1 += 1
        elif i % 2 == 0:
            textoDecodificado += fila3[i3]
            i3 += 1
        else:
            textoDecodificado += fila2[i2]
            i2 += 1
    textoDecodificado = textoDecodificado.replace("-", " ")
    return textoDecodificado.strip()

def escitalaCod(texto, lineas):
    """Función que codifica el texto dado utilizando cifrado Escítala. 
    Entradas:
        -texto: Mensaje dado por el usuario a codificar con el cifrado.
        -lineas: Cantidad de lineas en la que se divide el mensaje (texto) .
    Salidas:
        -texto codificado con el cifrado Escítala.
    Restricciones:
        -texto debe ser de tipo \"str\".
        -lineas debe ser un entero. 
        -lineas debe ser mayor a 1.
        """
    if type(texto) != str:
        raise Exception("El texto debe ser un string")
    if type(lineas) != int:
        raise Exception("Lineas debe ser un valor entero")
    if lineas <= 1:
        raise Exception("Lineas debe ser mayor a 1")
    texto =  texto.replace(" ", "-")
    textoModificado = ""
    textoCodificado = ""
    while len(texto)%lineas != 0:
        texto += "-"
    for i in range(lineas):
        textoModificado += texto[i::lineas]
    for i in range(len(textoModificado)):
        textoCodificado += textoModificado[i]
        if (i + 1) % 5 == 0 and i != len(texto) - 1:
           textoCodificado += " "
    return textoCodificado
def escitalaDec(texto, lineas):
    """Función que decodifica el texto dado utilizando cifrado Escítala. 
    Entradas:
        -texto: Mensaje dado por el usuario a decodificar con el cifrado.
        -lineas: Cantidad de lineas en la que se divide el mensaje (texto) .
    Salidas:
        -texto decodificado con el cifrado Escítala.
    Restricciones:
        -texto debe ser de tipo \"str\".
        -lineas debe ser un entero. 
        -lineas debe ser mayor a 1.
        """
    if type(texto) != str:
        raise Exception("El texto debe ser un string")  
    if type(lineas) != int:
        raise Exception("Lineas debe ser un valor entero")  
    if lineas <= 1:
        raise Exception("Lineas debe ser mayor a 1")    
    texto = texto.replace(" ", "")
    textoDecodificado = ""
    textoModificado = ""
    for i in range(len(texto)//lineas):
        textoModificado += texto[i::len(texto)//lineas]
    textoDecodificado = textoModificado.replace("-", " ")
    return textoDecodificado.strip()

def imprimirEntrada():
    """Subrutina que imprime un mensaje de bienvenida.
    Entradas: ninguna.
    Salidas: mensaje de bienvenida.
    Restricciones: ninguna."""
    print("   ____       _       _                          __   _          ")
    print("  / ___|_ __ (_)_ __ | |_ ___   __ _ _ __ __ _  / _| (_) __ _    ")
    print(" | |   | '__|| | '_ \\| __/ _ \\ / _` | '__/ _` || |_  | |/ _` |  ")
    print(" | |__ | |   | | |_) | || (_) | (_| | | | (_| ||  _| | | (_| |   ")
    print("  \\____|_|   |_| .__/ \\__\\___/ \\__, |_|  \\__,_||_|   |_|\\__,_|")
    print("               |_|             |___/                               ")
    print("")
    print("Bienvenido al programa de criptografía básica :D")
    print("")
    print("En este programa podrá elegir entre diferentes tipos de cifrado ya sea para codificar o decodificar mensajes")
    print("")
def codDecSalir():
    """Funcion que pregunta al usuario si desea codificar o decodificar
    seguidamente segun la eleccion del usuario invoca la funcion indicada
    Entradas: 
        -no tiene
    Salidas:
        - 1 o 2 dependiendo de si se decidio codificar o decodificar el mensaje
    Restricciones:
        -no tiene"""
    print("Desea codificar o decodificar un mensaje?")
    print("1. Codificacion")
    print("2. Decodificacion")
    print("0. Salir del programa")
    while True:
        try:
            eleccion = int(input("Elija alguna opción: "))
            if eleccion >= 0 and eleccion <= 2:
                print("")
                return eleccion
            else:
                print("Eleccion debe ser 0, 1 o 2")
        except ValueError:
            print("Eleccion debe ser un numero entero.")

def mensajeDespedida():
    """Funcion que imprime un mensaje de despedida al usuario
    Entradas: ninguna
    Salidas: mensaje de despedida
    Restricciones: ninguna"""
    print("Gracias por utilizar el programa :D")

def menuMetodos():
    """Programa que muestra el menu principal de codificacion y permite al usuario elegir
    el metodo.
    Entradas: ninguna
    Salidas: impresion en pantalla de las diferentes opciones a elegir
    Restricciones: ninguna"""
    print("Metodos a elegir: ")
    print("")
    print("1. Cifrado César")
    print("2. Cifrado Monoalfabetico")
    print("3. Cifrado Vignere")
    print("4. Cifrado Playfair Modificado")
    print("5. Cifrado Railfence")
    print("6. Cifrado Escitala")
    print("")
    while True:
        try:
            eleccion = int(input("Elija alguna opción: "))
            if eleccion >= 1 and eleccion <= 6:
                return eleccion
            else:
                print("Eleccion debe ser un numero entre el 1 y el 6")
        except ValueError:
            print("Eleccion debe ser un numero entero.")
def leerTexto(caracteresExtra = "", limpiar = True):
    """Funcion que solicita al usuario un texto valido.
    Entradas: ninguna
    Salidas: string con el texto ingresado por el usuario ya limpio
    Restricciones: ninguna"""
    while True:
        texto = str(input("Digite el mensaje: "))
        if limpiar:
            texto = limpiarTexto(texto)
        if esTextoValido(texto, caracteresExtra):
            return texto
        else:
         print("Texto invalido, intente de nuevo.")

def leerPalabraClave():
    """Funcion que solicita al usuario una palabra clave valida.
    Entradas: ninguna
    Salidas: string con la palabra clave ingresada por el usuario ya limpia
    Restricciones: ninguna"""
    while True:
        palabra = str(input("Escriba la palabra clave: "))
        palabra = limpiarTexto(palabra)
        if esTextoValido(palabra):
            return palabra
        print("Palabra invalida, intente de nuevo.")

def leerDesplazamiento():
    """Funcion que solicita al usuario el desplazamiento para el cifrado César,
    valida que sea un entero.
    Entradas: ninguna
    Salidas: entero con el desplazamiento ingresado por el usuario
    Restricciones: ninguna"""
    while True:
        try:
            desplazamiento = int(input("Escriba el desplazamiento: "))
            return desplazamiento
        except ValueError:
            print("El desplazamiento debe ser un numero entero.")

def leerLineas():
    """Funcion que solicita al usuario la cantidad de lineas para el cifrado Escítala.
    Entradas: ninguna
    Salidas: string con la cantidad de lineas ingresada por el usuario
    Restricciones: ninguna"""
    while True:
        try:
            lineas = int(input("Escriba la cantidad de lineas a utilizar: "))
            if lineas > 1:
                return lineas
            else:
                print("El numero de lineas debe ser un numero mayor a 1")
        except ValueError:
            print("El desplazamiento debe ser un numero entero.")

def procesarCodificacion(eleccion):
    """Funcion que solicita los datos necesarios y ejecuta la codificacion segun el metodo elegido.
    Entradas:
        -eleccion: entero del 1 al 6 que indica el metodo de codificacion
    Salidas:
        -impresion en pantalla del texto codificado
    Restricciones:
        -eleccion debe ser un entero del 1 al 6"""
    if eleccion == 5 or eleccion == 6:
        texto = leerTexto("-", False)
    else:
        texto = leerTexto("123" if eleccion == 4 else "", True)
    if eleccion == 1:
        desplazamiento = leerDesplazamiento()
        resultado = cesarCod(texto, desplazamiento)
    elif eleccion == 2:
        palabra = leerPalabraClave()
        resultado = monoCod(texto, palabra)
    elif eleccion == 3:
        palabra = leerPalabraClave()
        resultado = vignereCod(texto, palabra)
    elif eleccion == 4:
        palabra = leerPalabraClave()
        resultado = playfairCod(texto, palabra)
    elif eleccion == 5:
        resultado = railfenceCod(texto)
    else:
        lineas = leerLineas()
        resultado = escitalaCod(texto, lineas)
    print("")
    print(f"El mensaje codificado es: \"{resultado}\"")
    print("")
def procesarDecodificacion(eleccion):
    """Funcion que solicita los datos necesarios y ejecuta la decodificacion segun el metodo elegido.
    Entradas:
        -eleccion: entero del 1 al 6 que indica el metodo de decodificacion
    Salidas:
        -impresion en pantalla del texto decodificado
    Restricciones:
        -eleccion debe ser un entero del 1 al 6"""
    if eleccion == 5 or eleccion == 6:
        texto = leerTexto("-", False)
    else:
        texto = leerTexto("123" if eleccion == 4 else "", True)
    if eleccion == 1:
        desplazamiento = leerDesplazamiento()
        resultado = cesarDec(texto, desplazamiento)
    elif eleccion == 2:
        palabra = leerPalabraClave()
        resultado = monoDec(texto, palabra)
    elif eleccion == 3:
        palabra = leerPalabraClave()
        resultado = vignerDec(texto, palabra)
    elif eleccion == 4:
        palabra = leerPalabraClave()
        resultado = playfairDec(texto, palabra)
    elif eleccion == 5:
        resultado = railfenceDec(texto)
    else:
        lineas = leerLineas()
        resultado = escitalaDec(texto, lineas)
    print("")
    print(f"El mensaje decodificado es: \"{resultado}\"")
    print("")

def main():
    """Funcion principal del programa de critografía básica. Este programa interactúa con el usuario, de mensajes de bienvenida,
    describe brevemente el programa, permite elegir que método de encripción de quiere utilizar o si se desea salir del programa,
    en cada método de encripción se da la opción de elegir si se desea codificar o decodificar, muestra al usuario el resultado de
    la codificación/decodificación, y permite volver al menú principal para continuar con el uso del programa.
    Entradas: 
        -Ninguna.
    Salidas: 
        -Ninguna.
    Restricciones: 
        -Ninguna.
    Realizado por:
    Maximiliano Carmiol Díaz. Carnét: 2026006978
    Santiago Arrieta Salazar. Carnét: 2026017372
    Viviana Cordero Lewis. Carnét: 2026079158
    """
    imprimirEntrada()
    continuar = True
    while continuar:
        try:
            eleccion = codDecSalir()
            if eleccion == 0:
                mensajeDespedida()
                continuar = False
            elif eleccion == 1:
                metodo = menuMetodos()
                procesarCodificacion(metodo)
            else:
                metodo = menuMetodos()
                procesarDecodificacion(metodo)
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Intente de nuevo.")
if __name__ == "__main__":
    main()
