#Factorial de un número usando generadores
""" def factorial(limit:int):
    '''Factorial de un número'''
    current = 1
    for n in range(limit):

        current = current * (n+1)
        yield current

test = factorial(4)

for ix, item in enumerate(test):
    print(f"{ix + 1}: {item}")


def fibonacci(limit:int):
    '''Serie de fibonacci'''
    current = 1
    for n in range(limit):
        current = current + n
        yield current
test2 = fibonacci(4)

for ix, item in enumerate(test2):
    print(f"{ix}: {item}") """

class Proccesor:
    '''Describe processor'''
    def __init__(self, cores: int):
        self.cores = cores

class Memory:
    '''Describe memory'''
    def __init__(self, size: float, speed: float):
        self.size = size
        self.speed = speed

class Computer:
    '''Describe computer'''
    def __init__(self, processor: Proccesor, memory: Memory):
        self.proccessor = processor
        self.memory = memory
    
    def description(self):
        print(f"Proccessor cores: {self.proccessor.cores}")
        print(f"Memory size: {self.memory.size}Mb")
        print(f"Memory speed: {self.memory.speed} Hz")

my_computer = Computer(Proccesor(8), Memory(1080, 120))
my_computer.description()

