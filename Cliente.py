class Cliente:
    def __init__(self, nombre, apellido, cedula, edad, carrera, tipo_entrada):
        '''Clase que define un cliente'''
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
        self.carrera = carrera
        self.tipo_entrada = tipo_entrada

    def __str__(self):
        return f'{self.nombre};{self.apellido};{self.cedula};{self.edad};{self.carrera};{self.tipo_entrada}'