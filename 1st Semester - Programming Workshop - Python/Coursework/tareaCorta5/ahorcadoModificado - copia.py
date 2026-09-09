import random 
INTENTOS_MAX = 7
def limpiarPantalla():
    """Subrutina que imprime lineas en blanco para limpiar
    la pantalla.
    Entradas: ninguna.
    Salidas: 30 lineas en blanco.
    Restricciones: ninguna."""
    print("\n"*30)
def imprimirEntrada():
    """Subrutina que imprime un mensaje de bienvenida.
    Entradas: ninguna.
    Salidas: mensaje de bienvenida.
    Restricciones: ninguna."""
    print("Bienvenido al juego de")
    print("       .__                                     .___      ")
    print("_____  |  |__   ___________   ____ _____     __| _/____  ")
    print("\__  \ |  |  \ /  _ \_  __ \_/ ___\\\__  \   / __ |/  _ \ ")
    print(" / __ \|   Y  (  <_> )  | \/\  \___ / __ \_/ /_/ (  <_> )")
    print("(____  /___|  /\____/|__|    \___  >____  /\____ |\____/ ")
    print("     \/     \/                   \/     \/      \/       ")
    print()
    print("Tematica del juego: Paises")
    print()
    print("Creado por Maximiliano C.")
def esTextoValido(texto):
    """Funcion booleana que dice si un string es un texto valido
    para adivinar en el juego.
    Entradas: Texto a analizar
    Salidas: True si el texto contiene solo letras, espacios y tiene al menos
    un caracter, False si no.
    Restricciones: texto debe ser un string.  """
    if type(texto) != str:
        raise Exception ("texto debe ser un string.")
    if texto == "":
        return False
    for letra in texto:
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúüwxyz":
            return False
    return True
def leerTextoOriginal():
    """Funcion que lee de la consola la palabra o frase a ser 
    adivinada y retorna como resultado el texto leido.
    Entradas: texto del usuario
    Salidas: texto ingresado.
    Restricciones: ninguna."""
    texto = input("Ingrese la palabra o frase a adivinar: ")
    while not esTextoValido(texto):
        print("El texto solo puede contener letras y espacios.")
        texto = input("Ingrese la palabra o frase a adivinar: ")
    return texto
def preparar(texto):
    """Subrutina que convierte el texto a minusculas, sustituye acentos
    y elimina espacios al inicio y al final.
    Entradas: texto a procesar.
    Salidas: texto sin mayusculas, acentos y espacios al inicio y al final.
    Restricciones: texto debe ser un string."""
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
def adivino(texto, intentadas):
    """Funcion booleana que dice si el usuario ya adivino el texto.
    Entradas: 
     -texto: Texto preparado (sin tildes, ni acentos)
     -intentadas: letras que el usuario ha intentado
    Salidas: True si todas las letras del texto ya han sido intentadas
    False si no.
    Restricciones:
    - texto debe ser un string de letras sin acentos
    - string de letras sin acentos"""
    if type(texto) != str or type(intentadas) != str:
        raise Exception("El texto y las letras intentadas deben ser strings.")
    if not esTextoValido(texto):
        raise Exception("El texto y las intentadas contienen caracteres no validos. ")
    for letra in texto:
        if letra != " ":
            if letra not in intentadas:
                return False
    return True 
def enmascarar(texto, intentadas):
    """Retorna un string con un guion bajo por cada letra que no
    ha sido adivinada. Si una letra del texto aparece en las letras
    intentadas, entonces le agrega como tal en lugar del guion.
    Si el texto original tiene espacios, los sustituye con guiones
    normales.
    Entradas:
    texto: texto a adivinar.
    intentadas: letras que el ususario ha intentado.
    Salidas: string con el texto enmascarado.
    Restricciones: ninguna."""
    listaPalabras=texto.split()
    resultado = ""
    for palabra in listaPalabras:
        for letra in palabra:
            if letra in intentadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        resultado+= "- "
    return resultado[:-2]
def leerIntento(intentadas):
    """Funcion que pide al usuario que escriba una letra para adivinar.
    Si ya se encuentra en las intentadas o no es una letra, debe
    imprimir un mensaje de error y volver a pedir la letra.
    Entradas:
    intentadas: letras que el usuario a intentado
    Salidas: string con la letra elegida por el usuario.
    Restricciones: ninguna."""
    print()
    letra = input("Digite una letra: ")
    letra = letra.lower()
    while len(letra) != 1 or letra not in "abcdefghijklmnñopqrstuvwxyz" or letra in intentadas:
        print(f"Por favor ingrese una letra que no haya intentado. Intentadas : ({intentadas})")
        letra = input("Digite una letra: ")
        letra = letra.lower()
    print()
    return letra
