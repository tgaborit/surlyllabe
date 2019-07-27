# -*-coding:Utf-8 -*

""" Module permettant de décomposer un mot français en syllabes"""

import re


def get_vowel_consonant(word):
    """
    Fonction d'analyse d'un mot vers une chaîne de voyelles et consonnes.
    """
    # Set des voyelles
    vowel = {'a',      'à', 'â',
             'e', 'é', 'è', 'ê', 'ë',
             'i',           'î', 'ï',
             'o',           'ô',
             'u',      'ù', 'û',
             'y'}

    # Set des consonnes
    consonant = {'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}

    vowel_consonant_form = ""

    # Traduction en chaine de voyelles (v) et consonnes (c)
    for i, ch in enumerate(word):
        if ch.casefold() in vowel:
            vowel_consonant_form += "v"
        elif ch.casefold() in consonant:
            vowel_consonant_form += "c"

    return vowel_consonant_form


def replace_on(on_this, base, to_find, by):
    """
    Recherche et remplacement de caractères dans une chaîne d'analyse
    en fonction d'un pattern trouvé dans une autre chaîne.
    Retourne la chaîne d'analyse ainsi modifiée.
 
    -Usage-
    replace_on(get_vowel_consonant("chat"), "chat", "ch", "gg")
    """
    # Recherche du pattern
    pos = [(m.start(), m.end()) for m in re.finditer(to_find, base.casefold())]

    # Remplacement à la position correspondante dans l'autre chaîne
    for start, end in pos:
        on_this = on_this[0:start] + by + on_this[end:]
     
    return on_this


def special_cases(analysis_str, base):
    """
    Fonction de détection de cas particuliers de groupes de lettres
    par rapport au découpage syllabique
    Retourne la chaîne d'analyse ainsi modifiée.
    """
    # Set de groupes de lettres particuliers
    to_match_case = {"bl", "br", "ch", "cl", "cr", "dr", "fl", "fr", "gh",
                     "gl", "gn", "gr", "kl", "kr", "kh", "kn", "ph", "pl",
                     "pr", "rh", "qu", "tr", "th", "vr"}

    # Remplacement par "gg" dans la chaîne d'analyse
    for m in to_match_case:
        analysis_str = replace_on(analysis_str, base, m, "gg")

    # Cas particulier de "gu"
    analysis_str = replace_on(analysis_str, base, "gu", "gu")
    
    return analysis_str


def syl_analysis(word):
    """
    Fonction d'analyse syllabique d'un mot. Fait appel à la fonction de
    détection des voyelles et consonnes puis détecte les cas syllabiques
    particuliers en faisant appel à une seconde fonction.
    Retourne la chaîne d'analyse finale.
    """
    # Détection des voyelles et consonnes
    vowel_consonant_form = get_vowel_consonant(word)

    # Traitement des cas particuliers
    final_form = special_cases(vowel_consonant_form, word)

    return final_form


def syllabation(word):
    """
    Fonction générale de syllabisation d'un mot. Réalise l'annalyse des
    lettres du mot puis la compare à une liste de règles de syllabisation.
    Retourne une liste des syllabes du mot ainsi que la chaîne d'analyse
    syllabique du mot.
    """
    
    final_form = syl_analysis(word)

    # Règles de syllabisation de la langue française par ordre de priorité
    sub_rules = [r"(?=vc)ccv(?=gg)",      # chan-sti-quer
                 r"\bvvc\b",              # aic
                 r"\bvvvc\b",             # aies
                 r"\bcvvc\b",             # feuj
                 r"\bvvcc\b",             # airs
                 r"\bvcc\b",              # abc
                 r"\bccvc\b",             # ksar
                 r"\bcvcc\b",             # jack
                 r"\bggvvvvcc\b",         # frayeur
                 r"\bcvccgg\b",           # kitsch
                 r"\bcvc(?=gu)",          # -lon-guet
                 r"gu(?=cv)",             # la-gu-ne
                 r"guv(?=cv)",            # lar-gue-ra
                 r"guv(?=gg)",            #
                 r"guvc\b",               # al-gues
                 r"guvc(?=cv)",           #
                 r"cvvc(?=gu)",           # -four-gu
                 r"gu\b",                 #
                 r"guv\b",                #
                 r"guvv\b",               #
                 r"guvvc\b",              #
                 r"guvvcc\b",             #
                 r"guvc\b",               #
                 r"guvcc\b",              #
                 r"cvc(?=gu)",            # alanguis
                 r"\bvc(?=co)",           # -al-cooli
                 r"coo(?=cv)",            # al-coo-lisé
                 r"cooc\b",               # alcool
                 r"(?=vv)guc\b",          # -ai-gu
                 r"(?=vv)guv\b",          # -ai-gu
                 r"\bvv(?=gu)",           # -ai-gu
                 r"\bvv\b",               # ai
                 r"\bvc\b",               # ah
                 r"\bv\b",                # a
                 r"\bv(?=gg)",            # -i-vraie
                 r"\bc\b",                # a
                 r"\bco",                 # -co-ordonnée
                 r"\bggvvvvc\b",          # -choyait-
                 r"ggvc(?=gu)",           # -frin-gue
                 r"ggvvv\b",              # le-vreau-
                 r"ggvvvv\b",             # lam-proie-
                 r"ggvvvvc\b",            # lam-proies-
                 r"\bggvvc\b",            # -clair-
                 r"\bggvvv\b",            # -cloué-
                 r"\bggvcc\b",            # -click-
                 r"\bggcv(?=gg)",         # -chro-no
                 r"\bggcv(?=cv)",         # -phra-se
                 r"ggvvc(?=gg)",          # con-train-dra
                 r"cvggc\b",              # -right-
                 r"ocv",                  # co-opé-ration
                 r"oc",                   # co-or-donnée
                 r"\bvc(?=gg)",           # -as- phixiant      
                 r"(?=c)ggvvcc\b",        # as-treins-
                 r"ggvvccc\b",            # con-traints-
                 r"\bvvvcc\b",            # aient
                 r"\bggvvvc(?=cv)",       # -crayon-naient
                 r"\bggcv(?=cv)",         # -chré-tiens 
                 r"\bcvvvvc(?=cv)",       # couaille
                 r"\bcvvv(?=gg)",         # -coua-quait
                 r"\bcvcc(?=gg)",         # -cons-tuisons
                 r"cvgg\b",               # con-cept-
                 r"ccv\b",                # chap-ska-
                 r"ccvc\b",               # chap-skas-
                 r"gg\b",                 # conti-gu-
                 r"(?=cv)gg(?=cv)",       # confi-guré- #space
                 r"cvvv\b",               # ap-puyé
                 r"cvvvv\b",              # ap-puyée
                 r"cvvvvc\b",             # ap-puyées
                 r"ggvvvcc\b",            # acca-blaient-
                 r"cvvccc\b",             # at-teints- 
                 r"ggvvc(?=cv)",          # ac-quies-ce
                 r"ggvv(?=gg)",           # bi-blio-graphie
                 r"ggvvcc\b",             # abs-traits-
                 r"ggcv\b",               # algori-thme-
                 r"ggcvc\b",              # algori-thmes-
                 r"gggvc(?=cv)",          # dé-struc-turer
                 r"cvvvv(?=cv)",          # joyeu
                 r"cvvvvcc\b",            # accen-tuaient-
                 r"cvvcc\b",              # accen-tuant-
                 r"cvvv\b",               # accen-tuai-
                 r"cvvvcc\b",             # accen-tuai-
                 r"cvvvvc\b",             # a-boyait-
                 r"cvvvvvcc\b",           # a-boyaient-
                 r"cvvvc\b",              # accen-tuais-
                 r"cvvvc(?=cv)",          # a-boyan-te
                 r"cvvv(?=c)",            # a-boie-ment
                 r"\bvcc(?=cv)",          # abs-tient
                 r"\bvvc(?=c)",           # -ail-le
                 r"cvvc(?=gg)",           # abs-tien-dront
                 r"vc(?=gg)",             # -ab-scons
                 r"ggvvcc\b",             # -chiant-
                 r"ggvvvc\b",             # -truie-
                 r"ggvccc\b",             # aca-blants-
                 r"ggvvc\b",              # -chien-
                 r"ggvv(?=c)",            # -chaî-non
                 r"ggv\b",                # va-che-
                 r"ggvcc\b",              # quand
                 r"ggvc\b",               # chat
                 r"ggvc(?=cv)",           # auguille
                 r"ggvc(?=cc)",           # ?
                 r"ggvc(?=gg)",           # -char-treuse
                 r"ggv(?=c)",             # -sta-ble
                 r"vc(?=gg)",             # -an-gle
                 r"vcc(?=gg)",            # abs-trait
                 r"vcc(?=cv)",            # abs-tien
                 r"ggvv(?=c)",            # plau-sible
                 r"ggvv\b",               # mor-bleu-
                 r"ggv(?=gg)",            # re-blo-chon
                 r"cvccc\b",              # aba-tants
                 r"cvcc\b",               # gar-çons-
                 r"cvcc(?=cv)",           # -ping-pong
                 r"cvvc(?=c)",            # -ban-que
                 r"cvvc\b",               # poissoine-ries-
                 r"\bvc(?=cv)",           # -ac-cidentel
                 r"\bccv(?=c)",           # -mne-monique
                 r"cvc(?=c)",             # -ban-que
                 r"cvc\b",                # poi-son-
                 r"cvv(?=c)",             # -poi-sonnerie
                 r"cvv(?=gg)",            # a-bou-chement
                 r"cvc(?=c)",             # poi-son-nerie
                 r"cvc(?=gg)",            # rhodo-den-dron
                 r"cvv\b",                # poisonne-rie
                 r"\bvvv",                # -eau-
                 r"\bvv(?=cv)",           # aut
                 r"\bv(?=gg)",            # aut
                 r"cvv(?=cv)",            # -ton-ton
                 r"cv(?=cv)",             # tata
                 r"cv\b",                 #
                 r"vv(?=gg)",
                 r"cv",
                 r"v(?=cv)",
                 r"gg",
                 r"cc",                   # -cm-
                  
                 ]        

    # Assemblage des règles               
    regle = r"("
     
    for sr in sub_rules[:-1]:
        regle += sr + "|"
 
    regle +=  sub_rules[-1]
    regle +=  r")"
 
    syllabes = [ word[gr.start():gr.end()] for gr in
                 re.finditer(regle, final_form)]
     
    return syllabes


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

    # test fonction syl_analysis
    print("syl_analysis({}) = {}".format(
        repr("pachiderme"),
        repr(syl_analysis("pachiderme"))))
    
    # test fonction syllabation
    print("syllabation({}) = {}".format(
        repr("pharmacie"),
        repr(syllabation("pharmacie"))))
    
