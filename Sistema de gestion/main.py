from menus import *

def main():
    menu()
    print("")
    print("Ingrese una opcion: ")
    try:
        opcion = int(input())
        if opcion == 1:
            submenuCrear()
            print("")
            print("Ingrese una opcion: ")
            try:
                opcion = int(input())
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    print("Volviendo a menu principal")
                    menu()
                else:
                    print("Has ingresado un dato erroneamente.")
            except ValueError:
                print("Has ingresado un dato erroneamente.")
        elif opcion == 2:
            submenuActualizar()
            print("")
            print("Ingrese una opcion: ")
            try:
                opcion = int(input())
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    print("Volviendo a menu principal")
                    menu()
                else:
                    print("Has ingresado un dato erroneamente.")
            except ValueError:
                print("Has ingresado un dato erroneamente.")
        elif opcion == 3:
            submenuVerDetalle()
            print("")
            print("Ingrese una opcion: ")
            try:
                opcion = int(input())
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    print("Volviendo a menu principal")
                    menu()
                else:
                    print("Has ingresado un dato erroneamente.")
            except ValueError:
                print("Has ingresado un dato erroneamente.")
        elif opcion == 4:
            submenuVerTodos()
            print("")
            print("Ingrese una opcion: ")
            try:
                opcion = int(input())
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    print("Volviendo a menu principal")
                    menu()
                else:
                    print("Has ingresado un dato erroneamente.")
            except ValueError:
                print("Has ingresado un dato erroneamente.")
        elif opcion == 5:
            submenuEliminar()
            print("")
            print("Ingrese una opcion: ")
            try:
                opcion = int(input())
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    print("Volviendo a menu principal")
                    menu()
                else:
                    print("Has ingresado un dato erroneamente.")
            except ValueError:
                print("Has ingresado un dato erroneamente.")
        elif opcion == 6:
            submenuEliminarTodos()
            print("")
            print("Ingrese una opcion: ")
            try:
                opcion = int(input())
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    print("Volviendo a menu principal")
                    menu()
                else:
                    print("Has ingresado un dato erroneamente.")
            except ValueError:
                print("Has ingresado un dato erroneamente.")
        else:
            print("Error no has elegido ninguna de las opciones dadas.")
            menu()

    except ValueError:
        print("Error: Debes ingresar un numero valido.")
    

main()
