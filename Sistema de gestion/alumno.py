from utils import validarRut, validarCorreo

alumnos = []

class Alumno:
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

    def agregarAlumno():
        try:
            rut = input("Ingrese el rut del alumno: ")
            if not validarRut(rut):
                print("Rut invalido, intente de nuevo.")
                return
            nombre = input("Ingrese el nombre del Alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            correo = input("Ingrese el correo del alumno: ")
            if not validarCorreo(correo):
                print("Correo invalido, intente de nuevo.")
                return
            edad = int(input("Ingrese la edad del alumno: "))
            if edad < 0 or edad > 100:
                print("El alumno no puede ser menor de 0 años o mayor de 100 años")
                return
            direccion = input("Ingrese direccion del alumno: ")
            nuevo = Alumno(rut, nombre, apellido, correo, edad, direccion)
            alumnos.append(nuevo)
            print("Alumno agregado exitosamente.")
        except ValueError as ve:
            print(f"Error.{ve}")
        
    def actualizarAlumno(rut):
        try:
            for alumno in alumnos:
                if alumno.datos["rut"] == rut:
                    print("Alumno encontrado.")
                    alumno.mostrar()
                    nuevoNombre = input("Ingrese nuevo nombre: ")
                    nuevoApellido = input("Ingrese nuevo apellido: ")
                    nuevoCorreo = input("Ingrese nuevo correo: ")
                    if not validarCorreo(nuevoCorreo):
                        print("Correo invalido.")
                        return
                    nuevaEdad = int(input("Ingrese nueva edad: "))
                    if nuevaEdad < 0 or nuevaEdad > 100:
                        print("El alumno no puede ser menor a 0 años o mayor de 100 años")
                    nuevoDireccion = input("Ingrese nueva direccion: ")
                    alumno.datos["nombre"] = nuevoNombre
                    alumno.datos["apellido"] = nuevoApellido
                    alumno.datos["correo"] = nuevoCorreo
                    alumno.datos["edad"] = nuevaEdad
                    alumno.datos["direccion"] = nuevoDireccion
                    print("Alumno actualizado correctamente.")
                    return
            print("Alumno no encontrado.")
        except ValueError as ve:
            print(f"Error.{ve}")

    def verAlumno(rut):
        try:
            for alumno in alumnos:
                if alumno.datos["rut"] == rut:
                    print("Alumno encontrado.")
                    alumno.mostrar()
                    return
            print("Alumno no encontrado.")
        except ValueError as ve:
            print(f"Error.{ve}")

    def borrarAlumno(rut):
        try:
            for i, alumno in enumerate(alumnos):
                if alumno.datos["rut"] == rut:
                    del alumnos[i]
                    print("Alumno eliminado correctamente.")
                    return
            print("Alumno no encontrado.")
        except ValueError as ve:
            print(f"Error.{ve}")