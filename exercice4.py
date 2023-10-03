import random 
"""
1.Écrire une fonction qui génère aléatoirement un tableau de substitution Tab de 0 à 99.
"""
           
def generate_Tab()->dict:
    # L'alphabet utilisé pour créer le tableau de substitution
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Les fréquences d'apparition des lettres de l'alphabet en pourcentage
    Freq=[8.01, 0.88, 3.23, 3.91, 17.52, 1.06, 1.06, 0.88, 7.35, 0.44, 0.05, 5.77, 2.9, 7.22, 5.43, 2.94, 1.14, 6.69, 8.17, 7.07, 6.0, 1.41, 0.02, 0.47, 0.3, 0.12]
    # Le nombre de symboles correspondant à chaque lettre de l'alphabet
    Num_symboles = [8,1,3,4,16,1,1,1,7,1,1,5,3,7,5,3,1,6,8,7,6,1,1,1,1,1]
    # Initialisation du dictionnaire Tab qui représentera le tableau de substitution
    Tab={}
    # Générer une liste de chiffres de 00 à 99 et les mélanger aléatoirement
    generated_digits = [str(num).zfill(2) for num in range(100)]
    random.shuffle(generated_digits)
    # Créer le tableau de substitution pour chaque lettre de l'alphabet
    for index in range(len(ALPHABET)):
        Tab[ALPHABET[index]] = []
        # Remplir le tableau de substitution avec les chiffres générés
        for i in range(Num_symboles[index]):
            digit = generated_digits.pop(0)
            Tab[ALPHABET[index]].append(digit)
    print(Tab)
    return Tab

"""
2. Écrire une fonction qui crypte un texte par un chiffre homophone en se basant sur la table Tab. Cette fonction doit choisir d’une manière uniforme les choix de substitution.
"""
def encrypt(plain_text):
    # Génère le tableau de substitution Tab en utilisant la fonction précédemment définie
    Tab = generate_Tab()
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"# L'alphabet utilisé
    # Le nombre de symboles correspondant à chaque lettre de l'alphabet
    Num_symboles = [8,1,3,4,16,1,1,1,7,1,1,5,3,7,5,3,1,6,8,7,6,1,1,1,1,1]
    # Convertit la liste Num_symboles en un dictionnaire pour un accès plus facile
    Num_symboles = dict(zip(ALPHABET, Num_symboles))
     # Initialise un dictionnaire pos pour garder une trace de la position actuelle de substitution pour chaque lettre
    pos = dict(zip(ALPHABET, [0]*len(ALPHABET)))
    # Initialise une chaîne vide pour stocker le texte chiffré
    cipher_text = ""
    # Parcourt chaque lettre dans le texte d'origine
    for lettre in plain_text:
        # Vérifie si la lettre est alphabétique 
        if lettre.isalpha():
            # Ajoute le caractère chiffré au texte chiffré en utilisant le tableau de substitution Tab
            cipher_text+=Tab[lettre.upper()][pos[lettre.upper()]]
            # Met à jour la position de substitution pour la lettre actuelle
            if pos[lettre.upper()] +1 <Num_symboles[lettre.upper()]:
                pos[lettre.upper()]+=1
            else:
                pos[lettre.upper()]=0
        else:
            # Si la lettre n'est pas alphabétique, ajoute la lettre telle quelle au texte chiffré
            cipher_text+=lettre
    print(cipher_text)
"""
3. Refaire les questions 1. et 2. :
a. En utilisant un carré de Polybe (initialisé manuellement ou aléatoirement)
"""

def generate_matrix():
    # Définir les dimensions de la matrice
    rows,cols =5,5
    matrix = []
    # Créer une liste de toutes les lettres majuscules disponibles
    available_alphabets = [chr(i) for i in range(65, 91)]
    # Exclure certaines options pour éviter les conflits (comme I/J et V/W)
    exclude_options = [["I","J"],["V","W"]]
    chosen_exclude = random.choice(random.choice(exclude_options))
    available_alphabets.remove(chosen_exclude)
    matrix = []
    # Générer une matrice aléatoire de lettres majuscules sans répétitions dans chaque ligne
    for _ in range(rows):
        # Mélanger les lettres majuscules disponibles pour les choisir de manière aléatoire
        random.shuffle(available_alphabets)
        # Prendre les premières 'cols' lettres pour la ligne actuelle
        row = available_alphabets[:cols]
        # Ajouter la ligne à la matrice
        matrix.append(row)
        # Supprimer les lettres utilisées de la liste disponible
        available_alphabets = available_alphabets[cols:]
        
    return matrix,chosen_exclude
            
