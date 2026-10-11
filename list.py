###  LISTS ###

bicycles = ["trek", "cannondale", "redline", "specialized" ]
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) # Siempre dará el último de la lista

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

## EJERCICIOS ##

# 1. NOMBRES: Guarde los nombres de unos cuantos amigos en una lista 
# llamada nombres. Imprima el nombre de cada persona accediendo al 
# elemento correspondiente de la lista de uno en uno.

nombres = ["Catu", "primi", "brother", "aritz", "vergara"]
print(nombres[0].title())
print(nombres[1].title())
print(nombres[2].title())
print(nombres[3].title())
print(nombres[4].title())


for i in nombres:
    print(i.title())
    
# 2. SALUDOS: Empiece con la lista de antes, pero, en vez 
# de solo imporimier el nombre de cada persona, imprímales un mensaje

message1 = f"Mi mejor amigo se llama {nombres[0].title()} y tiene todo el cuerpo lleno de tatoos, y {nombres[1].title()} es calvo."
print(message1)


# 3. Su propia lista: Piense en su medio de transporte favorito, como la moto o el coche, 
# y haga una lista que incluya varios ejemplos. Use la lista para imprimir una serie de 
# frases sobre esos elementos, como "Me gustaría tener una moto Honda"

cars = ["ford", "opel", "peugeot", "mercedes", "ferrari"]
message2 = f"Mi coche es un {cars[0].title()} pero me gustaría tener un {cars[3].title()}, pero sobre todo me gustaría tener un {cars[-1].upper()} "

print(message2)

# MODIFICAR, AÑADIR Y ELIMINAR ELEMENTOS

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "Ducati" # Mofificamos el valor de la posición 0
print(motorcycles)
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.append('ducati') # Se añade al final
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')

print(motorcycles)

motorcycles.insert(2, 'ducati') #Con .insert(), primero ponemos la posición y después lo que queremos insertar
print(motorcycles)


# Método del para borrar
del motorcycles[0] #Para borrar elementos se pone del delante del nombre de la lista y entre corchetes la posición
print(motorcycles)

# Método pop() Elimina el último elemento pero te deja trabajar con el creando variables sobre la marcha
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle) # He sacado yamaha de motorcycle y la he puesto en popped_motorcycle

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# Cuando quiera eliminar un elemento de una lista para no volver a usarlo jamás use 'del',
# si desea usar un elemento al retirarlo de la lista, utilice pop()

# Método remove()
# Si no sabes la posición del elemento pero sabes el nombre entonces usa remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

## EJERCICIOS ##

# 1. Lista de invitados: Si pudiese invitar a cualquiera, a cenar, ¿a quién invitaría? 
# Haga una lista de al menos tres personas y úsela para imprimir un mensaje para cada persona.

invitarCena = []
invitarCena.append("catu")
invitarCena.append("primi")
invitarCena.append("brother")
print(invitarCena)

print(f"Me gustaría invitar a cenar a mi gran amigo / hermano {invitarCena[0]}")
print(f"Me gustaría invitar a cenar a mi gran amigo / hermano {invitarCena[1]}")
print(f"Me gustaría invitar a cenar a mi gran amigo / hermano {invitarCena[2]}")

print(f"{invitarCena[1]} ha rechazado la invitación")

# 2. Cambiar la lista de invitados: Acaba de enterarse de que uno de sus invitado no podrá 
# asistir, así que tiene que enviar un nuevo juego de invitaciones. Tendrá que pensar en otra persona para invitar
#   *Empiece con el programa del ejercicio 1. Añada una llamada print() al final del 
#   programa indicando el nombre del invitado que no puede asistir.
#   *Modifique la lista sustituyendo el nombre del invitado que no puede venir
#   por el de otra persona a la que va a invitar en su lugar.
#   *Imprima un segundo grupo de mensajes de invitación, uno para cada persona que haya en la lista ahora

invitarCena[1] = "Mari Pili"
print(f"Me gustaría invitar a cenar a mi gran amigo / hermano {invitarCena[0]}")
print(f"Me gustaría invitar a cenar a mi gran amigo / hermano {invitarCena[1]}")
print(f"Me gustaría invitar a cenar a mi gran amigo / hermano {invitarCena[2]}")

# 3. Más invitados: Acaba de encontrar una mesa más grande, así que dispone de más espacio. 
# piense en otros tres invitados más.
#   *Use insert() para añadir un nuevo invitado al principio de la lista
#   *Use insert() para añadir un nuevo invitado a la mitad de la lista
#   *Use un append() para añadir un nuevo invitado al final de la lista
#   *Imprima un nuevo juego de mensajes de invitación, uno para cada uno de la lista.

invitarCena.insert(0, 'vergara')
invitarCena.insert(2, 'albujer')
invitarCena.append('beni')
print(invitarCena)

for i in invitarCena:
    print(f'{i} me gustaría invitarte a cenar al Titas.')
    
# 4. Reducir la lista de invitados: Acaba de descubrir que la mesa no llegará a tiempo
# para la cena y solo tiene espacio para dos invitado.
#   *Use pop() para eliminar invitados hasta que queden 2. Cada vez que retire a uno 
#   imprima un mensaje diciendole que al final no puedes invitarle.
#   *Imprima un mensaje para las 2 personas que quedan 
#   Use "del" para borrar los dos últimos nombres de la lista y que quede vacía. Imprima
#   la lista para ver que realmente está vacía.

while len(invitarCena) > 2:
    eliminado = invitarCena.pop()
    print(f'{eliminado} se ha cancelado la cena')

""""
print(invitarCena)
last_friend = invitarCena.pop()
print(f'{last_friend} lo siento pero al final se ha cancelado la cena.')
last_friend2 = invitarCena.pop()
print(f'{last_friend2} lo siento pero al final se ha cancelado la cena.')
last_friend3 = invitarCena.pop()
print(f'{last_friend3} lo siento pero al final se ha cancelado la cena.')
last_friend4 = invitarCena.pop()
print(f'{last_friend4} lo siento pero al final se ha cancelado la cena.')
"""
for i in invitarCena:
    print(f'{i} la cena sigue en pie.')
    
del invitarCena[:]
print(invitarCena)
