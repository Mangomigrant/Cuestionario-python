ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BLANCO = "\033[97m"
NEGRITA = "\033[1m"
RESET = "\033[0m"

print(f"{ROJO}==================================={RESET}")
print(f"{ROJO}{NEGRITA} ALERTA: TU LÍNEA ESTÁ EN RIESGO.{RESET}")
print(f"{AMARILLO} PARA EVITARLO, CONTESTA ESTE CUESTIONARIO.{RESET}")
print(f"{ROJO}===================================\n{RESET}")

while True:
    nombre = input("1. Escribe tu nombre: ").strip()

    if nombre != "":
        break

    print("Error: no puedes dejar el nombre vacío.\n")


while True:
    try:
        edad = int(input("2. Escribe tu edad: "))

        if edad > 0:
            break
        else:
            print("Error: la edad debe ser mayor que 0.\n")

    except ValueError:
        print("Error: debes escribir la edad usando números enteros.\n")

while True:
    direccion = input("3. Escribe tu dirección: ").strip()

    if direccion != "":
        break

    print("Error: no puedes dejar la dirección vacía.\n")
    
while True:
    CURP = input("4. Escribe tu CURP: ").strip()

    if CURP != "" and len(CURP) == 18:
        break
    
    print("Error: el número de CURP debe tener exactamente 18 números.\n")

    print("Error: no puedes dejar el comentario vacío.\n")
    

while True:
    try:
        linea = (input("5. Escribe tu número de línea: "))

        if linea.isdigit() and len(linea) == 10:
            break
        else:
            print("Error: el número de línea tiene que tener 18 digitos.\n")

    except ValueError:
        print("Error: escribe el número de línea usando solamente números.\n")


while True:
    pagar = input("6. ¿Te gustaria pagar para desbloquear tu linea? (si/no): ").strip().lower()

    if pagar in ["si", "sí", "no"]:
        break

    print("Error: responde solamente con 'si' o 'no'.\n")

while True:
    tarjeta = input("6. Escribe tu número de tarjeta (16 dígitos): ").strip()

    if tarjeta.isdigit() and len(tarjeta) == 16:
        break

    print("Error: el número de tarjeta debe tener exactamente 16 números.\n")

    print("Error: no puedes dejar esta respuesta vacía.\n")


while True:
    INE = input("8. Escribe tu clave de lector: ").strip()

    if INE != "" and len(INE) == 18:
        break
    
    print("Error: el número de tarjeta debe tener exactamente 18 números.\n")

    print("Error: no puedes dejar el comentario vacío.\n")


print("\n===================================")
print("      CUESTIONARIO COMPLETADO")
print("===================================\n")

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Dirección: {direccion}")
print(f"CURP: {CURP}")
print(f"Número de línea: {linea}")
print(f"¿Te gustaría pagar?: {pagar}")
print(f"Número de tarjeta: {tarjeta}")
print(f"Clave de lector: {INE}")

print("\nGracias por responder el cuestionario.")