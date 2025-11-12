# argumentos y kwargs

# args: agumentos posicionales
def process_data(*args):
    '''Los argumentos llegan como una tupla'''
    print(type(args))
    print(f"Argumentos: {args}")

#process_data(1,2,3,4,5)
#process_data("uno", 2, "iii", False)

# kwargs: argumentos nombrados
def say_hello(**kwargs):
    print(type(kwargs))
    print(f"Argumentos nombrados: {kwargs}")

#say_hello(nombre="Dani", edad= 10)

# Generadores: eficiencia de memoria, para grandes volumenes de datos
def generate_data(limit: int):
    '''
    Docstring para generate_data
    
    :param limit: Limite superior
    :type limit: int
    '''
    print("Inicio de generador")
    for nn in range(limit):
        print(f"Bucle position {nn}")
        yield nn
    print("Fin de generador")

generador_5 = generate_data(3)

for item in generador_5:
    print(f"item: {item}")

# 