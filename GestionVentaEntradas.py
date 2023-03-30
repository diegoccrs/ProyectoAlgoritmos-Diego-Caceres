from Cliente import Cliente
from Boleto import Boleto
import random
import string
import os,sys
import ast

from GestionCarrerasEquipos import *

def obtener_datos_cliente(carreras):
    '''
    Obtiene los datos del cliente

    :param carreras: lista de carreras

    :return: cliente, circuito
    '''
    # esta seccion ingresa los datos del cliente con sus respectivas validaciones
    nombre = input('\nnombre: ')
    while not nombre.isalpha():
        print('Nombre no valido')
        nombre = input('\nnombre: ')
    apellido = input('\napellido: ')
    while not apellido.isalpha():
        print('Apellido no valido')
        apellido = input('\napellido: ')
    cedula = input('\ncedula: ')
    while not cedula.isdigit() or len(cedula) < 7 or len(cedula) > 8:
        print('Cedula no valida')
        cedula = input('\ncedula: ')
    edad = input('\nedad: ')
    while not edad.isdigit() or int(edad) < 0:
        print('Edad no valida')
        edad = input('\nedad: ')

    # esta seccion muestra las carreras
    print("\nCarreras:")
    print("-" * 110)
    print("{:<30} {:<20} {:<20} {:<20}".format("Nombre", "Ronda", "Fecha", "Circuito"))
    print("-" * 110)
    for i, carrera in enumerate(carreras):
        print("{:<30} {:<20} {:<20} {:<20}".format(carrera.nombre, carrera.numero_carrera, carrera.fecha_carrera, carrera.circuito))
    print("-" * 110)

    # esta seccion selecciona la carrera
    carrera = input('\nSeleccione la ronda: ')
    while not carrera.isdigit() or int(carrera) < 1 or int(carrera) > len(carreras):
        print('Carrera no valida')
        carrera = input('\nSeleccione la ronda: ')
    carrera = carreras[int(carrera)-1]
    circuito = carrera.circuito

    # esta seccion selecciona el tipo de entrada
    tipo_entrada = input('\nEscriba el tipo de entrada (General/VIP): ')
    while tipo_entrada.lower() != 'general' and tipo_entrada.lower() != 'vip':
        print('Tipo de entrada no valido')
        tipo_entrada = input('\nEscriba el tipo de entrada (General/VIP): ')
    tipo_entrada = tipo_entrada.lower()

    # esta seccion crea el cliente
    cliente = Cliente(nombre, apellido, cedula, edad, carrera, tipo_entrada)
    return cliente, circuito

def obtener_asiento(circuito, tipo_entrada):
    '''
    Obtiene el asiento del cliente

    :param circuito: nombre del circuito
    :param tipo_entrada: tipo de entrada

    :return: estado final de los mapas y la fila y columna del asiento
    '''
    # esta seccion muestra el mapa del circuito correspondiente leyendolo del archivo
    with open(os.path.join(sys.path[0], 'mapas.txt'), 'r') as archivo:
        mapas = archivo.readlines()

    circuitos = obtener_circuitos_archivo()

    # crear lista de mapas
    mapas = [mapa.strip() for mapa in mapas]
    mapas_2 = []
    for map in mapas:
        map = ast.literal_eval(map)
        mapas_2.append(map)

    # creamos una lista de los nombres de los circuitos
    circuitos_2 = []
    for circ in circuitos:
        circuitos_2.append(circ.nombre.lower())

    # obtenemos el index del circuito seleccionado
    idx_circuito = circuitos_2.index(circuito.lower())

    # esta seccion muestra el mapa del circuito correspondiente
    # revisamos la fila que tiene mas columnas
    max_columnas = 0
    for fila in mapas_2[idx_circuito]:
        if len(fila) > max_columnas:
            max_columnas = len(fila)

    # imprimimos los numeros de columnas
    for index in range(max_columnas):
        print(f'    {index+1}', end='')
    # imprimimos los numeros de filas y el mapa
    print()
    for index in range(len(mapas_2[idx_circuito])):
        print(f'{index+1}', end=' ')
        print(mapas_2[idx_circuito][index])

    while True:
        # esta seccion ingresa el asiento
        fila = input('\nEscriba la fila del asiento (numeros de la izquierda): ')
        while not fila.isdigit() or int(fila) < 1 or int(fila) > len(mapas_2[idx_circuito]):
            print('Fila no valida')
            fila = input('\nEscriba la fila del asiento (numeros de la izquierda): ')

        columna = input('\nEscriba la columna del asiento (numeros de arriba): ')
        while not columna.isdigit() or int(columna) < 1 or int(columna) > len(mapas_2[idx_circuito][int(fila)-1]):
            print('Columna no valida')
            columna = input('\nEscriba la columna del asiento (numeros de arriba): ')

        # esta seccion verifica que el asiento este disponible y corresponda al tipo de entrada del cliente
        asiento_seleccionado = mapas_2[idx_circuito][int(fila)-1][int(columna)-1]
        if asiento_seleccionado == 'X':
            print('Asiento no disponible')
        elif (tipo_entrada == 'general' and asiento_seleccionado != 'G') or (tipo_entrada == 'vip' and asiento_seleccionado != 'V'):
            print('El asiento no corresponde al tipo de entrada seleccionada')
        else:
            break


    # esta seccion cambia el asiento a ocupado
    mapas_2[idx_circuito][int(fila)-1][int(columna)-1] = 'X'

    return mapas_2, fila, columna
   
