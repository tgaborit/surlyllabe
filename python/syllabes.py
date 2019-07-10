# -*-coding:Utf-8 -*

""" Module permettant de décomposer un mot français en syllabes"""


def get_vowel_consonant(word):
    """ Fonction de conversion du mot en chaîne de voyelles et consonnes."""
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

# test du module syllabes
if __name__ == "__main__":
    chaine = "test"
    # test fonction get_vowel_consonant
    print("get_vowel_consonant({}) = {}".format(chaine,
                                                get_vowel_consonant(chaine)))
    
