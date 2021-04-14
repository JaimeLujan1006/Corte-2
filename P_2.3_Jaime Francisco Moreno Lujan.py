#Nombre: Jaime Francisco Moreno Lujan
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones Web Python
#Ejercicio 2.3 - Funciones
from random import randint#Se importa la libreria para poder hacer elecciones aleatorias como lo pide el ejercicio
from funcionesTeatro import * #Se importan todas las clases o funcines de la libreria o archivo que creamos con los metodos que nos ayudaran 

PRECIO_ORIGINAL = 100 #Dentro de una variable establecemos el valor original 
CAPACIDAD = 10000 #La capacidad total del auditorio 
monto_teorico = CAPACIDAD * PRECIO_ORIGINAL #En una variable hacemos el calculo de un total sin descuentos utilizando los datos anteriores 
suma_real_desc = 0 #Inicializamos una variable en 0 para la suma del descuento 
suma_percibida = 0 #Inicializamos una variable en 0 para la suma percibida 

pPCategoria = {"PRIMERA":0,"SEGUNDA":0,"TERCERA":0,"CUARTA":0,"QUINTA":0}#Dentro de un diccionario agregamos las categorias corresponientes con su inicializacion en 0  
descuentos ={
    "1":(PRECIO_ORIGINAL*0.30),
    "2":(PRECIO_ORIGINAL*0.10),#Se realizan las operaciones correspondientes por cada categoria dentro de otro diccionario
    "3":(PRECIO_ORIGINAL*0.15),
    "4":(PRECIO_ORIGINAL*0.25),
    "5":(PRECIO_ORIGINAL*0.35)
    }
suma_descuentos = [0, 0, 0, 0, 0]#Creamos una lista para la suma de los descuentos que utilizaremos despues
suma_entradas = {"1":0, "2":0, "3":0, "4":0, "5":0}#Hacemo uso de un diccionario mas para la suma de entradas y que nuestro codigo no sea tan extenso 

for i in range(10000):#Comenzamos con el ciclo de 10000 veces 
    edad = randint(5,120)#Eleccion aleatoria para las categorias asignadas que van desde los 5 a los 120 años de edad
    if edad >= 5 and edad <= 14:#Condicional en caso de que la eleccion aleatoria sea entre 5 y 14 años de edad
        pPCategoria["PRIMERA"] +=1#Se le suma 1 a la PRIMERA categoria
        suma_descuentos[0] += descuentos["1"]#Utilizando los diccinarios y listas cradas anteriormente, se ira agregando el valor o cantidad a la suma correspondiente 
        suma_entradas["1"] += PRECIO_ORIGINAL - descuentos["1"] 
    elif edad >= 15 and edad <= 19:#Condicional en caso de que la eleccion aleatoria sea entre 15 y 19 años de edad
        pPCategoria["SEGUNDA"] +=1#Se le suma 1 a la SEGUNDA categoria
        suma_descuentos[1] += descuentos["2"]
        suma_entradas["2"] += PRECIO_ORIGINAL - descuentos["2"]#Calculo para la grafica que construiremos posteriormente
    elif edad >= 20 and edad <= 45:#Condicional en caso de que la eleccion aleatoria sea entre 20 y 45 años de edad
        pPCategoria["TERCERA"] +=1#Se le suma 1 a la TERCERA categoria
        suma_descuentos[2] += descuentos["3"]#Utilizando los diccinarios y listas cradas anteriormente, se ira agregando el valor o cantidad a la suma correspondiente 
        suma_entradas["3"] += PRECIO_ORIGINAL - descuentos["3"]#Calculo para la grafica que construiremos posteriormente
    elif edad >= 46 and edad <= 65:#Condicional en caso de que la eleccion aleatoria sea entre 46 y 65 años de edad
        pPCategoria["CUARTA"] +=1#Se le suma 1 a la CUARTA categoria
        suma_descuentos[3] += descuentos["4"]#Utilizando los diccinarios y listas cradas anteriormente, se ira agregando el valor o cantidad a la suma correspondiente 
        suma_entradas["4"] += PRECIO_ORIGINAL - descuentos["4"]#Calculo para la grafica que construiremos posteriormente
    else:#Si no se cumple ninguna de las condiciones anteriores se entendera que es mayor a 65 años de edad 
        pPCategoria["QUINTA"] +=1#Se le suma 1 a la QUINTA categoria
        suma_descuentos[4] += descuentos["5"]#Utilizando los diccinarios y listas cradas anteriormente, se ira agregando el valor o cantidad a la suma correspondiente 
        suma_entradas["5"] += PRECIO_ORIGINAL - descuentos["5"]#Calculo para la grafica que construiremos posteriormente
        
