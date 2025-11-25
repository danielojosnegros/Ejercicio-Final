import random
#creo primero una lista y la paso la funcion de random para crear los numero aleatorio
numerosganadores = [random.randint(0, 100) for i in range(15)]
#convierto la lista en tupbla
tuplanumganadores= tuple(numerosganadores)

premio = 15
print("--------------------------------------------------------")
print("---COMPRUEBA TUS NÚMEROS GANADORES DE LA LOTERÍA--------")
print("--------------------------------------------------------")
while True:
    #un try except, para comprobar si el es un numero entero o no
    try:
        num = input(("Introduce tu número entero positivo para comprobar tu premio del (0 al 100): "))
        num = int(num)
    except ValueError:
        print("El dato introducido no es valido, por favor vuelva a intentarlo, Gracias.")
        continue
    #compruebo, si el numero esta entre el 0 y el 100
    if num >= 0 and num <= 100:
        # Muetro la tupla ganadora:
        print(f'Esta es la lista ganadora: {tuplanumganadores}')
        # Muestro el numero mayor
        print(f'Este es el número ganador mayor: {max(tuplanumganadores)}')
        # Muestro el numero menor
        print(f'Este es el número ganador menor: {min(tuplanumganadores)}')
        ganador = 0
        #recorro la tuupla en busca de numeros iguales y los voy contando
        for i in tuplanumganadores:
            if num == i:
                aparicion = tuplanumganadores.count(num)
                ganador = ganador + 1
    # si introduce un numero mayor a 100, salta este else, y le vuelvo a pedir el numero que tiene, por eso lo de continue.
    else:
        print("Este numero esta fuera del rango de premios")
        continue
    #con este if, compruebo cuantas vegas a aparecido el numero y depende, entro en uno u en otro.
    if ganador == 1:
        print(f'¡Felicidades!. Su número {num} se encutra dentro la lista ganadora. Ha ganado {premio}€')
        break

    elif ganador >= 2:
        suplemento = ganador * 5
        premio = 10 + suplemento
        print(f'¡Felicidades! Su número: {num} se encuentra dentro de la lista ganadora y además se ha repetido {aparicion} veces . Ha ganado un total de {premio}€.')
        break
#otro blucle para la respuesta del usuario
    while True:
        respuesta = input("Lo sentimos, su numero no ha resultado premiado, ¿Desea volver a intentarlo?: ")
        respuesta = respuesta.lower()
        if respuesta in ("si","sí","s"):
            repetir = True
            break
        elif respuesta in ("no","n"):
            repetir = False
            break
        else:
            print("Lo siento no he entendido, desea volver a intentarlo: ")
    if repetir:
        continue
    else:
        print("Gracias por jugar")
        break

