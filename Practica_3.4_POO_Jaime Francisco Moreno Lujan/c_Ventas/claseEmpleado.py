class Empleado:#Se crea la clase Empleado
    def __init__(self, nombre, edad, legajo, sueldo):#Se define el constrictor con los atributos requeridos
        self.nombre=nombre
        self.edad=edad#instancias mediante self para cada uno de los atributos
        self.legajo=legajo
        self.sueldoBase=sueldo
    
    def calcularSueldo(self, descuentos, bonos):#Se crea el metodo calcular Sueldo que tendra los parametros descuentos y bonos
        return self.sueldoBase-descuentos+bonos #Mediante aritmetica y tomando el atributo sueldo se hacen las operaciones correspondientes y regresa el resultado  

