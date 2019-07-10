# -*-coding:Utf-8 -*

""" Module permettant de décomposer un mot français en syllabes"""

import re


def get_vowel_consonant(word):
    """
    Fonction d'analyse d'un mot vers une chaîne de voyelles et consonnes.
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
    Recherche et remplacement de caractères dans une chaîne d'analyse
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


def special_cases(analysis_str, base):
    """
    Fonction de détection de cas particuliers de groupes de lettres
    par rapport au découpage syllabique
    """
    # Set de groupes de lettres particuliers
    to_match_case = {"bl", "br", "ch", "cl", "cr", "dr", "fl", "fr", "gh",
                     "gl", "gn", "gr", "kl", "kr", "kh", "kn", "ph", "pl",
                     "pr", "rh", "qu", "tr", "th", "vr"}

    # Remplacement par "gg" dans la chaîne d'analyse
    for m in to_match_case:
        analysis_str = replace_on(analysis_str, base,  m, "gg" )

    # Cas particulier de "gu"
    analysis_str = replace_on(analysis_str, base,  "gu", "gu" )
    
    return analysis_str


# test du module syllabes
if __name__ == "__main__":
    
    # test fonction get_vowel_consonant
    print("get_vowel_consonant({}) = {}".format(
        repr("test"), repr(get_vowel_consonant("test"))))
          
    # test fonction replace_on
    print("replace_on(get_vowel_consonant({0}), {0}, {1}, {2}) = {3}".format(
        repr("chat"), repr("ch"), repr("gg"),
        repr(replace_on(get_vowel_consonant("chat"), "chat", "ch", "gg"))))

    # test fonction special_cases
    print("special_cases(get_vowel_consonant({0}), {0}) = {1}".format(
        repr("guigne"),
        repr(special_cases(get_vowel_consonant("guigne"), "guigne"))))
