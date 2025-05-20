import re

def validarRut(rut):
    rut = rut.upper().replace("-", "").replace(".", "")

    if not rut[:-1].isdigit():
        return False
    
    cuerpo = rut[:-1]

    dv = rut[-1]

    suma = 0

    multiplicador = 2

    for digito in reversed(cuerpo):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    digitoVerificador = 11 - resto

    if digitoVerificador == 11:
        dvEsperado = '0'
    elif digitoVerificador == 10:
        dvEsperado = 'K'
    else:
        dvEsperado = str(digitoVerificador)

    return dv == dvEsperado

def validarCorreo(correo):
    patron = r'^[\w.-]+@[\w.-]+.\w+$'
    return re.match(patron, correo) is not None

def validarNota(nota):
    if nota < 4.0:
        return
    elif nota > 4.0 and nota < 7.0:
        return
    else:
        print("Nota invalida.")

def apruebaSiNo(nota):
    if nota < 4.0:
        print("No podras aprobar esta asignatura.")
        return
    elif nota > 4.0 and nota < 7.0:
        print("Aprobaste esta asignatura.")
        return
    else:
        print("Nota invalida.")