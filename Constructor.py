class Constructor:
    def __init__(self, nombre, id_equipo, nacionalidad, pilotos, puntos):
        '''Clase que define un constructor'''
        self.nombre = nombre
        self.id_equipo = id_equipo
        self.nacionalidad = nacionalidad
        self.pilotos = pilotos
        self.puntos = puntos

    def __str__(self):
        return f'{self.nombre};{self.id_equipo};{self.nacionalidad};{self.pilotos};{self.puntos}'