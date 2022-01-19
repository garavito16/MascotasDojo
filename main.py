from Ninja import Ninja
from Mascota import Mascota
from Perro import Perro

mascotita = Mascota("Sol","Gato",100)
ninja = Ninja("Alexander","Garavito",100,"RicoCat",mascotita)

ninja.alimentar().caminar().bañar()
print(mascotita.salud)
print(mascotita.energía)



perrito = Perro("Peluchin","Perro",5)
ninja2 = Ninja("Jorge","Vega",100,"Mi Mascot",perrito)

ninja2.bañar()
