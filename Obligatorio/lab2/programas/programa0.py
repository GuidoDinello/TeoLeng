# -*- coding: utf-8 -*-

import sys
import io
import nltk

def printT(t):
  print("label: ", t.label())
  for n in t:
    if type(n) is nltk.Tree:
      printT(n)
    else:
      print("leaf:", n)
    break

if __name__ == '__main__':
  grammar = """
  N -> N D | D
  D -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
  """
  grammar = nltk.CFG.fromstring(grammar)
  parser = nltk.LeftCornerChartParser(grammar)

  entries = ["7654321", "123", "1"]
  for w in entries:
    tree = list(parser.parse(w))[:1]
    printT(tree[0])
    print("\n")