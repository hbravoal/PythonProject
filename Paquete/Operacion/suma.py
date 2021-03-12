def multiplicar(num1,num2):
    print(num1*num2)
    return num1*num2

def dividir (num1,num2):
    try:
        print(num1,num2)
        return num1 / num2
    except ZeroDivisionError:
        print("Nose puede dividre por 0")
        return "Nose puede, error"

