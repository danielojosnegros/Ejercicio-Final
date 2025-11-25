#Clase persona, es la clae padre
class Persona:
    #construcotor de la clase, con los datos que nos pide el enunciado.
    def __init__ (self,nombre,apellido,nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
    def saludo(self):
        return f"'Bonjorno!. Mi nombre es {self.nombre} {self.apellido}"
#clase Italiano, que hereda de la clase padre de Persona.
class Italiano(Persona):
    idioma = "Italiano"
    #constructor de la clase
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido, nacionalidad ="Italiana")
    #funcion saludar, para llamarla luego cuando creemos el objeto.
    def saludar(self):
        return f'Bonjorno!. Mi nombre es {self.nombre} {self.apellido}, soy de nacionalidad {self.nacionalidad} y mi idioma es {self.idioma}'
#funcion para recibir los campos
def crear (nombre,apellido):
    return Italiano(nombre,apellido)

nombre = input("Cual es tu nombre: ")
apellido = input("Cual es tu apellido: ")

persona1 = crear(nombre, apellido)

print(persona1.saludar())
