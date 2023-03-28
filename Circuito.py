class Circuito:
    def __init__(self, nombre, pais, localidad, latitud, longitud):
        '''Clase que define un circuito'''
        self.nombre = nombre
        self.pais = pais
        self.localidad = localidad
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return f'{self.nombre};{self.pais};{self.localidad};{self.latitud};{self.longitud}'