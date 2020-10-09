class Persona:
    def __init__(self, id):
        self.id = id
        self.postura = {}
        self.postura_text = ""

        self.emotion = ""
        self.mirada = None

    def get_postura(self):
        return self.postura
    
    def set_postura(self, postura):
        self.postura = postura
