
class Vehículo:

    Color = ""
    Ruedas = 0
    Puertas = 0


class Coche(Vehículo):

    Velocidad = 0
    Cilindridada = 0


c = Coche()
c.Color = "Blanco"
c.Ruedas = 4
c.Puertas = 3
c.Velocidad = 230
c.Cilindrada = 1600

print("Es de color", c.Color)
print("Tiene", c.Ruedas, "ruedas")
print("Tiene", c.Puertas, "puertas")
print("Puede alcanzar una velocidad máxima de", c.Velocidad,"km/h")
print("Está equipado con un motor de", c.Cilindrada, "cc")
