# -*-coding:Utf-8 -*

"""
Programme réalisant la syllabisation d'un mot passé en paramètre, puis
encode le résultat pour donner un nombre dont les chiffres correspondent à la
taille des syllabes du mot.
"""

import argparse
from syllabes import *

# Gestion des arguments
parser = argparse.ArgumentParser(description="Proceeds to the syllabation of \
the word given, then encodes the result in a number whose Nth digit means \
the number of characters in the Nth syllable.")
parser.add_argument("word", type=str, help="word to analyse")
args = parser.parse_args()

# Encodage de la syllabisation :
# La chaîne du code est un nombre dont les chiffres correspondent à la taille
# des syllabes, à leur position respective.
ret_value = ""
for syllabe in syllabation(args.word):
    ret_value += str(len(syllabe))
    
# Affichage du code sur la sortie standard    
print(ret_value)
