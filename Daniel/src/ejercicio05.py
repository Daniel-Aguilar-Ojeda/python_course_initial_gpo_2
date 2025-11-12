#Manejo de errores
'''
try-except-else-finally

raise Error

custom error -> class MyCustomError(Error)

para loggin podemos usar un paquete, como logging
'''

import logging

from src.exepcions.exceptions import CustomError

logging.basicConfig(
    level= logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

""" logging.debug("Log nivel debug")
logging.info("Log nivel info")
logging.warning("Log nivel warning")
logging.error("Log nivel error") """

# error


def function_error(n:int):
    if n<0:
        raise CustomError("Number less than 0")
    logging.info("El número es correcto")

try:
    function_error(-5)
except Exception as e:
    logging.error(e)
else:
    logging.info("Ejecución correcta")
finally:
    logging.info("Ejecución finalizada")
