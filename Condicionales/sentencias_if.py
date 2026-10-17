### SENTENCIAS IF ###

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")
    
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
    
age1 = 18
age2 = 22
print(age1 >= 21 and age2 >= 21)
print(age1 >= 21 or age2 >=21)

#Comprobar si un elemento está en la lista... in

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#Comprobar si un valor no aparece en la lista..... not

banned_users = ['andrew', 'caroline', 'david']
user = 'david'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print("You are banned!!!!")
    
#Booleanos

game_active = True
can_edit = False

### PRUEBAS ###
# Pruebas condicionales: Escriba una serie de pruebas condicionales. Imprima una frase describiendo cada 
# pruebay su predicción para el resultado.
# car = "subaru"
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
#
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

moto = 'suzuki'
print("Is moto == 'suzuki'? I predict True.")
print(moto == 'suzuki')


print("\nIs moto == 'suzuki'? I predict False.")
print(moto == 'honda')

# Pruebas con el método lower()
car = "FORD"
print("Is car == ford, I predict False")
print(car.lower()== car)

# Pruebas de igualdad y desigualdad de cadenas
cadena = 'Hola soy una cadena'
cadena1 = 'Hola soy una Cadena'
print(cadena == cadena1)
print(cadena.upper() == cadena1.upper())




age = 17
if age > 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote!")    

if age < 4:
    print("You pass free")
elif age >= 4 and age <18:
    print("Your ticket cost is 25 dollars")
else:
    print("Your ticket cost is 40 dollars")
    
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"El precio de tu entrada es de {price}$.")
age = 70

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
print(f"El precio de tu entrada es de {price}$.")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
    
print("\nFinished making your pizza!!")

# Esta última estructura con sólo if no funcionaría con if elif.

### PROBANDO PROBANDO ###
# 1. Colores de Aliens: Imagine un alien que acaba de ser derribado en un juego. Cree una
# variable llamada color_alien y asígnele como valor 'verde', 'amarillo' o 'rojo'.
color_alien = ['verde', 'amarillo', 'azul']

# Escriba una sentencia if para comprobar si el color del alien es verde. Si lo es, imprima un 
# mensaje informando al jugador de que ha ganado 5 puntos
if 'verde' in color_alien:
    print("Has ganado 5 puntos")
if 'rojo' in color_alien:
    print()  

# 2. Aliens 2: elija un color para un alien igual que en el ejercicio 1 y escriba una cadena if else
# Si el color del alien es verde, imprima un mensaje informando al jugador de que ha ganado 5 puntos por disparar al alien\
# Si el color del extraterrestre no es verde, imprima una frase informando de que ha ganado 10 puntos

if 'verde' in color_alien:
    print("Ganas 5 puntos")
else:
    print("Ganas 10 puntos")

if 'negro' in color_alien:
    print("Ganas 5 puntos")
else:
    print("Ganas 10 puntos")
    
# if con listas

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
        
print("\nFinished making your pizza")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else: 
    print('Are you sure you want a plain pizza?')
    
available_toppings = ['mushrooms', 'olive', 'green peppers', 'pepperoni', 'pineaple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese', 'tomato']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")
        
print("\nFinished making your pizza!")

numero = 0

### EJERCICIOS PARA PROBAR ###

# Hola, Admin: Cree una lista de cinco o más nombres de usuario, incluyendo el nombre 'admin'
# Imagine que está escribiendo código que imprimirá un mensaje para cada usuario cuando inicien
# sesión en un sitio web. Pase en bucle por la lista e imprima un saludo para cada usuario:

users_List = ['david', 'fernando', 'primi', 'monica', 'admin']
#for user in users_List:
    #print(f"{user}, has iniciado sesión, bienvenido!!")

# Si el nombre de usuario es 'admin' imprima un saludo especial, como "Hola, admin, ¿Quieres ver un informe de estado?"
# De lo contrario el mensaje anterior
"""
users_List = ['david', 'fernando', 'primi', 'monica', 'admin']
for user in users_List:
    if user == 'admin':
        print(f"Hola, {user}, ¿quieres ver un informe de estado?")
    else:
        print(f"{user}, has iniciado sesión, bienvenido!!")
"""        
# Sin Usuarios: Añada una prueba if al programa anterior para asegurarse de que la lista no esté vacía
# Si está vacía print("¡Necesitamos encontrar algún usuario!")
# Borre todos los nombres de usuario de la lista y asegurese que imprime el mensaje correcto        
users_List = []
if users_List: 
    for user in users_List:
        if user == 'admin':
            print(f"Hola, {user}, ¿quieres ver un informe de estado?")
        else:
            print(f"{user}, has iniciado sesión, bienvenido!!") 
        
else:
    print("¡Necesitamos encontrar usuarios!!!")
    
# Comprobar los nombres de usuario: Haga lo siguiente para crear un programa que simule cómo 
# los sitios web se aseguran de que todos los usuarios tienen un nombre único.    
# Cree una lista con 5 o más nombres de usuario llamada current_users.
# Cree otra lista igual llamada new_users. Asegurate de que 2 o 3 nombres estan en la otra lista
# Pase un bucle por  la lista new_users para ver si cada nuevo nombre de usuario está ya usado.
# Si lo está, imprima diciendo que elija otro nombre, sino que si está disponible
# Asegurate que no distingue entre may y minusculas. Hacer una copia de current_users en minúsculas.

current_users = ['David', 'Jose', 'Ana', 'Lucía', 'Raúl']
new_users = ['pablo', 'jose', 'juan', 'ana', 'raúl']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"El nombre de usuario {user} ya está cogido, elija otro por favor.")
    else:
        print(f"Enhorabuena, {user} está disponible")
        
# Números ordinales en Inglés: los números ordinales indican su posición en una lista, como 1, 2, etc. \
# En inglés, la mayoría termina en th excepto 1, 2, y el 3 que terminan en st, nd y rd respectivamente.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in numbers:
    if n == 1:
        print("1st")
    elif n == 2:
        print("2nd")
    elif n == 3: 
        print("3rd")
    else:
        print(f"{n}th")
    
"""
anterior = 0
actual = 1
for i in range(0, 50):
    fib = anterior + actual
    anterior = actual
    actual = fib
    print(fib)
"""    
