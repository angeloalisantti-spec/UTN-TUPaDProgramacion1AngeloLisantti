def pedir_solo_letras(mensaje):
    """Pide un texto y valida que contenga únicamente letras (sin números ni símbolos)."""
    valido = False
    texto = ""
    while not valido:
        texto = input(mensaje).strip()
        # Rematamos espacios para verificar que el resto sean solo letras
        texto_sin_espacios = texto.replace(" ", "")
        
        if texto_sin_espacios != "" and texto_sin_espacios.isalpha():
            valido = True
        else:
            print("Error: Ingrese únicamente letras (no se permiten números ni caracteres especiales).")
    return texto


# VARIABLES DE LA AGENDA (Variables individuales)

# Lunes (4 cupos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Martes (3 cupos)
martes1 = ""
martes2 = ""
martes3 = ""


# INICIO DEL SISTEMA

print("=== SISTEMA DE GESTIÓN DE TURNOS ===")
operador = pedir_solo_letras("Ingrese el nombre del operador: ")
print("\n¡Bienvenido/a " + operador + "!")

ejecutando = True

while ejecutando:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Seleccione una opción (1-5): ").strip()

    # OPCIÓN 1: RESERVAR TURNO
    if opcion == "1":
        print("\n--- RESERVAR TURNO ---")
        print("1. Lunes")
        print("2. Martes")
        dia = input("Seleccione el día (1 o 2): ").strip()

        if dia == "1":
            # Verificar si está lleno
            if lunes1 != "" and lunes2 != "" and lunes3 != "" and lunes4 != "":
                print("No hay turnos disponibles para el día Lunes.")
            else:
                paciente = pedir_solo_letras("Ingrese el nombre del paciente: ")
                paciente_lower = paciente.lower()
                
                # Validar duplicados sin usar listas
                if (paciente_lower == lunes1.lower() or 
                    paciente_lower == lunes2.lower() or 
                    paciente_lower == lunes3.lower() or 
                    paciente_lower == lunes4.lower()):
                    print("El paciente '" + paciente + "' ya tiene un turno reservado el Lunes.")
                else:
                    # Guardar en el primer espacio libre
                    if lunes1 == "":
                        lunes1 = paciente
                    elif lunes2 == "":
                        lunes2 = paciente
                    elif lunes3 == "":
                        lunes3 = paciente
                    elif lunes4 == "":
                        lunes4 = paciente
                    print("Turno reservado con éxito para " + paciente + " el Lunes.")

        elif dia == "2":
            # Verificar si está lleno
            if martes1 != "" and martes2 != "" and martes3 != "":
                print("No hay turnos disponibles para el día Martes.")
            else:
                paciente = pedir_solo_letras("Ingrese el nombre del paciente: ")
                paciente_lower = paciente.lower()
                
                # Validar duplicados sin usar listas
                if (paciente_lower == martes1.lower() or 
                    paciente_lower == martes2.lower() or 
                    paciente_lower == martes3.lower()):
                    print("El paciente '" + paciente + "' ya tiene un turno reservado el Martes.")
                else:
                    # Guardar en el primer espacio libre
                    if martes1 == "":
                        martes1 = paciente
                    elif martes2 == "":
                        martes2 = paciente
                    elif martes3 == "":
                        martes3 = paciente
                    print("Turno reservado con éxito para " + paciente + " el Martes.")

        else:
            print("Día no válido. Seleccione 1 o 2.")

    # OPCIÓN 2: CANCELAR TURNO
    elif opcion == "2":
        print("\n--- CANCELAR TURNO ---")
        print("1. Lunes")
        print("2. Martes")
        dia = input("Seleccione el día (1 o 2): ").strip()

        if dia == "1":
            paciente = pedir_solo_letras("Ingrese el nombre del paciente a cancelar: ")
            paciente_lower = paciente.lower()
            cancelado = False

            if lunes1.lower() == paciente_lower:
                lunes1 = ""
                cancelado = True
            elif lunes2.lower() == paciente_lower:
                lunes2 = ""
                cancelado = True
            elif lunes3.lower() == paciente_lower:
                lunes3 = ""
                cancelado = True
            elif lunes4.lower() == paciente_lower:
                lunes4 = ""
                cancelado = True

            if cancelado:
                print("Turno de '" + paciente + "' cancelado exitosamente para el Lunes.")
            else:
                print("No se encontró ningún turno a nombre de '" + paciente + "' el Lunes.")

        elif dia == "2":
            paciente = pedir_solo_letras("Ingrese el nombre del paciente a cancelar: ")
            paciente_lower = paciente.lower()
            cancelado = False

            if martes1.lower() == paciente_lower:
                martes1 = ""
                cancelado = True
            elif martes2.lower() == paciente_lower:
                martes2 = ""
                cancelado = True
            elif martes3.lower() == paciente_lower:
                martes3 = ""
                cancelado = True

            if cancelado:
                print("Turno de '" + paciente + "' cancelado exitosamente para el Martes.")
            else:
                print("No se encontró ningún turno a nombre de '" + paciente + "' el Martes.")

        else:
            print("Día no válido. Seleccione 1 o 2.")

    # OPCIÓN 3: VER AGENDA DEL DÍA
    elif opcion == "3":
        print("\n--- VER AGENDA DEL DÍA ---")
        print("1. Lunes")
        print("2. Martes")
        dia = input("Seleccione el día (1 o 2): ").strip()

        if dia == "1":
            print("\nAgenda del Lunes:")
            print("Turno 1: " + (lunes1 if lunes1 != "" else "(libre)"))
            print("Turno 2: " + (lunes2 if lunes2 != "" else "(libre)"))
            print("Turno 3: " + (lunes3 if lunes3 != "" else "(libre)"))
            print("Turno 4: " + (lunes4 if lunes4 != "" else "(libre)"))

        elif dia == "2":
            print("\nAgenda del Martes:")
            print("Turno 1: " + (martes1 if martes1 != "" else "(libre)"))
            print("Turno 2: " + (martes2 if martes2 != "" else "(libre)"))
            print("Turno 3: " + (martes3 if martes3 != "" else "(libre)"))

        else:
            print("Día no válido. Seleccione 1 o 2.")

    # OPCIÓN 4: RESUMEN GENERAL
    elif opcion == "4":
        # Conteo de Lunes
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        # Conteo de Martes
        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print("\n--- RESUMEN GENERAL ---")
        print("Operador en turno: " + operador)
        print("LUNES  -> Ocupados: " + str(ocupados_lunes) + " | Disponibles: " + str(libres_lunes))
        print("MARTES -> Ocupados: " + str(ocupados_martes) + " | Disponibles: " + str(libres_martes))

        # Comparación
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Día con más turnos: Empate (ambos días tienen la misma cantidad de turnos ocupados).")

    # OPCIÓN 5: CERRAR SISTEMA
    elif opcion == "5":
        print("\nGracias por utilizar el sistema, " + operador + ". ¡Hasta luego!")
        ejecutando = False

    else:
        print("Opción inválida. Intente nuevamente.")