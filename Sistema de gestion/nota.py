from utils import validarNota

notas = []

class Nota:
    def __init__(self, id, nota, puntaje, ponderacion):
        self.datos = {
            "id":id,
            "nota":nota,
            "puntaje":puntaje,
            "ponderacion":ponderacion
        }

    def mostrar(self):
        print(f"id:{self.datos["id"]}")
        print(f"nota:{self.datos["nota"]}")
        print(f"puntaje:{self.datos["puntaje"]}")
        print(f"ponderacion:{self.datos["ponderacion"]}")

    def agregarNota():
        try:
            id = int(input("Ingrese el id de la nota: "))
            nota = float(input("Ingrese la nota: "))
            if not validarNota(nota):
                print("Nota invalida.")
                return
            puntaje = float(input("Ingrese el puntaje de la nota: "))
            ponderacion = int(input("Ingrese la ponderacion de la nota: "))
            nuevo = Nota(id, nota, puntaje, ponderacion)
            notas.append(nuevo)
            print("Nota agregada exitosamente.")
        except ValueError as ve:
            print(f"Error.{ve}")

    def actualizarNota(id):
        for nota in notas:
            if nota.datos["id"] == id:
                print("Nota encontrada.")
                nota.mostrar()
                nuevaNota = int(input("Ingrese nueva nota: "))
                if not validarNota(nuevaNota):
                    print("Nota invalida.")
                    return
                nuevoPuntaje = int(input("Ingrese nuevo puntaje: "))
                nuevaPonderacion = int(input("Ingrese nueva ponderacion: "))
                nota.datos["nota"] = nuevaNota
                nota.datos["puntaje"] = nuevoPuntaje
                nota.datos["ponderacion"] = nuevaPonderacion
                print("Nota actualizada correctamente.")
                return
        print("Nota no encontrada.")

    def verNota(id):
        for nota in notas:
            if nota.datos["id"] == id:
                print("Nota encontrada.")
                nota.mostrar()
                return
        print("Nota no encontrada.")

    def borrarNota(id):
        for i, nota in enumerate(notas):
            if nota.datos["id"] == id:
                del notas[i]
                print("Nota eliminada correctamente.")
                return
        print("Nota no encontrada.")

        hola