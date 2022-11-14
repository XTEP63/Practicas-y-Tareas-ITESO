import random
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

lineas = [line.rstrip('\n') for line in open("Proyecto/historia.txt")]
HISTORIA = {
    "mexico": lineas[0], 
    "faraones": lineas[1], 
    "pacifico": lineas[2], 
    "terremoto": lineas[3], 
    "nazi": lineas[4], 
    "cempasuchil": lineas[5], 
    "anaglicismo": lineas[6], 
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

respuestasHISTORIA = "mexico faraones pacifico terremoto nazi cempasuchil anglicismos homero thriller mapas".split()
respuetasGEO = "mexico america fronteras londres monterrey yucatan portugues españa puebla china".split()
respuestasCIENCIAS = "saturno carne cromo einstein tinta chicozapote estrellas física renal azufre".split()
respuestasDEPORTES = "brasil messi futbol hipodromo corea criquet halterofilia estadosunidos hockey touchdown".split()
respuestasARTE = "queen grecia manga davinci pikachu pintor enologo twitter filosofo rocinante".split()

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

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

def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
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
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')


print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    # Permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

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
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break

            
            
    