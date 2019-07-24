# -*-coding:Utf-8 -*

import argparse
from syllabes import *

parser = argparse.ArgumentParser()
parser.add_argument("word", type=str)
args = parser.parse_args()
ret_value = syllabation(args.word)
print(ret_value)