def aciertaIntento(texto, letra):
    """Funcion booleana que dice si un intento es correcto o no.
    Entradas:
    texto que se esta adivinando
    letra que intento el usuario
    Salidas: True si la letra se encuentra en el texto a adivinar
    False si no.
    Restricciones: ninguna."""
    return letra in texto
def imprimirMensajeAcierto():
    """Subrutina que imprime un mensaje de acierto cuando el usuario
    escribe una letra que estaba en el texto original a adivinar.
    Entradas: 
    ninguna
    Salidas:
    mensaje de acierto si el usuario acierta alguna letra
    del texto a adivinar.
    Restricciones: ninguna"""
    print("Ha adivinado! :D")
def imprimirMensajeNoAcierto():
    """Subrutina que imprime un mensaje de no acierto cuando el usuario
    escribe una letra que no estaba en el texto original a 
    adivinar.
    Entradas: 
    ninguna
    Salidas:
    mensaje de no acierto si el usuario no acierta alguna letra
    del texto a adivinar.
    Restricciones: ninguna"""
    print("Letra no encontrada! :(")
def imprimirMensajeVictoria(textoOriginal):
    """Subrutina que imprime un mensaje de victoria cuando el usuario
    gana el juego.
    Entradas: 
    textoOriginal: texto original a adivinar
    Salidas:
    mensaje de victoria si el usuario gana el juego.
    Restricciones: ninguna"""
    print(f"Felicidades! Ha adivinado el texto: {textoOriginal} ")
def imprimirMensajeDerrota(textoOriginal):
    """Subrutina que imprime un mensaje de derrota cuando el usuario
    pierde el juego e indica cual era el texto a adivinar.
    Entradas: 
    textoOriginal: texto original a adivinar
    Salidas:
    mensaje de derrota si el usuario pierde el juego y el texto
    a adivinar.
    Restricciones: ninguna"""
    print(f"Ha perdido. El texto a adivinar era: {textoOriginal}")
def leerJugarNuevamente():
    """Funcion booleana que pregunta al usuario si desea jugar
    de nuevo solo acepta "si" o "no".
    Entradas:
     ninguna
    Salidas: 
     True si el usuario escribe "si", false si no.
    Restricciones:
     ninguna. """
    print()
    respuesta = input("Desea jugar de nuevo? (si/no): ")
    respuesta = respuesta.lower()
    return respuesta == "si"
def imprimirMensajeDespedida():
    """"""
    print("Gracias por jugar! :D")
    print("Juega de nuevo pronto!!")
def imprimirRonda(texto, intentadas, intentos, ronda):
    """Esta funcion imprime los mensajes requeridos para cada
    ronda del juego.
    Imprime el numero de ronda actual, un mensaje que indica las letras
    que ya fueron utilizadas, cantidad de intentos fallidos y 
    tambien escribe el texto enmascarado
    Entradas:
    texto: texto preparado sin tildes ni acentos
    intentadas: letras que el usuario a intentado
    intentos: cantidad de intentos fallidos
    ronda: numero de ronda por la que va el juego.
    Salidas: Impresion en pantalla de la informacion de la ronda.
    Restricciones: ninguna."""
    print()
    print(f"RONDA NUMERO: {ronda}")
    print(f"Letras que ya fueron utilizadas: {intentadas}")
    print(f"Cantidad de intentos fallidos: {intentos}")
    print()
    print(enmascarar(texto, intentadas))
    print()
def ahorcado():
    """Subrutina principal del juego de ahorcado."""
    global INTENTOS_MAX
    limpiarPantalla()
    imprimirEntrada()
    continuar = True
    while continuar:
        textoOriginal = leerTextoOriginal()
        limpiarPantalla()
        texto = preparar(textoOriginal)
        intentadas = ""
        intentos = 0
        ronda = 1
        while intentos<INTENTOS_MAX and \
              not adivino(texto, intentadas):
            imprimirRonda(texto, intentadas, intentos, ronda)
            letraIntento = leerIntento(intentadas)
            if aciertaIntento(texto, letraIntento):
                imprimirMensajeAcierto()
            else:
                imprimirMensajeNoAcierto()
                intentos += 1
            intentadas += letraIntento
            ronda += 1
        if adivino(texto, intentadas):
            imprimirMensajeVictoria(textoOriginal)
        else:
            imprimirMensajeDerrota(textoOriginal)
        continuar = leerJugarNuevamente()
    imprimirMensajeDespedida()
if __name__ == "__main__":
    ahorcado()
