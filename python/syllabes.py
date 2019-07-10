# -*-coding:Utf-8 -*

""" Module permettant de décomposer un mot français en syllabes"""

import re


def get_vowel_consonant(word):
    """
    Fonction de conversion du mot en chaîne de voyelles et consonnes.
    """
    # Set des voyelles
    vowel = {'a', 'e', 'i', 'o', 'u', 'y'}

    # Set des consonnes
    consonant = {'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}

    vowel_consonant_form = ""

    # Traduction en chaine de voyelles (v) et consonnes (c)
    for i, ch in enumerate(word):
        if ch in vowel:
            vowel_consonant_form += "v"
        elif ch in consonant:
            vowel_consonant_form += "c"

    return vowel_consonant_form


def replace_on(on_this, base, to_find, by):
    """
    Recherche et remplacement de caractères dans une chaîne
    en fonction d'un pattern trouvé dans une autre chaîne
 
    -Usage-
    replace_on(get_vowel_consonant("chat"), "chat", "ch", "gg")
    """

    # Recherche du pattern
    pos = [(m.start(), m.end()) for m in re.finditer(to_find, base) ]

    # Remplacement à la position correspondante dans l'autre chaîne
    for start, end in pos:
        on_this = on_this[0:start] + by + on_this[end:]
     
    return on_this


# test du module syllabes
if __name__ == "__main__":
    chaine = "test"
    
    # test fonction get_vowel_consonant
    print("get_vowel_consonant({}) = {}".format(chaine,
                                                get_vowel_consonant(chaine)))
