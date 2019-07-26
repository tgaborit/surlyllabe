# -*-coding:Utf-8 -*

import argparse
from syllabes import *

parser = argparse.ArgumentParser()
parser.add_argument("word", type=str)
args = parser.parse_args()

ret_value = ""

for syllabe in syllabation(args.word):
    ret_value += str(len(syllabe))
    
print(ret_value)
