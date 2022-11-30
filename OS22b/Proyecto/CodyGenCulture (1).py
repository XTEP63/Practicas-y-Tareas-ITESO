import time
import random

def elegirCategoria():
    # Validación de categorías
    lis_Historia = ["Historia","HISTORIA","historia","1"]
    lis_Geografia = ["Geografia","GEOGRAFIA","geografia","2"]
    lis_Ciencia = ["Ciencia","CIENCIA","ciencia","3"]
    lis_Deportes = ["Deportes","DEPORTES","deportes","4"]
    lis_Arte = ["Arte y entretenimiento","Arte","ARTE","ARTE Y ENTRETENIMIENTO","arte","arte y entretenimiento","5"]
    lis_Categorias =["Arte y entretenimiento","Arte","ARTE","ARTE Y ENTRETENIMIENTO","arte","arte y entretenimiento","5","Deportes","DEPORTES","deportes","4","Ciencia","CIENCIA","ciencia","3","Historia","HISTORIA","historia","1","Geografia","GEOGRAFIA","geografia","2",]

    #Respuestas -----
    respuestasHISTORIA = "mexico ".split()
    respuetasGEO = "mexico america fronteras londres monterrey yucatan portugues españa puebla china".split()
    respuestasCIENCIAS = "saturno carne cromo einstein tinta chicozapote estrellas fisica renal azufre".split()
    respuestasDEPORTES = "brasil messi futbol hipodromo corea criquet halterofilia estadosunidos hockey touchdown".split()
    respuestasARTE = "queen grecia manga davinci pikachu pintor enologo twitter filosofo rocinante".split()
    palabras = "".split()
    
    #Elección de un tema
    print("\n")
    print("-----------------------------------------------------------------------")
    print("Elige un tema:")
    print("\t1. Historia")
    print("\t2. Geografía")
    print("\t3. Ciencia")
    print("\t4. Deportes")
    print("\t5. Arte y entretenimiento")
    print("-----------------------------------------------------------------------")
    print("\n")

    # Validación de la respuuesta de categorías
    categoria = input("Elige la que mas te guste: ")
    while True:
        if categoria not in lis_Categorias:
            print("Esa categoria no existe.")
            print("Elige una categoria válida")
            print("-----------------------------------------------------------------------")
            print("\n")
            print("\t1. Historia")
            print("\t2. Geografía")
            print("\t3. Ciencia")
            print("\t4. Deportes")
            print("\t5. Arte y entretenimiento")
            print("-----------------------------------------------------------------------")
            print("\n")
            categoria = input("Elige la que mas te guste: ")
        else:
            break
    print("¡Preparate, ya empieza el juego!")

    # Respuestas según la categoría
    if categoria in lis_Historia:
        palabras = respuestasHISTORIA
        cat = "Historia"
    elif categoria in lis_Geografia:
        palabras = respuetasGEO
        cat = "Geografia"
    elif categoria in lis_Ciencia:
        palabras = respuestasCIENCIAS
        cat = "Ciencia"
    elif categoria in lis_Deportes:
        palabras = respuestasDEPORTES
        cat = "Deportes"
    elif categoria in lis_Arte:
        palabras = respuestasARTE
        cat = "Arte"

    return cat, palabras


jugar_no = "No", "no", "nO", "NO", "n", "N"
jugar_si = "Si", "si", "sI", "SI", "s", "S"
IMÁGENES_AHORCADO = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''      

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Diccionarios de categorías
# Historia
lineas = [line.rstrip('\n') for line in open("Proyecto/historia.txt")]

HISTORIA = {
    "mexico": lineas[0], 
    "faraones": lineas[1], 
    "pacifico": lineas[2], 
    "terremoto": lineas[3], 
    "nazi": lineas[4], 
    "cempasuchil": lineas[5], 
    "anglicismos": lineas[6], 
    "homero": lineas[7], 
    "thriller": lineas[8], 
    "mapas": lineas[9] 
    }

