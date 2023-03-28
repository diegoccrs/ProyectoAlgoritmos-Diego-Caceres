import os, sys
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
import json
from Constructor import Constructor
from Circuito import Circuito
from Carrera import Carrera
from Piloto import Piloto

def obtener_pilotos_api():
    '''
    Obtiene los pilotos de la api y los guarda en un archivo

    :return: lista de objetos de la clase Piloto
    '''
    url = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json'
    response = requests.get(url)
    pilotos_api = json.loads(response.text)

    # esta seccion guarda los constructores en una lista de objetos
    pilotos_obtenidos = []
    for piloto in pilotos_api:
        pilotos_obtenidos.append(Piloto(piloto['firstName'], piloto['lastName'], piloto['dateOfBirth'], piloto['nationality'], piloto['team'], piloto['permanentNumber'], 0))

    # esta seccion revisa si el archivo existe para borrarlo
    if os.path.exists(os.path.join(sys.path[0], 'pilotos.txt')):
        os.remove(os.path.join(sys.path[0], 'pilotos.txt'))

    # esta seccion guarda los equipos en el archivo
    for piloto in pilotos_obtenidos:
        with open(os.path.join(sys.path[0], 'pilotos.txt'), 'a', encoding='utf-8') as archivo:
            archivo.write(f"{str(piloto)}\n")

    return pilotos_obtenidos

def obtener_pilotos_archivo():
    '''
    Obtiene los pilotos del archivo y los guarda en una lista

    :return: lista de objetos de la clase Piloto
    '''
    # esta seccion revisa si el archivo no existe y obtiene los pilotos de la api
    if not os.path.exists(os.path.join(sys.path[0], 'pilotos.txt')):
        obtener_pilotos_api()

    # esta seccion guarda los pilotos en una lista de objetos
    pilotos_obtenidos = []
    with open(os.path.join(sys.path[0], 'pilotos.txt'), 'r', encoding='utf-8') as archivo:
        pilotos = archivo.readlines()

    for piloto in pilotos:
        piloto = piloto.rstrip()
        split = piloto.split(';')
        pilotos_obtenidos.append(Piloto(split[0], split[1], split[2], split[3], split[4], split[5], split[6]))

    return pilotos_obtenidos

def obtener_constructores_api():
    '''
    Obtiene los constructores de la api y los guarda en un archivo

    :return: lista de objetos de la clase Constructor
    '''
    url = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json'
    response = requests.get(url)
    constructores_api = json.loads(response.text)

    # esta seccion guarda los constructores en una lista de objetos
    constructores_obtenidos = []
    for constructor in constructores_api:
        constructores_obtenidos.append(Constructor(constructor['name'], constructor['id'], constructor['nationality'], [], 0))

    # esta seccion obtiene los pilotos correspondientes a cada constructor
    pilotos = obtener_pilotos_archivo()
    for piloto in pilotos:
        for constructor in constructores_obtenidos:
            if piloto.equipo == constructor.id_equipo:
                constructor.pilotos.append(piloto.nombre + ' ' + piloto.apellido)

    # esta seccion revisa si el archivo existe para borrarlo
    if os.path.exists(os.path.join(sys.path[0], 'constructores.txt')):
        os.remove(os.path.join(sys.path[0], 'constructores.txt'))

    # esta seccion guarda los equipos en el archivo
    for constructor in constructores_obtenidos:
        with open(os.path.join(sys.path[0], 'constructores.txt'), 'a', encoding='utf-8') as archivo:
            archivo.write(f"{str(constructor)}\n")

    return constructores_obtenidos

def obtener_constructores_archivo():
    '''
    Obtiene los constructores del archivo y los guarda en una lista

    :return: lista de objetos de la clase Constructor
    '''
    # esta seccion revisa si el archivo no existe y obtiene los constructores de la api
    if not os.path.exists(os.path.join(sys.path[0], 'constructores.txt')):
        obtener_constructores_api()

    # esta seccion guarda los constructores en una lista de objetos
    constructores_obtenidos = []
    with open(os.path.join(sys.path[0], 'constructores.txt'), 'r', encoding='utf-8') as archivo:
        constructores = archivo.readlines()

    for constructor in constructores:
        constructor = constructor.rstrip()
        split = constructor.split(';')
        constructores_obtenidos.append(Constructor(split[0], split[1], split[2], split[3], split[4]))

    return constructores_obtenidos

