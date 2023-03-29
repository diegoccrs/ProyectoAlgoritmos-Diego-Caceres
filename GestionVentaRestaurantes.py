import json
import os,sys

from GestionCarrerasEquipos import obtener_circuitos_archivo

def es_numero_perfecto(numero):
    '''
    Determina si un numero es perfecto

    :param numero: numero a evaluar

    :return: True si es perfecto, False si no lo es
    '''
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero

def obtener_datos_comida(cedula, edad, circuito, restaurantes):
    '''
    Obtiene los datos de la comida

    :param cedula: cedula del cliente
    :param edad: edad del cliente
    :param circuito: nombre del circuito
    :param restaurantes: lista de restaurantes
    '''
    # obtener los restaurantes del circuito
    circuitos = obtener_circuitos_archivo()

    # creamos una lista de los nombres de los circuitos
    circuitos_2 = []
    for circ in circuitos:
        circuitos_2.append(circ.nombre.lower())

    # obtenemos el index del circuito seleccionado
    idx_circuito = circuitos_2.index(circuito.lower())

    # obtenemos los restaurantes del circuito
    restaurantes_circuito = restaurantes[idx_circuito]


    # reemplaza las comillas simples por comillas dobles para que sea un JSON válido
    restaurantes_circuito = restaurantes_circuito.replace("'", '"')

    # convierte el string en un objeto JSON
    restaurantes_circuito = json.loads(restaurantes_circuito)

    # mostrar restaurantes siempre y cuando la lista no este vacia
    if len(restaurantes_circuito) == 0:
        print('No hay restaurantes disponibles')
        return
    
    print('Restaurantes disponibles:')
    print()
    for i, restaurante in enumerate(restaurantes_circuito):
        print(f'{i+1}. {restaurante["name"]}')

    # obtener restaurante
    rest = input('restaurante: ')
    print()
    while not rest.isdigit() or int(rest) > len(restaurantes_circuito):
        print('Restaurante no valido')
        rest = input('restaurante: ')

    print(restaurantes_circuito[int(rest)-1]["name"])
    print()
    print('Productos disponibles:')
    print()
    # revisar que la lista de productos no este vacia
    if len(restaurantes_circuito[int(rest)-1]["items"]) == 0:
        print('No hay productos disponibles')
        return
    
    if int(edad) < 18:
        print('Productos disponibles para menores de edad')
        productos_aptos = []
        for producto in restaurantes_circuito[int(rest)-1]["items"]:
            if producto["type"] != 'drink:alcoholic':
                productos_aptos.append(producto)

        for i, producto in enumerate(productos_aptos):
            precio = float(producto["price"]) + float(producto["price"]) * 0.16
            print(f'{i+1}. {producto["name"]} - ${precio}')

    else:
        for i, producto in enumerate(restaurantes_circuito[int(rest)-1]["items"]):
            precio = float(producto["price"]) + float(producto["price"]) * 0.16
            print(f'{i+1}. {producto["name"]} - ${precio}')

    # obtener productos
    productos = []

    while True:
        producto = input('\nproducto: ')
        while not producto.isdigit() or int(producto) < 1 or int(producto) > len(restaurantes_circuito[int(rest)-1]["items"]):
            print('Producto no valido')
            producto = input('\nproducto: ')


        precio = restaurantes_circuito[int(rest)-1]["items"][int(producto)-1]["price"]
        precio_iva = float(precio) + float(precio) * 0.16
        productos.append(f'{restaurantes_circuito[int(rest)-1]["items"][int(producto)-1]["name"]} - ${precio_iva}')
        print('Producto agregado')
        continuar = input('agregar otro producto (s/n): ')
        while continuar != 's' and continuar != 'n':
            print('Opcion no valida')
            continuar = input('agregar otro producto (s/n): ')
        if continuar == 'n':
            break

    # calcular total
    total = 0
    for producto in productos:
        total += float(producto.split('$')[-1])

    # calcular descuento
    descuento = 0
    if es_numero_perfecto(int(cedula)):
        descuento = total * 0.15

    # mostrar total
    print()
    print(f'Productos:')
    for producto in productos:
        print("     " + producto)
    print(f"Subtotal: ${total}")
    print(f"Descuento: ${descuento}")
    print(f"Total: ${total - descuento}")
    print()

    # confirmar compra
    confirmar = input('confirmar compra? (s/n): ')
    while confirmar != 's' and confirmar != 'n':
        print('Opcion no valida')
        confirmar = input('confirmar compra? (s/n): ')
    if confirmar == 's':
        print()
        print('Compra exitosa!')
        print('Gracias por comprar')
        print()
    
        # solo guardar nombre de productos
        productos = [producto.split('-')[0].strip() for producto in productos]

        # guardar compra
        with open(os.path.join(sys.path[0], 'compras.txt'), 'a', encoding='utf-8') as f:
            f.write(f'{cedula};{total-descuento};{productos}\n')

        return

    else:
        print('Ha cancelado su compra')
        return

def obtener_datos_cliente(boletos, restaurantes):
    '''
    Obtener los datos del cliente para comprar en los restaurantes

    :param boletos: lista de boletos
    :param restaurantes: lista de restaurantes
    '''
    # obtener cedula
    cedula = input('\ncedula: ')
    while not cedula.isdigit() or len(cedula) < 7 or len(cedula) > 8:
        print('Cedula no valida')
        cedula = input('\ncedula: ')

    es_vip = False
    # validar la cedula
    for boleto in boletos:
        cedula_boleto = boleto.split(';')[4]
        tipo_entrada_boleto = boleto.split(';')[5]

        if cedula == cedula_boleto and tipo_entrada_boleto.lower() == 'vip':
            print('Es VIP, bienvenido')
            es_vip = True
            circuito = boleto.split(';')[7]
            edad_boleto = boleto.split(';')[8].strip()
            obtener_datos_comida(cedula, edad_boleto, circuito, restaurantes)

    if not es_vip:
        print('No es VIP')