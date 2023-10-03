from Exercice1 import decalage
"""
Écrire l’algorithme de Vigenère tel que :
- La clé et le texte à chiffrer seront passés en paramètres.
- Mettre le résultat du chiffrement dans un fichier texte.
- Ecrire un programme permettant le déchiffrement d’un texte chiffré.
"""
def getMatrix()->list:
    """
    Génère une matrice de substitution pour l'algorithme de Vigenère.

    Returns :
        list : La matrice de substitution.
    """
    # Crée une liste vide de 26 éléments pour stocker la matrice
    matrix = [0]*26
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # L'alphabet
    # Boucle pour générer chaque ligne de la matrice
    for i in range(26):
        if i==0:
            # Pour la première ligne, utilisez l'alphabet sans decalage
            ch=alphabet 
        else:
            # Pour les lignes suivantes, effectuez un décalage de l'alphabet
            ch = decalage(alphabet,i) 
        # Convertit la chaîne en une liste de caractères et l'ajoute à la matrice
        matrix[i]=list(ch) 
    # Retourne la matrice de substitution générée
    return matrix

def Vigenère(texte:str,clé:str):
    """
    Chiffre un texte en utilisant l'algorithme de Vigenère.

    Args :
        texte (str) : Le texte à chiffrer.
        clé (str) : La clé de chiffrement.
    """
    # Obtient la matrice de substitution pour Vigenère
    matrix = getMatrix()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Initialise une chaîne vide pour stocker le texte chiffré
    Texte_chiffré=""
    # Calcule la clé complète en répétant la clé initiale pour correspondre à la longueur du texte
    key = clé*int(len(texte)/len(clé))+clé[:int(len(texte)%len(clé))]
    # Parcourt chaque caractère du texte
    for index,value in enumerate(texte):
        if value.isalpha():
            # Pour les caractères alphabétiques, effectue le chiffrement de Vigenère
            col = alphabet.index(key[index].upper()) # Colonne dans la matrice de substitution
            row = alphabet.index(texte[index].upper()) # Ligne dans la matrice de substitution
            if value.islower():
                Texte_chiffré+=matrix[row][col].lower() # Ajoute la lettre chiffrée en minuscules
            else:
                Texte_chiffré+=matrix[row][col] # Ajoute la lettre chiffrée en majuscules
        else:
            # Pour les caractères non alphabétiques, ajoute tels quels au texte chiffré
            Texte_chiffré+=value
    # Enregistre le texte chiffré dans un fichier texte nommé "chiffre_de_Vigenère.txt"
    with open("chiffre_de_Vigenère.txt","w") as f:
        f.write(Texte_chiffré)
def déchiffrement(Texte_chiffré:str,clé:str):
    """
    Déchiffre un texte chiffré à l'aide de l'algorithme de Vigenère.

    Args :
        Texte_chiffré (str) : Le texte chiffré à déchiffrer.
        clé (str) : La clé de déchiffrement.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Initialise une chaîne vide pour stocker le texte déchiffré
    Texte_originale=""
    # Obtient la matrice de substitution pour Vigenère
    matrix= getMatrix()
    # Calcule la clé complète en répétant la clé initiale pour correspondre à la longueur du texte chiffré
    key = clé*int(len(texte)/len(clé))+clé[:int(len(texte)%len(clé))]
    
    for index,value in enumerate(Texte_chiffré):
        if value.isalpha():
            # Pour les caractères alphabétiques, effectue le déchiffrement
            col = alphabet.index(key[index].upper()) # Colonne dans la matrice de substitution
            ch_lettre = Texte_chiffré[index].upper() # Lettre chiffrée en cours de traitement
            row_index = None # Indice de ligne dans la matrice de substitution
            # Parcourt les lignes de la matrice pour trouver la lettre déchiffrée correspondante
            for i, row in enumerate(matrix):
                if row[col] == ch_lettre:
                    row_index = i
                    break
            lettre= alphabet[row_index] # Lettre déchiffrée
            if value.islower():
                # Ajoute la lettre déchiffrée en minuscules
                Texte_originale+=lettre.lower()  
            else:
                # Ajoute la lettre déchiffrée en majuscules
                Texte_originale+=lettre
        else:
            # Pour les caractères non alphabétiques, ajoute tels quels au texte déchiffré
            Texte_originale+=value
    # Affiche le texte déchiffré
    print(Texte_originale)
texte = open("message_originale.txt","r").read()
Vigenère(texte,"MATHWEB")
Texte_chiffré = open("chiffre_de_Vigenère.txt","r").read()
déchiffrement(Texte_chiffré,"MATHWEB")