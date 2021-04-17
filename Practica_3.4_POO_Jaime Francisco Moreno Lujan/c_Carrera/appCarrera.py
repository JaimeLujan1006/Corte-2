#Nombre: Jaime Francisco Moreno Lujan
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones Web Python
#Ejercicio 3.4 - POO
from claseCarrera import * #Importamos la claseCarrera que necesitaremos
from claseMateria import * #Importamos la claseMateria que necesitaremos 

ing=Carrera("Ingenieria")#Se agrega un carrera en ing
algebra=Materia("Algebra","Ricardo Quinteros", 2010)#Establecemos atributos en la clase Materia con la variable algebra
fisica=Materia("Fisica","Margarita Gomez", 2006)#Establecemos atributos en la clase Materia con la variable fisica
quimica=Materia("Quimica","Lorena Rios", 2003)#Establecemos atributos en la clase Materia con la variable quimica

ing.agregarMateria(algebra,134)#Agregamos mediante el metodo agregarMateria a la variable ing 
#print(ing.materias) Se pierde sentido con la modificacion del codigo

print(algebra.fechaInicioDictado)#Mostramos el resultado del metodo fechaInicioDictado que depende del año de cada materia
print(fisica.fechaInicioDictado)#Mostramos el resultado del metodo fechaInicioDictado que depende del año de cada materia
print(quimica.fechaInicioDictado)#Mostramos el resultado del metodo fechaInicioDictado que depende del año de cada materia

print(ing.materias)#Muestra espacio en memoria 
print(len(ing.materias))#Muestra la cantidad de materias en ing

copia=ing.materias #Se hace una copia de las materias
print(copia)#Se muestra el espacio en memoria que sera la misma o la ya existente de la materia copiada
