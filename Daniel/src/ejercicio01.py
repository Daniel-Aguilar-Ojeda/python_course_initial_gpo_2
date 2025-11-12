'''
Docstring para Daniel.src.ejercicio01
'''
from urllib.parse import uses_relative


mi_variable = 28
print(type(mi_variable))
mi_variable = 1.65
print(type(mi_variable))
mi_variable = "Hola"
print(type(mi_variable))
mi_variable = False
print(type(mi_variable))

#listas
fruits = ["apple", "banana", "pineaple"]
fruits.append("strawberry")
print("first fruit: ", fruits[0])

#tupla - inmutables
coordenates = (91, -19.2)
print("Lat: ", coordenates[0])

#diccionario
user_info = {"name":"Daniel", "rol":"frontend", "active": True}
print("user rol: ", user_info["rol"])

#Sets
lenguages = {"python", "java", "c#"}
print("lenguages: ", lenguages)

# Strins
first_name = "Daniel"
last_name = "Aguilar"
print(f"{first_name} {last_name}")

#asignación multiple
x,y,z = 10, 20, 30

#asignación encadenada
x = y = z = 0

#compresiones
lenguages_list = [lenguage for lenguage in lenguages]
print("Lenguage list: ", lenguages_list)

#break, continue y else en bloques
for n in range(5):
    if n == 3:
        break
    else:
        print(f"n: {n}")

