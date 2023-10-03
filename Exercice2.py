import random
"""
1. Écrire une fonction qui génère aléatoirement une table de substitution monoalphabétique Tab (Attention : éviter les répétitions)
"""

def table_substitution()->dict:
    """
    Génère une table de substitution pour les caractères de l'alphabet.

    Retours :
        dict : Un dictionnaire où les clés sont les lettres originales et les valeurs sont leurs lettres substituées correspondantes.
    """
    # Crée un dictionnaire vide pour stocker la table de substitution
    Tab = {}
    # Définit l'alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Convertit la chaîne de l'alphabet en une liste de lettres individuelles
    liste_alphabet = list(alphabet)
    # Crée une copie de la liste de l'alphabet à mélanger
    shuffled_alphabet = liste_alphabet.copy()
    # Mélange la copie de la liste de l'alphabet de manière aléatoire
    random.shuffle(shuffled_alphabet)
    # Parcourt les listes de l'alphabet original et mélangé simultanément
    for lettre_originale, lettre_substituee in zip(liste_alphabet, shuffled_alphabet):
        # Associe la lettre originale à la lettre substituée dans le dictionnaire
        Tab[lettre_originale] = lettre_substituee
    # Retourne la table de substitution
    return Tab
"""
2. Écrire un programme qui lit un fichier texte ( .txt) et crypte son contenu par un chiffrement par substitution mono-alphabétique via la table Tab et range le résultat dans un autre fichier text.
"""
def cryptage():
    """
    Effectue le chiffrement mono-alphabétique d'un fichier texte et enregistre le résultat dans un autre fichier.
    """
    # Obtient la table de substitution à partir de la fonction table_substitution()
    Tab = table_substitution()
    # Lit le contenu du fichier texte d'origine
    with open("message_originale.txt","r") as f:
        texte_originale = f.read()
    # Initialise une chaîne vide pour stocker le texte chiffré
    Texte_chiffré = ""
    # Parcourt chaque lettre dans le texte d'origine
    for lettre in texte_originale:
        if lettre.isalpha():
            # Vérifie si le caractère est en minuscules ou majuscules
            if lettre.islower():
                # Si la lettre est en minuscule, la convertit en majuscule, chiffre, puis reconvertis en minuscule pour préserver la casse
                Texte_chiffré+=Tab[lettre.upper()].lower()
            else:
                # Si la lettre est en majuscule, chiffre directement
                Texte_chiffré+=Tab[lettre]
        else:
            Texte_chiffré+=lettre
    # Enregistre le texte chiffré dans un nouveau fichier texte
    with open("message_chiffré.txt","w") as f:
        f.write(Texte_chiffré)

"""
3. Écrire une fonction qui calcule la fréquence d’apparition des lettres dans un text et range le résultat pour un traitement ultérieur. (Ne pas compter les espaces)
"""
def fréquence_apparition(texte:str)->dict:
    """
    Calcule la fréquence d'apparition des lettres dans un texte donné, en ignorant les espaces, et stocke les résultats dans un dictionnaire.

    Args :
        texte (str) : Le texte dans lequel la fréquence des lettres doit être calculée.

    Returns:
        dict : Un dictionnaire où les clés sont les lettres en majuscules et les valeurs sont les fréquences d'apparition  correspondantes dans le texte.
    """
    # Initialise un dictionnaire vide pour stocker les fréquences d'apparition
    freq = {}
    # Convertit le texte en minuscules pour ignorer la casse
    texte=texte.lower()
    # Parcourt chaque lettre dans le texte
    for lettre in texte:
        if lettre.isalpha() and lettre not in freq.keys():
            # Si la lettre est alphabétique et n'est pas déjà dans le dictionnaire, compte son nombre d'occurrences dans le texte
            freq[lettre.upper()] = texte.count(lettre)
    # Retourne le dictionnaire des fréquences d'apparition
    return freq
"""
4. En se basant sur la table de fréquences de la langue utilisée pour la rédaction du texte, tenter de cryptanalyser un text intercepté (chaine de plus de 500 caractères) en supposant qu’il a été crypté par substitution mono-alphabétique.
"""
def decryptage(Tab:dict,Texte_chiffré:str):
    """
    Décrypte un texte chiffré en utilisant une table de correspondance mono-alphabétique.

    Args :
        Tab (dict) : Une table de correspondance mono-alphabétique où les clés sont les lettres chiffrées et les valeurs sont les lettres déchiffrées.
        Texte_chiffré (str) : Le texte chiffré à décrypter.
    """
    # Initialise une chaîne vide pour stocker le texte déchiffré
    texte_originale = ""
    # Parcourt chaque lettre dans le texte chiffré
    for lettre in Texte_chiffré:
        if lettre.isalpha() and Tab[lettre.upper()]!=None:
            if lettre.islower():
                # Si la lettre est en minuscule, la convertit en majuscule, déchiffre, puis reconvertis en minuscule
                texte_originale+=Tab[lettre.upper()].lower()
            else:
                # Si la lettre est en majuscule, déchiffre directement
                texte_originale+=Tab[lettre]
        else:
            # Si la lettre n'est pas alphabétique ou n'a pas de correspondance, ajoute telle quelle
            texte_originale+=lettre
    # Affiche le texte déchiffré
    print(texte_originale)
def getMax(d):
    max_key = next(iter(d))
    for key in d:
        if d[key] > d[max_key]:
            max_key = key
    return max_key
def cryptanalyse(Texte_chiffré:str):
    """
    Effectue une analyse de fréquence sur un texte chiffré et tente de décrypter le texte en utilisant une table de fréquence de référence.

    Args :
        Texte_chiffré (str) : Le texte chiffré à analyser et à décrypter.
    """
    # Tableau de fréquence des lettres dans la langue francaise (en pourcentage)
    tab_freq ={'A': 8.167,'B': 1.492,'C': 2.782,'D': 4.253,'E': 12.702,'F': 2.228,'G': 2.015,'H': 6.094,'I': 6.966,'J': 0.153,'K': 0.772,'L': 4.025,'M': 2.406,'N': 6.749,'O': 7.507,'P': 1.929,'Q': 0.095,'R': 5.987,'S': 6.327,'T': 9.056,'U': 2.758,'V': 0.978,'W': 2.36,'X': 0.15,'Y': 1.974,'Z': 0.074}
    # Trie le tableau de fréquence de référence en ordre décroissant de fréquence
    sorted_tab_freq = {key: value for key, value in sorted(tab_freq.items(), reverse=True, key=lambda item: item[1])}
    # Calcule la fréquence d'apparition des lettres dans le texte chiffré
    texte_freq = fréquence_apparition(Texte_chiffré)
    # Trie la fréquence des lettres dans le texte chiffré en ordre décroissant
    sorted_texte_freq = {key: value for key, value in sorted(texte_freq.items(), reverse=True, key=lambda item: item[1])}
    # Initialise un dictionnaire pour faire correspondre les lettres chiffrées avec les lettres déchiffrées
    match_tab = {key: None for key, value in tab_freq.items()}
    # Tente de faire correspondre les lettres chiffrées avec les lettres de la table de référence
    while len(sorted_texte_freq)>0:
        key = getMax(sorted_tab_freq)
        value =  getMax(sorted_texte_freq)
        match_tab[value] = key
        del sorted_tab_freq[key]
        del sorted_texte_freq[value]
    # Appelle la fonction de déchiffrement
    decryptage(match_tab,Texte_chiffré)

cryptage()
with open("message_chiffré.txt","r") as f:
    Texte_chiffré = f.read()  
cryptanalyse(Texte_chiffré)

