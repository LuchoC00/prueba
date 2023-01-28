def remplazarIconos(palabra, remplazo):
    letras = "qwertyuiopasdfghjklñzxcvbnm1234567890"
    palabraNueva = ""
    for letra in palabra.lower():
        if letra in letras:
            palabraNueva+= letra
        else:
            palabraNueva+= remplazo
    return palabraNueva

class materia():
    def __init__(self, nombre, correlativas) -> None:
        self.nombre = remplazarIconos(nombre, " ")
        self.correlativas = correlativas
    
    def dameCorrelativas(self):
        Correlativas = []
        for correlativa in self.correlativas:
            Correlativas.append(correlativa.nombre)
        print(Correlativas)

    def dameNombre(self):
        print(self.nombre)
            

introduccion_a_la_matematica = logica_y_teoria_de_los_numeros = calculo_para_computacion = None

introduccion_a_la_matematica = materia("introduccion_a_la_matematica", [])
Introduccion_a_la_Programacion = materia("Introduccion a la Programacion", [])
TLED = materia("TLED", [])
PSEC = materia("PSEC", [])
Programación_1 = materia("Programación_1", [Introduccion_a_la_Programacion])
Organizacion_del_computador_1 = materia("Organizacion del computador 1", [Introduccion_a_la_Programacion])	
logica_y_teoria_de_los_numeros = materia("logica_y_teoria_de_los_numeros", [introduccion_a_la_matematica])
Algebra_Lineal = materia("Algebra Lineal", [introduccion_a_la_matematica])
Sistemas_Operativos_y_Redes_1 = materia("Sistemas Operativos y Redes 1", [Programación_1, Organizacion_del_computador_1])
calculo_para_computacion = materia("calculo_para_computacion", [logica_y_teoria_de_los_numeros])
Organizacion_del_computador_2 = materia("Organizacion del computador 2", [Organizacion_del_computador_1])
Sistemas_Operativos_y_Redes_2 = materia("Sistemas Operativos y Redes 2", [Sistemas_Operativos_y_Redes_1])
Programación_2 = materia("Programación 2", [Programación_1])	
Bases_de_Datos_1 = materia("Bases de Datos 1", [Programación_1, Organizacion_del_computador_1])
Probabilidad_y_Estadista = materia("Probabilidad y Estadista", [calculo_para_computacion])
Matemática_Discreta	= materia("Matemática Discreta", [calculo_para_computacion, logica_y_teoria_de_los_numeros])
Modelado_y_Optimizacion = materia("Modelado y Optimizacion", [Probabilidad_y_Estadista])
Programación_3 = materia("Programación 3", [Programación_2])
Teoria_de_la_Computacion = materia("Teoria de la Computacion", [Programación_3])
Base_de_Datos_2 = materia("Base de Datos 2", [Bases_de_Datos_1, Programación_3])
Especificacion_y_Verificacion_del_Software = materia("Especificacion y Verificacion del Software", [Programación_3])
Ingeniería_de_Software_1 = materia("Ingeniería de Software 1", [Programación_3])
Ingeniería_de_Software_2 = materia("Ingeniería de Software 2", [Ingeniería_de_Software_1, Especificacion_y_Verificacion_del_Software])
Proyecto_Profesional_1	= materia("Proyecto Profesional 1", [Ingeniería_de_Software_1, Especificacion_y_Verificacion_del_Software, Bases_de_Datos_1]) 
Informática_y_Sociedad = materia("Informática y Sociedad", [Ingeniería_de_Software_1])
Gestion_de_Proyectos = materia("Gestion de Proyectos", [Ingeniería_de_Software_2, Proyecto_Profesional_1])
Proyecto_Profesional_2 = materia("Proyecto Profesional 2", [Proyecto_Profesional_1])
Practica_Profecional_Supervisada = materia("Practica Profecional Supervisada", [Proyecto_Profesional_2, Base_de_Datos_2])
Taller_de_Tesina_de_Licenciatura = materia("Taller de Tesina de Licenciatura", [Proyecto_Profesional_2, Base_de_Datos_2])


calculo_para_computacion.dameCorrelativas()