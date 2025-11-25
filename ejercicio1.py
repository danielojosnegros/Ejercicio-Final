#compruebo con esta funcion, si el numero es primo o no, y lo paso por parametro.
# Las funiones se  colocan al principio del codido
def numprimo(num):
    #si el numero es menor o igual a 1, devuelvo falso, por que no es primo,  pongo un mensaje
    if num <= 1:
        return print("El numero introducido es", num, " y NO es primo")
    # Hago un bucle, y divido el numero entre los numero encontrado, y si la divivision es 0, devuelvo true
    for i in range(2, num):
        if num % i == 0:
            return print(f'El numero introducido es {num}, y NO es primo')
    # si ninguna de las cosas se cumple, eso es que el numero es primo, y devuelvo verdadero.
    return print(f'El numero introducido es {num}, y SI es primo')


#creo un blucle while, para  que se repita simpre, hasta que se introduzca el numero bien.
while True:
    num = input("Introduce un número entero y positivo:")
    #compruebo con if si el el dato tiene una coma o un punto, para decir que no es entero
    if "." in num or "," in num:
        print("No ha introducido un número entero. Por favor, vuelva a intentarlo.")
        continue
    #con el try except, compruebo, que es un numero, que no sea otro valor, y si eso salta la excepcion de value error
    try:
        #convierto el numero a un entero.
        num = int(num)
    except ValueError:
        print("El dato introducido no es número. Por favor, vuelva a intentarlo")
        continue
    #vuelto a comprobar si el numero es menor a 0
    if num <= 0:
        print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo")
    #si el numero es entero y positivo, lo paso a la funcion de numprimo, para comprobar y mostrarlo por pantalla
    elif num > 0:
        numprimo(num)
        break
        



