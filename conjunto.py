conjunto = set();  # Inicializar
conjunto = {20,30,30,'Hla',True} # No permite lista.
conjunto.add('Added')
conjunto.discard(2)

print(conjunto)
print(20 in conjunto ) #Si existe 20 en Conjunto
print(20 not  in conjunto ) #Si existe 20 en Conjunto
conjunto.clear()
print(conjunto)