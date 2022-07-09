# -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk.parse.generate import generate

MASCULINE_DETERMINANT = "Det_M"
FEMININE_DETERMINANT = "Det_F"

def parse(s):
    active_grammar = f"""
    S -> GN_F V GN | GN_M V GN
    GN -> GN_M | GN_F
    GN_M -> NP_M | {MASCULINE_DETERMINANT} N_M | {MASCULINE_DETERMINANT} N_NEUTRO
    GN_F -> NP_F | {FEMININE_DETERMINANT} N_F | {FEMININE_DETERMINANT} N_NEUTRO
    {MASCULINE_DETERMINANT} -> "el" | "ese" | "un" | "tu"
    {FEMININE_DETERMINANT} -> "la" | "esa" | "una" | "tu"
    NP_M -> "Pedro" | "Juan"
    NP_F -> "Julia" | "Marta"
    N_NEUTRO -> "elefante"
    N_M -> "hueso" | "pescado" | "kiwi" | "mango" | "perro" | "gato"
    N_F -> "manzana" | "banana" | "naranja" | "pera" | "frutilla" | "perra" | "gata"
    V -> "come" | "salta" | "trepa" | "descubre" | "aplasta"
    """

    active_grammar = nltk.CFG.fromstring(active_grammar)
    s_tokenized = s.split()
    parser = nltk.LeftCornerChartParser(active_grammar)
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

def generate_passive(tree):
    """
    Generates the passive voice from a parsed list.
    """
    
    MASCULINE_VERB = 0
    FEMENINE_VERB = 1
    
    active_to_passive = {
        "come" : ["es comido por", "es comida por"], 
        "salta" : ["es saltado por", "es saltada por"],
        "trepa" : ["es trepado por", "es trepada por"],
        "descubre" : ["es descubierto por", "es descubierta por"],
        "aplasta" : ["es aplastado por", "es aplastada por"],
    }

    verb = tree[1][0]
    verb_gender = FEMENINE_VERB
    determinant_label = tree[2][0][0].label()
    if determinant_label == MASCULINE_DETERMINANT:
        verb_gender = MASCULINE_VERB

    new_node = nltk.Tree(verb_gender, [active_to_passive[verb][verb_gender]])
    new_tree = nltk.Tree('S', [tree[2], new_node, tree[0]])
    return new_tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
        tree = parse(s)
        if tree:
            passive = generate_passive(tree[0])
            salida = ""
            for node in passive:
                for text in node.leaves():
                    salida += " " + text
            salida = salida[1:]
        else:
            salida = "NO PERTENECE"
    except:
        salida = "NO CUBRE"

    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
