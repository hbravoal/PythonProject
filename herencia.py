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

persona1 = Persona("Henry",20,"Bravo","Hombre")
persona1.datosPersonales()

class Empleado(Persona):
    def datosEmpleado(self,vacaciones,salario):
        print(f"Vacciones: {vacaciones}, salario : {salario}")



empleado1 = Empleado("maria",20,"Lina","Femenino")
empleado1.datosPersonales()
empleado1.datosEmpleado("Enero",2000)

class Gerente(Empleado):
    def acciones(self,acciones):
        print(f"accionmes{acciones}")


gerente1 =Gerente("Henry",20,"Bravo","Masc")
gerente1.datosPersonales()