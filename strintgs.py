### STRINGS ###

name = 'Ada Lovelace carpena'
print(name.title()) #Pone la primera letra de cada palabra en mayúsculas

print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message =f"Hello, {full_name.title()}!!!"
print(message)

print("\tPython") #Esto hace una tabulación
print("Languages:\nPython\nC\nJavaScript") #Salto de línea
print("Languages:\n\tPython\n\tC\n\tJavaScript") #La combinación de los dos


#Eliminar espacios en blanco
favorite_lenguage = "python t     "
favorite_lenguage = favorite_lenguage.rstrip() # Elimina los espacios a la derecha
print(favorite_lenguage)

favorite_lenguage = "  r   python "
favorite_lenguage = favorite_lenguage.lstrip() # Elimina los espacios a la izquierda
print(favorite_lenguage)

favorite_lenguage = "       r    python   t       "
favorite_lenguage = favorite_lenguage.strip() # Elimina los espacios a la derecha y a la izquierda
print(favorite_lenguage)

nostarch_url = "https://deivilskiller@gmail.com"
print(nostarch_url.removeprefix("https://")) #Elimina lo que queramos de una url

# Apostrofes

message = "One of Python's strengths is its diverse community."
print(message)

## EJERCICIOS STRINGS ##

# 1. Mensaje personal: Use una variable para representar el nombre de una persona
# e imprima un mensaje para esa persona. El mensaje debería ser sencillo, por ejemplo:
# "Hola, Eric, ¿Te gustaría aprender Python hoy?"

name = "David"
message = f"Hola, {name}, ¿te gustaría aprender Python hoy?"
print(message)

# 2. Grafía de nombres: Usse una variable para representar el nombre de una persona
# e imprima ese nombre en minúsculas, mayúsculas y mayúsculas inicial

complete_name = "daVid MurCia sÁnchez"
print(complete_name.lower())
print(complete_name.upper())
print(complete_name.title())

# 3. Cita célebre: Busque una cita de un personaje al que admire. Imprima la cita
# y el nombre del autor. La salida debería tener un aspecto similar a esto, incluidas las comillas:
#       Albert Einstein once said, "A person who never made a mistake never tried anything new"

print(('Edmun Burke dijo: "Los que no conocen la historia están destinados a repertirla"'))

# 4. Repite el ejecicio 3 pero, esta vez, represente el nombre del autor en una variable llamada
# famous_person. Después componga el mensaje y represéntelo con una nueva variable llamada
# message. Imprima el mensaje

famous_person = "Edmon Burke"
message = f"{famous_person} dijo: 'Los que no conocen la historia están destinados a repertirla'"
print(message)

# 5. Eliminar espacios de nombres: Use una variable para representar el nombre de una persona 
# e incluya algunos caracteres de espacio en blanco al principio y al final del nombre. 
# Asegúrese de usar cada combinación de caracteres, \n, \t, al menos una vez.
# Imprima el nombre una vez, de modo que se muestren los espacios alrededor.

name = "    Alejandra    \nMartinez                  \ntoledo           "
print(name)
print(name.lstrip())

# 6. Extensiones de archivos: Python cuenta con el método removesuffix(), que funciona exactamente igual
# que el método removeprefix(). Asigne el valor 'Python_notes.tx' a una variable llamada filename. 
# A continuación, utilice el método removesufix() para mostrar el nombre de archivo sin la extensión 
# de archivo, como ocurre con algunos exploradores de archivo.

filename = 'python_notes.tx'
print(filename.removesuffix(".tx"))