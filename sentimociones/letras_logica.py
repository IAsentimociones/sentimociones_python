"""
Módulo letras_logica.py

Implementación de lógica de negocio para obtener letras de canciones de diferentes páginas web
"""
import urllib.parse
import requests
from bs4 import BeautifulSoup
import cancion_logica
from comun import cadena


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
    cancion_code_url = urllib.parse.quote(cadena.prepararCadena(nombre_cancion))
    cantante_code_url = urllib.parse.quote(cadena.prepararCadena(nombre_autor))
    print('------------------')
    print('cancion: ', cancion_code_url)
    print('cantante: ', cantante_code_url)

    # prepara URL de Lyrics para buscar letras por cancion y autor
    cancion_autor_code_url = cancion_code_url + '%20' + cantante_code_url 
    #urllib.parse.quote(cancion_code_url + ' ' + cantante_code_url)
    url_busqueda_lyrics = '%s%s' % (WEB_LYRICS, cancion_autor_code_url) 
    print('URL búsqueda en Lyrics: ', url_busqueda_lyrics)
    print('------------------')

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
        
        # valida autor y canción para obtener el enlace a la letra de la canción
        if ((cadena.contieneCadena(cancion_lyrics, nombre_cancion) and cadena.contieneCadena(autor_lyrics, nombre_autor)) 
            or (cadena.contieneCadena(nombre_cancion, cancion_lyrics) and cadena.contieneCadena(nombre_autor, autor_lyrics))):
            url_letra_cancion =  ref.attrs['onclick']
            print ('coinciden autor y cancion. Url de letra: ', url_letra_cancion)
            break
        else:
            print('autor y canción no coinciden')
            print('-----------------')

        
    if url_letra_cancion == '':
        print('No se pudo determinar la URL de la canción')
        print('-----------------')
    else:
        print ('referencia url letra canción: ', url_letra_cancion)
        url_letra_cancion = url_letra_cancion.split('=')[1].replace('\'','')
        print ('url letra canción: ', url_letra_cancion)
        print('-----------------')

        
        # obtiene contenido de la página web de la letra de la canción
        page_letra_cancion = requests.get(url_letra_cancion)
        soup_letra_cancion = BeautifulSoup(page_letra_cancion.content, "html.parser")

        # obtiene el cuerpo del contenido web de la letra de la canción
        results_letra_cancion = soup_letra_cancion.find(id="content-body")
        job_elements_letra = results_letra_cancion.find_all("div", class_="lyric clearfix")
        for job_element in job_elements_letra:
            letra = job_element.find("pre", id="lyric-body-text")
        if (hasattr(letra_cancion, 'text')):
            letra_cancion = letra.text

    return letra_cancion

