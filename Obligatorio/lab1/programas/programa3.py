# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    matches = re.findall(r'<\w*(D|d)(ate|ATE)\w*>(\s*)(.*)(\s*)</\w*(D|d)(ate|ATE)\w*>', texto)
    count = len(matches)

    return str(count)

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
