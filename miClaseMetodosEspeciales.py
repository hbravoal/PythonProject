class Coche():
    def __init__(self,brand,km,year):
        self.brand= brand
        self.km = km
        self.year= year
        print("Se ha creado un auto",self.brand)

    def __del__(self): #Eliminar el objeto
        print('Se ha vendido el auto',self.brand)

    def __str__(self):
        return "El auto es un {}, tiene {} y es del año".format(self.brand,self.km,self.year)

micoche = Coche("Audi",2000,1993)
print(str(micoche))

