
from Mascota import Mascota

class Ninja:
    # implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
    def __init__(self,nombre:str, apellido:str, premios:int, comida_mascota:str, mascota:Mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota
    
    # implementa los siguientes métodos:
    # caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self):
        print("Se esta paseando a la mascota")
        self.mascota.jugar()
        return self
    
    # alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self):
        print("Se esta alimentando a la mascota")
        self.mascota.comer()
        return self

    # bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def bañar(self):
        print("Se esta limpiando a la mascota")
        self.mascota.ruido()
        return self