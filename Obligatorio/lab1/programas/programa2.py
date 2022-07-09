# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    x = re.findall("<[\s]*Resolution[\s]*>[\s]*.*[\s]*<X>[\s]*(\d{1,5})[\s]*<[\s]*/[\s]*X[\s]*>", texto)
    res_x = x[0]
    y = re.findall("<[\s]*Resolution[\s]*>[\s]*.*[\s]*<Y>[\s]*(\d{1,5})[\s]*<[\s]*/[\s]*Y[\s]*>", texto)
    res_y = y[0]
    texto = f"Resolucion X: {res_x}\nResolucion Y: {res_y}"
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
