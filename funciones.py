import random
from main import *

insturmentos_array = ["Guitarra" , "Saxofón" , "Flauta" , "Piano" , "Batería", 
                      "Maracas" , "Violín" , "Bajo" , "Triángulo" , "Contrabajo"]

def instrumento_aleatorio():
    instrumento_aleatorio = random.choice(range(len(insturmentos_array)))
    # insturmentos_array.pop(instrumento_aleatorio) #Marca error de "fuera de rango de lista"
    return insturmentos_array[instrumento_aleatorio]

print(instrumento_aleatorio())