#Clases y objetos

class Gelatina: #Inicializamos el molde
    def __init__(self,sabor,color,tamaño):
        self.sabor=sabor
        self.color=color
        self.tamaño= tamaño

    def imprimir(self):
        print(f"Sabor: {self.sabor}")
        print(f"color: {self.color}")
        print(f"tamaño: {self.tamaño}")

gel1 = Gelatina("Best","Roja","Grande")

gel1.imprimir()