import os, sys

class Carrera:
    def __init__(self, nombre, numero_carrera, fecha_carrera, circuito, podium):
        '''Clase que define una carrera'''
        self.nombre = nombre
        self.numero_carrera = numero_carrera
        self.fecha_carrera = fecha_carrera
        self.circuito = circuito
        self.podium = podium

    def finalizar_carrera(self, pilotos):
        puntos_por_posicion = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

        # esta seccion obtiene los resultados de la carrera
        print()
        print('Ingrese los resultados de la carrera')
        print()
        podium_obtenido = []
        for i in range(1, 11):
            piloto_encontrado = False
            while not piloto_encontrado:
                print('Posicion ' + str(i))
                piloto = input('Ingrese el nombre y apellido del piloto: ')
                piloto = piloto.lower()

                # esta seccion busca el piloto
                for piloto_objeto in pilotos:
                    if piloto_objeto.nombre.lower() + ' ' + piloto_objeto.apellido.lower() == piloto:
                        piloto_encontrado = True
                        piloto_objeto.puntos = int(piloto_objeto.puntos)
                        piloto_objeto.puntos += puntos_por_posicion[i - 1]
                        podium_obtenido.append(piloto_objeto.nombre.lower() + ' ' + piloto_objeto.apellido.lower())
                        break

                if not piloto_encontrado:
                    print('Piloto no encontrado')

        self.podium = podium_obtenido

        # esta seccion actualiza el archivo de pilotos
        with open(os.path.join(sys.path[0], 'pilotos.txt'), 'w', encoding='utf-8') as archivo:
            for piloto in pilotos:
                archivo.write(f"{str(piloto)}\n")


    def __str__(self):
        return f'{self.nombre};{self.numero_carrera};{self.fecha_carrera};{self.circuito};{self.podium}'