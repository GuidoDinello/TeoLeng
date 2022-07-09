# -*- coding: utf-8 -*-

import sys
import io
import nltk

def parse(s):
    # a^nb^mc^k: ( n=m ∨ m=k ∨ n=k ) min(n,m,k) > 0
    grammar = """
    S -> AB C | A BC | AC
    AB -> 'a' AB 'b' | 'a' 'b'
    C -> 'c' C | 'c'
    A -> 'a' A | 'a'
    BC -> 'b' BC 'c' | 'b' 'c'
    AC -> 'a' AC 'c' | 'a' B 'c'
    B -> 'b' B | 'b'
    """
    grammar = nltk.CFG.fromstring(grammar)
    s_tokenized = list(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = list(parser.parse(s_tokenized))[:1]
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
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
