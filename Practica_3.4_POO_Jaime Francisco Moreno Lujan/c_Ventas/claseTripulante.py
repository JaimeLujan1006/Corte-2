from claseEmpleado import * #Se importa la clase Empleado ya que la clase Tripulante la hereda 
class Tripulante(Empleado):#Se crea una clase hija mas que hereda los atributos de la clase Padre(Empleado)
    def mostrarRenovacionLicencia(self):#Definimos un metodo para la renovacion de licencia instanciando self predeterminado para utilizar los paramentros requeridos, no se piden mas atributos
        if self.edad<50: #Condicional si l edad es menor de 50 años
            print("Renueva su licencia cada 1 año") #Si se cumple la condicion anterior, muestra la leyenda correspondiente 
        else:#Si no se cumle la condicion anterior
            print("Renueva su licencia cada 6 meses")#Se muestra la leyenda asignada