def generate_Tab_Polybe():
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Générer une matrice de substitution aléatoire
    matrix,chosen_exclude = generate_matrix()
    print(matrix)
    Tab={}
    
    Tab[chosen_exclude]=['00']
    for index_row, row in enumerate(matrix):
        for index_col, col in enumerate(row):
            Tab[matrix[index_row][index_col]]=[]
            for j in range(5):
                if j !=index_col:
                    for i in range(5):
                        if i!=index_row:
                            Tab[matrix[index_row][index_col]].append(matrix[index_row][j]+matrix[i][index_col])
    print(Tab)
    return Tab

def encrypt_Polybe(plain_text):
    Tab = generate_Tab_Polybe()
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Initialiser un dictionnaire pour suivre la position actuelle de substitution pour chaque lettre
    pos = dict(zip(ALPHABET, [0]*len(ALPHABET)))
    # Initialise une chaîne vide pour stocker le texte chiffré
    cipher_text = ""
    # Parcourt chaque lettre dans le texte d'origine
    for lettre in plain_text:
        if lettre.isalpha():
            cipher_text+=Tab[lettre.upper()][pos[lettre.upper()]]
            # Mettre à jour la position de substitution pour la lettre actuelle
            if pos[lettre.upper()] +1 <len(Tab[lettre.upper()]):
                pos[lettre.upper()]+=1
            else:
                pos[lettre.upper()]=0
        else:
            cipher_text+=lettre
    print(cipher_text)
"""
b. En utilisant l’alternative 2
"""

def generate_matrix_alt2():
    # Définir les dimensions de la matrice
    rows,cols =5,5
    matrix = []
    # Créer une liste de toutes les lettres majuscules disponibles
    available_alphabets = [chr(i) for i in range(65, 91)]
    # Exclure certaines options pour éviter les conflits (comme I/J et V/W)
    exclude_options = [["I","J"],["V","W"]]
    chosen_exclude = random.choice(random.choice(exclude_options))
    available_alphabets.remove(chosen_exclude)
    matrix = []
    # Générer une matrice aléatoire de lettres majuscules sans répétitions dans chaque ligne
    for _ in range(rows):
        # Mélanger les lettres majuscules disponibles pour les choisir de manière aléatoire
        random.shuffle(available_alphabets)
        # Prendre les premières 'cols' lettres pour la ligne actuelle
        row = available_alphabets[:cols]
        # Ajouter la ligne à la matrice
        matrix.append(row)
        # Supprimer les lettres utilisées de la liste disponible
        available_alphabets = available_alphabets[cols:]
        
    return matrix,chosen_exclude
            
def generate_Tab_Polybe_alt2():
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    classes = [[1,2,3,4,5],[6],[7],[8],[9]]
    matrix,chosen_exclude = generate_matrix()
    print(matrix)
    Tab={}
    Tab[chosen_exclude]=['00']
    for index_row, row in enumerate(matrix):
        for index_col, col in enumerate(row):
            Tab[matrix[index_row][index_col]]=[]
            rows = classes[index_row]
            cols = classes[index_col]
            for i in range(len(rows)):
                for j in range(len(cols)):
                    Tab[matrix[index_row][index_col]].append(str(rows[i])+str(cols[j]))
    print(Tab)
    return Tab

def encrypt_Polybe_alt2(plain_text):
    Tab = generate_Tab_Polybe_alt2()
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pos = dict(zip(ALPHABET, [0]*len(ALPHABET)))
    # Initialise une chaîne vide pour stocker le texte chiffré
    cipher_text = ""
    # Parcourt chaque lettre dans le texte d'origine
    for lettre in plain_text:
        if lettre.isalpha():
            cipher_text+=Tab[lettre.upper()][pos[lettre.upper()]]
            if pos[lettre.upper()] +1 <len(Tab[lettre.upper()]):
                pos[lettre.upper()]+=1
            else:
                pos[lettre.upper()]=0
        else:
            cipher_text+=lettre
    print(cipher_text)
encrypt_Polybe_alt2("CCCIICC")