class Coche():

    def __init__(self):
        self.marca="Audi"
        self.color="Rojo"
        self.__rueda=4  #Private property
        self.enMarcha=False 

    def arrancar(self,arrancamos):
        self.enMarcha=arrancamos

        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"
    
    def __str__(self): #Sirve para las carácteristicas
        return "Este auto es marca {} de color {} tiene {} y el estado {}".format(self.marca,self.color,self.__rueda,self.enMarcha) 


carro1 =Coche()

print(carro1.arrancar(True))
print(str(carro1))

print("*****Another Vehicle")

miCoche2= Coche()
miCoche2.rueda=20 #No es posible
print(str(miCoche2))