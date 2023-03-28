class Piloto:
    def __init__(self, nombre, apellido, fecha_nacimiento, lugar_nacimiento, equipo, numero, puntos):
        '''Clase que define un piloto'''
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.equipo = equipo
        self.numero = numero
        self.puntos = puntos

    def __str__(self):
        return f'{self.nombre};{self.apellido};{self.fecha_nacimiento};{self.lugar_nacimiento};{self.equipo};{self.numero};{self.puntos}'