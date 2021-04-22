#Nombre: Jaime Francisco Moreno Lujan
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones Web Python
#Ejercicio de evaluacion U2
class Caja:
    #Constructor
    def __init__(self,ancho, largo, alto):
     self.ancho = ancho
     self.largo = largo
     self.alto = alto
     
    #metodo para mostrar contenido de la caja
    def mostrar(self):
        return print("Alto:",self.alto, "Ancho:",self.ancho, "Largo:",self.largo)
 
    #metodo para calcular volumen de la caja
    def calcularVolumen(self):
        r = self.ancho * self.alto * self.largo
        return r
    
    #metodo para calcular el area frontal
    def areaFrontal(self):
        return self.ancho * self.alto
    
    #metodo para calcular area lateral
    def areaLateral(self):
        return self.largo * self.alto
    
    #metodo para calcular area superior
    def areaSuperior(self):
        return self.largo * self.ancho
    
    #metodo para calcular area total
    def calcularAreaTotal(self):
        r = 2 * self.areaFrontal() + 2 * self.areaLateral() + 2 * self.areaSuperior()
        return r
    
    # metodo que regresa un clon de sí misma
    def clon(self):
        c = Caja(self.ancho, self.largo, self.alto)
        return c
    
    #metodo que regresa una caja 25% más grande
    def crearCajaGrande(self):
        nuevoAlto = self.alto * 1.25
        nuevoAncho = self.ancho * 1.25
        nuevoLargo = self.largo * 1.25
        
        cajaNueva = Caja(nuevoAncho, nuevoLargo, nuevoAlto)
        return cajaNueva
    
    #metodo para comparar cajas
    def cabe1DentroDe2(self, c, cajaNueva):
        #se comparan todas las dimensiones
        if c.ancho < cajaNueva.ancho and c.alto < cajaNueva.alto and c.largo < cajaNueva.largo:
            return "Sí Cabe"
    
        else:
            return "No cabe"
        