def obtenerLetraConLetras4u(nombre_cancion, nombre_autor):
    """
    Función que extrae la letra de una canción desde letras4u.com 
    Argumentos:
        nombre_cancion: nombre de la cancion
        nombre_autor: nombre de autor o cantante
    Retorna: letra de la canción o vacío
    """
    
    WEB_LETRAS4U = "https://www.letras4u.com/buscar.php?letrade="
    SUBMIT_BUSCAR = '&Submit=Buscar'
    letra_cancion = ''

    # codifica el nombre de la canción y el nombre del cantante como parámetro de URL
    cancion_param_url = cadena.prepararCadena(nombre_cancion).replace(' ', '+').replace('++', '+')
    cantante_param_url = cadena.prepararCadena(nombre_autor).replace(' ', '+').replace('++', '+')
    print('------------------')
    print('cancion: ', cancion_param_url)
    print('cantante: ', cantante_param_url)

    # prepara URL de Lyrics para buscar letras por cancion y autor
    cancion_autor_code_url = cancion_param_url + '+' + cantante_param_url
    url_busqueda_letras4u = '%s%s%s' % (WEB_LETRAS4U, cancion_autor_code_url, SUBMIT_BUSCAR) 
    print('URL búsqueda en Letras4u: ', url_busqueda_letras4u)
    print('------------------')

    # Obtiene el contenido web del resultado de búsqueda
    page_letra4u = requests.get(url_busqueda_letras4u)
    conten_letra4u = BeautifulSoup(page_letra4u.content, "html.parser")

    # Obtiene el contenido del div principal donde está el resultado de búsqueda de letras4u
    div_main = conten_letra4u.find(id="main")

    #obtiene los tipo span donde están los resultados
    elementos_span = div_main.find_all("span")

    # obtiene por cada elemento del resultado de búsquea la canción-autor para validar el enlace de la letra de la canción
    url_letra_cancion = ''
    for span in elementos_span:
        link_cancion_autor = span.find("a")
        if (hasattr(link_cancion_autor, 'text')):
            cancion_autor = link_cancion_autor.text
            link_letra = link_cancion_autor.get("href")  
            print('cancion autor: ', cancion_autor)
            print('link letra: ', link_letra)
            # valida autor y canción para obtener el enlace a la letra de la canción
            if cadena.contieneCadena(nombre_cancion, cancion_autor) and cadena.contieneCadena(nombre_autor, cancion_autor):
                url_letra_cancion =  link_letra
                print ('coinciden autor y cancion. Url de letra: ', url_letra_cancion)
                break
            else:
                print('autor y canción no coinciden')
                print('-----------------')
    
    # obtiene letra de canción
    if url_letra_cancion == '':
        print('No se pudo determinar la URL de la canción')
        print('-----------------')
    else:
        print ('url letra canción: ', url_letra_cancion)
        print('-----------------')
        
        # obtiene contenido de la página web de la letra de la canción
        page_letra_cancion = requests.get(url_letra_cancion)
        contenido_letra_cancion = BeautifulSoup(page_letra_cancion.content, "html.parser")

        # obtiene el div principal donde está la letra de la canción
        div_container = contenido_letra_cancion.find("div", class_="grid-container")

        # obtiene el elemento table donde está la letra
        table_elments = div_container.find_all("table")

        for table in table_elments:
            letra = table.find("td")
            if (hasattr(letra, 'text')):
                letra_cancion = letra_cancion + letra.text.replace('\n\n\n', '')    

    return letra_cancion

def obtenerLetraConYaLetras(nombre_cancion, nombre_autor):
    """
    Función que extrae la letra de una canción desde YaLetras.com 
    Argumentos:
        nombre_cancion: nombre de la cancion
        nombre_autor: nombre de autor o cantante
    Retorna: letra de la canción o vacío
    """
    
    WEB_YALETRAS = "https://www.yaletras.com/search?q="
    letra_cancion = ''

    # codifica el nombre de la canción y el nombre del cantante como parámetro de URL
    cancion_param_url = cadena.prepararCadena(nombre_cancion).replace(' ', '+').replace('++', '+')
    #cantante_param_url = cadena.prepararCadena(nombre_autor).replace(' ', '+').replace('++', '+')
    # prepara nombre del cantante para mejorar la búsqueda
    cantante_param_url = cadena.cadenaCorta(nombre_autor)
    print('------------------')
    print('cancion: ', cancion_param_url)
    print('cantante: ', cantante_param_url)

    # prepara URL de Lyrics para buscar letras por cancion y autor
    cancion_autor_code_url = cancion_param_url + '+' + cantante_param_url
    url_busqueda_letras4u = '%s%s' % (WEB_YALETRAS, cancion_autor_code_url) 
    print('URL búsqueda en yaletras.com: ', url_busqueda_letras4u)
    print('------------------')

    # Obtiene el contenido web del resultado de búsqueda
    page_yaletras = requests.get(url_busqueda_letras4u)
    conten_yaletras = BeautifulSoup(page_yaletras.content, "html.parser")

    # Obtiene el contenido del div principal donde está el resultado de búsqueda de letras4u
    page_body = conten_yaletras.find(id="page_body")

    #obtiene los tipo articles del contenido blog
    articulos_blog = page_body.find_all("article")

    # obtiene por cada sección de artículos el div principal, contenedor H3 y enlace a
    url_letra_cancion = ''
    for article in articulos_blog:
        div_contenedor = article.find("div", class_="post-title-container")
        h3 = div_contenedor.find("h3")
        a = h3.find("a")
        if (hasattr(a, 'text')):
            cancion_autor = a.text.replace('\n', '')
            link_letra = a.get("href") 
            print('cancion autor: ', cancion_autor)
            print('link letra: ', link_letra)

            # valida autor y canción para obtener el enlace a la letra de la canción
            if cadena.contieneCadena(nombre_cancion, cancion_autor) and cadena.contieneCadena(cantante_param_url, cancion_autor):
                url_letra_cancion =  link_letra
                print ('coinciden autor y cancion. Url de letra: ', url_letra_cancion)
                break
            else:
                print('autor y canción no coinciden')
                print('-----------------')

    # obtiene letra de canción
    if url_letra_cancion == '':
        print('No se pudo determinar la URL de la canción')
        print('-----------------')
    else:
        print ('url letra canción: ', url_letra_cancion)
        print('-----------------')

        # obtiene contenido de la página web de la letra de la canción
        page_letra_cancion = requests.get(url_letra_cancion)
        contenido_letra_cancion = BeautifulSoup(page_letra_cancion.content, "html.parser")

        # obtiene el div principal donde está la letra de la canción
        div_body = contenido_letra_cancion.find("div", class_="post-body")

        # obtiene el div contenedor de la letra de la canción
        divs_style = div_body.find('div', attrs={'style': 'text-align: center;'})
        for div in divs_style:
            if (hasattr(div, 'text')):
                letra_cancion = letra_cancion + div.text + ' '

    return letra_cancion

