from models.livre import Livre
from services.livre_service import LivreService
from views.affichage import afficher_livres

def menu_livres(db):
    service = LivreService(db)
    while True:
        print("\\n--- GESTION DES LIVRES ---")
        print("1. Ajouter  2. Lister  3. Rechercher  4. Supprimer  5. Modifier quantité  0. Retour")
        choix = input("Choix : ").strip()
        try:
            if choix == "1":
                titre = input("Titre : ").strip()
                quantite = int(input("Quantité : "))
                isbn = input("ISBN (facultatif) : ").strip() or None
                auteur_id = input("ID auteur (facultatif) : ").strip() or None
                categorie_id = input("ID catégorie (facultatif) : ").strip() or None
                editeur = input("Éditeur (facultatif) : ").strip()
                annee = input("Année (facultatif) : ").strip() or None
                livre = Livre(titre, quantite, isbn, auteur_id, categorie_id, editeur, annee)
                print(f"Livre ajouté avec l'identifiant {service.ajouter(livre)}.")
            elif choix == "2":
                afficher_livres(service.lister())
            elif choix == "3":
                afficher_livres(service.rechercher(input("Titre, ISBN ou auteur : ").strip()))
            elif choix == "4":
                service.supprimer(int(input("ID du livre à supprimer : ")))
                print("Livre supprimé.")
            elif choix == "5":
                service.modifier_quantite(int(input("ID du livre : ")),
                                          int(input("Nouvelle quantité totale : ")))
                print("Quantité mise à jour.")
            elif choix == "0":
                break
            else:
                print("Choix invalide.")
        except (ValueError, TypeError) as erreur:
            print(f"Erreur : {erreur}")
        except Exception as erreur:
            print(f"Une erreur est survenue : {erreur}")
