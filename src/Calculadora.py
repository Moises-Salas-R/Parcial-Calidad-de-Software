def Sumar(num1, num2):
    return num1 + num2

def Restar(num1, num2):
    return num1 - num2

def Multiplicar(num1, num2):
    return num1 * num2

def Dividir(num1, num2):
    if num2 == 0:
        raise ValueError("error: el número es cero")
    return num1 / num2

if __name__ == "__main__": # pragma: no cover
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    print("operaciones")
    print("1:suma")
    print("2:resta")
    print("3:multiplicación")
    print("4:división")

    operación = input("elige una operación: ")

    if (operación == "1"):
        resultado = num1 + num2
        print(resultado)
    elif (operación == "2"):
        resultado = num1 - num2
        print(resultado)
    elif (operación == "3"):
        resultado = num1 * num2
        print(resultado)
    elif (operación == "4"):
        resultado = num1 / num2
        if (num2 != 0):
            print(resultado)
        else:
            print("error: el número es cero")
    else:
        print("números inválidos")



