#inyección manual
class Contenedor:
    def __init__(self):
        self.registro = {}

    def registrar(self, nombre, provider):
        self.registro[nombre] = provider
    
    def resolver(self, nombre):
        return self.registro[nombre]()
    
class Logger:
    def info(self, msg):
        print(f"[INFO] {msg}")

class Servicio:
    def __init__(self, logger):
        self.logger = logger

    def procesar_data(self):
        self.logger.info("Procesando data")

contenedor = Contenedor()

contenedor.registrar("logger", Logger)
contenedor.registrar("service", lambda: Servicio(contenedor.resolver("logger")))

service = contenedor.resolver("service")

service.procesar_data()
