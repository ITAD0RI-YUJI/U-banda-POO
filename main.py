class Instrumento:
    def __init__(self , nombre):
        self.nombre_instrumento = nombre
    
    def afinar(self):
        return print("\n• Afinando instrumento...")

class Musico(Instrumento):
    def tocar_instrumento(self):
        return print("♥ Tocando instrumento...")