def obtenerLetraConCancioneros(nombre_cancion, nombre_autor):
    """
    Función que extrae la letra de una canción desde cancioneros.com 
    Argumentos:
        nombre_cancion: nombre de la cancion
        nombre_autor: nombre de autor o cantante
    Retorna: letra de la canción o vacío
    """
    WEB_CANCIONEROS = "https://www.cancioneros.com/letras/buscar.php?CT="
    letra_cancion = ''

    # codifica el nombre de la canción y el nombre del cantante como parámetro de URL
    cancion_param_url = cadena.prepararCadena(nombre_cancion).replace(' ', '+').replace('++', '+')
    cantante_param_url = cadena.prepararCadena(nombre_autor).replace(' ', '+').replace('++', '+')
    print('------------------')
    print('cancion: ', cancion_param_url)
    print('cantante: ', cantante_param_url)

    # prepara URL de Lyrics para buscar letras por cancion y autor
    cancion_autor_code_url = cancion_param_url + '+' + cantante_param_url
    url_busqueda_cancioneros = '%s%s' % (WEB_CANCIONEROS, cancion_autor_code_url) 
    print('URL búsqueda en cancioneros.com: ', url_busqueda_cancioneros)
    print('------------------')

    # Obtiene el contenido web del resultado de búsqueda
    page = requests.get(url_busqueda_cancioneros)
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtiene el contenido del div principal donde está el resultado de búsqueda de letras4u
    div_caixa = soup.findAll("div", class_="caixa_cerca")
    ul_lista_can = soup.findAll("ul", class_="llista_can")
    a_lista = soup.findAll("a")

    url_letra_cancion = ''
    for a in a_lista:
        cancion_a = a.find("div", class_="llista_titol")
        autor_a = a.find("div", class_="llista_artista")
        url_letra_a = a.get("href") 
        if cancion_a != None and autor_a != None:
            # valida autor y canción para obtener el enlace a la letra de la canción
            print('nombre_cancion ', nombre_cancion)
            print('cancion_a.text ', cancion_a.text)
            if cadena.contieneCadena(nombre_cancion, cancion_a.text) or cadena.contieneCadena(cancion_a.text, nombre_cancion):
                url_letra_cancion =  url_letra_a
                print ('coinciden autor y cancion. Url de letra: ', url_letra_cancion)
                break
            else:
                print('autor y canción no coinciden')
                print('-----------------')
    # obtiene letra de canción
    if url_letra_cancion == '':
        print('No se pudo determinar la URL de la canción')
        print('-----------------')
    else:
        print ('url letra canción: ', url_letra_cancion)
        print('-----------------')

        url_letra_cancion = 'https://www.cancioneros.com/letras/' + url_letra_cancion
        page_letra_cancion = requests.get(url_letra_cancion)
        soup_letra_cancion = BeautifulSoup(page_letra_cancion.content, "html.parser")

        # obtiene el cuerpo del contenido web de la letra de la canción
        results_letra_cancion = soup_letra_cancion.find("div", class_="inner")
        p_letras = soup_letra_cancion.find("p", class_="lletra_can")
        for p in p_letras:
            if (hasattr(p, 'text')):
                letra_cancion = letra_cancion + p.text

    return letra_cancion

