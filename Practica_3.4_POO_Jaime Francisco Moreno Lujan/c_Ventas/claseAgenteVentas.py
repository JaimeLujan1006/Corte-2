from claseEmpleado import *#Se importa la clase Empleado ya que la hereda la clase AgenteVentas
class AgenteVentas(Empleado):#Se crea una clase hija que heredara los atributos de Empleado
    def __init__(self, nombre, edad, legajo, sueldo, mostrador):#Mediante un contructor se le pedira los atributos heredadodos y los propios, en este caso mostrador 
        self.numeroMostrador=mostrador#Instanciamos el atributo metodo que se guardara en numeroMostrador
        super().__init__(nombre, edad, legajo, sueldo)#Para poder utilizar el constructor init de la clase padre tenemos que llamarla con super junto con los atributos que necesitaremos
