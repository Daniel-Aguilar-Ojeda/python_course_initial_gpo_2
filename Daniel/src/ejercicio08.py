#Purebas unitarias
class Notificador:
    def enviar_mensaje(self, mensaje:str):
        return f"Hola, {mensaje}"
    
    def cancelar(self):
        return "Mensaje no enviado"
    