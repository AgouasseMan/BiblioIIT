from models.adherent import Adherent
from services.adherent_service import AdherentService
from views.affichage import afficher_adherents

def menu_adherents(db):
    service = AdherentService(db)
    while True:
        print("\\n--- GESTION DES ADHÉRENTS ---")
        print("1. Inscrire  2. Lister  3. Rechercher  4. Suspendre/Réactiver  0. Retour")
        choix = input("Choix : ").strip()
        try:
            if choix == "1":
                adherent = Adherent(
                    input("Nom : "), input("Prénom : "),
                    input("Téléphone : "), input("Email : ")
                )
                if not adherent.nom or not adherent.prenom:
                    raise ValueError("Le nom et le prénom sont obligatoires.")
                print(f"Adhérent inscrit avec l'identifiant {service.ajouter(adherent)}.")
            elif choix == "2":
                afficher_adherents(service.lister())
            elif choix == "3":
                afficher_adherents(service.rechercher(input("Nom, prénom ou téléphone : ")))
            elif choix == "4":
                identifiant = int(input("ID adhérent : "))
                statut = input("Nouveau statut (ACTIF/SUSPENDU) : ").strip().upper()
                service.changer_statut(identifiant, statut)
                print("Statut mis à jour.")
            elif choix == "0":
                break
            else:
                print("Choix invalide.")
        except (ValueError, TypeError) as erreur:
            print(f"Erreur : {erreur}")
