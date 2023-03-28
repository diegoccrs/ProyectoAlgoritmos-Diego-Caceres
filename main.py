import os,sys
import Estadisticas
import GestionVentaRestaurantes
import GestionAsistenciaCarreras
import GestionCarrerasEquipos
import GestionVentaEntradas

def main():
    # obtenemos los datos de los archivos
    pilotos = GestionCarrerasEquipos.obtener_pilotos_archivo()
    constructores = GestionCarrerasEquipos.obtener_constructores_archivo()
    carreras = GestionCarrerasEquipos.obtener_carreras_archivo()
    circuitos = GestionCarrerasEquipos.obtener_circuitos_archivo()

    # abrir el archivo de boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r', encoding='utf-8') as archivo:
        boletos = archivo.readlines()

    # abrir el archivo restaurantes
    with open(os.path.join(sys.path[0], 'restaurantes.txt'), 'r', encoding='utf-8') as archivo:
        restaurantes = archivo.readlines()

    print("\n" + "="*30)
    print(" "*7 + "BIENVENIDO")
    print("="*30 + "\n")

    print("a) Filtrar constructores por pais")
    print("b) Filtrar pilotos por constructor")
    print("c) Filtrar carreras por pais del circuito")
    print("d) Filtrar carreras por mes")
    print("e) Finalizar una carrera")
    print("f) Comprar un boleto")
    print("g) Usar mi boleto")
    print("h) Comprar en restaurantes")
    print("i) Mostrar estadísticas")
    print("j) Cerrar sistema\n")

    seleccion = input("Por favor, ingrese su opción: ")
    print()
    while seleccion != 'j':
        if seleccion == 'a':
            GestionCarrerasEquipos.obtener_constructores_por_pais(constructores)
        elif seleccion == 'b':
            GestionCarrerasEquipos.obtener_pilotos_por_constructor(pilotos)
        elif seleccion == 'c':
            GestionCarrerasEquipos.obtener_carreras_por_pais_circuito(carreras, circuitos)
        elif seleccion == 'd':
            GestionCarrerasEquipos.obtener_carreras_en_un_mes(carreras)
        elif seleccion == 'e':
            GestionCarrerasEquipos.finalizar_carrera_funcion(carreras, pilotos, constructores)
        elif seleccion == 'f':
            GestionVentaEntradas.crear_compra(carreras)
            # recargar el archivo de boletos
            with open('boletos.txt', 'r') as archivo:
                boletos = archivo.readlines()
        elif seleccion == 'g':
            # obtener el codigo del boleto
            codigo = input('Ingrese el codigo del boleto: ')
            print()
            GestionAsistenciaCarreras.validar_boleto(boletos, codigo)
        elif seleccion == 'h':
            GestionVentaRestaurantes.obtener_datos_cliente(boletos, restaurantes)
            # recargar archivo restaurantes
            with open('restaurantes.txt', 'r') as archivo:
                restaurantes = archivo.readlines()
        elif seleccion == 'i':
            print("\n" + "="*40)
            print(" "*7 + "MENÚ DE ESTADÍSTICAS")
            print("="*40 + "\n")

            print("a) Obtener promedio de gasto de un cliente VIP")
            print("b) Obtener datos de los circuitos")
            print("c) Obtener circuito con mayor asistencia")
            print("d) Obtener circuito con mayores boletos vendidos")
            print("e) Obtener top 3 productos más vendidos")
            print("f) Obtener top 3 clientes con más boletos\n")

            seleccion2 = input("Por favor, ingrese su opción: ")
            print()
            if seleccion2 == 'a':
                print(f"El promedio de gasto de un client VIP es: {Estadisticas.promedio_gasto_vip()}")
            elif seleccion2 == 'b':
                Estadisticas.tabla_asistencia()
            elif seleccion2 == 'c':
                Estadisticas.carrera_mas_asistencias()
            elif seleccion2 == 'd':
                Estadisticas.carrera_mas_boletos_vendidos()
            elif seleccion2 == 'e':
                Estadisticas.tres_productos_mas_vendidos()
            elif seleccion2 == 'f':
                Estadisticas.tres_clientes_mas_boletos()
            else:
                print('Error. Seleccione una opcion valida')
        else:
            print('Error. Seleccione una opcion valida')

        print("\n" + "="*30)
        print(" "*7 + "MENÚ PRINCIPAL")
        print("="*30 + "\n")

        print("a) Filtrar constructores por pais")
        print("b) Filtrar pilotos por constructor")
        print("c) Filtrar carreras por pais del circuito")
        print("d) Filtrar carreras por mes")
        print("e) Finalizar una carrera")
        print("f) Comprar un boleto")
        print("g) Usar mi boleto")
        print("h) Comprar en restaurantes")
        print("i) Mostrar estadísticas")
        print("j) Cerrar sistema\n")

        seleccion = input("Por favor, ingrese su opción: ")
        print()


main()

# obtener los equipos, estadios y restaurantes partidos de la api para reiniciar los archivos
#pilotos = GestionCarrerasEquipos.obtener_pilotos_api()
#constructores = GestionCarrerasEquipos.obtener_constructores_api()
#carreras = GestionCarrerasEquipos.obtener_carreras_api()