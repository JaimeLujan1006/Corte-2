class Materia: #Creamos clase Materia
    def __init__(self, nombre, profesor, fecha):#Definimos el contructor con sus atributos correspondientes
        self.nombre=nombre#Instanciamos nombre y pofesor 
        self.profesor=profesor
        #no puede ser anterior a 2006
        self.fechaInicioDictado=fecha#Instanciamos la fecha y la guardamos en la variable fechaInicioDictado

    @property#Decorador para crear una propiedad con el atributo
    def fechaInicioDictado(self):#Se define el metodo fechaInicioDictado con los atributos anteriores
        #print("prueba")
        return self._fechaInicioDictado#Antes de regresar los resultados pasa por una validacion, junto con ello se crea un atributo privado 

    @fechaInicioDictado.setter#Decorador para mostrar el año
    def fechaInicioDictado(self, fecha):#Definimos el metodo agregando la fecha que se comparara despues
        if fecha<2006:#Si la fecha es menos a 2006
            self._fechaInicioDictado=2006#La fecha de inicio dictado se establecera en 20006
        else:#Si no se cumple la condicion anterior
            self._fechaInicioDictado=fecha#Se deja la fecha que por logica sera superior a 2006
