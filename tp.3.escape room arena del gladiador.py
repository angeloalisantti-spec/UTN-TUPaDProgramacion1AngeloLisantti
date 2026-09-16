
# FUNCIONES DE VALIDACIÓN (Sintaxis estricta sin try/except)

def pedir_nombre_gladiador():
    """Pide y valida el nombre del Gladiador (solo letras y espacios)."""
    valido = False
    nombre = ""
    while not valido:
        nombre = input("Nombre del Gladiador: ").strip()
        nombre_sin_espacios = nombre.replace(" ", "")
        
        # Debe contener solo letras y no estar vacío
        if nombre_sin_espacios != "" and nombre_sin_espacios.isalpha():
            valido = True
        else:
            print("Error: Solo se permiten letras.")
    return nombre


def pedir_opcion_menu():
    """Pide y valida que la opción sea un número y esté entre 1 y 3."""
    valido = False
    opcion = 0
    while not valido:
        entrada = input("Opción: ").strip()
        if entrada.isdigit():
            opcion = int(entrada)
            if 1 <= opcion <= 3:
                valido = True
            else:
                print("Error: Ingrese un número entre 1 y 3.")
        else:
            print("Error: Ingrese un número válido.")
    return opcion



# PASO 1: CONFIGURACIÓN DEL PERSONAJE

print("--- BIENVENIDO A LA ARENA ---")
nombre_jugador = pedir_nombre_gladiador()  # String


# PASO 2: INICIALIZACIÓN DE ESTADÍSTICAS

vida_jugador = 100         # Int
vida_enemigo = 100         # Int
pociones = 3               # Int
ataque_pesado_base = 15    # Int
dano_enemigo = 12          # Int
turno_gladiador = True     # Boolean


# PASO 3: EL CICLO DE COMBATE

print("\n=== INICIO DEL COMBATE ===")

# El ciclo se repite mientras ambos combatientes tengan más de 0 de vida
while vida_jugador > 0 and vida_enemigo > 0:


    # TURNO DEL JUGADOR

    if turno_gladiador:
        print("\n" + nombre_jugador + " (HP: " + str(vida_jugador) + ") vs Enemigo (HP: " + str(vida_enemigo) + ") | Pociones: " + str(pociones))
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = pedir_opcion_menu()

        # Acción 1: Ataque Pesado
        if opcion == 1:
            dano_final = float(ataque_pesado_base)  # Float
            
            # Si la vida del enemigo es menor a 20, se realiza un Golpe Crítico (x 1.5)
            if vida_enemigo < 20:
                dano_final = ataque_pesado_base * 1.5  # Asignación Float
                print("¡GOLPE CRÍTICO!")

            vida_enemigo -= int(dano_final)
            print("¡Atacaste al enemigo por " + str(dano_final) + " puntos de daño!")

        # Acción 2: Ráfaga Veloz (Uso de for con range)
        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for golpe in range(3):
                vida_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")

        # Acción 3: Curar
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Te has curado. Recuperaste 30 HP. Pociones restantes: " + str(pociones))
            else:
                print("¡No quedan pociones!")

        # Cede el turno al enemigo
        turno_gladiador = False


    # TURNO DEL ENEMIGO (Ataca si sigue con vida)

    if vida_enemigo > 0 and not turno_gladiador:
        vida_jugador -= dano_enemigo
        print(">> ¡El enemigo contraataca por " + str(dano_enemigo) + " puntos!")
        
        if vida_jugador > 0:
            print("=== NUEVO TURNO ===")
        
        # Cede el turno al jugador para la siguiente ronda
        turno_gladiador = True


# PASO 4: FIN DEL JUEGO

print("            FIN DE LA BATALLA            ")

if vida_jugador > 0:
    print("¡VICTORIA! " + nombre_jugador + " ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")