suma_percibida = obtenerSumaEntradas(suma_entradas)#Hacemos uso de las funciones que importamos al principio y que ya han sido programadas para realizar las operaciones que necesitamos
print(f"La suma total percibida es $ {suma_percibida:7.2f}")#Se muestra la leyenda de la suma total percibida junto con el valor correspondiente, a eso mismo se le agrega un espacion aproximado para que las cifras esten aliniadas y no se pierda el sentido de lo que se muestra 

suma_real_desc = obtenerSumaDescuentos(suma_descuentos)#Hacemos uso de las funciones que importamos al principio y que ya han sido programadas para realizar las operaciones que necesitamos
print(f"Se dejo de percibir $ {suma_real_desc:0.2f}")#Se muestra la leyenda de se dejo de percibir junto con el valor correspondiente, a eso mismo se le agrega un espacion aproximado para que las cifras esten aliniadas y no se pierda el sentido de lo que se muestra 

porcentaje1 = (suma_real_desc/monto_teorico) * 100 #Creamos una variable donde se guardara el porcentaje una vez teniendo la suma real del descuento 
print(f"Lo que equivale a {porcentaje1:0.2f}% ")#Se muestra el porcentaje obtenido anteriormente con su leyenda 

print(f"Se puedo haber obtenido {monto_teorico:0.2f}")#Se muestra el total que se pudo haber obteniddo utilizando la variable donde se habia guardado la cantidad

por1 = (pPCategoria['PRIMERA'] / CAPACIDAD) *100#Porcentaje para la primera categoria una vez teniendo el total de personas entre la capacidad total por el 100 por ciento
por2 = (pPCategoria['SEGUNDA'] / CAPACIDAD) *100#Porcentaje para la segunda categoria una vez teniendo el total de personas entre la capacidad total por el 100 por ciento
por3 = (pPCategoria['TERCERA'] / CAPACIDAD) *100#Porcentaje para la tercera categoria una vez teniendo el total de personas entre la capacidad total por el 100 por ciento
por4 = (pPCategoria['CUARTA'] / CAPACIDAD) *100#Porcentaje para la cuarta categoria una vez teniendo el total de personas entre la capacidad total por el 100 por ciento
por5 = (pPCategoria['QUINTA'] / CAPACIDAD) *100#Porcentaje para la quinta categoria una vez teniendo el total de personas entre la capacidad total por el 100 por ciento

bar1 = int(por1)
bar2 = int(por2)#Todos las valores anteriores los convertimos a un valor entero para poder mostralo en la grafica 
bar3 = int(por3)
bar4 = int(por4)
bar5 = int(por5)

print("Entraron por rango de edad")#Se muestran resultados finales en barrra
print(f"  5-14: {pPCategoria['PRIMERA']:7.2f} : {por1:5.2f}% :{('=' * bar1)}")
print(f" 15-19: {pPCategoria['SEGUNDA']:7.2f} : {por2:5.2f}% :{('=' * bar2)}")#Con ayuda de un singo =, multimplicaremos la cantidad entera del porcentage por categoria para simular una grafica de barras. Cada barra estara alineada, por lo que se utiliza un espacio aproximado para que no pierda su forma 
print(f" 20-45: {pPCategoria['TERCERA']:7.2f} : {por3:5.2f}% :{('=' * bar3)}")
print(f" 46-65: {pPCategoria['CUARTA']:7.2f} : {por4:5.2f}% :{('=' * bar4)}")
print(f"  65->: {pPCategoria['QUINTA']:7.2f} : {por5:5.2f}% :{('=' * bar5)}")