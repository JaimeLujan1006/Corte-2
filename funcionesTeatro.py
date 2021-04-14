def obtenerSumaDescuentos(suma_descuentos):#defiimos una funcion que utilizara como parametro la suma_descuentos de nustro programa 
    suma = 0 #Se inicializa una variable suma en 0
    for v in suma_descuentos:#Utilizamos un ciclo for para los acumulados 
        suma += v#Se le suma a la varible suma los resultados obtenidos 
    return suma#Regresa el valor total de la suma 

def obtenerSumaEntradas(suma_entradas):
    suma = 0
    for v in suma_entradas.values():#El método values() devuelve un objeto de vista que muestra una lista de todos los valores en el diccionario
        suma += v
    return suma