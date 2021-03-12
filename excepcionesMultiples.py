c = int (input("Ingrese valor"))
try:
    c/0
except ValueError:
    print('Nos epude sumar una cadena')
except Exception as err:
    print(f'Error{type(err).__name__}')