def crear_mapa_circuito(filas_general, columnas_general, filas_vip, columnas_vip):
    '''
    Crea un mapa con la capacidad del circuito

    :param filas_general: cantidad de filas de la zona general
    :param columnas_general: cantidad de columnas de la zona general
    :param filas_vip: cantidad de filas de la zona vip
    :param columnas_vip: cantidad de columnas de la zona vip

    :return: mapa del estadio
    '''

    # esta seccion crea el mapa del estadio con las filas de cada zona
    mapa_circuito = []
    for i in range(filas_general):
        mapa_circuito.append(['G'] * columnas_general)
    for i in range(filas_vip):
        mapa_circuito.append(['V'] * columnas_vip)

    return mapa_circuito

def obtener_carreras_api():
    '''
    Obtiene las carreras, circuitos y restaurantes de la api y los guarda en un archivo

    :return: lista de objetos de la clase Carrera, lista de objetos de la clase Circuito y lista de objetos de la clase Restaurante
    '''
    url = 'https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
    response = requests.get(url)
    carreras_api = json.loads(response.text)

    # esta seccion guarda las carreras en una lista de objetos
    carreras_obtenidas = []
    mapas = []
    circuitos_obtenidos = []
    restaurantes_obtenidos = []
    for carrera in carreras_api:
        carreras_obtenidas.append(Carrera(carrera['name'], carrera['round'], carrera['date'], carrera['circuit']["name"], []))
    
        # esta seccion crea el mapa de cada circuito
        filas_general = carrera['map']['general'][0]
        columnas_general = carrera['map']['general'][1]
        filas_vip = carrera['map']['vip'][0]
        columnas_vip = carrera['map']['vip'][1]
        mapa = crear_mapa_circuito(filas_general, columnas_general, filas_vip, columnas_vip)
        mapas.append(mapa)

        # esta seccion guarda los circuitos en una lista de objetos
        circuitos_obtenidos.append(Circuito(carrera['circuit']["name"], carrera['circuit']['location']['country'], carrera['circuit']['location']['locality'], carrera['circuit']['location']['lat'], carrera['circuit']['location']['long']))

        # esta seccion guarda los restaurantes de cada carrera en una lista de objetos
        restaurantes_obtenidos.append(carrera['restaurants'])

    # esta seccion revisa si el archivo existe para borrarlo
    if os.path.exists(os.path.join(sys.path[0], 'mapas.txt')):
        os.remove(os.path.join(sys.path[0], 'mapas.txt'))

    # esta seccion guarda  los mapas en el archivo
    for mapa in mapas:
        with open(os.path.join(sys.path[0], 'mapas.txt'), 'a', encoding='utf-8') as archivo:
            archivo.write(f"{mapa}\n")
    
    # esta seccion si el archivo existe para borrarlo
    if os.path.exists(os.path.join(sys.path[0], 'carreras.txt')):
        os.remove(os.path.join(sys.path[0], 'carreras.txt'))

    # esta seccion guarda los estadios en el archivo
    for carrera in carreras_obtenidas:
        with open(os.path.join(sys.path[0], 'carreras.txt'), 'a', encoding='utf-8') as archivo:
            archivo.write(f"{str(carrera)}\n")

    # esta seccion revisa si el archivo existe para borrarlo
    if os.path.exists(os.path.join(sys.path[0], 'circuitos.txt')):
        os.remove(os.path.join(sys.path[0], 'circuitos.txt'))

    # esta seccion guarda los circuitos en el archivo
    for circuito in circuitos_obtenidos:
        with open(os.path.join(sys.path[0], 'circuitos.txt'), 'a', encoding='utf-8') as archivo:
            archivo.write(f"{str(circuito)}\n")

    # esta seccion revisa si el archivo existe para borrarlo
    if os.path.exists(os.path.join(sys.path[0], 'restaurantes.txt')):
        os.remove(os.path.join(sys.path[0], 'restaurantes.txt'))

    # esta seccion guarda los restaurantes en el archivo
    for restaurante in restaurantes_obtenidos:
        with open(os.path.join(sys.path[0], 'restaurantes.txt'), 'a', encoding='utf-8') as archivo:
            archivo.write(f"{str(restaurante)}\n")

    # esta seccion revisa si el archivo existe para borrarlo
    if os.path.exists(os.path.join(sys.path[0], 'boletos.txt')):
        os.remove(os.path.join(sys.path[0], 'boletos.txt'))

    # esta seccion crea el archivo de boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'a', encoding='utf-8') as archivo:
        archivo.write('')

    return carreras_obtenidas

