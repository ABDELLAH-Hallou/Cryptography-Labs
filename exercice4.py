"""
1.Écrire une fonction qui génère aléatoirement un tableau de substitution Tab de 0 à 99. 
Attention : éviter les répétitions.
"""
import random
# def generate_number(generated_digits):
#     if len(generated_digits) == 100:
#         return False,generated_digits
#     digit = f"{random.randint(0, 99):02d}"
#     while digit in generated_digits:
#         digit = f"{random.randint(0, 99):02d}"
#     generated_digits.append(digit)
#     return digit,generated_digits
        
            
def generate_Tab():
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Freq=[8.01, 0.88, 3.23, 3.91, 17.52, 1.06, 1.06, 0.88, 7.35, 0.44, 0.05, 5.77, 2.9, 7.22, 5.43, 2.94, 1.14, 6.69, 8.17, 7.07, 6.0, 1.41, 0.02, 0.47, 0.3, 0.12]
    Num_symboles = [8,1,3,4,16,1,1,1,7,1,1,5,3,7,5,3,1,6,8,7,6,1,1,1,1,1]
    Tab={}
    # generated_digits = []
    generated_digits = [str(num).zfill(2) for num in range(100)]
    random.shuffle(generated_digits)
    for index in range(len(ALPHABET)):
        Tab[ALPHABET[index]] = []
        for i in range(Num_symboles[index]):
            # digit,generated_digits = generate_number(generated_digits)
            digit = generated_digits.pop(0)
            Tab[ALPHABET[index]].append(digit)
    print(Tab)
    return Tab

"""
2. Écrire une fonction qui crypte un texte par un chiffre homophone en se basant sur la table Tab. Cette fonction doit choisir d’une manière uniforme les choix de substitution.
"""
def encrypt(plain_text):
    Tab = generate_Tab()
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Num_symboles = [8,1,3,4,16,1,1,1,7,1,1,5,3,7,5,3,1,6,8,7,6,1,1,1,1,1]
    Num_symboles = dict(zip(ALPHABET, Num_symboles))
    pos = dict(zip(ALPHABET, [0]*len(ALPHABET)))
    # Initialise une chaîne vide pour stocker le texte chiffré
    cipher_text = ""
    # Parcourt chaque lettre dans le texte d'origine
    for lettre in plain_text:
        if lettre.isalpha():
            cipher_text+=Tab[lettre.upper()][pos[lettre.upper()]]
            if pos[lettre.upper()] +1 <Num_symboles[lettre.upper()]:
                pos[lettre.upper()]+=1
            else:
                pos[lettre.upper()]=0
        else:
            cipher_text+=lettre
    print(cipher_text)
"""
3. Refaire les questions 1. et 2. :
a. En utilisant un carré de Polybe (initialisé manuellement ou aléatoirement)
"""

def generate_matrix():
    # Define the dimensions of the matrix
    rows,cols =5,5
    matrix = []
    # Create a list of all available uppercase letters
    available_alphabets = [chr(i) for i in range(65, 91)]
    exclude_options = [["I","J"],["V","W"]]
    chosen_exclude = random.choice(random.choice(exclude_options))
    available_alphabets.remove(chosen_exclude)
    # Initialize an empty matrix
    matrix = []
    # Generate a random matrix of uppercase letters without duplicates in each row
    for _ in range(rows):
        # Shuffle the available alphabets to randomize the selection
        random.shuffle(available_alphabets)
        # Take the first 'cols' alphabets for the current row
        row = available_alphabets[:cols]
        # Add the row to the matrix
        matrix.append(row)
        # Remove the used alphabets from the available list
        available_alphabets = available_alphabets[cols:]
        
    return matrix,chosen_exclude
            
def generate_Tab_Polybe():
    ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
"""
b. En utilisant l’alternative 2
"""

def generate_matrix_alt2():
    # Define the dimensions of the matrix
    rows,cols =5,5
    matrix = []
    # Create a list of all available uppercase letters
    available_alphabets = [chr(i) for i in range(65, 91)]
    exclude_options = [["I","J"],["V","W"]]
    chosen_exclude = random.choice(random.choice(exclude_options))
    available_alphabets.remove(chosen_exclude)
    # Initialize an empty matrix
    matrix = []
    # Generate a random matrix of uppercase letters without duplicates in each row
    for _ in range(rows):
        # Shuffle the available alphabets to randomize the selection
        random.shuffle(available_alphabets)
        # Take the first 'cols' alphabets for the current row
        row = available_alphabets[:cols]
        # Add the row to the matrix
        matrix.append(row)
        # Remove the used alphabets from the available list
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