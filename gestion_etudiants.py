FICHIER = "books.txt"

def charger_livres():
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            livres = [line.strip().split(";") for line in f.readlines()]
            return [{"title": l[0], "author": l[1]} for l in livres]
    except FileNotFoundError:
        return []

def sauvegarder_livres(livres):
    with open(FICHIER, "w", encoding="utf-8") as f:
        for livre in livres:
            f.write(f"{livre['title']};{livre['author']}\n")

def ajouter_livre(title, author):
    livres = charger_livres()
    livres.append({"title": title, "author": author})
    sauvegarder_livres(livres)
    print(f"Livre ajouté : {title} - {author}")

def afficher_livres():
    livres = charger_livres()
    for l in livres:
        print(f"{l['title']} - {l['author']}")

if __name__ == "__main__":
    while True:
        print("\n1. Ajouter un livre\n2. Voir les livres\n3. Quitter")
        choix = input("Votre choix : ")
        if choix == "1":
            t = input("Titre : ")
            a = input("Auteur : ")
            ajouter_livre(t, a)
        elif choix == "2":
            afficher_livres()
        elif choix == "3":
            break
        else:
            print("Choix invalide")