def obtener_carreras_archivo():
    '''
    Obtiene las carreras del archivo y los guarda en una lista

    :return: lista de objetos de la clase Carrera
    '''
    # esta seccion guarda las carreras en una lista de objetos
    carreras_obtenidas = []
    with open(os.path.join(sys.path[0], 'carreras.txt'), 'r', encoding='utf-8') as archivo:
        carreras = archivo.readlines()

    for carrera in carreras:
        carrera = carrera.rstrip()
        split = carrera.split(';')
        carreras_obtenidas.append(Carrera(split[0], split[1], split[2], split[3], split[4]))

    return carreras_obtenidas

def obtener_circuitos_archivo():
    '''
    Obtiene los circuitos del archivo y los guarda en una lista

    :return: lista de objetos de la clase Circuito
    '''
    # esta seccion guarda los circuitos en una lista de objetos
    circuitos_obtenidos = []
    with open(os.path.join(sys.path[0], 'circuitos.txt'), 'r', encoding='utf-8') as archivo:
        circuitos = archivo.readlines()

    for circuito in circuitos:
        circuito = circuito.rstrip()
        split = circuito.split(';')
        circuitos_obtenidos.append(Circuito(split[0], split[1], split[2], split[3], split[4]))

    return circuitos_obtenidos

def obtener_constructores_por_pais(constructores):
    '''
    Obtiene los constructores de una nacionalidad

    :param constructores: lista de objetos de la clase Constructor
    '''

    # esta seccion muestra las nacionalidades
    print('Nacionalidades disponibles:')
    nacionalidades = []
    for constructor in constructores:
        if constructor.nacionalidad not in nacionalidades:
            nacionalidades.append(constructor.nacionalidad)
            print(constructor.nacionalidad)

    # esta seccion obtiene la nacionalidad
    print()
    nacionalidad = input('Ingrese la nacionalidad a buscar: ')
    print()
    nacionalidad = nacionalidad.lower()

    # esta seccion busca los constructores con esa nacionalidad
    constructores_encontrados = []
    for constructor in constructores:
        # esta seccion revisa si la nacionalidad existe y busca los constructores
        if nacionalidad == constructor.nacionalidad.lower():
            constructores_encontrados.append(constructor.nombre)

    # esta seccion imprime los constructores encontrados
    if len(constructores_encontrados) > 0:
        print('Constructores encontrados:')
        for constructor in constructores_encontrados:
            print(constructor)
    else:
        print('No se encontraron constructores con esa nacionalidad')

def obtener_pilotos_por_constructor(pilotos):
    '''
    Obtiene los pilotos de un constructor

    :param pilotos: lista de objetos de la clase Piloto
    '''
    # esta seccion muestra los constructores
    print('Constructores disponibles:')
    constructores = []
    for piloto in pilotos:
        if piloto.equipo not in constructores:
            constructores.append(piloto.equipo)
            print(piloto.equipo)

    # esta seccion obtiene el constructor
    print()
    constructor = input('Ingrese el constructor a buscar: ')
    print()
    constructor = constructor.lower()

    # esta seccion busca los pilotos con ese constructor
    pilotos_encontrados = []
    for piloto in pilotos:
        # esta seccion revisa si el constructor existe y busca los pilotos
        if constructor == piloto.equipo.lower():
            pilotos_encontrados.append(piloto.nombre + ' ' + piloto.apellido)

    # esta seccion imprime los pilotos encontrados
    if len(pilotos_encontrados) > 0:
        print('Pilotos encontrados:')
        for piloto in pilotos_encontrados:
            print(piloto)
    else:
        print('No se encontraron pilotos con ese constructor')

