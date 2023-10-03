import numpy as np
from sympy import Matrix
import math
"""
1. Écrire une fonction qui retourne l’inverse d’un nombre n dans Z/26Z s’il existe et 0 sinon.
"""
def inverse_mod_26(n):
    for i in range(26):
        if (n * i) % 26 == 1:
            return i
    return 0

"""
2. Écrire une fonction qui génère une matrice Q inversible Z/26Z.
"""
def generate_invertible_matrix():
    while True:
        # Générez une matrice 2x2 avec des éléments aléatoires dans Z/26Z
        Q = np.random.randint(0, 26, (2, 2))
        # Vérifiez si la matrice est inversible en calculant son déterminant
        det = Matrix(Q).det()
        if det != 0 and math.gcd(det, 26) == 1:
            return Q
"""
3. Écrire une fonction qui crypte un texte via le chiffre de Hill basé sur la matrice Q.
"""
def encrypt(text, matrix):
    encrypted_text = ""
    step=2
    for i in range(0, len(text), step):
        if text[i].isalpha():
            # Transformez chaque paire de lettres en un vecteur 2x1
            x1 = [ord(text[i]) - ord('A' if text[i].isupper() else 'a')]
            x2 = [ord(text[i+1]) - ord('A' if text[i+1].isupper() else 'a')]
            pair = np.array([x1, x2])
            # Appliquez la multiplication matricielle
            y = np.dot(matrix, pair) % 26
            # Convertissez le résultat en une paire de lettres
            z1 = chr(y[0][0] + ord('A' if text[i].isupper() else 'a'))
            z2 = chr(y[1][0] + ord('A' if text[i+1].isupper() else 'a'))
            encrypted_text += z1 + z2
            step=2
        else:
            encrypted_text += text[i]
            step=1
    return encrypted_text
"""
4. Écrire une fonction qui décrypte un texte via le chiffre de Hill basé sur la matrice Q.
"""
def decrypt(text, matrix):
    matrix_inverse = Matrix(matrix).inv_mod(26)
    decrypted_text = ""
    step=2
    for i in range(0, len(text), step):
        if text[i].isalpha():
            # Transformez chaque paire de lettres en un vecteur 2x1
            x1 = [ord(text[i]) - ord('A' if text[i].isupper() else 'a')]
            x2 = [ord(text[i+1]) - ord('A' if text[i+1].isupper() else 'a')]
            pair = np.array([x1, x2])
            # Appliquez la multiplication matricielle
            y = np.dot(matrix_inverse, pair) % 26
            # Convertissez le résultat en une paire de lettres
            z1 = chr(y[0][0] + ord('A' if text[i].isupper() else 'a'))
            z2 = chr(y[1][0] + ord('A' if text[i+1].isupper() else 'a'))
            decrypted_text += z1 + z2
            step=2
        else:
            decrypted_text +=text[i]
            step=1
    return decrypted_text

"""
5. Écrire un programme qui illustre les questions de 1. à 4.
"""

matrix = generate_invertible_matrix()
print("Matrice Q inversible :")
print(matrix)

message = "HELLOHILLL"
encrypted_message = encrypt(message, matrix)
print("Message chiffré :")
print(encrypted_message)

decrypted_message = decrypt(encrypted_message, matrix)
print("Message déchiffré :")
print(decrypted_message)
