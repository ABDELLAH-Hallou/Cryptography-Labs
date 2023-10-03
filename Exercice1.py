"""
1. Écrire une fonction qui prend en paramètre une chaine de caractère ch ainsi qu’un nombre de décalage k (entre 1 et 25) et retourne la chaine ch cryptée par le chiffre de César de décalage k.
"""
def decalage(ch:str,k:int)->str:
    """
    Décale les lettres d'une chaîne de caractères ch de k positions dans l'alphabet.

    Args:
        ch (str): La chaîne de caractères d'entrée.
        k (int): Le nombre de positions de décalage.

    Returns:
        str: La chaîne résultante avec les lettres décalées.

    Raises:
        ValueError: Si k est en dehors de la plage valide [1, 25].
    """
    # Vérifie si k est en dehors de la plage valide (1 à 25 inclus)
    if k>25 or k<1:
        raise ValueError("Le nombre de décalage k doit être entre 1 et 25")
    # Initialise une liste pour stocker les caractères décalés
    shifted_ch = [0]*len(ch)
    # Parcourt chaque caractère de la chaîne d'entrée
    for index,item in enumerate(ch):
        # Vérifie si le caractère est en minuscules ou majuscules
        if item.islower():
            origin = ord("a")
        else:
            origin = ord("A")
        # Applique le décalage à la lettre en tenant compte de la casse
        shifted_ch[index] = chr((( ord(item) - origin + k ) %26 ) + origin )
    # Retourne la chaîne de caractères décalée
    return "".join(shifted_ch)

"""
En déduire un programme qui lit une chaine de caractères ch et lui applique le cryptage et le décryptage en affichant à chaque étape le résultat.
"""

def cryptage():
    """
    Fonction pour crypter un message en utilisant le décalage de lettres.

    Demande à l'utilisateur de saisir un message secret, le crypte en utilisant un décalage de 3 positions, puis affiche le texte crypté.

    Utilise la fonction 'decalage' pour effectuer le cryptage.
    """
    # Demande à l'utilisateur de saisir le message secret
    texte_originale = str(input("tapez votre message secret: "))
    # Appelle la fonction 'decalage' pour crypter le texte
    Texte_chiffré = decalage(texte_originale,3)
    # Affiche le texte crypté
    print(f"votre texte chiffré est: {Texte_chiffré}")

"""
Écrire un programme qui cryptanalyse un message intercepté en supposant que ce dernier a été crypté par le chiffre de César.
"""

def cryptanalyse(Texte_chiffré:str):
    """
    Effectue une attaque statique pour déchiffrer un texte chiffré avec la méthode de décalage (Chiffre de César).
    Args:
        texte_chiffre (str): Le texte chiffré à déchiffrer.
    """    
    for k in range(1, 26):
        # Initialise une liste pour stocker les caractères déchiffrés
        ch = [0]*len(Texte_chiffré)
        # Parcourt chaque caractère du texte chiffré
        for index,item in enumerate(Texte_chiffré):
            # Vérifie si le caractère est en minuscules ou majuscules
            if item.islower():
                origin = ord('a')
            else:
                origin = ord('A')
            # Déchiffre le caractère en fonction de la valeur de décalage 'k'
            ch[index] = chr(((ord(item) - origin - k) % 26) + origin)
        # Combine les caractères pour former le texte déchiffré
        ch = "".join(ch)
        # Affiche le texte déchiffré pour le décalage 'k' actuel
        print(f'Décalage de {k}: {ch}')


if __name__ == "__main__":
    cryptage()
    cryptanalyse("khoor")


    