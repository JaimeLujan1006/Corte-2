#Nombre: Jaime Francisco Moreno Lujan
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones Web Python
#Ejercicio 3.4 - POO
from claseAgenteVentas import *
from claseEmpleado import *#Se importan las clases necesarias
from claseTripulante import *
from claseGerente import *

marcos=Empleados("Marcos Rios", 221, 30000) #Variable con sus atributos para la clase Empleado
julia=Gerente("Julia Campos", 109, 60000) #Variable con sus atributos para la clase Gerente


print(marcos.calcularSueldo(1000)) #Se muestra el resultado del metodo calcularSueldo implementado en la clase Empleados  dando como atributo los descuentos
print(julia.calcularSueldo(1600, 100))# Se muestra el resultado del metodo calcularSueldo implementado en la clase Gerente dando como atributos los descuentos y bonificaciones

pedro=AgenteVentas("Pedro Martinez", 32, "A120", 55000, 4)#En una variable pedro usaremos la clase AgenteVentas con sus respectivos atributos
print(pedro.nombre)#Mostramos el atributo nombre de pedro
print(pedro.calcularSueldo(100, 3000))#Mostramos el resultado del metodo calcularSueldo dando los atributos necesarios para efectuarla

lucas=Tripulante("Lucas Gutierrez", 40, "H618", 60000)#Dentro de la variable lucas utilizamos la clase Tripulante agregando los atributos necesarios
lucas.mostrarRenovacionLicencia()#Efectuamos el metodo mostrarRenovacionLicencia que nos debolvera un resultado en automatico(print desde metodo)

diego=Tripulante("Diego Enriquez", 66, "H467", 60450)#Dentro de la variable diego hacemos lo anterior con una edad que no cumpla con la condicional del metodo mostrarRenovacionLicencia para mostrar el otro resultado
diego.mostrarRenovacionLicencia()#Llamamos el motodo mostrarRenovacionLicencia que nos regresara mediante un print la opcion restante en las condicionales