class Mascota:
    # implementa __init__( name , tipo , golosinas ):
    def __init__(self, name:str, tipo:str, golosinas:int):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 0
        self.energía = 0

    # implementa los siguientes métodos:
    # dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energía += 25

    # comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energía += 5
        self.salud += 10

    # jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.salud += 5

    # ruido() - imprime el sonido que produce la mascota
    def ruido(self):
        print("La mascota emite un sonido")