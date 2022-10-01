"""
Módulo archivo.py

Funciones comunes para tratamiento de archivos
"""
def leer_datos(file):
    """
    Función que permite leer datos de un archivo
    Argumentos:
        archivo: nombre del archivo
    Retorna: datos del archivo
    """
    datos = []
    with open(file, 'r')as f:
        for linea in f:
            linea = linea.strip()
            etiqueta = ' '.join(linea[1:linea.find("]")].strip().split())
            texto = linea[linea.find("]")+1:].strip()
            datos.append([etiqueta, texto])
    return datos