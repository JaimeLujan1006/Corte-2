#Nombre: Jaime Francisco Moreno Lujan
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones Web Python
#Ejercicio de evaluacion U2
from claseCaja import *
#construimos un objeto de la clase caja
cajita = Caja(5, 6, 1.5)

#usamos el metodo mostrar
cajita.mostrar()
#mostramos su volumen
print ("Volumen: ", cajita.calcularVolumen())
#echo $v
#mostramos su area
print ("Area Total: ", cajita.calcularAreaTotal())
#creamos clon
miClon = cajita.clon()
#mostramos info del clon
miClon.mostrar()
#creamos una caja mas grande a partir del clon con ayuda de cajita
caja25MasGrande = cajita.crearCajaGrande()
#mostramos info de la caja mas grande
caja25MasGrande.mostrar()
#verificamos si la primer caja cabe en la segunda
Res = miClon.cabe1DentroDe2(cajita, caja25MasGrande)
print ("Mas grande?:", Res)