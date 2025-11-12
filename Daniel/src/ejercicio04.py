#decoradores: añade funcionalidades

import time


def decorador(func):
    def envoltura():
        print("Inicio")
        func()
        print("final")

    return envoltura

def decoradorArgs(func):
    def envoltura(*args, **kwargs):
        print("Inicio con keywors y argumentos")
        func(*args, **kwargs)
        print("final")

    return envoltura

@decorador
def say_hello():
    print("Hola mundo")

#say_hello()

# Medir tiempo de ejecucion de una función
def time_execution(func):
    def envoltura(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Exetution time: {end - start} s")
    return envoltura

@time_execution
def test_sleep():
    time.sleep(5)
    print(f"función completa ")


test_sleep()


