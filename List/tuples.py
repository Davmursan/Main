### TUPLAS ###

dimensions = (200, 50) # Así se define una tupla
print(dimensions[0]) # Para ver el índice de la tupla va entre corchetes[]
print(dimensions[1])
print(type(dimensions))

#dimensions[0] = 250 #No se puede alterar una tupla
#print(dimensions)

my_tuple = (3) 
print(type(my_tuple)) # El resultado arroja class int porque no hemos definido bien la tupla

my_tuple = (3,)
print(type(my_tuple)) # Para definir una tupla aunque solo tenga un elemento hay que poner la coma

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Aunque no se puede modificar una tupla, si se puede asignar un nuevo valor
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
    
## PROBANDO LAS TUPLAS ##

# 4-13. Bufé: Un restaurante de tipo bufé ofrece solo cinco comidas básicas. Piense en 5 platos 
# básicos y guárdelos en una tupla.

menuBar = ("paella", "espaguetis", "potaje de garbanzos", "cocido", "sopa de ajo")

# Use un bucle for para imprimir cada comida 
for plato in menuBar:
    print(plato)
    
# Intente modificar alguno de los elementos y asegúrese que python rechaza el cambio
#menuBar[3] = "fideuá"
#print(menuBar) # Da error

# El restaurante cambia su menú, sustituyendo 2 comidas. 
# Añada una línea que rehaga la tupla y use un bucle for para imprimir cada uno de los elementos modificados
print("Menú del martes: ")
for plato in menuBar:
    print(plato.title())
    
menuBar = ("paella", "filete empanado", "lentejas", "cocido", "sopa de ajo")
print("Menú del miércoles: ")
for plato in menuBar:
    print(plato.title())
    


