import os,sys

def validar_boleto(boletos, codigo):
    '''
    Valida si el codigo de boleto existe en el archivo de boletos

    :param boletos: lista de boletos
    :param codigo: codigo de boleto

    :return: True si el codigo existe y no ha sido usado, False si no existe o ya fue usado    
    '''
    # esta seccion valida el codigo de boleto
    for boleto in boletos:
        codigo_boleto = boleto.split(';')[0]
        estado = boleto.split(';')[6]

        if codigo == codigo_boleto and estado == 'False':
            # cambiar el estado del boleto a usado
            boletofinal = boleto.replace('False', 'True')

            # registrar asistencia en archivo
            with open(os.path.join(sys.path[0], 'asistencia.txt'), 'a', encoding='utf-8') as archivo:
                archivo.write(f"{boletofinal.split(';')[4]};{boletofinal.split(';')[7]}\n")
            print('Boleto valido, asistencia registrada')
            # reemplazar el boleto en la lista de boletos
            boletos[boletos.index(boleto)] = boletofinal

            # guardar los cambios en el archivo
            with open('boletos.txt', 'w', encoding='utf-8') as archivo:
                archivo.writelines(boletos)
                return True

    print('Boleto invalido o usado')
    return False