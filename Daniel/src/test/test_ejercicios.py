from src.ejercicio08 import Notificador


def test_enviar():
    notificador = Notificador()
    msj = notificador.enviar_mensaje("tienes un mensaje pendiente")
    assert "Hola, tienes un mensaje pendiente" in msj

def test_cancelar_mensaje():
    notificador = Notificador()
    msj = notificador.cancelar()
    assert "Mensaje no enviado" in msj 