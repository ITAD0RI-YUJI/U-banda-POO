class Instrumento:
    def afinar(self):
        pass
    
    def tocar(self):
        pass
    
    def mostrar(self):
        return "\n◘ Instrumento: " + str(type(self)).split(".")[-1][-2]


class Guitarra:
    def afinar(self):
        return "\n• Afinando Guitarra"
    
    def tocar(self):
        return "\n♠ Tocando Guitarra"


class Piano:
    def afinar(self):
        return "\n• Afinando piano"
    
    def tocar(self):
        return "\n♠ Tocando piano"


class Saxo:
    def afinar(self):
        return "\n• Afinando saxofón"
    
    def tocar(self):
        return "\n♠ Tocando saxofón"

class Platillos:
    def afinar(self):
        return "\n• Afinando Platillos"
    
    def tocar(self):
        return "\n♠ Tocando Platillos"

class Acordeon:
    def afinar(self):
        return "\n• Afinando Acordeón"
    
    def tocar(self):
        return "\n♠ Tocando Acordeón"

class Tambores:
    def afinar(self):
        return "\n• Afinando Tambores"
    
    def tocar(self):
        return "\n♠ Tocando Tambores"

class Bajo:
    def afinar(self):
        return "\n• Afinando Bajo"
    
    def tocar(self):
        return "\n♠ Tocando Bajo"

class Maracas:
    def afinar(self):
        return "\n• Afinando Maracas"
    
    def tocar(self):
        return "\n♠ Tocando Maracas"

class Bateria:
    def afinar(self):
        return "\n• Afinando Batería"
    
    def tocar(self):
        return "\n♠ Tocando Batería"

class Triangulo:
    def afinar(self):
        return "\n• Afinando Triángulo"
    
    def tocar(self):
        return "\n♠ Tocando Triángulo"