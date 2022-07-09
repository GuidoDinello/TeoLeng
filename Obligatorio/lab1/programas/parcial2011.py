# -*- coding: utf-8 -*-
import re

def programa(texto):
    """
        Escriba una función en Python que tome como entrada un texto en español y
    retorne el mismo texto pero removiendo las ocurrencias del string “muy” y las risas:
    secuencias de uno o más “ja”.
    Ejemplos:
    “eso fue gracioso” → “eso fue gracioso”
    “ja, eso fue gracioso” → “, eso fue gracioso“
    “eso fue muy gracioso jajaja” → “eso fue gracioso “

    re.sub(r'{pattern}', {substitute_for}, {origin})
    """
    filtered = re.sub(r"(muy|(ja)+)", "", texto)
    return filtered

def programa2(texto):
    """
        Escriba, con la sintaxis de Python, una expresión regular que permita
    encontrar colores expresados en formato hexadecimal.
    Un color en formato hexadecimal se representa con un # seguido de 6 dígitos
    hexadecimales (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f). Asuma que las letras solo
    pueden estar en minúscula.
    Ejemplos: #111111, #ab12e3, #eeeeee
    """
    matches = re.findall(r'(#[0-9-a-f]{6})', texto)
    return matches

"""
¿Qué función del módulo re de Python usaría si quisiera encontrar todas las
ocurrencias de dicha expresión regular en un string?
"""
#Para encontrar todas las ocurrencias de una expresion en un string deberiamos
#usar la funcion re.findall()

if __name__ == '__main__':
    test1 = [
        "eso fue gracioso",
        "ja, eso fue gracioso",
        "eso fue muy gracioso jajaja"
    ]
    test2 = [
        "#111111, #ab12e3, #eeeeee, #ggggggh"
    ]
    for text in test1:
        print(text + " ==> " + programa(text))
    for text in test2:
        print(text + " ==> ", end = "")
        print(programa2(text))