#Data clases
from dataclasses import dataclass
from typing import List
@dataclass
class Motor: 
    tipo:str

@dataclass
class Rueda:
    tamano:int

@dataclass
class Coche:
    marca: str
    motor: Motor
    ruedas: List[Rueda]
    
    def __str__(self):
        return(f"Marca: {self.marca} \n"
        f"Tipo de motor: {self.motor.tipo}\n"
        f"Número de ruedas: {len(self.ruedas)}")

auto_uno = Coche("VW", Motor("Diesel"), [Rueda(2), Rueda(2)])

print(auto_uno)


