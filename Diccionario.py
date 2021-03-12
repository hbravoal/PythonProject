#Clave y valor 
# No puede existir claves repetidas

diccionario = {"Martin":{"Nombre": "Henry", "Años":20},"Pepe":"Rojas"}
print(diccionario["Martin"])
diccionario["Jorge"] = "Paez"
del(diccionario["Martin"])
print(diccionario)