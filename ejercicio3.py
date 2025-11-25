#importo la clase random para generar numeros aleatorios.
import random
print("----- Juegos de dados---------------------")
input("Presione intro para lanzar el jugador 1: ")
dado1j1 = random.randint(1,6)
dado2j1 = random.randint(1,6)
print(f'Primer dado del jugador 1 : {dado1j1}')
print(f'Segundo dado del jugador 1 : {dado2j1}')
input("Presione intro para lanzar el jugador 2: ")
dado1j2 = random.randint(1,6)
dado2j2 = random.randint(1,6)
print(f'Primer dado del jugador 1 : {dado2j1}')
print(f'Segundo dado del jugador 1 : {dado2j2}')

#se comprueban los datos
if dado1j1 == dado1j1 or dado1j1 == dado2j1 or dado1j1 == dado1j2 or dado1j1 == dado2j2:
    print("gana jugador 1")
else:
    print("gana jugador 2")


