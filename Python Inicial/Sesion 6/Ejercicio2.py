
class Alumno:

    def start(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def resultado(self):
        if self.nota < 5:
            print(self.nombre, ", has suspendido este exámen con un ", self.nota, ". Revisa las respuestas"
                                                                                 " y no dudes en consultarme cualquier duda.", sep='')
        else:
            print("Enhorabuena ", self.nombre,
                  ", has aprobado. Pero recuerda que esto no es un sprint, si no una carrera de resistencia.", sep='')


Juan = Alumno()
Luis = Alumno()
Isabel = Alumno()

Juan.start("Juan Alberto", 3.7)
Luis.start("Luis Perez", 5.4)
Isabel.start("Isabel Diaz", 7.2)

Juan.resultado()
Luis.resultado()
Isabel.resultado()
