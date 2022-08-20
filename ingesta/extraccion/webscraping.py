"""
Módulo webscraping.py

Implementa estrategias de webscraping para la extracción de información de una página web
"""
import requests
from bs4 import BeautifulSoup
import numpy as np

def obtenerContenido(url):
    """
    Función que obtiene el contenido general de una página Web
    Argumentos:
        url: dirección de la página web que se desea obtener su contenido
    Retorna: contenido del la página web
    """
    pagina = requests.get(url)
    contenido = BeautifulSoup(pagina.content, "html.parser")
       
    return contenido

def obtenerElementos(url, contenedor, divPrincipal, elementosExtraer):
    """
    Función que obtiene los valores de los elementos que contienen una página Web
    Argumentos:
        url: dirección de la página web que se desea obtener su contenido
        contenedor: id del contenedor principal HTML
        divPrincipal: class del div que contiene los elementos a extraer
        elementosExtraer: nombre del componente y class del elemento que se desea extraer
    Retorna: Valores de los elementos de una página web
    """
    elementos = []
    contenido = obtenerContenido(url)
    resultados = contenido.find(id=contenedor)
    elementos_div = resultados.find_all("div", class_=divPrincipal)
    for elemento_div in elementos_div:
        valoresHtml = []
        for elemento_extraer in elementosExtraer:
            elementoHtml, classHtml = elemento_extraer
            valor = elemento_div.find(elementoHtml, class_=classHtml)
            valoresHtml.append(valor.text.strip())
        elementos.append(valoresHtml)
    return elementos
