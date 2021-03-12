import sys
#por defecto en 0 esta la ruta del archivo.
# recibe dos argumentos
if(len(sys.argv)==3):
    texto =sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)

else:
    print('Error, you should enter two arguments.')
    

print (sys.argv)

#Ejectar: >python E:\BIG\Projects\GitHub\PythonProject\entrada_argumentos.py "hola" 2