# Projet 2 : Générateur de mots de passe
# Auteur : Khady Lo

import random
import string

def generer_mot_de_passe(longueur=12):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*?"
    mot_de_passe = "".join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

print("=== Générateur de mots de passe ===")
taille = input("Longueur du mot de passe souhaitée (par défaut 12) : ")

if taille.isdigit():
    taille = int(taille)
    print("Mot de passe généré :", generer_mot_de_passe(taille))
else:
    print("Mot de passe généré :", generer_mot_de_passe())
