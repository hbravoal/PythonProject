class Coche():

    def __init__(self):
        self.marca="Audi"
        self.color="Rojo"
        self.rueda=4
        self.enMarcha=False

    def arrancar(self,arrancamos):
        self.enMarcha=arrancamos

        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"
    
    def __str__(self): #Sirve para las carácteristicas
        return "Este auto es marca {} de color {} tiene {} y el estado {}".format(self.marca,self.color,self.rueda,self.enMarcha) 


carro1 =Coche()

print(carro1.arrancar(True))
print(str(carro1))
