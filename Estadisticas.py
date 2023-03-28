import os,sys
try:
    import matplotlib.pyplot as plt
except ImportError:
    os.system("pip install matplotlib")
    import matplotlib.pyplot as plt

def promedio_gasto_vip():
    '''
    Calcula el promedio de gasto de los boletos VIP

    :return: promedio de gasto de los boletos VIP    
    '''
    #abrir archivo boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r', encoding='utf-8') as archivo:
        boletos = archivo.readlines()

    total_boletos = 0
    for boleto in boletos:
        precio = boleto.split(';')[2]
        total_boletos += float(precio)

    #abrir archivo compras
    with open(os.path.join(sys.path[0], 'compras.txt'), 'r', encoding='utf-8') as archivo:
        compras = archivo.readlines()

    total_compras = 0
    for compra in compras:
        precio = compra.split(';')[1]
        total_compras += float(precio)

    # promedio total
    promedio_total = (total_boletos + total_compras) / (len(boletos) + len(compras))

    return promedio_total

def tabla_asistencia():
    '''
    Genera una tabla con la asistencia de cada partido
    '''

    # leemos los archivos y guardamos la información en diccionarios
    ventas = {}
    asistencias = {}

    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r', encoding='utf-8') as archivo:
        for linea in archivo.readlines():
            datos = linea.strip().split(';')
            circuito = datos[7]
            if circuito not in ventas:
                ventas[circuito] = 0
            ventas[circuito] += 1

    with open(os.path.join(sys.path[0], 'asistencia.txt'), 'r', encoding='utf-8') as archivo:
        for linea in archivo.readlines():
            datos = linea.strip().split(';')
            circuito = datos[1]
            if circuito not in asistencias:
                asistencias[circuito] = 0
            asistencias[circuito] += 1

    # calculamos la relación asistencia/venta y almacenamos los resultados en una lista de tuplas
    resultados = []
    for circuito in ventas:
        print(circuito)
        if circuito in asistencias:
            resultados.append((circuito, asistencias[circuito], ventas[circuito], asistencias[circuito] / ventas[circuito]))

    # ordenamos los resultados por asistencia de mejor a peor
    resultados.sort(key=lambda x: x[3], reverse=True)

    # imprimimos los resultados
    print("-" * 110)
    print("{:<35} {:<20} {:<15} {:<20}".format("Circuito", "Boletos vendidos", "Asistencia", "Relación asistencia/venta"))
    print("-" * 110)
    for res in resultados:
        print("{:<35} {:<20} {:<15} {:<20}".format(res[0], res[2], res[1], res[3]))
    print("-" * 110)

def carrera_mas_asistencias():
    '''
    Obtiene la carrera con mayor asistencia
    '''

    asistencias = {}
    # abrir archivo asistencia
    with open(os.path.join(sys.path[0], 'asistencia.txt'), 'r', encoding='utf-8') as archivo:
        for linea in archivo.readlines():
            datos = linea.strip().split(';')
            circuito = datos[1]
            if circuito not in asistencias:
                asistencias[circuito] = 0
            asistencias[circuito] += 1

    # obtener carrera con mayor asistencia
    max_asistencia = 0
    carrera = ''
    for circuito in asistencias:
        if asistencias[circuito] > max_asistencia:
            max_asistencia = asistencias[circuito]
            carrera = circuito

    print(f"El circuito con mayor asistencia fue {carrera} con {max_asistencia} asistentes")

    # los obtenemos por separado para poder graficarlos
    circuitos = list(asistencias.keys())
    assitencia = list(asistencias.values())

    # obtenemos el indice del circuito con mayor asistencia
    index = circuitos.index(carrera)

    # Configura el color de las barras
    colores = ['blue' if i != index else 'red' for i in range(len(circuitos))]

    # graficamos los resultados
    plt.bar(circuitos, assitencia, color=colores)
    plt.title("Asistencia por circuito")
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para que sean legibles
    plt.xlabel("Circuito")
    plt.ylabel("Asistencia")

    # Ajusta el espacio alrededor del gráfico
    plt.subplots_adjust(bottom=0.25)

    plt.show()

