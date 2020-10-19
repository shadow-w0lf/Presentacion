from clasificador import Clasificador

class Cuadro:
    clasificador = None
    def __init__(self):
        self.clasificador = Clasificador()

    def mostrar(self, imagen):
        postura, vector = self.clasificador.posturaPersona(imagen)
        return postura , vector
    def ToClase(self, post):
        Posturas = [\
            'Mano Izquierda Apuntando',
            'Mano derecha Apuntando'
            'Brazos cruzados'
            'Mano alzada'
            'Mano Cabeza'
            'Manos costado'
            'Expositiva'
            'Manos cadera'
            'Mano Mentón'
            'Mano derecha Abierta'
            'Mano Izquierda Abierta'
            'Manos Juntas']
        return Posturas[post]