### HACER LISTAS NUMÉRICAS ###

### FUNCIÓN range()
for value in range(1,5):# Imprime del 1 al 4, la iteración se para en el segundo número del parentesis sin contarlo
    print(value)
    
for value in range(1, 6):# Lo hago así para que se vea el 5
    print(value)
    
for value in range(6): # Si no le damos un inicio empezará en 0
    print(value)
    
    
# Modo para hacer una lista de números
numbers = list(range(1, 6))
print(numbers)

# Para saltarse números con un rango determinado
even_numbers = list(range(2, 11, 2)) #Mostramos los pares del 2 al 10 incluidos al llegar hasta 11
print(even_numbers)

# Crear una lista con números al cuadrado
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square) 
print(squares) # Cuando se utiliza append() para añadir el print se tiene que sacar del for

# Sin la variable intermedia
squares = []
for value in range(1, 11):
    squares.append(value**2)    
print(squares) # Cuando se utiliza append() para añadir el print se tiene que sacar del for

## MÍNIMO, MÁXIMO Y SUMA DE UNA LISTA DE NÚMEROS ##
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits)) 
print(sum(digits)) 

### LISTAS POR COMPRENSIÓN ###

squares = [value ** 2 for value in range(1, 11)]
print(squares)

### EJERCICIOS ###
# 1. Contar hasta 20: Use un bucle for para imprimir los números del 1 al 20, ambos incluidos
for num in range(1, 21):
    print(num)
    
# 2. Un millón: Haga una lista de números de uno a un 1000000 y luego use un bucle for para imprimir los números
unMillon = []
for value in range(1, 1000001):
    unMillon.append(value)
#print(unMillon) # Cuando se utiliza append() para añadir el print se tiene que sacar del for

# 3. Sumar un millón: Use min(), max() y sum() con la lista anterior

print(min(unMillon))
print(max(unMillon))
print(sum(unMillon))

# 4. Números impares: Use el tercer argumento de la función range() para hacer una lista
# de los números impares comprendidos entre 1 y 20. Utilice un bucle for para imprimir cada número

for num in range(1, 21, 2):
    print(num)
    
# 5. Treses: Haga una lista de los múltiplos de 3 comrpendidos entre el 3 y el 30. Use un bucle for
numbers = []
for num in range(3, 31, 3):
    numbers.append(num)
print(numbers) # Cuando se utiliza append() para añadir el print se tiene que sacar del for

# 6. Cubos: Un número elevado a la tercera potencia e sun cubo, por ejemplo el cubo de 2 
# se escribe como 2**3 en Python. Haga una lista de los 10 primeros cubos (del 1 al 10)

cube = []
for value in range(1, 11):
    cube.append(value**3)
print(cube)

# 7. Comprension de cubos: Use una lista por compresión de los 10 primeros cubos

cube = [value**3 for value in range(1, 11)]
print(cube)