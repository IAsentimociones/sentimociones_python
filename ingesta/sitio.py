"""
Módulo sitio.py

Implementación de lógica de sitios web
"""
from bdd import mongoDB_cliente
from datetime import date

def insertarSitio(url, lista_canciones ):
    """
    Función que inserta una coleccion del sitio web
    Argumentos:
        url: dirección de la página o sitio web 
        lista_canciones: lista de canciones obtenida en ese sitio web
    Retorna: identificador principial del sitio web registrado en BDD
    """
    fecha_actual = date.today()
    coleccionSitio = {"url": url, "fecha_extraccion": fecha_actual.strftime("%d/%m/%Y"), "lista_canciones": lista_canciones}
    sitio_id = mongoDB_cliente.insertarDocumento("SITIOS", coleccionSitio)
       
    return sitio_id

