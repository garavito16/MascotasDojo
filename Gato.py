from Mascota import Mascota

class Gato(Mascota):

    def __init__(self, name: str, tipo: str, golosinas: int):
        super().__init__(name, tipo, golosinas)

    def ruido(self):
        print("El gato esta maullando")