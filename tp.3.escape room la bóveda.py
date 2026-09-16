
# VALIDACIONES DE ENTRADA

def pedir_nombre_agente():
    """Pide y valida el nombre del agente (solo letras y espacios)."""
    valido = False
    nombre = ""
    while not valido:
        nombre = input("Ingrese su nombre de agente: ").strip()
        # Verificamos que al quitar espacios solo queden letras y no esté vacío
        if nombre.replace(" ", "") != "" and nombre.replace(" ", "").isalpha():
            valido = True
        else:
            print("Error: El nombre debe contener únicamente letras.")
    return nombre


def pedir_numero_validado(mensaje, minimo, maximo):
    """Pide un número y valida que sea entero dentro del rango [minimo, maximo]."""
    valido = False
    numero = 0
    while not valido:
        entrada = input(mensaje).strip()
        if entrada.isdigit():
            numero = int(entrada)
            if minimo <= numero <= maximo:
                valido = True
            else:
                print("Error: Seleccione una opción entre " + str(minimo) + " y " + str(maximo) + ".")
        else:
            print("Error: Ingrese un número válido sin letras ni símbolos.")
    return numero



# VARIABLES INICIALES

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Control de racha anti-spam
forzar_seguidas = 0


# INICIO DEL JUEGO

print("=========================================")
print("       ESCAPE ROOM: LA BÓVEDA           ")
print("=========================================")
agente = pedir_nombre_agente()
print("\n¡Bienvenido/a, Agente " + agente + "!")
print("Misión: Abrir las 3 cerraduras de la bóveda antes de quedarte sin tiempo o energía.")

bloqueado_por_alarma = False

# El juego continúa mientras tenga recursos, no haya ganado y no esté bloqueado
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado_por_alarma:
    
    # Evaluar la regla de bloqueo por alarma antes del turno
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado_por_alarma = True
        break

    # Mostrar estado actual
    print("\n-----------------------------------------")
    print("ESTADO DEL AGENTE: " + agente)
    print("• Energía: " + str(energia) + " / 100")
    print("• Tiempo restante: " + str(tiempo))
    print("• Cerraduras abiertas: " + str(cerraduras_abiertas) + " / 3")
    print("• Estado de Alarma: " + ("ACTIVADA 🚨" if alarma else "Inactiva 🟢"))
    print("• Código Parcial Hackeado: '" + codigo_parcial + "' (Longitud: " + str(len(codigo_parcial)) + ")")
    print("-----------------------------------------")

    print("MENÚ DE ACCIONES:")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = pedir_numero_validado("Seleccione una acción (1-3): ", 1, 3)

    
    # OPCIÓN 1: FORZAR CERRADURA
    
    if opcion == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2
        
        print("\n--> Intentando forzar la cerradura...")

        # Regla Anti-spam: 3ra vez seguida
        if forzar_seguidas == 3:
            alarma = True
            print("¡REGLA ANTI-SPAM! Forzaste la cerradura 3 veces seguidas y el mecanismo se trabó.")
            print("¡La alarma del sistema se ha ACTIVADO!")
        else:
            # Riesgo de alarma si la energía está por debajo de 40
            # Se evalúa la energía actual luego de aplicar el costo
            if energia < 40:
                print("ADVERTENCIA: Tenés la energía muy baja (menos de 40). Hay riesgo de activar la alarma.")
                eleccion_riesgo = pedir_numero_validado("Elegí un número de seguridad (1-3): ", 1, 3)
                if eleccion_riesgo == 3:
                    alarma = True
                    print(" ¡Cometiste un error al forzar a ciegas y disparaste la ALARMA!")

            # Si no saltó la alarma en este turno, se abre 1 cerradura
            if not alarma or (alarma and forzar_seguidas < 3 and eleccion_riesgo != 3 if 'eleccion_riesgo' in locals() else True):
                if not alarma:
                    cerraduras_abiertas += 1
                    print(" ¡Éxito! Lograste abrir 1 cerradura de la bóveda.")

    
    # OPCIÓN 2: HACKEAR PANEL
    
    elif opcion == 2:
        forzar_seguidas = 0  # Corta la racha anti-spam
        energia -= 10
        tiempo -= 3

        print("\n--> Iniciando secuencia de hackeo de panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print("  [Paso " + str(paso) + "/4] Procesando algoritmo... Código actual: " + codigo_parcial)

        # Si el código llega a 8 o más letras, abre una cerradura si aún faltan
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("🔓 ¡CÓDIGO COMPLETO RECONOCIDO! El panel liberó automáticamente 1 cerradura.")

    
    # OPCIÓN 3: DESCANSAR
    
    elif opcion == 3:
        forzar_seguidas = 0  # Corta la racha anti-spam
        tiempo -= 1

        # Recuperación básica de energía
        energia += 15
        if energia > 100:
            energia = 100
        
        # Penalización si la alarma está encendida
        if alarma:
            energia -= 10
            print("\n--> Descansaste, pero la ALARMA encendida no te deja descansar bien (-10 energía extra).")
        else:
            print("\n--> Descansaste y recuperaste energía.")


# CONDICIONES DE FIN DE JUEGO

print("FIN DE LA MISIÓN")

if cerraduras_abiertas >= 3:
    print("¡VICTORIA!")
    print("El Agente " + agente + " logró abrir las 3 cerraduras y vulnerar la bóveda a tiempo.")
elif bloqueado_por_alarma:
    print(" DERROTA POR BLOQUEO DE SEGURIDAD ")
    print("La alarma estaba encendida y el tiempo cayó a 3 o menos. El sistema bloqueó la bóveda por completo.")
elif energia <= 0 or tiempo <= 0:
    print(" DERROTA ")
    if energia <= 0:
        print("El Agente " + agente + " se quedó sin energía y colapsó.")
    if tiempo <= 0:
        print("Se agotó el tiempo límite para cumplir la misión.")