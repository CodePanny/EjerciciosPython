# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, 
# lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Coche:
    marca: ""
    modelo: ""
    puertas: 0
    potencia: 0
    cilindrada: 0
    precio: 0

    def __init__(self, marca, modelo, puertas, potencia, cilindrada, precio):
        self.marca = marca
        self.modelo = modelo
        self.puertas = puertas
        self.potencia = potencia
        self.cilindrada = cilindrada
        self.precio = precio

    def getnombrecompleto(self):
        return self.marca + " " + self.modelo

c1 = Coche("Honda", "Civic", 3, 160, 1600, 19000)
f = open('coches.bin', 'wb')
pickle.dump(c1, f)
f.close()

