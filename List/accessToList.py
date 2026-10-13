### ACCEDER A PARTES DE UNA LISTA ###

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # charles, martina y michael

print(players[1:4]) # martina, michael y florence
print(players[:4]) # Si se omite la parte izquierda se empieza desde el principio de la lista (por eso aquí salen los 4 primeros nombres)
print(players[2:]) # Así empieza desde el final hasta la posición 2 incluida
print(players[-3:]) # Así se sacan los 3 últimos de la lista

# Pasándolo por un bucle for
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())
    
## COPIAR LISTAS ##
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy frend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

## ESTO NO FUNCIONA
"""
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
"""

### EJERCICIOS ###
# 1. TROZOS: Partiendo de uno de los programas que hemos escrito en este capítulo, añada varias líneas al final que hagan lo siguiente:
#   Imprimir el mensaje "Estos son los 3 primeros elementos de la lista: ". A continuación, use un trozo para 
#   imprimir los tres primeros elementos de la lista de ese programa

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Estos son los tres primeros números de mi lista: ")
print(number_list[:3])

#   Imprime el mensaje "Estos están en medio de la lista"
print("Estos números están en medio de la lista: ")
print(number_list[3:7])

# 2. Mis pizzas, sus pizzas: Empiece con el programa del principio. Haga una copia de la lista y llámela friend_pizzas.

my_pizzas = ['margarita', 'carbonara', 'hawuaiana']
friend_pizzas = my_pizzas[:]

#   Añada una pizza nueva a la original y a la del amigo
my_pizzas.append('barbacoa')
friend_pizzas.append('tropical')

# Comprobar si hay dos listas diferentes y mostrar un mensaje "Mis pizzas favoritas son:", luego haz un bucle con los dos
print("Mis pizzas favoritas son: ")
for pizza in my_pizzas:
    print("-", pizza)
    
print("\nLas pizzas favoritas de mi amigo son: ")
for pizza in friend_pizzas:
    print("-", pizza)