from musicos import *
from random import choice

class Banda: 
    def __init__(self):
        self.musicos = []
        self.instrumentos = [Guitarra() , Piano() , Saxo()]
        self.amigos = ["Felipe" , "Esteban" , "Erick" , "Juliana" , "Zayed" , "Aranda"]

    def crear_banda(self , cantidad_musicos):
        for i in range(cantidad_musicos):
            self.musicos.append(Musico(choice(self.amigos)))
            self.musicos[-1].asignar_instrumento(choice(self.instrumentos))
    
    def afinar_banda(self):
        for m in self.musicos:
            print(m.afinar_instrumento())

    def tocar_banda(self):
        for m in self.musicos:
            print(m.tocar_instrumento())

    def mostrar_banda(self):
        for m in self.musicos:
            print(m.nombre)
            print(type(m.instrumento))

if __name__ == "__main__":
    b = Banda()
    b.crear_banda(3)
    b.mostrar_banda()

    print("\n• Afinando la banda")
    b.afinar_banda()

    print("\n♠ A tocar: ")
    b.tocar_banda()