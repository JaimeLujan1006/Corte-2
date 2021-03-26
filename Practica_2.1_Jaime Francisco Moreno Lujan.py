#Nombre: Jaime Francisco Moreno Lujan
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones Web Python
#Ejercicio 2.1 - Votos
import random  #Empezamos importando la libreria necesaria ya que sabemos lo que tenemos que hacer, en este caso tomar un valor aleatorio de una lista
#Ejercicio 1
A = "Amarillo" #Primera variable necesaria que tendra como identificacion "Amarillo"
B = "Morado" #Segunda variable necesaria que tendra como identificacion "Morado"
C = "Rojo" #Tercera variable necesaria que tendra como identificacion "Rojo"
voto = str(input("Partido a votar[A, B o C]:")) #La variable voto nos almacenara la votacion hecha por el usuario desde la consola 
if voto.lower() == "a": #Condicional en caso de que el voto sea a o A(.lower() nos ayuda a convertir las mayusculas en minisculas y asi se cumpla la condicional)
    print("Usted ha votado por el partido:",A) #Se muestra la leyenda en caso de que se cumpla la condicional anterior 
elif voto.lower() == "b": #Condicional en caso de que el voto sea b o B
    print ("Usted ha votado por el partido:",B) #Se muestra la leyenda en caso de que se cumpla la condicional anterior 
elif voto.lower() == "c": #Condicional en caso de que el voto sea c o C
    print ("Usted ha votado por el partido:",C) #Se muestra la leyenda en caso de que se cumpla la condicional anterior 
else : #Condicional en caso de que no se cumpla ninguna de las anteriores
    print ("Opción errónea") # Muestra la leyeda de error
print()#Espacio en consola
print()#Espacio en consola
#Ejercicio 2
D = 0 #Variable iiciada en 0 que corresponde al partido Amarillo
E = 0 #Variable iiciada en 0 que corresponde al partido Morado
F = 0 #Variable iiciada en 0 que corresponde al partido Rojo
print("Espere un momento por favor, se estan contabilizando los votos...") #Mensaje de espera ya que se esta ejecutando un ciclo de dos millones de veces y se estan contabilizando los votos
for i in range(0,2000000): #Ciclo for que se repetira dos millones de veces simulando una votacion 
    partidos = ['Amarillo', 'Morado', 'Rojo'] #Creamos una lista con los partidos participantes 
    voto = (random.choice(partidos)) #Dentro de la variable voto almacenaremos la eleccion aleatoria hecha con random.choice() que tiene por parametro la lista de partidos creada anteriormente 
    if voto == 'Amarillo': #Condicional en caso de que la eleccion anterior sea Amarillo 
        D += 1 #Se le sumara un voto en la variable correspondiente, en este caso D, si se comple la condicional anterior 
    elif voto == 'Morado': #Condicional en caso de que la eleccion anterior sea Morado
        E += 1 #Se le sumara un voto en la variable correspondiente, en este caso E, si se cumple la condicional anterior 
    elif voto == 'Rojo': #Condicional en caso de que la eleccion anterior sea Rojo
        F += 1 #Se le sumara un voto en la variable correspondiente, en este caso F, si se cumple la condicional anterior 
print ("Votos por el partido Amarillo:",D) #Muestra el mensaje seguido de los votos acumulados en la variable correspondiente luego del ciclo de dos millones de veces 
print ("Votos por el partido Morado:",E) #Muestra el mensaje seguido de los votos acumulados en la variable correspondiente luego del ciclo de dos millones de veces
print ("Votos por el partido Rojo:",F) #Muestra el mensaje seguido de los votos acumulados en la variable correspondiente luego del ciclo de dos millones de veces
print() #Espacio en consola
if D > E and F: #Condicional si la cantidad de votos para D(Amarillo) es mayor que E(Morado) y F(Rojo)
    print("El partido ganador es:",A) #Muestra leyenda ganadora del partido correspondinte en caso de que se sumpla la condicion anterior 
elif E > D and F: #Condicional si la cantidad de votos para E(Morado) es mayor que D(Amarillo) y F(Rojo)
    print("El partido ganador es:",B) #Muestra leyenda ganadora del partido correspondinte en caso de que se sumpla la condicion anterior
elif F > D and E: #Condicional si la cantidad de votos para F(Rojo) es mayor que D(Amarillo) y E(Morado)
    print("El partido ganador es:",C) #Muestra leyenda ganadora del partido correspondinte en caso de que se sumpla la condicion anterior
#Fin     

