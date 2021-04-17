class Gato:#Se crea la clase Gato
    especie="mamifero"#Atributo de clase
    def __init__(self, nombre, edad):#Contrictor con el con el cual instanciaremos los parametros requeridos
        self.nombre=nombre#Los self se requieren para instanciar el objeto, en este caso el nombre 
        self.edad=edad#Este self se requiere para instanciar el objeto, en este caso la edad
        self.alimentos=[]#Este self hace referencia a que se creara, de ser necesario, una lista de alimentos favoritos

    def verEtapaDeVida(self):#Este es otro metodo mediante el atributo edad con el cual nos mostrara la etapa del gato
        if self.edad>1:#Condicional en caso de que la edad sea mayor a 1 año
            print(self.nombre, "es adulto")#Si se cumple la condicion anterior, se mostrara el nombre del gato junto con la leyenda correspondiente, en este caso "es adulto"
        else:#Si no se cumple la condicion anterior 
            print(self.nombre, "es cachorro")#Se muestra por logica la edad es 1, por lo que al igual que lo anterior, se mostrara el nombre junto con la leyenda "es cachorro" 
    
    def esAlimentoFavorito(self, alimento):#Metoso en caso de querer saber si un alimento es favorito del gato en cuestion
        return alimento in self.alimentos# Al ingresar el alimento, este lo comprueba en la lista del atributo alimentos y si es verdadero, regresa verdadero
