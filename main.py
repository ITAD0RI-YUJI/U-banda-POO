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