# GEOGRAFÍA
lineas = [line.rstrip('\n') for line in open("Proyecto/geografia.txt")]
GEOGRAFIA = {
    "mexico": lineas[0], 
    "america": lineas[1], 
    "fronteras": lineas[2], 
    "londres": lineas[3], 
    "monterrey": lineas[4], 
    "yucatan": lineas[5], 
    "portugues": lineas[6], 
    "españa": lineas[7], 
    "puebla": lineas[8], 
    "china": lineas[9] 
    }

# CIENCIA
lineas = [line.rstrip('\n') for line in open("Proyecto/ciencia.txt")]
CIENCIA = {
    "saturno": lineas[0], 
    "carne": lineas[1], 
    "cromo": lineas[2], 
    "einstein": lineas[3], 
    "tinta": lineas[4], 
    "chicozapote": lineas[5], 
    "estrellas": lineas[6], 
    "fisica": lineas[7], 
    "renal": lineas[8], 
    "azufre": lineas[9] 
    }

# DEPORTES
lineas = [line.rstrip('\n') for line in open("Proyecto/deportes.txt")]
DEPORTES = {
    "brasil": lineas[0], 
    "messi": lineas[1], 
    "futbol": lineas[2], 
    "hipodromo": lineas[3], 
    "corea": lineas[4], 
    "criquet": lineas[5], 
    "halterofilia": lineas[6], 
    "estadosunidos": lineas[7], 
    "hockey": lineas[8], 
    "touchdown": lineas[9] 
    }

# ARTE-ENTRETENIMIENTO
lineas = [line.rstrip('\n') for line in open("Proyecto/arte-entretenimiento.txt")]
ARTE = {
    "queen": lineas[0], 
    "grecia": lineas[1], 
    "manga": lineas[2], 
    "davinci": lineas[3], 
    "pikachu": lineas[4], 
    "pintor": lineas[5], 
    "enologo": lineas[6], 
    "twitter": lineas[7], 
    "filosofo": lineas[8], 
    "rocinante": lineas[9] 
    }



# Bienvenida al jugador
print("\n")
print("¡Hola! Bienvedido a CodyGenCulture, tu juego para aprender sobre cultura general")
print("Juego del ahorcado :)")
print("-----------------------------------------------------------------------")
nombre = input("¡Hola! ¿Como te llamas?: ")
print("-----------------------------------------------------------------------")
time.sleep(1)

# Reglas del juego
print("\n")
print(nombre + " para empezar tienes que saber las reglas del juego:")
print("1. Responde con tu conocimiento.")
print("2. No uses espacios, acentos o caracteres numéricos; (sólo letras).")
print("3. ¡Diviértete!.")

categoria, palabras = elegirCategoria()

def obtenerPalabraAlAzar(listaDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    
    índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[índiceDePalabras]        
        

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()

def obtenerIntento(categoria, letrasProbadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        
        if categoria == "Historia":
            print(HISTORIA[palabraSecreta])
        elif categoria == "Geografia":
            print(GEOGRAFIA[palabraSecreta])
        elif categoria == "Deportes":
            print(DEPORTES[palabraSecreta])
        elif categoria == "Ciencia":
            print(CIENCIA[palabraSecreta])
        elif categoria == "Arte":
            print(ARTE[palabraSecreta])
        
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento

def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres seguir jugando ? (sí o no)')
    roud = input()
    
    while True:
        if roud in ["si","Si","si","sI"]:
            return ("s")
        elif roud in ["no","No","NO","nO"]:
            break
        else:
            print("Si o No, -_-")
            roud = input("Quieres jugar otras ronda ?: ")
            continue


print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    # Permite al jugador escribir una letra.
    intento = obtenerIntento(categoria,letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento

        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True

    # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
    if juegoTerminado:
        
        if len(palabras) > 0:
            palabras.remove(palabraSecreta)

        if len(palabras) == 0:
            print("WOW! Has acabado esta categoria te gustaria eleguir otra ?")
            
        if jugarDeNuevo():
            if len(palabras) == 1:
                categoria, palabras = elegirCategoria()
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break