def obtener_carreras_por_pais_circuito(carreras, circuitos):
    '''
    Obtiene las carreras de un pais

    :param carreras: lista de objetos de la clase Carrera
    :param circuitos: lista de objetos de la clase Circuito
    '''
    # esta seccion muestra los paises
    print('Paises disponibles:')
    paises = []
    for circuito in circuitos:
        if circuito.pais not in paises:
            paises.append(circuito.pais)
            print(circuito.pais)

    # esta seccion obtiene el pais
    print()
    pais = input('Ingrese el pais a buscar: ')
    print()
    pais = pais.lower()

    # esta seccion busca los circuitos con ese pais
    circuitos_encontrados = []
    for circuito in circuitos:
        # esta seccion revisa si el pais existe y busca los circuitos
        if pais == circuito.pais.lower():
            circuitos_encontrados.append(circuito.nombre)

    # esta seccion busca las carreras con esos circuitos
    carreras_encontradas = []
    for carrera in carreras:
        # esta seccion revisa si el circuito existe y busca las carreras
        if carrera.circuito in circuitos_encontrados:
            carreras_encontradas.append(carrera.nombre)

    # esta seccion imprime las carreras encontradas
    if len(carreras_encontradas) > 0:
        print('Carreras encontradas:')
        for carrera in carreras_encontradas:
            print(carrera)
    else:
        print('No se encontraron carreras en ese pais')

def obtener_carreras_en_un_mes(carreras):
    '''
    Obtiene las carreras de un mes

    :param carreras: lista de objetos de la clase Carrera
    '''
    # esta seccion obtiene el mes
    print()
    mes = input('Ingrese el mes a buscar (Ej: 04): ')
    print()
    mes = mes.lower()

    # esta seccion busca las carreras con ese mes
    carreras_encontradas = []
    for carrera in carreras:
        # esta seccion revisa si el mes existe y busca las carreras
        if mes == carrera.fecha_carrera.split('-')[1].lower():
            carreras_encontradas.append(carrera.nombre)

    # esta seccion imprime las carreras encontradas
    if len(carreras_encontradas) > 0:
        print('Carreras encontradas:')
        for carrera in carreras_encontradas:
            print(carrera)
    else:
        print('No se encontraron carreras en ese mes')

def finalizar_carrera_funcion(carreras, pilotos, constructores):
    '''
    Finaliza una carrera

    :param carreras: lista de objetos de la clase Carrera
    :param pilotos: lista de objetos de la clase Piloto
    :param constructores: lista de objetos de la clase Constructor
    '''
    # esta seccion muestra las carreras que aun no tienen podio
    print('Carreras disponibles:')
    for carrera in carreras:
        if carrera.podium == '[]':
            print(carrera.nombre)

    # esta seccion busca la carrera
    carrera_encontrada = False
    while not carrera_encontrada:
        carrera = input('Ingrese el nombre de la carrera a finalizar: ')
        carrera = carrera.lower()

        # esta seccion busca la carrera
        for carrera_objeto in carreras:
            if carrera_objeto.nombre.lower() == carrera:
                carrera_encontrada = True
                carrera_objeto.finalizar_carrera(pilotos)
                break

        if not carrera_encontrada:
            print('Carrera no encontrada')

    # cargamos la lista de pilotos actualizada
    pilotos = obtener_pilotos_archivo()

    # esta seccion suma los puntos de los pilotos a los constructores
    for piloto in pilotos:
        for constructor in constructores:
            if piloto.equipo == constructor.id_equipo:
                constructor.puntos = int(constructor.puntos)
                constructor.puntos += int(piloto.puntos)
                break

    # esta seccion actualiza el archivo de carreras
    with open(os.path.join(sys.path[0], 'carreras.txt'), 'w', encoding='utf-8') as archivo:
        for carrera in carreras:
            archivo.write(f"{str(carrera)}\n")

    # esta seccion actualiza el archivo de constructores
    with open(os.path.join(sys.path[0], 'constructores.txt'), 'w', encoding='utf-8') as archivo:
        for constructor in constructores:
            archivo.write(f"{str(constructor)}\n")