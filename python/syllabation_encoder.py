# -*-coding:Utf-8 -*

import argparse
from syllabes import *

parser = argparse.ArgumentParser(description="Proceeds to the syllabation of \
the word given, then encodes the result in a number whose Nth digit means \
the number of characters in the Nth syllable.")
parser.add_argument("word", type=str)
args = parser.parse_args()

ret_value = ""

for syllabe in syllabation(args.word):
    ret_value += str(len(syllabe))
    
print(ret_value)
