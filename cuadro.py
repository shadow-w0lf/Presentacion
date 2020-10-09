from clasificador import Clasificador

class Cuadro:
    clasificador = None
    def __init__(self):
        self.clasificador = Clasificador()

    def mostrar(self, imagen):
        postura, vector = self.clasificador.posturaPersona(imagen)
        return postura , vector
    def ToClase(self, post):
        Posturas = ["Apuntando", "Brazos Cruzados", "Mano alzada", "Mano Cabeza", "Brazos costados", "Postura abierta", "Manos caderas", "Mano A  Menton", "Mano abierta"]
        return Posturas[post]