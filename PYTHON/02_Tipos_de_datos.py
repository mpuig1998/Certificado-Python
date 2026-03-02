#Numeros enteros (int)
i = 10
y = -5

#Numeros decimales (float)
temperatura_dia = 12.5
temperatura_noche = -7.5

#Numeros complejos (complex)
i = 2 + 8j

#Cadenas de texto (str)
nombre = "Un nombre"
saludo = 'Hola, ¿Que tal estás?'

#Datos booleanos (bool)
licencia = True
es_amigo = False

#Listas (list), colección de elementos ordenada y mutable
ropa = ["abrigo", "zapatos", "pantalones", "camisa"]
lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_mixta = [10, "Guido van Rossum", True, 2.5, "Python", False]

#Tuplas (tuple), colección de elementos ordenada y inmutable
equipo = ("nombre 1", "nombre 2" "nombre 3")
tupla_numerica = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla_mixta = (10, "Guido van Rossum", True, 2.5, "Python", False)

#Conjuntos (set), colecciones no ordenadas de elementos unicos
equipo = {"nombre 1", "nombre 2" "nombre 3"}
conjunto_numerico = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_mixto = {10, "Guido van Rossum", True, 2.5, "Python", False}

#Diccionarios (dict), colección de pares claves:valor
persona = {"nombre":"Un nombre", "edad":23, "ciudad":"Sevilla" }
viajes = {"Guadalajara": False, "Milano": True, "Paris": False, }

#Datos None, representan las variables en ausencia de un valor
i = None 

# COMPROBACIÓN DEL TIPO DE DATO CON "type()"
x = 5
y = 2.5
z = "Guido van Rossum"
a = True
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)                
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}             
diccionario = {"Ubicacion A": 1, "Ubicación B": 2, "Ubicación C": 3}   

print(type(x))
print("Comprobando tipo de dato:", type(x))                      # <class 'int'>
print("Comprobando tipo de dato:", type(y))                      # <class 'float'>
print("Comprobando tipo de dato:", type(z))                      # <class 'str'>
print("Comprobando tipo de dato:", type(a))                      # <class 'bool'>
print("Comprobando tipo de dato:", type(lista))                  # <class 'list'>
print("Comprobando tipo de dato:", type(tupla))                  # <class 'tuple'>
print("Comprobando tipo de dato:", type(conjunto))               # <class 'set'>
print("Comprobando tipo de dato:", type(diccionario))            # <class 'dict'>