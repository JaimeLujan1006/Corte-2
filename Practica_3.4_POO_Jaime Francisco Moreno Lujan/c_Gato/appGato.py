#Nombre: Jaime Francisco Moreno Lujan
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones Web Python
#Ejercicio 3.4 - POO
from claseGato import *#Importamos la clase necesaria
p = Gato ("Pelusa", 1)#En una variable p ponemos los atributos necesarios
print ("El nombre del gato es:",p.nombre)#Mostramos el atributo nombre de la variable p
print ("La edad del gato es:",p.edad)#Mostramos la atributo edad de la variable p

p.raza="Siames"#Agregamos un atributo dinamico que solo esa varible tendra
print(p.raza)#Se muestra el atributo recien agregado 
print(p)#Se muestra el espacio en memoria

p.alimentos.append("pescado")#Agregamos independientemente con append un alimento a la lista alimentos
p.alimentos=["leche", "galletas"]#Agregamos los atributos multiples de ser necesario a la variable p mediante una lista(Lo agregado independintemente se borrara) 
print(p.alimentos)#Mostramos los alimentos favoritos del atributo alimentos de la variable p

print(p.verEtapaDeVida())#Mostramos el resultado del metodo verEtapaDeVida respecto a la edad del gato asignada anteriormente, esto nos devolvera como resultado si es carchorro o adulto

g = Gato ("Cleo", 3)#En una nueva variable agregamos nuevos atributos con la clase Gato
p.alimentos=["leche","galletas","arroz"]#Agregamos nuevos alimentos favoritos de la nueva p como lo hicimos anteriormente para actualizarlos 
g.alimentos=["pan","pescado"]#Agregamos alimentos favoritos de la nueva variable g

print(p.alimentos)#Mostramos los alimentos favoritos de la variable p
print(g.alimentos)#Mostramos los alimentos favoritos de la variable g

print(p.nombre,"es de especie",p.especie)#Mostramos el atributo generico de la calse que lleva por nombre especie y que se agrega a todo objeto con la clase Gato
print(g.nombre,"es de especie",g.especie)

print("Atributo estatico de Gato:",Gato.especie)#Mostramos atributo estatico de la clase Gato