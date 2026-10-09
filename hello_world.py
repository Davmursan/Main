message = "Hello Python world!"
print(message)

def sumar(num1,num2):
    return num1 + num2

def restar(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

def dividir(num1,num2):
    if num2 == 0:
        return "Error: No se puede dividir entre cero"
    return num1 / num2

print("-------------------")
print("----CALCULADORA----")
print("-------------------")
print("Elige un número del 1 al 4\n 1: Sumar\n 2: Restar\n 3: Multiplicar\n 4: Dividir")


operacion = int(input("Introduzca un número para elegir la operación: "))

match operacion:
    case 1:
        print("Has elegido sumar")
        num1 = float(input("Introduzca el primer número: "))
        num2 = float(input("Introduzca el segundo número: "))
        print("La suma es:", sumar(num1,num2))
        
    case 2:
            print("Has elegido restar")
            num1 = float(input("Introduzca el primer número: "))
            num2 = float(input("Introduzca el segundo número: "))
            print("La resta es:", restar(num1,num2))
            
    case 3:
            print("Has elegido multiplicar")
            num1 = float(input("Introduzca el primer número: "))
            num2 = float(input("Introduzca el segundo número: "))
            print("La multiplicación es:", multiplicar(num1,num2))
            
    case 4:
            print("Has elegido dividir")
            num1 = float(input("Introduzca el primer número: "))
            num2 = float(input("Introduzca el segundo número: "))
            print("La división es:", dividir(num1,num2))
            
    case _:
        print("Opción no válida")
        








