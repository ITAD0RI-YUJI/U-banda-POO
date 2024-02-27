import random
from main import *

insturmentos_array = ["Guitarra" , "Saxofón" , "Flauta" , "Piano" , "Batería", 
                      "Maracas" , "Violín" , "Bajo" , "Triángulo" , "Contrabajo"]

def instrumento_aleatorio():
    instrumento_aleatorio = random.choice(range(len(insturmentos_array)))
    # insturmentos_array.pop(instrumento_aleatorio) #Marca error de "fuera de rango de lista"
    return insturmentos_array[instrumento_aleatorio]

# instrumento = Instrumento(instrumento_aleatorio())
musico = Musico(instrumento_aleatorio())

# instrumento.nombre_instrumento(instrumento_aleatorio())

print(musico.nombre_instrumento())

#1. en conclusión entendí el ejercicio, me toca preguntar, por qué se usa 
    #herencia? y qué toca hacer exactamente en el ejercicio, ya que no
    #entiendo.

#2. qué es el error "TypeError: 'str' object is not callable, en la línea 17"
    #lo he solucionado varias veces, pero no recuerdo como lo hice XD