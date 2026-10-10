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
