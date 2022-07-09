# -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk.parse.generate import generate

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:

        grammar = """
        S -> GN_F V GN | GN_M V GN
        GN -> GN_M | GN_F
        GN_M -> NP_M | Det_M N_M
        GN_F -> NP_F | Det_F N_F
        Det_M -> "el" | "ese" | "un" | "tu"
        Det_F -> "la" | "esa" | "una" | "tu"
        NP_M -> "Pedro" | "Juan"
        NP_F -> "Julia" | "Marta"
        N_M -> "elefante" | "hueso" | "pescado" | "kiwi" | "mango" | "perro" | "gato"
        N_F -> "manzana" | "banana" | "naranja" | "pera" | "frutilla" | "perra" | "gata"
        V_M -> "es comido por" | "es saltado por" | "es trepado por" | "es descubierto por" | "es aplastado por" | V
        V_F -> "es comida por" | "es saltada por" | "es trepada por" | "es descubierta por" | "es aplastada por" | V
        V -> "come" | "salta" | "trepa" | "descubre" | "aplasta"
        """
        grammar = nltk.CFG.fromstring(grammar)
        s_tokenized = s.split()
        parser = nltk.LeftCornerChartParser(grammar)
        tree = list(parser.parse(s_tokenized))[:1]
        if tree:
            salida = "PERTENECE"
        else:
            salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()