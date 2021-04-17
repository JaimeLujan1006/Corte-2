class Carrera:#Se crea la clase Carrera
    def __init__(self, nombre):#Definimos el constructor con sus atributos
        self.nombre=nombre#Instanciamos el atributo nombre 
        #self.materias=[]
        self.materias={}#Instanciamos y agregamos el atributo materias mediante una coleccion
        #self.__materias={} "Eso lo usamos para no poder hacer copias"

    def agregarMateria(self, materia, codigo):#Definimos un metodo agregar materias con los atributos materia y codigo
        self.materias[codigo]=materia#Se toma el codigo de la materia y lo agragamos al diccionario de materias
        #self.__materias[codigo]=materia "Seguridad para copias"



