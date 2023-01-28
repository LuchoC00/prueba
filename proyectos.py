

def remplazarIconos(palabra, remplazo = ""):
    letras = "qwertyuiopasdfghjklñzxcvbnm1234567890|"
    palabraNueva = ""
    for letra in palabra.lower():
        if letra in letras:
            palabraNueva+= letra
        else:
            palabraNueva+= remplazo
    return palabraNueva

def añadirCorrelativas(correlativas = []):
    cantidad = int(input("ingrese la cantidad de correlativas que tiene, Si no posee correlativas ingrese 0"))
    while cantidad > 0:
        correlativa = input("Ingrese el nombre de la correlativa").capitalize()
        correlativas.append(correlativa)
        cantidad -=1
    return correlativas
    
class materias():
    def __init__(self, nombre, correlativas) -> None:
        self.nombre = nombre
        self.correlativas = correlativas
    
    def comprimirClase(self):
        return self.nombre + ";" + ",".join(self.correlativas)        
        
    def dameNombre(self):
        return self.nombre
    
    def claseMateria(self, materia, diccionario):
        if materia in diccionario:
            return diccionario[materia]

    def todasLasCorrelativas(self, diccionario):
        todasCorrelativas = []
        salir = False
        while not salir:
            salir = True
            for especialidad in diccionario:
                if especialidad.nombre in self.correlativas:
                    if especialidad.nombre not in todasCorrelativas:
                        todasCorrelativas.append(especialidad.nombre)
                        salir = True
        return todasCorrelativas

    def agregarCorrelativa(self, diccionario):
        correlativa = input("Introduzca la correlativa a agregar")
        if correlativa in diccionario:
            self.correlativas.append(correlativa)
            print(f"Se ha añadido {correlativa} a la lista de correlativas")
        else:
            print(f"la materia {correlativa} NO existe en el diccionario")

    def quitarCorrelativa(self):
        correlativas = "\n".join(self.correlativas)
        quitar = input(f"ingrese la correlativa a quitar, las opciones son las siguientes:\n{correlativas}")
        if quitar in correlativas:
            self.correlativas.pop(self.correlativas.index(quitar))
            print(f"Se ha quitado la correlativa {quitar} de la lista de correlativas de {self.nombre}")
    

#--Desempaqueta y Añade las clases--#
archivo = open("clases.txt","r")
clases = {}
cont = 0
for linea in archivo:
    nombreMateria, correlativas = linea.split(";")
    correlativas = correlativas[:-1].split(",")

    clases[nombreMateria] = materias(nombreMateria,correlativas)
    cont+=1
archivo.close()    

#backup
backup = open("clases.txt","w")
for clase in clases.values():
    backup.write(clase.comprimirClase()+"\n")
backup.close()

archivo = open("clases.txt","w")
nombreMateria = None
while nombreMateria != "Salir":
    #--Area de trabajo--#

    #--Añade nuevas clases--#
    nombreMateria = input("Ingrese el nombre de la materia\nSi quiere salir, Ingrese 'salir'").capitalize()
    if nombreMateria != "Salir": 
        correlativas = añadirCorrelativas()
        clases[nombreMateria] = materias(nombreMateria, correlativas)

    #--Guarda las clases ya creadas--#
    else:
        for clase in list(clases.values()):
            print(clase.comprimirClase())
            archivo.write(clase.comprimirClase()+"\n")
archivo.close()