def carrera_mas_boletos_vendidos():
    '''
    Obtiene la carrera con mayor cantidad de boletos vendidos
    '''

    boletos = {}
    # abrir archivo boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r', encoding='utf-8') as archivo:
        for linea in archivo.readlines():
            datos = linea.strip().split(';')
            circuito = datos[7]
            if circuito not in boletos:
                boletos[circuito] = 0
            boletos[circuito] += 1

    # obtener carrera con mayor asistencia
    max_boletos = 0
    carrera = ''
    for circuito in boletos:
        if boletos[circuito] > max_boletos:
            max_boletos = boletos[circuito]
            carrera = circuito

    print(f"El circuito con mayor cantidad de boletos vendidos fue {carrera} con {max_boletos} boletos vendidos")

    # los obtenemos por separado para poder graficarlos
    circuitos = list(boletos.keys())
    boletos_vendidos = list(boletos.values())

    # obtenemos el indice del circuito con mayor asistencia
    index = circuitos.index(carrera)

    # Configura el color de las barras
    colores = ['blue' if i != index else 'red' for i in range(len(circuitos))]
    # graficamos los resultados
    plt.bar(circuitos, boletos_vendidos, color=colores)
    plt.title("Boletos vendidos por circuito")
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para que sean legibles
    plt.xlabel("Circuito")
    plt.ylabel("Boletos vendidos")

    # Ajusta el espacio alrededor del gráfico
    plt.subplots_adjust(bottom=0.25)

    plt.show()

def tres_productos_mas_vendidos():
    '''
    Obtiene los 3 productos mas vendidos
    '''
    ventas_productos = {}
    # abrir archivo compras
    with open(os.path.join(sys.path[0], 'compras.txt'), 'r', encoding='utf-8') as archivo:
        for linea in archivo.readlines():
            datos = linea.strip().split(';')
            productos_string = datos[2].strip("[]")
            productos = [producto.strip().strip('"\'') for producto in productos_string.split(',')]
            for producto in productos:
                if producto not in ventas_productos:
                    ventas_productos[producto] = 0
                ventas_productos[producto] += 1

    # ordenamos los productos según las ventas y tomamos los primeros 3
    productos_ordenados = sorted(ventas_productos.items(), key=lambda x: x[1], reverse=True)[:3]

    # imprimimos los 3 productos con mas ventas
    print("Top 3 productos más vendidos en el restaurante")
    for i, (producto, ventas) in enumerate(productos_ordenados, start=1):
        print(f"{i}. {producto}: {ventas} ventas")

    # los obtenemos por separado para poder graficarlos
    productos = [producto for producto, _ in productos_ordenados]
    ventas = [venta for _, venta in productos_ordenados]

    plt.bar(productos, ventas)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para que sean legibles
    plt.xlabel('Productos')
    plt.ylabel('Ventas')
    plt.title('Top 3 productos más vendidos')

    # Ajusta el espacio alrededor del gráfico
    plt.subplots_adjust(bottom=0.25)

    plt.show()

def tres_clientes_mas_boletos():
    '''
    Obtiene los 3 clientes que mas boletos han comprado
    '''
    ventas_boletos = {}
    # abrir archivo boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r', encoding='utf-8') as archivo:
        for linea in archivo.readlines():
            datos = linea.strip().split(';')
            cedula = datos[4]
            if cedula not in ventas_boletos:
                ventas_boletos[cedula] = 0
            ventas_boletos[cedula] += 1

    # ordenamos los clientes según las ventas y tomamos los primeros 3
    clientes_ordenados = sorted(ventas_boletos.items(), key=lambda x: x[1], reverse=True)[:3]

    # imprimimos los 3 clientes con mas ventas
    print("Top 3 clientes que más boletos han comprado")
    for i, (cliente, ventas) in enumerate(clientes_ordenados, start=1):
        print(f"{i}. {cliente}: {ventas} boletos")

    # los obtenemos por separado para poder graficarlos
    clientes = [cliente for cliente, _ in clientes_ordenados]
    ventas = [venta for _, venta in clientes_ordenados]

    plt.bar(clientes, ventas)
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para que sean legibles
    plt.xlabel('Clientes')
    plt.ylabel('Ventas')
    plt.title('Top 3 clientes que más boletos han comprado')

    # Ajusta el espacio alrededor del gráfico
    plt.subplots_adjust(bottom=0.25)

    plt.show()