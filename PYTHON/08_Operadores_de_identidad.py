"""
||---------------------------------------------------------------------||
||-------------------------OPERADORES DE IDENTIDAD---------------------||
||---------------------------------------------------------------------||
||-----IS-Compara dos coleciones si es el mismo objeto en memoria------||
||-IS NOT-Compara dos colecciones si NO son el mismo objeto en memoria-||
||---------------------------------------------------------------------||
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Operador "IS"
print(a is b)  #Imprime False
print(a == b)  #Imprime True, diferencia igualdad
print(a is a)  #Imprime True

#Operador "IS NOT"
print(a is not b)  #Imprime True
print(a is not a)  #Imprime False
