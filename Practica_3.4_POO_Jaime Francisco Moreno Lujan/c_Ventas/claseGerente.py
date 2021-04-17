class Empleados:#Creamos la clase Empleado
    def __init__(self, nombre, legajo, sueldo):#Definimos el contrictor correspondiente con los atributos necesarios
        self.nombre=nombre
        self.legajo=legajo#instanciamos los atributos 
        self.sueldoBruto=sueldo
    
    def calcularSueldo(self, descuentos):#Definimos el metodo con el atributo descuentos
        return self.sueldoBruto-descuentos#Regresa el resultado de la operacion par calcular el sueldo

class Gerente(Empleados):#Creamos la clase hija que heredara los atributos de Empleado
    def calcularSueldo(self, descuentos, bonificaciones):#definimos el metodo sueldo con los atributos descuentos y bonificaciones
        return self.sueldoBruto-descuentos+bonificaciones#Regresa el resultado de sueldo brtuto con las operaciones necesarias 

