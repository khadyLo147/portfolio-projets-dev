# Mini-projet : Gestion d'étudiants en Python avec sauvegarde
# Auteur : Khady Lo

# Nom du fichier pour sauvegarder les étudiants
FICHIER_ETUDIANTS = "etudiants.txt"

# Charger les étudiants depuis le fichier
def charger_etudiants():
    try:
        with open(FICHIER_ETUDIANTS, "r", encoding="utf-8") as f:
            return [ligne.strip() for ligne in f.readlines()]
    except FileNotFoundError:
        return ["Alice Dupont", "Mohamed Fall", "Sophie Ndiaye"]  # Liste par défaut

# Sauvegarder les étudiants dans le fichier
def sauvegarder_etudiants():
    with open(FICHIER_ETUDIANTS, "w", encoding="utf-8") as f:
        for e in etudiants:
            f.write(e + "\n")

# Liste des étudiants
etudiants = charger_etudiants()

def ajouter_etudiant(nom):
    etudiants.append(nom)
    print(f"Étudiant ajouté : {nom}")
    sauvegarder_etudiants()

def supprimer_etudiant(nom):
    if nom in etudiants:
        etudiants.remove(nom)
        print(f"Étudiant supprimé : {nom}")
        sauvegarder_etudiants()
    else:
        print("Étudiant introuvable.")

def afficher_etudiants():
    if not etudiants:
        print("Aucun étudiant enregistré.")
    else:
        print("Liste des étudiants :")
        for e in etudiants:
            print(f"- {e}")

# Programme principal
while True:
    print("\n--- Gestion des Étudiants ---")
    print("1. Ajouter")
    print("2. Supprimer")
    print("3. Afficher")
    print("4. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom de l'étudiant : ")
        ajouter_etudiant(nom)

    elif choix == "2":
        nom = input("Nom à supprimer : ")
        supprimer_etudiant(nom)

    elif choix == "3":
        afficher_etudiants()

    elif choix == "4":
        print("Programme terminé.")
        break

    else:
        print("Choix invalide.")