def es_ondulado(cedula):
    '''
    Verifica si el número de cédula es ondulado

    :param cedula: número de cédula

    :return: True si el número es ondulado, False si no lo es
    '''

    # convierte el número en una lista de dígitos y verifica si hay exactamente dos dígitos distintos en el número. Si no, retorna False
    digitos = [int(d) for d in str(cedula)]
    
    if len(set(digitos)) != 2:
        return False

    # recorre la lista de dígitos y verifica si los dígitos se alternan correctamente. Si no, retorna False
    for i in range(len(digitos)-2):
        if digitos[i] == digitos[i + 2]:
            continue
        else:
            return False

    # si se cumplen todas las condiciones, retorna True
    return True

def calcular_costo_entrada(cliente):
    '''
    Calcula el costo de la entrada

    :param cliente: diccionario con los datos del cliente

    :return: costo inicial de la entrada, descuento, iva y total
    '''
    # esta seccion calcula el costo de la entrada
    if cliente.tipo_entrada == 'general':
        costo_entrada = 150
    else:
        costo_entrada = 340

    # Verifica si la cédula es ondulada y aplica el descuento si es necesario
    if es_ondulado(cliente.cedula):
        descuento = 0.5
        costo_entrada *= (1 - descuento)
        print('Felicidades! Tu cédula es un número ondulado y tienes un 50% de descuento en tu entrada.')
    else:
        descuento = 0

    # esta seccion calcula el iva
    iva = costo_entrada * 0.16

    # esta seccion calcula el total
    total = costo_entrada + iva

    return costo_entrada, descuento, iva, total

def crear_compra(carreras):
    '''
    Crea una compra

    :param partidos: lista con los partidos
    '''
    # esta seccion obtiene los datos del cliente
    cliente, circuito = obtener_datos_cliente(carreras)

    # esta seccion obtiene el asiento
    mapas, fila, columna = obtener_asiento(circuito, cliente.tipo_entrada)
    asiento = f'{fila}-{columna}'

    # esta seccion calcula el costo de la entrada
    costo_entrada, descuento, iva, total = calcular_costo_entrada(cliente)

    # esta seccion genera un codigo unico del boleto
    letras = string.ascii_lowercase
    codigo = ''.join(random.choice(letras) for i in range(6))

    # esta seccion crea el boleto
    boleto = Boleto(codigo, asiento, total, cliente)

    # esta seccion muestra la compra
    print()
    print('Compra:')
    print(f'Nombre: {cliente.nombre}')
    print(f'Apellido: {cliente.apellido}')
    print(f'Cedula: {cliente.cedula}')
    print(f'Edad: {cliente.edad}')
    print(f'Circuito: {circuito}')
    print(f'Tipo de entrada: {cliente.tipo_entrada}')
    print(f'Asiento: {boleto.asiento}')
    print(f'Subtotal: {costo_entrada}')
    print(f'Descuento: {descuento}')
    print(f'IVA: {iva}')
    print(f'Total: {total}')
    print()

    # esta seccion confirma la compra
    confirmacion = input('Confirmar compra (s/n): ')
    while confirmacion.lower() != 's' and confirmacion.lower() != 'n':
        print('Opcion no valida')
        confirmacion = input('Confirmar compra (s/n): ')
    confirmacion = confirmacion.lower()

    if confirmacion == 's':
        # esta seccion guarda el mapa en el archivo
        with open(os.path.join(sys.path[0], 'mapas.txt'), 'w') as archivo:
            for mapa in mapas:
                archivo.write(f"{str(mapa)}\n")

        # esta seccion guarda el boleto en el archivo
        with open(os.path.join(sys.path[0], 'boletos.txt'), 'a', encoding='utf-8') as archivo:
            archivo.write(f'{boleto}\n')
        
            print('Pago completado, codigo:', codigo)
            print('Gracias por su compra! Guarde su codigo para poder ingresar al circuito')