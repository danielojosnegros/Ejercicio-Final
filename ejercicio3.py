#importo la clase random para generar numeros aleatorios.
import random
print("----- Juegos de dados---------------------")
partidasj1 = 0
partidasj2 = 0
while partidasj1 < 3 and partidasj2 < 3:
    input("Presione intro para lanzar el jugador 1: ")
    dado1j1 = random.randint(1,6)
    dado2j1 = random.randint(1,6)
    print(f'Primer dado del jugador 1 : {dado1j1}')
    print(f'Segundo dado del jugador 1 : {dado2j1}')
    input("Presione intro para lanzar el jugador 2: ")
    dado1j2 = random.randint(1,6)
    dado2j2 = random.randint(1,6)
    print(f'Primer dado del jugador 1 : {dado1j2}')
    print(f'Segundo dado del jugador 1 : {dado2j2}')

    #voy a guardar todos los dados en una coleccion
    resultado = {dado1j1,dado2j1,dado1j2,dado2j2}
    print (resultado)

#se comprueban los datos
    if  len(resultado) < 4:
        partidasj1 += 1
        print("gana jugador 1")
        if partidasj1 == 3:
            print("Enorabuena el Jugador 1 ha ganado")
            try:
                repetir = input("¿Desea volver a jugar otra partida¿: ").lower()
                if repetir in ("si","sí"):
                    partidasj1 = 0
                    partidasj2 = 0
                if repetir == "no":
                    break
            except ValueError:
                print("No se ha entendido bien ")
        #print(partidasj1)
    else:
        partidasj2 += 1
        print("gana jugador 2")
        if partidasj2 == 3:
            print("Enorabuena el Jugador 2 ha ganado")
            try:
                repetir = input("¿Desea volver a jugar otra partida¿: ").lower()
            except ValueError:
                print("No se ha entendido bien ")

                if repetir in ("si","sí"):
                    partidasj1 = 0
                    partidasj2 = 0
                if repetir == "no":
                    break
            except ValueError:
                print("No se ha entendido bien ")
       # print(partidasj2)
