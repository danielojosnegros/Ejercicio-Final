#creo la agenda vacia, que es un dicionario.
agenda = dict()
print("-------Bienvenido mi agenda de contactos--------")
while True:
    # Pido el nombre del contacto
    nombre = input("Indique el nombre del contacto: ")

    # Compruebo si el nombre ya existe, y si exite repetimos el primer bucle while.
    if nombre in agenda:
        print("El nombre ya existe en la agenda. Por favor, introduzca otro nombre.")
        continue

    # Pido el primer telefono
    while True:
        try:
            telefono1 = int(input("Introduzca el primer número de teléfono: "))
            # si el telefono es valido, salimos del bulce
            break
        except ValueError:
            print("Número no válido. Por favor, introduzca un número correcto.")

    # Pido el segundo telefono
    while True:
        telefono2 = input("Introduzca el segundo número de teléfono (opcional, deje en blanco si no tiene): ")
        # Si  el telefono2 lo deja en blanco, añadimos a la agenda el nombre y el primer telefono y salimos
        if telefono2 == "":
            agenda[nombre] = [telefono1]
            break
        try:
            #si nos introduce un telefono, comprobamos con el try si es entero y si es entero lo añadimos a la agenda con el primer telefono y salimos
            telefono2 = int(telefono2)
            agenda[nombre] = [telefono1, telefono2]
            break
        except ValueError:
            print("Número no válido. Intente de nuevo o deje en blanco si no tiene segundo teléfono.")

    # Pregunto si el usuario desea continuar o salir, para mostrar los datos de la agenda.
    while True:
        continuar = input("¿Desea añadir otro contacto? (sí/no): ").lower()
        # si nos dice que desa continuar, salimos del buble de pregunta, y volvemos al primer while.
        if continuar in ["sí", "si"]:
            break
        # si nos dice que no, pues mostramos la agenda y ya con el exit terminamos el programa.
        elif continuar == "no":
            print("\nAgenda final:")
            for nombre_contacto, telefonos in agenda.items():
                print(f"{nombre_contacto}: {telefonos}")
            exit()
        # si no escribe algo bien, le mostramos este mensaje, y vuelve al bucle.
        else:
            print("Respuesta no válida. Por favor, responda 'sí' o 'no'.")
