fecha=input("Fecha (formato 'dia, DD/MM'):")#Empezando el programa, establecemos una variable fecha para pedir con un input que se ingrese por usuario, la fecha en el fomrato establecido 
fecha=fecha.lower()#El ejercicio no pide que se respete la entrada en mayusculas y minusculas, por lo tanto hacemos uso de lower para que en caso de que el usuario ingrese mayusculas,estas se convertiran a minusculas y las seguira respetando por igual 
diasemana=fecha[0:fecha.find(',')]#Tenemos que tomar el dia en letra de la fecha ingresada por usuario e ingresarla a la variable diasemana para guardarla, se usa la herramienta .find para tomar de una cadena de caracteres, el espacio que necesitaremos para el ejercicio   
dianro=int(fecha[fecha.find(' ')+1:fecha.find('/')])#Al igual que el dia en letra, lo hacemos con el dia en numero utilizado la misma herramienta con los espacios correspondientes o caracteres marcados en el formato de fecha 
mesnro=int(fecha[fecha.find('/')+1:])#Para el mes repetimos lo anterior, respetando caracteres de la cadena en el formato de fecha
if dianro>31 or mesnro>12:#El ejercicio nos marca que si el dia y mes rebasan las fechas naturales del calendario como el dia 31 y mes 12, nos marque la leyenda de Fecha incorrecta 
    print("Fecha incorrecta")#Se imprime la leyenda 
else:#En caso de que se cumpla con una fecha correcta, se prosigue con el programa 
    if diasemana in "lunes,martes,miercoles":#Si el dia en letra es lunes,martes o miercoles, se efectua lo siguiente
        respuesta=input("¿Se tomaton examenes? S/N: ")#Se pregunta al usuario si se tomaron examenes, teniendo como respuesta S o N
        if respuesta.lower()=="s":#Para que sea indistinto mayusculas y minusculas, volvemos a utilizar la herramienta lower para convertir o conservar todo en minusculas y pueda continuar el programa 
            aprobados=int(input("Cantidad de aprobados: "))#Se le pregunta al usuario la cantidad de alumnos aprobados
            reprobados=int(input("Cantidad de reprobados: "))#Se le pregunta al usuario la cantidad de alumnos reprobados
            print("Porcenataje de aprobados: ",(aprobados*100)/(aprobados+reprobados),"%")#Al final de la condicional anterior y ya teniendo los datos requeridos, el programa muestra el porcentaje de alumnos reprobados con respecto al total de la suma entre aprobados y reprobados  
    elif diasemana == "jueves":#La siguiente condicional en caso de que el dia en letras sea jueves 
        asistencia=int(input("Porcenataje de asistencia: "))#Se pide al usuario el porcentaje de asistencia
        if asistencia>50:#Si el porcentaje de asistencia es mayor a 50
            print("Asistio la mayoria")#Se imprime la leyenda si se cumple la condicional anterior
        else:#Si no se cumple la condicional anterior
            print("No asistio la mayoria")#Se imprimprime la leyenda No asistio la mayoria
    elif diasemana == "viernes":#Si la condicional de dia en letra es viernes
        if dianro==1 and (mesnro==1 or mesnro==7):#El ejecicio nos dice que en caso de que el dia en numero sea igual a 1 y el mes sea igual a 1 o 7...
            print("Comienzo de nuevo ciclo")#Si se cumple la condicional anterior, se muestra la leyenda Comienzo de nuevo ciclo
            alumnos=int(input("Cantidad de alumnos: "))#Se pide la cantidad de alumnos del nuevo ciclo
            arancel=float(input("Arancel: $"))#Se ingresa por usuario la cantidad en Arancel
            print("Ingreso total: $", alumnos*arancel)#Se muestra el ingreso total obtenido de la multiplicacion de alumnos y arancel  
    else:#Si no se cumple con ninguna de las condicionales anteriores...
        print("Fecha incorrecta")#Se muestra la leyenda Fecha incorrecta 
        
print("Fin del programa")#Por ultima se muestra la leyenda Fin del programa y se concluye lo programado