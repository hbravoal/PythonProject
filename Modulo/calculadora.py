def suma(num1,num2):
    print( num1 + num2)
    return num1 + num2

def resta(num1,num2):
    print(num1- num2)
    return num1- num2

def multiplicar(num1,num2):
    print(num1*num2)
    return num1*num2

def dividir (num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Nose puede dividre por 0")
        return "Nose puede, error"


# op1 =int ( input("Introduce Num 1 :"))
# op2 =int ( input("Introduce Num 2 :"))

# operacion = input("Introduce operación (suma,resta,mult,div)")

# if operacion == "suma":
#     print(suma(op1,op2))

# elif operacion == "resta":
#     print(resta(op1,op2))

# elif operacion == "mult":
#     print(multiplicar(op1,op2))

# elif operacion == "div":
#     print(dividir(op1,op2))
# else:
#     print('Error')