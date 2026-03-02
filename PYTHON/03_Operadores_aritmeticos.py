"""
||-------------------------||
||-OPERADORES--ARITMETICOS-||
||-------------------------||
||--------SUMA (+)---------||
||-------RESTA (-)---------||
||---MULTIPLICACIÓN (*)----||
||-----EXPONENTE (**)------||
||------DIVISIÓN (/)-------||
||--DIVISIÓN ENTERA (//)---||
||-------MODULO (%)--------||
||-------------------------||
"""
# SUMA
print(10 + 10)  # Imprime 20
# RESTAR
print(12 - 2)   # Imprime 10
# MULTIPLICACIÓN
print(5 * 2)    # Imprime 10
# EXPONENTE
print(2 ** 3)   # Imprime 8 
# DIVISIÓN
print(20 / 2)   # Imprime 10.0
# DIVISIÓN ENTERA
print(21 // 2)  # Imprime 10
# MODULO
print(11 % 1)   # Imprime 1 

# OPERACIONES COMPUESTAS
# Orden de las matematicas de izquierda a derecha
print(15 - 20 * (2 + 1)) # Imprime -45

# OPERACIONES CON VARIABLES
a = 5
b = 2
resultado = a * b
print(resultado)# Imprime 10

# OPERACIONES COMPUESTAS CON VARIABLES
o = 2
p = 3
q = 3
print(o + p * (o + q)) # Imprime 17

# SUMA (str)
saludo = "Hola"
espacio = " "
nombre = "Un nombre"
concatenacion = saludo + espacio + nombre
print(concatenacion)  # Imprime "Hola Un nombre"

# MULTIPLICACIÓN (str)
multiplicando = "Strings "
multiplicacion_string = multiplicando * 10
print(multiplicacion_string)  # Imprime Strings Strings Strings...