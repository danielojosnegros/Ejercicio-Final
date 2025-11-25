#He creado un dicionarioa alumno que es el general y dentro otro dicionario para meter los datos de cada alumno, siendo alumno la clave
# y el otro diccionario los valores con su asignatura y su nota
alumnos = {
    "alumno1" : {"Latin": 8, "Castellano": 8, "Frances": 9 , "Ingles" : 4},
    "alumno2" : {"Latin": 7, "Castellano": 6, "Frances": 7 , "Ingles" : 2},
    "alumno3" : {"Latin": 10, "Castellano": 7, "Frances": 8 , "Ingles" : 9},
    "alumno4" : {"Latin": 4, "Castellano": 4, "Frances": 3 , "Ingles" : 2},
    "alumno5" : {"Latin": 9, "Castellano": 8, "Frances": 9 , "Ingles" : 6}
}
#funciona para mostrar los suspensos
def suspensos(a):
    #se crea un dicionario contador, para meter los suspensos
    contador = {}
    #recorrer el dicionario.
    for alu,notas in a.items():
        for asignatura, nota in notas.items():
            #un condicional, para saber que nota en menos a 5
           if nota < 5:
               #asignamos a contador el total de suspenso
               contador [asignatura] = contador.get(asignatura, 0) + 1
    #recorrer el contrador en asignatura y el alumno.
    for asignatura, alu in contador.items():
        print(f'{asignatura} se ha suspendido por  {alu}')
#funcion para calcular la media, se reccore el primer dicionario y luego se suma los valores de las notas y se cuenta las cantidad de notas,
#se saca la media de la suma de las notas y la cantidad de notas.
def notamedia(a):
    for alu,notas in a.items():
        total = sum(notas.values())
        cantidad = len(notas)
        media = total / cantidad
        print(f'El {alu} ha tendido una nota media de {media}')

'''parecido al anterior, pero se añade un condicional para saber que alumnos han aprobado
a lo mejor seria mejor invocar a la funcion de nota media, pero me lio un poco todavia.'''
def aprobados(a):
    for alu,notas in a.items():
        total = sum(notas.values())
        cantidad = len(notas)
        media = total / cantidad
        if media >= 5:
            print(alu)

#mostramos las datos que nos pide el ejercicio, llamando a las funciones
print("----------Suspensos---------------------")
suspensos(alumnos)

print("----------Nota Media--------------------")
notamedia(alumnos)

print("----------Aprobados---------------------")
aprobados(alumnos)