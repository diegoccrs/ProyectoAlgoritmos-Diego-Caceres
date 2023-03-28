class Boleto:
    def __init__(self, codigo, asiento, total, cliente):
        '''Clase que define un boleto'''
        self.codigo = codigo
        self.asiento = asiento
        self.total = total
        self.cliente = cliente
        self.usado = False

    def __str__(self):
        return f'{self.codigo};{self.asiento};{self.total};{self.cliente.nombre} {self.cliente.apellido};{self.cliente.cedula};{self.cliente.tipo_entrada};{self.usado};{self.cliente.carrera.circuito};{self.cliente.edad}'