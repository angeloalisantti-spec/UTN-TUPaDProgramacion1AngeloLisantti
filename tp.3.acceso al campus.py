# EJERCICIO 2 - ACCESO AL CAMPUS Y MENÚ SEGURO

# Credenciales correctas
usuario_correcto = "alumno"
clave_correcta = "python123"

# Cantidad de intentos
intentos = 0
acceso = False

# LOGIN - máximo 3 intentos
while intentos < 3 and not acceso:

    usuario = input(f"Intento {intentos + 1}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")
        intentos += 1


# Si falla los 3 intentos
if not acceso:
    print("Cuenta bloqueada.")


# MENÚ
else:

    opcion = ""

    while opcion != "4":

        print("\n1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ")

        # Validar que sea un número
        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        # Validar que esté entre 1 y 4
        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")

        elif opcion == "1":
            print("Inscripto")

        elif opcion == "2":

            nueva_clave = input("Nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: la clave debe tener mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirme la nueva clave: ")

            while nueva_clave != confirmacion:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirme la nueva clave: ")

            clave_correcta = nueva_clave

            print("Clave cambiada correctamente.")

        elif opcion == "3":
            print("¡Seguí adelante, si no te sale como ami no pasa nada!")

        elif opcion == "4":
            print("Sesión finalizada.")