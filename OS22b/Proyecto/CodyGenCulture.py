import time
import random

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
print("2. No uses MAYÚSCULAS, espacios, acentos o caracteres numéricos; (sólo letras).")
print("3. ¡Diviértete!.")

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
categoria = int(input("Elige la que mas te guste: "))
print("¡Preparate, ya empieza el juego!")

# Diccionario de preguntas
from random import randint

# HISTORIA
lineas = [line.rstrip('\n') for line in open("historia.txt")]
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
lineas = [line.rstrip('\n') for line in open("geografia.txt")]
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
lineas = [line.rstrip('\n') for line in open("ciencia.txt")]
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
lineas = [line.rstrip('\n') for line in open("deportes.txt")]
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
lineas = [line.rstrip('\n') for line in open("arte-entretenimiento.txt")]
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

# Respuestas ------
respuestasHISTORIA = "mexico faraones pacifico terremoto nazi cempasuchil anglicismos homero thriller mapas"
respuetasGEO = "mexico america fronteras londres monterrey yucatan portugues españa puebla china"
respuestasCIENCIAS = "saturno carne cromo einstein tinta chicozapote estrellas física renal azufre"
respuestasDEPORTES = "brasil messi futbol hipodromo corea criquet halterofilia estadosunidos hockey touchdown"
respuestasARTE = "queen grecia manga davinci pikachu pintor enologo twitter filosofo rocinante"


# Random de preguntas
def ask_ans():
    return randint(1, 10)

# Categorías
if categoria in ["Historia", "historia", "hist", "Hist", "H", "h", "1"]:
    pregAleatoria = ask_ans()
    print(HISTORIA(pregAleatoria))
    

