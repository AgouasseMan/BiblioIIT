from views.livre_view import menu_livres
from views.adherent_view import menu_adherents
from views.emprunt_view import menu_emprunts
from views.penalite_view import menu_penalites
from views.catalogue_view import menu_referentiels
from views.statistiques_view import afficher_statistiques

def lancer_menu(db):
    while True:
        print("\\n========== GESTION DE BIBLIOTHÈQUE ==========")
        print("1. Gestion des livres")
        print("2. Gestion des adhérents")
        print("3. Emprunts et retours")
        print("4. Gestion des pénalités")
        print("5. Auteurs et catégories")
        print("6. Statistiques")
        print("0. Quitter")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            menu_livres(db)
        elif choix == "2":
            menu_adherents(db)
        elif choix == "3":
            menu_emprunts(db)
        elif choix == "4":
            menu_penalites(db)
        elif choix == "5":
            menu_referentiels(db)
        elif choix == "6":
            afficher_statistiques(db)
        elif choix == "0":
            print("Fermeture de l'application.")
            break
        else:
            print("Choix invalide.")
