#clase
class Producto:
    """Clase Producto: Almacena el nombre y precio de un artículo
    """

    def __init__(self, nombre:str, precio:float):
        self.__nombre = nombre
        self.precio = precio

    @property
    def nombre(self)->str:
        '''Retorna la propiedad nombre de manera segura'''
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_name:str)->None:
        '''Permite actualizar la propiedad'''
        #print(f"nuevo nombre: {new_name}")
        self.__nombre = new_name
    


pan = Producto("Pan", 3.5)
pan.nombre = "Pan Intr"
# print(f"Producto: {pan.nombre} con precio: {pan.precio}")


#Herencia y composición
class Animal:
    def __init__(self, name:str):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Making sound...")
    
class Dog(Animal):

    def __init__(self, name:str):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name}: Woof woof")

strage_animal = Animal("uknown")
#strage_animal.make_sound()

pupy = Dog("puppy")
#pupy.make_sound()

#Modelado de objetos mediante composición y herencia
class Motor: 
    def __init__(self, tipo:str):
        self.tipo = tipo
    
class Rueda:
    def __init__(self, tamano:int):
        self.tamano = tamano

class Coche:
    def __init__(self, marca:str, motor: Motor, ruedas: list[Rueda]):
        self.marca = marca
        self.motor = motor
        self.ruedas = ruedas
    
    def descripcion(self):
        print(f"Marca: {self.marca}")
        print(f"Tipo de motor: {self.motor.tipo}")
        print(f"Número de ruedas: {len(self.ruedas)}")

auto_uno = Coche("VW", Motor("Diesel"), [Rueda(2), Rueda(2)])
auto_uno.descripcion()

#Data clases