def obtenerLetraConGoogle(nombre_cancion, nombre_autor):
    """
    Función que extrae la letra de una canción desde google.com 
    Argumentos:
        nombre_cancion: nombre de la cancion
        nombre_autor: nombre de autor o cantante
    Retorna: letra de la canción o vacío
    """
    WEB_GOOGLE = "https://www.google.com/search?q=letra+"
    letra_cancion = ''

    # codifica el nombre de la canción y el nombre del cantante como parámetro de URL
    cancion_param_url = cadena.prepararCadena(nombre_cancion).replace(' ', '+').replace('++', '+')
    cantante_param_url = cadena.prepararCadena(nombre_autor).replace(' ', '+').replace('++', '+')
    print('------------------')
    print('cancion: ', cancion_param_url)
    print('cantante: ', cantante_param_url)

    # prepara URL de Lyrics para buscar letras por cancion y autor
    cancion_autor_code_url = cancion_param_url + '+' + cantante_param_url
    url_busqueda_google = '%s%s' % (WEB_GOOGLE, cancion_autor_code_url) 
    print('URL búsqueda en cancioneros.com: ', url_busqueda_google)
    print('------------------')

    page = requests.get(url_busqueda_google)
    soup = BeautifulSoup(page.content, "html.parser")

    # obtiene todas las referencias con letras de canciones
    a_main = soup.findAll("a")
    url_letra_cancion = ''
    for a in a_main:
        href = a.get("href") 
        if cadena.contieneCadena('https', href) and cadena.contieneCadena('letra', href) and not cadena.contieneCadena('google', href) and cadena.contieneCadena(cadena.cadenaCorta(nombre_cancion), href) and cadena.contieneCadena(cadena.cadenaCorta(nombre_autor), href):
            url_letra_cancion = href.replace('/url?q=', '')
            print ('coinciden autor y cancion. Url de letra: ', url_letra_cancion)
            break

    if url_letra_cancion == '':
        print('No se pudo determinar la URL de la canción')
        print('-----------------')
    else:
        url_letra_simple =  url_letra_cancion.split('&')
        print ('url letra canción: ', url_letra_simple[0])
        print('-----------------')

        es_letrassingle_es = cadena.contieneCadena('www.letraseningles.es', url_letra_simple[0])
        es_letras_com = cadena.contieneCadena('www.letras.com', url_letra_simple[0])
        es_letras_boom = cadena.contieneCadena('www.letrasboom.com', url_letra_simple[0])

        page_letra_cancion = requests.get(url_letra_simple[0])
        soup_letra_cancion = BeautifulSoup(page_letra_cancion.content, "html.parser")
        if es_letrassingle_es or es_letras_com:
            p_main = soup_letra_cancion.find_all("p")
            aux = 0
            for p in p_main:
                if (es_letras_com):
                    spans = p.findAll("span")
                    if (not spans):
                        if hasattr(p, 'text'):
                            letra_cancion = letra_cancion + p.text + ' '
                    else:
                        for span in spans:
                            if hasattr(span, 'text'):
                                letra_cancion = letra_cancion + span.text + ' '
                elif (es_letrassingle_es):
                    if hasattr(p, 'text'):
                        if (cadena.contieneCadena(cadena.cadenaCorta(nombre_autor), p.text)):
                            aux = aux + 1
                        if (aux == 1):
                                letra_cancion = letra_cancion + p.text
        elif es_letras_boom:
            div_main = soup_letra_cancion.find("div", class_='lyricbody')
            p_main = div_main.find_all("p")
            letra_cancion = ''
            aux = 0
            for p in p_main:
                if hasattr(p, 'text'):
                    letra_cancion = letra_cancion + p.text + ' '
   
    return letra_cancion
