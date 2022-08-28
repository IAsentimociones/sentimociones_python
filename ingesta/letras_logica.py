"""
Módulo letras_logica.py

Implementación de lógica de negocio para obtener letras de canciones de diferentes páginas web
"""
import urllib.parse
import requests
from bs4 import BeautifulSoup
import cancion_logica


def obtenerLetraConLyrics(nombre_cancion, nombre_autor):
    """
    Función que extrae la letra de una canción desde Lyrics 
    Argumentos:
        nombre_cancion: nombre de la cancion
        nombre_autor: nombre de autor o cantante
    Retorna: letra de la canción o vacío
    """
    
    WEB_LYRICS = "https://www.lyrics.com/lyrics/"
    letra_cancion = ''

    # codifica el nombre de la canción y el nombre del cantante como parámetro de URL
    cancion_code_url = urllib.parse.quote(nombre_cancion)
    cantante_code_url = urllib.parse.quote(nombre_autor)

    # prepara URL de Lyrics para buscar letras por cancion y autor
    cancion_autor_code_url = urllib.parse.quote(cancion_code_url + ' ' + cantante_code_url)
    url_busqueda_lyrics = '%s%s' % (WEB_LYRICS, cancion_autor_code_url) 
    print('URL búsqueda en Lyrics: ', url_busqueda_lyrics)

    # obtiene del contenido web la letra de la canción
    page = requests.get(url_busqueda_lyrics)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content-body")
    job_elements = results.find_all("div", class_="sec-lyric clearfix")
    
    # obtiene elementos del autor, cancion y enlace donde está la letra de la canción
    url_letra_cancion = ''
    for job_element in job_elements:
        cancion_elem = job_element.find("p", class_="lyric-meta-title")
        autor_elem = job_element.find("p", class_="lyric-meta-album-artist")
        
        if autor_elem == None:
            autor_lyrics = ''
        else:
            autor_lyrics = autor_elem.text

        cancion_lyrics = cancion_elem.text
        ref = job_element.find("pre", class_="lyric-body")

        print("cancion lyrics: ", cancion_lyrics)
        print("autor lyrics: ", autor_lyrics)
        print("url letra lyrics: ", ref.attrs['onclick'])
        print("cancion bdd: " + nombre_cancion)
        print("autor bdd: " + nombre_autor)
        print('-----------------')

        # valida autor y canción para obtener el enlace a la letra de la canción
        if cancion_lyrics.casefold() == nombre_cancion.casefold() and autor_lyrics.casefold() == nombre_autor.casefold():
            url_letra_cancion =  ref.attrs['onclick']
            print (url_letra_cancion)
        
    if url_letra_cancion != '':
        print ('referencia url letra canción: ', url_letra_cancion)
        url_letra_cancion = url_letra_cancion.split('=')[1].replace('\'','')
        print ('url letra canción: ', url_letra_cancion)
        
        # obtiene contenido de la página web de la letra de la canción
        page_letra_cancion = requests.get(url_letra_cancion)
        soup_letra_cancion = BeautifulSoup(page_letra_cancion.content, "html.parser")

        # obtiene el cuerpo del contenido web de la letra de la canción
        results_letra_cancion = soup_letra_cancion.find(id="content-body")
        job_elements_letra = results_letra_cancion.find_all("div", class_="lyric clearfix")
        for job_element in job_elements_letra:
            letra = job_element.find("pre", id="lyric-body-text")
        letra_cancion = letra.text

    return letra_cancion
