# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    res: str = ""

    find: list[list[str,str]] = re.findall(r'<([\w]*)>[^>]* (http[s]?://[^> ]+) [^>]*>', texto)

    i: int = 1
    for tag_and_link in find:
        if not re.search(r".uy", tag_and_link[1]):
            res += f"{tag_and_link[0]} -- {tag_and_link[1]}"
            if len(find) != i:
                res += "\n"
        i+=1
    return res

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
