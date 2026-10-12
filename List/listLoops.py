### TRABAJO CON LISTAS ###

## BUCLES --for ##

magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print(magician.title())
    
# Una buena práctica es dar el nombre a la variable relacionado con el nombre de la lista
# Ejemplos: for cat in cats, for dog in dogs, for item in lest_of_items

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!!")

# ERRORES
#magicians = ['alice', 'david', 'caroline']
#for magician in magicians:
#print(magician.title()) #Si esta línea no tiene la sangría da error en la ejecución indentationError

## EJERCICIOS ##

# 1. Pizzas: Piense en al menos tres de sus pizzas favoritas. Guarde estos nombres en una lista 
# y use un bucle for para imprimir el nombre de cada pizza
pizzas = ['barbacoa', 'romana', 'hawaiana']
for pizza in pizzas:
    print(pizza.title())
    
#   -Modifique su bucle for para imprimir una oración usando el nombre de la pizza en vez de 
#   solo el nombre. Para cada pizza debería tener al menos una línea de salida con una 
#   oración simple.
for pizza in pizzas:
    print(f"Me gusta la pizza sabor {pizza.title()}")

#   -Añada una línea al final del programa, fuera del bucle, que indique cuánto le gusta la pizza.
#   La salida debería tener tres o más líneas sobre sus pizzas favoritas y al final una frase adicional
print("¡Me encanta la pizza!!!")    

# Animales: Piense en al menos tres animales diferentes que tengan una característica en común.
# guarde los nombres en una lista y use un bucle for para imprimir el nombre de cada animal

animales = ['gato', 'perro', 'loro']
for animal in animales:
    print(animal.title())

#   -Modifique su programa para imprimir una oración sobre cada animal
for animal in animales:
    print(f"Un {animal.title()} sería un buen animal de compañia")
    
#   -Añada una línea al final diciendo qué tienen estos animales en común.
    print(f"Son muy sociables\n")
    
print('¡Cualquiera de estos animales sería una excelente mascota!!!')