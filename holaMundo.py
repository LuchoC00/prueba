archivo = open("libro.txt","r",1,"UTF-8")
print(archivo)
dicc = {}
for linea in archivo:
    materia, correlativas = linea.split(";")
    materia = materia.capitalize()
    correlativas = correlativas[:-1].split(",")
    listaNueva =[]
    for correlativa in correlativas:
        correlativa = correlativa.capitalize()
        listaNueva.append(correlativa)
    print(materia,listaNueva)
archivo.close()