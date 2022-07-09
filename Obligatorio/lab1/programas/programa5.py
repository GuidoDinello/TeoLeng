# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    # Removes tags containing only numbers
    texto = re.sub(r'<\w*>[\s\n]*\d+\.?[\d]*[\s\n]*</\w*>', '', texto)
    # Removes tags without content
    texto = re.sub(r'<\w*>[\s\n]*</\w*>', '\n', texto)
    # Removes lines with only spaces in case there are
    texto = re.sub(r'^(\s*(\n))', '', texto, flags=re.MULTILINE)
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