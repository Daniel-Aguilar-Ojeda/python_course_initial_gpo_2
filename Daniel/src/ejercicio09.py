from abc import ABC, abstractmethod
#Inyección de dependencias

#-- Inyección por constructor. 
class ServiceEmailA:
    def enviar_email(self, msg:str):
        print(f"Email enviado: {msg}")

class NotificadorA:
    def __init__(self, service: ServiceEmailA):
        self.service = service

    def notificar(self, msg:str):
        self.service.enviar_email(msg)

notificador = NotificadorA(ServiceEmailA())
#notificador.notificar("cupón!!")

#-- Inyección por setter. 
class ServiceEmail0:
    def enviar_email(self, msg:str):
        print(f"Email enviado: {msg}")

class Notificador0:
    def set_email_service(self, service: ServiceEmail0):
        self.service = service
    

    def notificar(self, msg:str):
        self.service.enviar_email(msg)

email_service = ServiceEmail0()
notificador = Notificador0()
notificador.set_email_service(email_service)
notificador.notificar("cupón!!")

#
class MotorBase(ABC):
    @abstractmethod
    def encender(self):
        pass

class MotorElectrico(MotorBase):
    def encender(self):
        print("Encendido eléctrico")

class MotorGasolina(MotorBase):
    def encender(self):
        print("Encendido por combustión")

class Auto:
    def __init__(self, motor_base: MotorBase):
        self.motor = motor_base
    
    def arrancar(self):
        self.motor.encender()

auto_electrico = Auto(MotorElectrico())
auto_gas = Auto(MotorGasolina())
auto_electrico.arrancar()
auto_gas.arrancar()