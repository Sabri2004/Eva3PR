asignaturas = []

class Asignatura:
    def __init__(self, id, nombre, descripcion):
        self.datos = {
            "id":id,
            "nombre":nombre,
            "descripcion":descripcion,
        }

    def mostrar(self):
        print(f"id:{self.datos["id"]}")
        print(f"nombre:{self.datos["nombre"]}")
        print(f"descripcion:{self.datos["descripcion"]}")

    def agregarAsignatura():
        id = int(input("Ingrese el id de la asignatura: "))
        nombre = input("Ingrese el nombre de la asignatura: ")
        descripcion = input("Ingrese la descripcion de la asignatura: ")
        nuevo = Asignatura(id, nombre, descripcion)
        asignaturas.append(nuevo)
        print("Asignatura agregada exitosamente.")
        
    def actualizarAsignatura(id):
        for asignatura in asignaturas:
            if asignatura.datos["id"] == id:
                print("Asignatura encontrada.")
                asignatura.mostrar()
                nuevoId = int(input("Ingrese nuevo id: "))
                nuevoNombre = input("Ingrese nuevo nombre: ")
                nuevaDescripcion = input("Ingrese nueva descripcion: ")
                asignatura.datos["id"] = nuevoId
                asignatura.datos["nombre"] = nuevoNombre
                asignatura.datos["descripcion"] = nuevaDescripcion
                print("Asignatura actualizada correctamente.")
                return
        print("Asignatura no encontrada.")

    def verAsignatura(id):
        for asignatura in asignaturas:
            if asignatura.datos["id"] == id:
                print("Asignatura encontrada.")
                asignatura.mostrar()
                return
        print("Asignatura no encontrada.")

    def borrarAsignatura(id):
        for i, asignatura in enumerate(asignaturas):
            if asignatura.datos["id"] == id:
                del asignaturas[i]
                print("Asignatura eliminada correctamente.")
                return
        print("Asignatura no encontrada.")