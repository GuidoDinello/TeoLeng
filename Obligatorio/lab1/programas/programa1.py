# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    fecha = re.findall("<[\s]*FileModifyDate[\s]*>[\s]*(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}).*[\s]*<[\s]*/[\s]*FileModifyDate[\s]*>", texto)
    [anio, mes, dia, hora, min] = fecha[0]
    texto = f"{hora}:{min} del {anio}-{mes}-{dia}"
    return texto

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
