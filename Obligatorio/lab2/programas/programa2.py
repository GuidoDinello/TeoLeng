# -*- coding: utf-8 -*-

from multiprocessing.sharedctypes import Value
import sys
import io
import nltk
from nltk.tree import Tree
import string
from nltk.parse.generate import generate

NOT = "NOT"
OR = "OR"
AND = "AND"
PARENTESIS = "PARENTESIS"

def parse(s):
    grammar = f"""
    S -> {PARENTESIS} | {NOT} | {OR} | {AND} | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p'| 'q'| 'r'| 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
    {PARENTESIS} -> '(' S ')'
    {NOT} -> 'not' S
    {OR} -> S 'or' S
    {AND} -> S 'and' S
    """

    grammar = nltk.CFG.fromstring(grammar)
    s_tokenized = s.split()
    parser = nltk.LeftCornerChartParser(grammar)
    tree = list(parser.parse(s_tokenized))[:1]
    
    return tree

def prefix(tree) -> string:
    """
    Generates the prefix form of a logical proposition.
    """

    # cambiar el verbo
    if type(tree) is nltk.tree.Tree:
        label: string = tree.label()
        if label == "S":
            return prefix(tree[0])
        elif label == NOT:
            return f"not({prefix(tree[1])})"
        elif label == OR:
            return f"or({prefix(tree[0])},{prefix(tree[2])})"
        elif label == AND:
            return f"and({prefix(tree[0])},{prefix(tree[2])})"
        elif label == PARENTESIS:
            return prefix(tree[1])
        else:
            raise ValueError("Invalid label")
    else:
        return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s)
      if tree:
          salida = prefix(tree[0])
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
