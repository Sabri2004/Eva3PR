from utils import validarRut, validarCorreo

profesores = []

class Profesor:
    def __init__(self, rut, nombre, apellido, correo, edad, direccion):
        self.datos = {
            "rut":rut,
            "nombre":nombre,
            "apellido":apellido,
            "correo":correo,
            "edad":edad,
            "direccion":direccion
        }

    def mostrar(self):
        print(f"rut:{self.datos["rut"]}")
        print(f"nombre:{self.datos["nombre"]}")
        print(f"apellido:{self.datos["apellido"]}")
        print(f"correo:{self.datos["correo"]}")
        print(f"edad:{self.datos["edad"]}")
        print(f"direccion:{self.datos["direccion"]}")

    def agregarProfesor():
        try:
            rut = input("Ingrese el rut del profesor: ")
            if not validarRut(rut):
                print("Rut invalido, intente de nuevo.")
                return
            nombre = input("Ingrese el nombre del profesor: ")
            apellido = input("Ingrese el apellido del profesor: ")
            correo = input("Ingrese el correo del profesor: ")
            if not validarCorreo(correo):
                print("Correo invalido, intente de nuevo")
                return
            edad = int(input("Ingrese la edad del profesor: "))
            if edad < 23 or edad > 70:
                print("El profesor no puede ser menor a 23 años o mayor de 70 años.")
                return
            direccion = input("Ingrese direccion del profesor: ")
            nuevo = Profesor(rut, nombre, apellido, edad, direccion)
            profesores.append(nuevo)
            print("Profesor agregado exitosamente.")
        except ValueError as ve:
            print(f"Error.{ve}")

    def actualizarProfesor(rut):
        try:
            for profesor in profesores:
                if profesor.datos["rut"] == rut:
                    print("Profesor encontrado.")
                    profesor.mostrar()
                    nuevoNombre = input("Ingrese nuevo nombre: ")
                    nuevoApellido = input("Ingrese nuevo apellido: ")
                    nuevoCorreo = input("Ingrese nuevo correo: ")
                    if not validarCorreo(nuevoCorreo):
                        print("Correo invalido.")
                        return
                    nuevaEdad = int(input("Ingrese nueva edad: "))
                    if nuevaEdad < 23 or nuevaEdad > 70:
                        print("El profesor no puede ser menor de 23 años o mayor de 70 años")
                    nuevaDireccion = input("Ingrese nueva direccion: ")
                    profesor.datos["nombre"] = nuevoNombre
                    profesor.datos["apellido"] = nuevoApellido
                    profesor.datos["correo"] = nuevoCorreo
                    profesor.datos["edad"] = nuevaEdad
                    profesor.datos["direccion"] = nuevaDireccion
                    print("Profesor actualizado correctamente.")
                    return
            print("Profesor no encontrado.")
        except ValueError as ve:
            print(f"Error.{ve}")

    def verProfesor(rut):
        try:
            for profesor in profesores:
                if profesor.datos["rut"] == rut:
                    print("Profesor encontrado.")
                    profesor.mostrar()
                    return
            print("Profesor no encontrado.")
        except ValueError as ve:
            print(f"Error.{ve}")

    def borrarProfesor(rut):
        try:
            for i, profesor in enumerate(profesores):
                if profesor.datos["rut"] == rut:
                    del profesores[i]
                    print("Profesor eliminado correctamente.")
                    return
            print("Profesor no encontrado.")
        except ValueError as ve:
            print(f"Error.{ve}")