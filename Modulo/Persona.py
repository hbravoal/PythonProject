class Persona():
    def __init__(self,nombre,edad,apellido,sexo):
        self.nombre=nombre
        self.edad= edad
        self.apellido =apellido
        self.sexo= sexo

    def datosPersonales(self):
        print(f"nombre {self.nombre}")
        print(f"apellido {self.apellido}")
        print(f"edad {self.edad}")
        print(f"sexo {self.sexo}")

